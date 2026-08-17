// agent-resilience — three-tier fallback helpers

const tier1 = {
  default(value, defaultFn) {
    if (value === null || value === undefined || value === '') {
      return typeof defaultFn === 'function' ? defaultFn() : defaultFn;
    }
    return value;
  }
};

const tier2 = {
  skipIf(row, condition, reason, log = console.log) {
    if (condition) {
      log(`[SKIP] ${reason}`);
      return null;
    }
    return row;
  }
};

const tier3 = {
  async askHuman({ channel, question, context, notifier }) {
    if (!notifier) throw new Error('Tier 3 needs a notifier — pass a Slack/Discord/email function.');
    const result = await notifier({ channel, text: `${question}\n\n${context}` });
    return { paused: true, threadId: result?.thread_ts || result?.id };
  }
};

function summary({ processed, succeeded, skipped, defaultsUsed, questionsRaised }) {
  return [
    `Processed: ${processed}`,
    `Succeeded: ${succeeded}`,
    `Skipped (Tier 2): ${skipped.length}`,
    ...skipped.map(s => `  - ${s}`),
    `Tier 1 defaults used: ${defaultsUsed}`,
    `Tier 3 questions raised: ${questionsRaised.length}`,
    ...questionsRaised.map(q => `  - ${q}`)
  ].join('\n');
}

module.exports = { tier1, tier2, tier3, summary };
