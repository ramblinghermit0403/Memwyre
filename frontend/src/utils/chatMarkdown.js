import MarkdownIt from 'markdown-it';

const markdown = new MarkdownIt({
    html: false,
    linkify: true,
    breaks: true,
});

const THINK_BLOCK_REGEX = /<(think|thinking)>([\s\S]*?)<\/\1>/gi;

const normalizeWhitespace = (text = '') =>
    (text || '')
        .replace(/\r\n/g, '\n')
        .replace(/\r/g, '\n')
        .replace(/\n{3,}/g, '\n\n')
        .trim();

const stripMalformedThinking = (text = '') =>
    (text || '')
        .replace(/<(think|thinking)>[\s\S]*$/i, '')
        .replace(/<\/(think|thinking)>/gi, '')
        .replace(/<(think|thinking)>/gi, '');

export const splitChatContent = (rawContent = '') => {
    const source = String(rawContent || '');
    const thinkMatches = [...source.matchAll(THINK_BLOCK_REGEX)];
    const reasoningText = thinkMatches.length > 0
        ? normalizeWhitespace(thinkMatches[0][2] || '')
        : '';

    let answerText = source.replace(THINK_BLOCK_REGEX, '');
    answerText = stripMalformedThinking(answerText);
    answerText = normalizeWhitespace(answerText);

    return {
        reasoningText,
        answerText
    };
};

export const renderChatMarkdown = (text = '') => markdown.render(text || '');
