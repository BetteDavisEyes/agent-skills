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

Read `references/request-classifier.md` first, then `references/lead-track-guidance.md`.

## Evidence Priority

Use evidence in this order:

1. `references/request-classifier.md`
2. `references/lead-template-shortlist-core.json`
3. `references/lead-template-shortlist-regional.json` when geography, language, or locale-specific sources matter
4. `references/lead-track-guidance.md`
5. `octoparse-link-template` when a recommendation involves more than one template
6. template-specific docs in the sibling `templates/` directory, when available
7. Octoparse MCP template detail tools
8. official Octoparse template pages

Do not search the whole template catalog first unless the split shortlist clearly cannot satisfy the request.

## Recommendation Rules

Apply these rules strictly:

- Prefer the curated shortlist over the full lead-generation category.
- Use the core shortlist by default and widen to the regional shortlist only when the classifier says geography or language materially affects the recommendation.
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
- [ ] Step 2: Run the request classifier
- [ ] Step 3: Read the core shortlist first
- [ ] Step 4: Decide output preference
- [ ] Step 5: Select the best template or chain
- [ ] Step 6: Validate with template details if needed
- [ ] Step 7: Create or recommend the task workflow
- [ ] Step 8: Summarize fields, risks, and next steps
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

### Step 2: Run the Request Classifier

Open `references/request-classifier.md`.

Use it to normalize:

- lead track
- whether contact details are actually required
- source preference
- whether regional routing is needed
- whether reviews are actually required

### Step 3: Read the Core Shortlist First

Open `references/lead-template-shortlist.json` as the entry manifest, then load `references/lead-template-shortlist-core.json`.

Use the core shortlist to quickly determine:

- which primary defaults fit the request
- which templates are discovery templates versus enrichment templates
- which typical chains are preferred
- what key inputs and outputs matter
- whether a core template already satisfies the request

Only load `references/lead-template-shortlist-regional.json` when the classifier indicates that geography, language, or locale-specific sources matter.

### Step 4: Decide Output Preference

Choose one of:

- `quick answer`
- `task setup`
- `run and sample`
- `export-ready`

If execution is requested and one essential detail is missing, ask one concise follow-up. Prioritize:

- target source or geography
- desired lead fields
- result size

### Step 5: Select the Best Template or Chain

Use the shortest chain that satisfies the user.

Keep the output focused:

- one primary chain
- alternatives only if they cover a materially different need, geography, or language

If the recommendation involves more than one template:

- use `octoparse-link-template` to validate that the chain is a real output-to-input workflow before presenting it
- do not rely on similar field names or similar search inputs alone
- if the relationship is only a paired strategy rather than a true chain, say so explicitly

### Step 6: Validate with Template Details If Needed

If the shortlist is not enough, use Octoparse MCP template detail tools to confirm:

- required inputs
- placeholders
- constraints or remarks
- whether the template is a better fit than the shortlist default

Use sibling `templates/` docs when available to refine or override high-level assumptions.

### Step 7: Create or Recommend the Task Workflow

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

### Step 8: Summarize Fields, Risks, and Next Steps

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
