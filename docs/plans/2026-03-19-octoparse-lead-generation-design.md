# Octoparse Lead Generation Skill Design

## Goal

Create an `octoparse-lead-generation` skill that turns a lead-generation request into a small set of recommended Octoparse templates or template chains.

This skill does not replace the template category pages or Octoparse MCP tools. It sits above them and narrows the decision space:

- category pages answer "what exists"
- MCP tools answer "what can be searched, inspected, created, and run"
- this skill answers "for a lead-generation request, what should the agent recommend and do first"

## Why This Skill Exists

Users can already browse the Lead Generation category and agents can already call Octoparse MCP tools. The missing layer is a stable workflow that:

- maps a natural-language lead request to a small recommended template set
- prefers internally approved templates over the full catalog
- separates `local-business-leads` from `b2b-company-leads`
- avoids over-recommending similar templates, especially in large families such as Google Maps
- explains when a template is for discovery versus enrichment

## Scope

First version scope:

- local-business leads
- B2B company leads
- shortlist-first recommendations
- task recommendation and task execution guidance
- export preference handling

Out of scope for the first version:

- exhaustive coverage of every lead-generation template
- full template-chain reasoning across the whole Octoparse catalog
- CLI or code-first instructions for end users

## Key Product Decisions

### 1. Shortlist-first

Do not search the entire Lead Generation category by default.

Start from a curated shortlist of approved stable templates. Use the broader category or template search only when the shortlist cannot satisfy the request.

### 2. Two internal tracks, one skill

The skill supports two lead tracks:

- `local-business-leads`
- `b2b-company-leads`

Keep them inside one skill for now. This makes triggering easier when the user does not know template names or even the lead type.

### 3. Recommendation over raw choice

Do not dump many templates on the user.

Default behavior:

- one primary recommendation
- one or two alternatives only if they are meaningfully different

### 4. MCP-first execution, no CLI burden

The end user should not need to write commands, JSON payloads, or template IDs.

The agent should use Octoparse MCP tools internally when execution is requested.

### 5. Export preferences matter

Lead-generation requests differ by delivery intent. The skill should support:

- quick answer in chat
- task setup only
- run and sample
- export-ready workflow

## Prerequisites

The skill assumes:

- Octoparse MCP is connected
- OAuth authentication is completed
- the agent can access template search, template detail, and task creation tools

If MCP is unavailable, the skill can still recommend templates from the shortlist, but should not pretend it can create or run tasks.

## Curated Template Strategy

Use a slim reference file instead of putting the shortlist into `SKILL.md`.

Reasons:

- better retrieval efficiency
- easier future expansion
- easier review and update workflow
- keeps `SKILL.md` focused on behavior, not inventory

## Initial Shortlist

### local-business-leads

- `1577 Google Maps Scraper`
- `941 Google Maps Reviews Scraper`
- `1463 Superpages Scraper`
- `944 Yellow Pages Scraper (Cloud)`
- `1683 Gelbe Seiten Details Scraper (Cloud by URLs)`

### b2b-company-leads

- `15 Google Search Scraper`
- `2150 Google Search Email Finder (Premium)`

## Important Recommendation Rules

- Amazon-style product templates are not lead-generation defaults.
- Review-only templates are not treated as lead-discovery templates.
- Within Google Maps, prefer `1577 Google Maps Scraper` as the primary discovery template.
- Keep `941 Google Maps Reviews Scraper` as enrichment, not as the first discovery step.
- Do not recommend a large family of near-duplicate templates unless the shortlist is insufficient.

## Output Shape

The skill should always produce:

- recommended template or template chain
- why it fits the request
- expected fields
- risks and limits
- next enrichment step

If the user wants action, it should also decide an output preference:

- quick answer
- task setup
- run and sample
- export-ready

## Planned Files

- `skills/octoparse-lead-generation/SKILL.md`
- `skills/octoparse-lead-generation/references/lead-template-shortlist.json`
- `skills/octoparse-lead-generation/references/lead-track-guidance.md`

