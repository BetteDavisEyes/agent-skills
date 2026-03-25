# Competitor Monitoring Guidance

Use this file to guide shortlist selection and workflow recommendations.

## Scenario Intent

This scenario focuses on social media competitor monitoring through:

- competitor account monitoring
- brand mention discovery
- comment collection for downstream sentiment analysis

## Core Platforms

Prefer these platforms first:

- `Twitter/X`
- `TikTok`
- `Reddit`
- `YouTube`

These platforms form the default first-version recommendation set because they have the strongest and clearest template coverage for this scenario.

## Secondary Platforms

Use these only when the request clearly requires them:

- `Naver Blog`
- `Weibo`
- `Xiaohongshu`
- `LinkedIn`
- `Gab`

## Important Guardrail

Do not describe comment analysis as a template capability.

Use language like:

- `collect comments for sentiment analysis`
- `collect replies for downstream AI analysis`

Do not use language like:

- `the template analyzes sentiment`

## Core Recommendation Patterns

### Competitor Account Monitoring

Typical recommendation patterns:

- account URL or profile URL -> account/profile template
- channel URL -> channel template

### Brand Mention Monitoring

Typical recommendation patterns:

- keyword or advanced search -> search template
- hashtag -> hashtag or advanced search template

### Comment Monitoring

Typical recommendation patterns:

- content URL already available -> comments template
- content discovery plus comments needed -> smallest valid workflow or a combined template when available

## Full-Chain Monitoring

Support a `full-chain` recommendation when the user wants:

- competitor account monitoring
- brand mention monitoring
- comment collection for downstream sentiment analysis

in the same monitoring plan.

In a `full-chain` recommendation:

- organize the answer by track or by platform
- make it clear which templates are for owned-content monitoring
- make it clear which templates are for brand mention discovery
- make it clear which templates are for comments and replies

## All-Core-Platforms Monitoring

Support an `all-core-platforms` recommendation when the user wants monitoring across:

- `Twitter/X`
- `TikTok`
- `Reddit`
- `YouTube`

In these cases:

- prefer a per-platform recommendation structure
- avoid collapsing all platforms into one mixed list without grouping
- keep the recommendation concise by naming one primary template set per platform and track

## Chain Validation Rule

If a recommendation involves more than one template:

- validate the chain with `octoparse-link-template`

If a template is already a combined workflow:

- recommend it directly
- do not also present its upstream component as a required chain
