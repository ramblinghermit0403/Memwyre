const axios = require('axios');
const fs = require('fs');
const readline = require('readline');

async function readStdin() {
  return new Promise((resolve) => {
    let data = '';
    process.stdin.on('data', (chunk) => {
      data += chunk;
    });
    process.stdin.on('end', () => {
      try {
        resolve(JSON.parse(data));
      } catch (e) {
        resolve({});
      }
    });
    // Fallback if stdin is empty or closed
    setTimeout(() => resolve({}), 1000);
  });
}

function writeOutput(data) {
  console.log(JSON.stringify(data));
}

async function parseTranscript(filePath) {
  const messages = [];
  try {
    if (!fs.existsSync(filePath)) return messages;
    
    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity
    });

    for await (const line of rl) {
      if (!line.trim()) continue;
      try {
        messages.push(JSON.parse(line));
      } catch (e) {
        // Skip malformed JSONL lines
      }
    }
  } catch (err) {
    // Silently handle read errors
  }
  return messages;
}

async function main() {
  try {
    const input = await readStdin();
    const cwd = input.cwd || process.cwd();
    const sessionId = input.session_id;
    const transcriptPath = input.transcript_path;
    const projectName = cwd.split(/[/\\]/).pop();

    if (!transcriptPath || !sessionId) {
      writeOutput({ continue: true });
      return;
    }

    const apiKey = process.env.MEMWYRE_API_KEY;
    if (!apiKey) {
      writeOutput({ continue: true });
      return;
    }

    // Read the raw terminal log
    const transcript = await parseTranscript(transcriptPath);
    if (transcript.length === 0) {
      writeOutput({ continue: true });
      return;
    }

    // POST transcript to backend for async Signal Extraction
    const apiUrl = process.env.MEMWYRE_API_URL || 'http://127.0.0.1:8000';
    
    try {
      await axios.post(`${apiUrl}/api/v1/plugin/capture`, {
        session_id: sessionId,
        project_name: projectName,
        cwd: cwd,
        transcript: transcript
      }, {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        },
        timeout: 5000 // Ensure we don't hang the terminal exit
      });
    } catch (apiError) {
      // Background capture failed, but we shouldn't block the user from exiting
    }

    writeOutput({ continue: true });

  } catch (err) {
    writeOutput({ continue: true });
  }
}

main();
