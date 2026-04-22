import { mkdir, writeFile, readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const outputPath = path.resolve(__dirname, '../public/other/lib-paiad.js');
const outputDir = path.dirname(outputPath);

const customUrl = process.env.PAIAD_URL?.trim();
const sources = [
  customUrl,
  'https://cdn.jsdelivr.net/gh/wdssmq/userscript@main/dist-lib/lib-paiad.js',
  'https://raw.githubusercontent.com/wdssmq/userscript/main/dist-lib/lib-paiad.js',
].filter(Boolean);

async function fetchFrom(url) {
  const response = await fetch(url, {
    headers: {
      'user-agent': 'dev-bt2mag/update-paiad',
      accept: 'application/javascript,text/plain;q=0.9,*/*;q=0.8',
    },
  });

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }

  const content = await response.text();

  if (!content || !content.trim()) {
    throw new Error('Empty file content');
  }

  return content;
}

async function hasExistingFile(filePath) {
  try {
    const existing = await readFile(filePath, 'utf8');
    return Boolean(existing.trim());
  } catch {
    return false;
  }
}

async function main() {
  const errors = [];

  for (const url of sources) {
    try {
      const content = await fetchFrom(url);

      await mkdir(outputDir, { recursive: true });
      await writeFile(outputPath, content, 'utf8');

      console.log(`[update:paiad] Updated from: ${url}`);
      console.log(`[update:paiad] Output: ${outputPath}`);
      return;
    } catch (error) {
      errors.push(`${url} -> ${error.message}`);
    }
  }

  if (await hasExistingFile(outputPath)) {
    console.warn('[update:paiad] Update failed, keep existing local file.');
    for (const item of errors) {
      console.warn(`[update:paiad] ${item}`);
    }
    return;
  }

  console.error('[update:paiad] Update failed and no local file exists.');
  for (const item of errors) {
    console.error(`[update:paiad] ${item}`);
  }
  process.exitCode = 1;
}

await main();
