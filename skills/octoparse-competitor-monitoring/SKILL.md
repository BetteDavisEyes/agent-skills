---
name: octoparse-competitor-monitoring
description: Recommend Octoparse workflows for social media competitor monitoring. Use this skill whenever the user wants to monitor competitor accounts, track brand mentions across social media, collect posts, videos, comments, and replies for downstream sentiment analysis, compare competitor content performance, or decide which Octoparse templates should be used for TikTok, Twitter/X, Reddit, YouTube, and related social platforms.
---

# Octoparse Competitor Monitoring

Use this skill to recommend Octoparse templates and workflows for social media competitor monitoring.

This is a scenario skill, not a single-template task skill.

## Scenario Boundary

This skill should cover:

- monitoring competitor-owned social media accounts
- discovering posts or videos that mention a competitor brand
- collecting comments and replies for downstream sentiment analysis
- recommending a small set of Octoparse templates instead of the full social media catalog

This skill should not cover:

- Meta platforms as a first-version promise
- e-commerce review monitoring
- news-media monitoring
- parameter configuration for one specific template
- direct task execution when the user only wants a task created

Sentiment analysis itself is not an Octoparse template capability.

This skill helps collect posts, videos, comments, and replies for downstream sentiment analysis. Sentiment analysis itself is not an Octoparse template capability and should be handled after collection.

## Prerequisites

Use this skill when:

- Octoparse MCP is connected
- the agent can access Octoparse template search and template detail tools
- template-specific docs or internal shortlist references are available when needed

Do not require the end user to write commands or use CLI tools.

## Internal Tracks

This skill uses three tracks:

1. `competitor-account-monitoring`
2. `brand-mention-monitoring`
3. `comment-monitoring`

Read `references/request-classifier.md` before selecting templates.

## Evidence Priority

Use sources in this order:

1. the user request and monitoring goal
2. `references/request-classifier.md`
3. `references/competitor-monitoring-shortlist-core.json`
4. `references/competitor-monitoring-shortlist-secondary.json`
5. `references/competitor-monitoring-guidance.md`
6. Octoparse MCP template details and official template pages when more evidence is needed
7. `octoparse-link-template` if a multi-template chain must be validated

## Platform Strategy

Default `core` platforms:

- `Twitter/X`
- `TikTok`
- `Reddit`
- `YouTube`

Default `secondary` platforms:

- `Naver Blog`
- `Weibo`
- `Xiaohongshu`
- `LinkedIn`
- `Gab`

Secondary and regional platforms are stored in `references/competitor-monitoring-shortlist-secondary.json`.

## Recommendation Rules

- If the user wants to monitor competitor-owned accounts, route to `competitor-account-monitoring`.
- If the user wants to discover posts, videos, or discussions that mention a brand or keyword, route to `brand-mention-monitoring`.
- If the user wants comments, replies, complaints, feedback, or user reactions, route to `comment-monitoring`.
- If the user wants end-to-end competitor monitoring, support a `full-chain` recommendation that combines:
  - `competitor-account-monitoring`
  - `brand-mention-monitoring`
  - `comment-monitoring`
- If the user wants all major supported social media platforms monitored together, support an `all-core-platforms` recommendation across:
  - `Twitter/X`
  - `TikTok`
  - `Reddit`
  - `YouTube`
- If the user already has direct content URLs, prefer detail or comments templates over search templates.
- If the user needs both content discovery and comments, recommend the smallest valid workflow.
- Use `octoparse-link-template` to validate multi-template chains before presenting them as true workflows.
- Do not treat "paired strategy" and "true output-to-input chain" as the same thing.

## Output Preferences

Supported modes:

- `quick answer`
  - recommend templates or workflows only
- `task setup`
  - recommend templates and prepare the user for task creation
- `run and sample`
  - recommend templates and indicate the best sample-first workflow
- `export-ready`
  - recommend templates and indicate the best production-ready collection workflow

## Workflow

1. Classify the request using `references/request-classifier.md`.
2. Decide whether the request belongs to one track, multiple tracks, or a `full-chain` workflow.
3. Check whether the request targets one platform, multiple platforms, or `all-core-platforms`.
4. Check the `core` shortlist first.
5. Only read the `secondary` shortlist when platform, language, or region clearly requires it.
6. If the recommendation needs more than one template, validate the workflow with `octoparse-link-template`.
7. Return a concise recommendation with reasons, risks, and next step.

## Response Contract

Always provide:

### Track
- the selected monitoring track

### Platform Fit
- which platform family fits the request best

### Recommended Template or Workflow
- one primary recommendation first
- alternatives only when they materially help

### Why This Fits
- what the template is good at
- why it matches the request

### Risks and Limits
- note login limits, comment limits, or platform constraints
- distinguish collection from downstream analysis

### Next Step
- what the user should provide next if task execution is needed

## What Not to Do

Do not:

- promise sentiment analysis as a native template capability
- recommend the full social media catalog by default
- recommend secondary platforms when a core platform already fits
- confuse content discovery with comment collection
- present an unvalidated multi-template workflow as if it were confirmed

## Success Condition

This skill succeeds when the user gets:

- a clear monitoring track
- a small, defensible shortlist recommendation
- a platform-appropriate template choice
- realistic guidance about what Octoparse collects versus what AI analysis should do next
