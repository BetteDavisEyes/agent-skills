---
name: octoparse-lead-generation
description: Recommend and run Octoparse lead-generation workflows. Use this skill whenever the user wants leads, prospects, business contacts, company contacts, local business lists, outreach targets, emails, phones, websites, or lead enrichment, even if they do not know template names. This skill should also be used when a user asks for the best Octoparse templates for lead generation, wants a smaller recommended set instead of the full lead category, or needs help deciding between local-business leads and B2B company leads.
---

# Octoparse Lead Generation

Use this skill to turn a lead-generation request into a small recommended Octoparse template set or template chain.

This skill narrows the decision space:

- the category page shows what exists
- MCP tools inspect, create, and run templates
- this skill chooses the small recommended set to use first

## Prerequisites

This skill assumes:

- Octoparse MCP is connected
- OAuth authentication is completed
- the agent can access Octoparse template search, template detail, and task tools

Important:

- do not ask the end user to write CLI commands
- do not ask the end user to prepare JSON payloads unless they explicitly want that level of control
- if MCP is unavailable, you may still recommend templates from the shortlist, but you must say that task creation and execution cannot be completed from the current environment

## Core Tracks

This skill supports two internal tracks:

1. `local-business-leads`
2. `b2b-company-leads`

Read `references/lead-track-guidance.md` after opening the shortlist.

## Evidence Priority

Use evidence in this order:

1. `references/lead-template-shortlist.json`
2. `references/lead-track-guidance.md`
3. `octoparse-link-template` when a recommendation involves more than one template
4. template-specific docs in the sibling `templates/` directory, when available
5. Octoparse MCP template detail tools
6. official Octoparse template pages

Do not search the whole template catalog first unless the shortlist clearly cannot satisfy the request.

## Recommendation Rules

Apply these rules strictly:

- Prefer the curated shortlist over the full lead-generation category.
- Keep recommendations tight: one primary recommendation, then one or two alternatives only when materially helpful.
- Do not treat Amazon or generic product-review templates as lead-generation defaults.
- Do not treat review-only templates as lead-discovery templates.
- Treat `Contact Details Scraper` as the default contact-enrichment template.
- Whenever an upstream template can provide a business `website URL`, prefer chaining it into `Contact Details Scraper` for lead enrichment.
- For `b2b-company-leads`, use a tighter split:
  - if the user does not need contact details, prefer `Google Search Scraper`
  - if the user needs contact details such as email or phone, prefer `Google Search Email Finder (Premium)`
- For Google Maps, prefer `1577 Google Maps Scraper` for discovery and `941 Google Maps Reviews Scraper` only when reviews are explicitly needed.
- If the user's request is not satisfied by the shortlist, say so clearly and then widen the search using Octoparse MCP tools.

## Output Preferences

When the user asks for help, infer or confirm the delivery mode.

Supported modes:

- `quick answer`
- `task setup`
- `run and sample`
- `export-ready`

Defaults:

- guidance only -> `quick answer`
- create something -> `task setup`
- test or verify output -> `run and sample`
- list, deliverable, or large dataset -> `export-ready`

Ask at most one concise follow-up question if a missing preference would materially change execution.

## Workflow

Copy this checklist and track progress:

```text
Task Progress:
- [ ] Step 1: Determine lead track
- [ ] Step 2: Read the shortlist first
- [ ] Step 3: Decide output preference
- [ ] Step 4: Select the best template or chain
- [ ] Step 5: Validate with template details if needed
- [ ] Step 6: Create or recommend the task workflow
- [ ] Step 7: Summarize fields, risks, and next steps
```

### Step 1: Determine Lead Track

Classify the request into one of these buckets:

- `local-business-leads`
  - restaurants, salons, dentists, clinics, gyms, local stores, map listings, regional directories
- `b2b-company-leads`
  - company contacts, outreach targets, website-based lead discovery, search-engine lead discovery
- `mixed`
  - the user needs both local discovery and company/contact enrichment

If mixed, state the recommended primary track and explain why.

### Step 2: Read the Shortlist First

Open `references/lead-template-shortlist.json`.

Use it to quickly determine:

- which track applies
- which templates are primary defaults
- which templates are discovery templates versus enrichment templates
- which typical chains are preferred
- what key inputs and outputs matter
- which languages are good defaults

Do not start from the full lead-generation category unless the shortlist is clearly insufficient.

### Step 3: Decide Output Preference

Choose one of:

- `quick answer`
- `task setup`
- `run and sample`
- `export-ready`

If execution is requested and one essential detail is missing, ask one concise follow-up. Prioritize:

- target source or geography
- desired lead fields
- result size

### Step 4: Select the Best Template or Chain

Use the shortest chain that satisfies the user.

Keep the output focused:

- one primary chain
- alternatives only if they cover a materially different need, geography, or language

If the recommendation involves more than one template:

- use `octoparse-link-template` to validate that the chain is a real output-to-input workflow before presenting it
- do not rely on similar field names or similar search inputs alone
- if the relationship is only a paired strategy rather than a true chain, say so explicitly

### Step 5: Validate with Template Details If Needed

If the shortlist is not enough, use Octoparse MCP template detail tools to confirm:

- required inputs
- placeholders
- constraints or remarks
- whether the template is a better fit than the shortlist default

Use sibling `templates/` docs when available to refine or override high-level assumptions.

### Step 6: Create or Recommend the Task Workflow

If the user only wants guidance:

- recommend the best template or chain
- explain the expected inputs

If the user wants action:

- use Octoparse MCP tools to inspect template details
- create the task when enough inputs are known
- run a small sample only if requested or if it is the clearest way to verify fit

If the chain includes website-driven enrichment:

- prefer `Contact Details Scraper`
- explain that it accepts website URLs and enriches leads with emails, phones, and other contact fields

### Step 7: Summarize Fields, Risks, and Next Steps

Always include:

- the recommended template or chain
- why it fits
- the most likely output fields
- risks and limitations
- the next enrichment step, if useful

## Response Contract

Always return these sections:

### Recommended Workflow

Show the best template or template chain.

Examples:

- `Google Maps Scraper`
- `Google Maps Scraper -> Google Maps Reviews Scraper`
- `Google Maps Scraper -> Contact Details Scraper`
- `Google Search Email Finder (Premium)`

### Why This Fits

Explain why the recommendation matches the user's lead type and requested fields.

### Expected Fields

List the main fields the user should expect.

### Risks and Limitations

Always mention important caveats, such as:

- a discovery template may not return email directly
- website-based enrichment depends on an upstream website URL field
- a review template enriches local-business leads but is not a lead source on its own
- `Google Search Scraper` and `Google Search Email Finder (Premium)` are not a default direct chain just because their search inputs look similar
- for `b2b-company-leads`, `Google Search Email Finder (Premium)` should replace `Google Search Scraper` when contact details are explicitly required
- the shortlist is intentionally narrow and may exclude valid but lower-priority variants
- geography or language may require a regional directory template instead of the default English/global option

### Next Step

State the best next action:

- ask one missing execution question
- inspect template details
- create the task
- run a sample
- stop at recommendation

## What Not To Do

Do not:

- start by dumping the whole lead-generation category
- recommend many near-duplicate templates from the same family
- force the user to know template names
- force the user to write CLI commands
- treat reviews as lead discovery
- treat product/review catalog scraping as lead-generation by default
- skip website-based contact enrichment when a strong upstream website URL is already available

## Success Condition

This skill succeeds when the user gets:

- a small, defensible recommended template set
- a clear reason for the recommendation
- a path to create or run the right task without browsing dozens of templates
