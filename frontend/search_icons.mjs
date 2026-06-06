import { toc } from '@lobehub/icons';

const searchTerms = ['cursor', 'windsurf', 'claude', 'code', 'visual', 'antigravity', 'openai', 'codex'];

const results = {};

for (const term of searchTerms) {
  results[term] = toc.filter(icon => 
    icon.id.toLowerCase().includes(term.toLowerCase()) || 
    icon.title.toLowerCase().includes(term.toLowerCase()) ||
    icon.fullTitle.toLowerCase().includes(term.toLowerCase())
  ).map(icon => icon.id);
}

console.log(JSON.stringify(results, null, 2));
