import { spawn } from 'node:child_process';
import { existsSync } from 'node:fs';
import { mkdir, mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';
import ffmpegInstaller from '@ffmpeg-installer/ffmpeg';
import { chromium } from 'playwright';

const PORT = 4173;
const HOST = '127.0.0.1';
const CAPTURE_PATH = '/__video/intro-capture';
const CAPTURE_URL = `http://${HOST}:${PORT}${CAPTURE_PATH}`;
const VIDEO_WIDTH = 1920;
const VIDEO_HEIGHT = 1080;
const SERVER_START_TIMEOUT_MS = 60_000;
const CAPTURE_TIMEOUT_MS = 80_000;
const INTRO_DURATION_SECONDS = 60;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const frontendRoot = path.resolve(__dirname, '..');
const outputFile = path.resolve(frontendRoot, 'public', 'intro-generated.mp4');

const npmCommand = 'npm';

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function spawnProcess(command, args, options = {}) {
  return spawn(command, args, {
    cwd: frontendRoot,
    env: process.env,
    stdio: ['ignore', 'pipe', 'pipe'],
    shell: process.platform === 'win32',
    windowsHide: true,
    ...options
  });
}

async function runCommand(command, args, options = {}) {
  await new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: 'pipe', ...options });
    let stderr = '';

    if (child.stderr) {
      child.stderr.on('data', (chunk) => {
        stderr += chunk.toString();
      });
    }

    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) {
        resolve();
        return;
      }

      reject(
        new Error(
          `Command failed: ${command} ${args.join(' ')}\n${stderr || `Exit code ${code}`}`
        )
      );
    });
  });
}

async function stopServer(serverProcess) {
  if (!serverProcess || serverProcess.exitCode !== null || !serverProcess.pid) {
    return;
  }

  if (process.platform === 'win32') {
    await runCommand('taskkill', ['/pid', String(serverProcess.pid), '/t', '/f'], {
      windowsHide: true
    }).catch(() => {});
    return;
  }

  serverProcess.kill('SIGTERM');
  await new Promise((resolve) => {
    const timeout = setTimeout(() => {
      if (serverProcess.exitCode === null) {
        serverProcess.kill('SIGKILL');
      }
      resolve();
    }, 5_000);

    serverProcess.on('close', () => {
      clearTimeout(timeout);
      resolve();
    });
  });
}

async function waitForServer(url, serverProcess, timeoutMs) {
  const startedAt = Date.now();

  while (Date.now() - startedAt < timeoutMs) {
    if (serverProcess.exitCode !== null) {
      throw new Error('Vite dev server exited before becoming ready.');
    }

    try {
      const response = await fetch(url, { method: 'GET' });
      if (response.ok) {
        return;
      }
    } catch {
      // Ignore connection errors while server starts.
    }

    await sleep(350);
  }

  throw new Error(`Timed out waiting for Vite server at ${url}.`);
}

async function transcodeToMp4(inputWebm, outputMp4, trimStartSeconds) {
  if (!existsSync(inputWebm)) {
    throw new Error(`Captured .webm not found at ${inputWebm}`);
  }

  const ffmpegPath = ffmpegInstaller.path;
  const normalizedTrimStart = Math.max(0, Number(trimStartSeconds) || 0);
  const ffmpegArgs = [
    '-y',
    '-ss',
    normalizedTrimStart.toFixed(3),
    '-i',
    inputWebm,
    '-t',
    String(INTRO_DURATION_SECONDS),
    '-an',
    '-c:v',
    'libx264',
    '-preset',
    'medium',
    '-crf',
    '20',
    '-pix_fmt',
    'yuv420p',
    '-movflags',
    '+faststart',
    outputMp4
  ];

  await runCommand(ffmpegPath, ffmpegArgs, { windowsHide: true });
}

async function main() {
  let serverProcess = null;
  let browser = null;
  let tempDir = null;

  try {
    await mkdir(path.dirname(outputFile), { recursive: true });
    tempDir = await mkdtemp(path.join(tmpdir(), 'memwyre-intro-'));

    console.log(`Starting Vite dev server on ${HOST}:${PORT}...`);
    serverProcess = spawnProcess(npmCommand, [
      'run',
      'dev',
      '--',
      '--host',
      HOST,
      '--port',
      String(PORT),
      '--strictPort'
    ]);

    serverProcess.stdout?.on('data', (chunk) => {
      const line = chunk.toString();
      if (line.trim()) {
        process.stdout.write(`[vite] ${line}`);
      }
    });

    serverProcess.stderr?.on('data', (chunk) => {
      const line = chunk.toString();
      if (line.trim()) {
        process.stderr.write(`[vite] ${line}`);
      }
    });

    await waitForServer(CAPTURE_URL, serverProcess, SERVER_START_TIMEOUT_MS);

    console.log(`Opening capture scene at ${CAPTURE_URL}...`);
    browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
      viewport: { width: VIDEO_WIDTH, height: VIDEO_HEIGHT },
      screen: { width: VIDEO_WIDTH, height: VIDEO_HEIGHT },
      recordVideo: {
        dir: tempDir,
        size: { width: VIDEO_WIDTH, height: VIDEO_HEIGHT }
      }
    });

    const page = await context.newPage();
    const recordingStartedAt = Date.now();
    await page.goto(CAPTURE_URL, { waitUntil: 'networkidle' });
    const introStartedAtHandle = await page.waitForFunction(
      () => (typeof window.__INTRO_STARTED_AT__ === 'number' ? window.__INTRO_STARTED_AT__ : null),
      null,
      { timeout: 10_000 }
    );
    const introStartedAt = Number(await introStartedAtHandle.jsonValue());

    await page.waitForFunction(() => window.__INTRO_DONE__ === true, null, {
      timeout: CAPTURE_TIMEOUT_MS
    });
    await page.waitForTimeout(100);

    const recordedVideo = page.video();
    if (!recordedVideo) {
      throw new Error('Playwright did not expose a recorded video handle.');
    }

    await context.close();
    const webmPath = await recordedVideo.path();
    console.log(`Captured .webm at: ${webmPath}`);
    const trimStartSeconds = Math.max(0, (introStartedAt - recordingStartedAt) / 1000);

    console.log(`Transcoding to mp4: ${outputFile}`);
    await transcodeToMp4(webmPath, outputFile, trimStartSeconds);

    console.log('Intro video generated successfully.');
    console.log(`Output: ${outputFile}`);
  } finally {
    if (browser) {
      await browser.close().catch(() => {});
    }
    await stopServer(serverProcess);
    if (tempDir) {
      await rm(tempDir, { recursive: true, force: true }).catch(() => {});
    }
  }
}

main().catch((error) => {
  console.error('Failed to render intro video.');
  console.error(error);
  process.exitCode = 1;
});
