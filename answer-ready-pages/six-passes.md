# The six passes

Adapted from Robert Niechciał's "Semantic OS" workshop skills (LLM Mastery,
14 November 2026), which he published under an MIT notice. Rewritten for our
pipeline rather than copied. His versions take pasted input and need no keys;
ours can read the page from the database and search data from DataForSEO.

Every pass has a fixed output shape. That is the point: two runs, or two pages,
can be laid side by side.

## 1. Fan-out

**Input:** one question in the customer's words. Optional: People Also Ask and
related searches for it.

**Method:** decompose three ways.

- Semantic: the entity, its attributes, its relationships, time and place.
- Intent: what the person actually wants, what they are assuming, what they
  will ask next.
- Verification: the fact-check, the source or authority question, the
  comparison.

Aim for 5 to 10 sub-questions. Tag each:

- `CONFIRMED`: also present in the search data.
- `PREDICTED`: from the model only.
- `SERP-ONLY`: in the search data, missed by the model. A gap candidate only
  after checking the page does not already answer it.

With no search data, mark every line unknown. No engine publishes the
sub-queries it really runs, so these are candidates, not demand.

**Output:** header (question, entity, intent, complexity); table of
sub-question, purpose, source type, tag; what each implies for the page; a
gap checklist.

**Use:** track the sub-questions in the battery, not just the head question.
Check Bing rank for each. Bing Webmaster Tools' AI Performance report shows
real fan-out searches for our own sites and is better than any prediction.

## 2. Frame

**Input:** a topic or verb phrase, and a perspective (buyer, seller, expert).

**Method:** fill fifteen roles and turn each into a question with a High,
Medium or Low priority for this page's job.

Agent, Patient, Instrument, Location, Time, Cause, Purpose, Manner, Result,
Condition, Beneficiary, Source, Cost, Alternative, Part.

Roles combine (Cost with Instrument is "how much and how to pay for it").
Frames nest (financing inside enrolling). Covering more roles does not make a
page better; the High rows the fan-out missed are what to add.

**Output:** the role table; suggested H2s; related frames that may deserve
their own page.

For a programme page the roles that usually go missing are Time (how long,
when it starts), Condition (prerequisites, licensure), Cost and Alternative
(the cheaper or faster route). Those are also where our crossed data sits.

## 3. Vocabulary

**Input:** one keyword, with market, language and what the site offers.

**Method:** five relations, each with a job on the page.

| relation | job |
|---|---|
| Synonyms | match differently worded queries |
| Broader terms | intro context, heading hierarchy |
| Narrower terms | H2 sections |
| Parts | completeness, spec questions |
| Opposites | "X vs Y" sections |

Prefer terms that appear in real queries. Check for domain accuracy: related
is not the same as synonymous. In his own demo the plain chat listed a paddling
pool as a type of swimming pool.

## 4. Chunk check

**Input:** the article as markdown, navigation and footer removed.

**Five checks:**

1. Heading structure: hierarchy sound, H2s answer sub-questions, headings
   descriptive.
2. Answer first: does each H2's opening sentence answer its heading.
3. Autonomy: does each section name its subject, with no "as mentioned
   above" and no orphaned "this".
4. Term distribution: no section empty of the key terms.
5. Length: 200 to 500 words a section is a reference point, never pass or fail.

**Output:** heading tree with marks; a table of sections quoting the phrase
that breaks autonomy; a ranked list of what to fix. He also emits a readiness
score out of ten. It moved from 5 to 6 between two runs on one page. Record it
if you like; do not act on it.

## 5. Answer-first rewrite

**Input:** the weak section, and the whole page as the only source of facts.

**Method:** identify the question the section answers; find the buried answer;
rewrite as answer, then evidence, then context. Cut introductions,
announcements and empty adjectives. Replace a vague word with a value only if
the source supports it.

**Never invent a number.** Where one is needed and missing, write
`[FACT NEEDED: what]`. That tag is our `[VERIFY]` by another name and goes the
same route.

About 50 words for the opening answer is a guide, not a rule. For a long text,
apply the same shape at each level: page, section, paragraph.

In our pipeline this pass is the only one that produces prose, so it is the
only one that goes to DeepSeek and the humanizer.

## 6. Fact triples

**Input:** any single text.

**Method:** list the entities; for each, the attributes; for each attribute,
the value **with the conditions that change its meaning** (unit, date, state,
programme). Keep only triples traceable to a quoted passage. Mark gaps
`[missing]`.

**Then compare.** Run the same extraction on the pages that rank for the query
(he used seven) and sort our facts into three piles:

| pile | meaning | action |
|---|---|---|
| Confirmed | the same value in at least two sources | keep |
| Alone | only we state it | our best content and our weakest proof: the outreach list |
| Conflict | another source disagrees | fix it or explain the difference on the page |

Cautions from his own run: three of seven comparison pages were truncated, so
"alone" meant "not in the text I had"; and most confirmations came from one
page. Read the full pages.

For us the Alone pile is where crossed-source figures land. Net price against
median wage exists nowhere else, by design. Under the ClashEval result he cites
(answers were right 15.6% of the time when every source counted equally and
77.1% when sources confirmed each other on specifics; a research benchmark,
not a description of any live engine), a figure nobody else repeats is the one
an engine is least able to trust. Getting one independent page to quote it,
with its method, is the missing half of information gain.
