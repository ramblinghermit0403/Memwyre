const esbuild = require('esbuild');
const path = require('path');
const fs = require('fs');

async function build() {
  const distDir = path.join(__dirname, '../dist');
  if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir);
  }

  const entryPoints = [
    path.join(__dirname, '../src/inject-memory.js'),
    path.join(__dirname, '../src/capture-session.js')
  ];

  await esbuild.build({
    entryPoints,
    bundle: true,
    platform: 'node',
    target: 'node18',
    format: 'cjs',
    outdir: distDir,
    outExtension: { '.js': '.cjs' },
    minify: true,
  });

  console.log('Build complete');
}

build().catch((err) => {
  console.error(err);
  process.exit(1);
});
