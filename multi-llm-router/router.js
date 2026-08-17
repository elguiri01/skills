// multi-llm-router — pick cheapest model per task
// Drop your API keys in .env next to this file.

require('dotenv').config({ path: __dirname + '/.env' });

const ROUTES = {
  classify_reply: { model: 'deepseek-chat', provider: 'deepseek', fallback: 'claude-haiku-4-5' },
  extract_json: { model: 'deepseek-chat', provider: 'deepseek', fallback: 'gpt-4.1-mini' },
  long_form_content: { model: 'deepseek-reasoner', provider: 'deepseek', fallback: 'claude-sonnet-4-6' },
  code_review: { model: 'gpt-5', provider: 'openai', fallback: 'claude-opus-4-7' },
  architectural_reasoning: { model: 'claude-opus-4-7', provider: 'anthropic', fallback: null },
  mcp_loop: { model: 'claude-haiku-4-5', provider: 'anthropic', fallback: 'claude-sonnet-4-6' },
  safety_critical: { model: 'claude-sonnet-4-6', provider: 'anthropic', fallback: 'claude-opus-4-7' },
};

async function callOpenAI(model, prompt) {
  const res = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${process.env.OPENAI_API_KEY}` },
    body: JSON.stringify({ model, messages: [{ role: 'user', content: prompt }] })
  });
  const data = await res.json();
  return data.choices?.[0]?.message?.content;
}

async function callDeepSeek(model, prompt) {
  const res = await fetch('https://api.deepseek.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${process.env.DEEPSEEK_API_KEY}` },
    body: JSON.stringify({ model, messages: [{ role: 'user', content: prompt }] })
  });
  const data = await res.json();
  return data.choices?.[0]?.message?.content;
}

async function callAnthropic(model, prompt) {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({ model, max_tokens: 4096, messages: [{ role: 'user', content: prompt }] })
  });
  const data = await res.json();
  return data.content?.[0]?.text;
}

async function call(provider, model, prompt) {
  if (provider === 'openai') return callOpenAI(model, prompt);
  if (provider === 'deepseek') return callDeepSeek(model, prompt);
  if (provider === 'anthropic') return callAnthropic(model, prompt);
  throw new Error(`Unknown provider: ${provider}`);
}

async function route({ task, input, schema = null, retry = true }) {
  const config = ROUTES[task];
  if (!config) throw new Error(`Unknown task: ${task}. Add it to ROUTES table.`);

  const prompt = schema
    ? `${input}\n\nReturn ONLY valid JSON matching this schema: ${JSON.stringify(schema)}`
    : input;

  let result = await call(config.provider, config.model, prompt);

  if (schema && retry) {
    try {
      result = JSON.parse(result.match(/\{[\s\S]*\}/)?.[0] || result);
    } catch (e) {
      if (config.fallback) {
        const fallbackProvider = ROUTES[task].provider === 'deepseek' ? 'anthropic' : 'openai';
        result = await call(fallbackProvider, config.fallback, prompt);
        try { result = JSON.parse(result.match(/\{[\s\S]*\}/)?.[0] || result); } catch (e2) { return null; }
      }
    }
  }
  return result;
}

module.exports = { route, ROUTES };
