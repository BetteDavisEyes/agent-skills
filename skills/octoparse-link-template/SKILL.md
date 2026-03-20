---
name: octoparse-link-template
description: Help users design and validate Octoparse template chains. Use this skill whenever the user asks which Octoparse templates should be linked together, whether one Octoparse template's output can feed another template's input, how to enrich data across listing/detail/review/contact templates, or when a template seems insufficient and the user needs downstream templates. This skill should also be used when the user describes a data goal without knowing template names, when they know one template but want to know what other templates can extend or enrich its results, or when another Octoparse skill is drafting or revising a multi-template workflow and needs chain validation before presenting it.
---

# Octoparse Link Template

Use this skill to determine whether one Octoparse template can feed another template.

This skill is for linking templates together, not just finding a single template.

Typical use cases:
- The user describes a data goal and needs a multi-template workflow.
- The user asks whether one template can connect to another.
- The user asks what downstream templates can enrich the output of a template.
- The user says a single template is not enough and wants reviews, details, contact info, or more fields.
- The user wants to know whether a field in one template's output can be reused as another template's input.

This skill supports two entry modes:
1. Goal-first
2. Template-first

## Goal-first mode

Use this mode when the user starts with a business outcome or data request.

Examples:
- "I want restaurant details, reviews, and contact enrichment."
- "I need emails, phone numbers, and reviews for Google Maps businesses."
- "I want to collect listing data first, then enrich it with comments."

Your job:
- infer which template chain best matches the requested goal
- identify required intermediate fields
- explain why the chain works
- surface missing fields and risks

## Template-first mode

Use this mode when the user already has a template in mind and wants to know what can be connected after it.

Examples:
- "What can I run after Google Maps Listings Scraper?"
- "Can this template feed the reviews template?"
- "This template is not enough. What else should I use after it?"

Your job:
- identify what the template can likely output
- identify which downstream templates can consume those outputs
- explain direct links vs links that require an intermediate template
- warn when a field match is inferred rather than documented

## Output contract

Always return these sections:

### Recommended Chain

Show the best template chain in order.

Format:
`Template A -> Template B -> Template C`

If there is more than one reasonable chain, show the recommended one first and briefly mention alternatives.

### Field Mapping

Explicitly map upstream output fields to downstream input fields.

Format:
- `field_from_template_A` -> `input_field_of_template_B`
- `field_from_template_B` -> `input_field_of_template_C`

Be specific about URL types and do not collapse different URL categories into one.

### Why This Chain Works

Explain the logic of the chain in plain language.

Focus on:
- what each template contributes
- why the downstream template can consume the upstream result
- why this chain is better than a weaker or shorter alternative

### Risks and Limitations

Always include risk notes.

Common risks:
- output field is inferred, not documented
- a template may not expose the exact downstream field needed
- a field may exist only for some records
- email often requires website extraction first
- reviews volume depends on public availability
- listing URLs and place detail URLs are not always interchangeable

### Possible Enrichments

Suggest what the user can add next if they want more data.

Examples:
- add a reviews template after a listing template
- add a contact or website-based enrichment step after a details template
- add a details template between listing and review when the URL type does not match directly

## Evidence priority

Use evidence in this order, from strongest to weakest:

1. Local template docs
- `TEMPLATE.md`
- `INPUT.md`
- `OUTPUT.md`
- `LIMITATIONS.md`
- `FAQ.md`
- `TIPS.md`

2. Stable template index
- `references/stable-templates.json`
- treat this file as the slim index, not the full template knowledge base
- use it first for fast filtering, category narrowing, input/output matching, and initial chain design
- do not expect it to contain every execution detail or every template nuance

3. Template-specific docs in the sibling `templates/` directory
- if a candidate template has a dedicated folder in `templates/`, read that folder after the slim index
- prefer:
  - `TEMPLATE.md`
  - `LIMITATIONS.md`
  - `FAQ.md`
- use these files to refine or override slim-index assumptions when they provide stronger evidence

4. Template input metadata
- use Octoparse MCP template detail tools when available
- input field names from template metadata are strong evidence for downstream requirements

5. Official Octoparse template detail pages
- use the template description
- use FAQ and "How to Use" sections
- use the template page's data preview or parameter definitions when visible

6. Inference
- infer only when stronger evidence is unavailable
- clearly label inferred conclusions as inferred

Never present an inferred link as fully confirmed if it is not documented.

## Decision process

Follow this process every time:

1. Identify request type
- Is the user goal-first or template-first?
- If mixed, handle both and state the recommended interpretation.

2. Normalize template names
- If the user gives an approximate or incorrect template name, normalize it to the most likely actual template.
- If there is ambiguity, say which template you are assuming.

3. Check the slim index first
- read `references/stable-templates.json` before opening heavier sources
- use it to shortlist likely templates by category, record granularity, input fields, output fields, and collection stages
- use `placeholder` and `remark` to clarify ambiguous input semantics, especially when field names are inconsistent

4. Open template-specific docs only when needed
- if the shortlisted template has a folder in the sibling `templates/` directory, read its `TEMPLATE.md`, `LIMITATIONS.md`, and `FAQ.md`
- use these files to resolve ambiguity, special constraints, or language/site-specific behavior

5. Determine the target data goal
Examples:
- listing discovery
- details enrichment
- review collection
- contact enrichment
- email enrichment
- article body extraction
- product detail expansion

6. Determine required downstream input fields
Read the downstream template input requirements first.

Examples:
- review scraper may require `place detail URL`
- detail scraper may require `listing URL` or `product URL`
- contact enrichment may require `website URL`

7. Determine candidate upstream output fields
Use documented outputs first.
If output docs are missing, infer carefully from template description and data preview.

8. Compare field compatibility
Decide whether the upstream output can feed the downstream input:
- directly
- indirectly through a transformation
- not at all
- only through an intermediate template

9. Recommend the best chain
Prefer:
- stable MCP-supported templates
- chains with documented field compatibility
- fewer steps when data quality is equal
- richer chains when the user's goal explicitly requires enrichment

10. Explain risks
Always note:
- inferred links
- field uncertainty
- likely missing fields
- format mismatches
- volume limits if relevant

## Important linking rules

Read `references/linking-rules.md` before making final linking decisions.

Apply these principles strictly:

### Do not treat all URLs as interchangeable

Distinguish:
- search result URL
- listing page URL
- place details page URL
- business website URL
- product listing URL
- product detail URL
- review page URL
- article page URL

A chain is only direct if the downstream template accepts the exact type of URL or field the upstream template produces.

### Do not claim email is directly available unless documented

A template that outputs:
- place URL
- phone
- website
does not automatically output email.

If email is needed, it often requires:
- website extraction first
- then a website-based contact or email template

### Do not assume similar field names mean compatibility

Examples:
- `Page_URL` may be a listing page URL, not a place detail URL
- `URL` may refer to different object types depending on the template
- `website` is not the same as `place URL`

### Prefer intermediate templates when necessary

If the user wants reviews but only has a listing-level output, recommend an intermediate details step if needed.

## Output field inference rules

If `OUTPUT.md` is missing, use `references/output-inference-rules.md`.

Use inference only when needed.

### High-confidence inference is allowed when:
- the template description explicitly says it extracts that field
- the data preview on the official template page shows that field
- the template category and description strongly imply a standard output shape

### Low-confidence inference should be labeled clearly

Use phrases like:
- `likely outputs`
- `appears to support`
- `based on the template description`
- `inferred from the template page`

## Stable template preference

Prefer templates marked as stable in `references/stable-templates.json`.

Remember:
- `references/stable-templates.json` is a slim retrieval index
- use it for fast first-pass reasoning
- use sibling `templates/` docs for deeper per-template validation when available

If a non-stable or undocumented template is required to complete the chain:
- say so clearly
- explain why it is still being recommended
- identify the risk of using it

## Recommended response style

Be concise but structured.
Use practical language.
Do not just say "yes" or "no".
Always give the user a usable chain or a clear reason why the chain is blocked.

## Response template

Use this structure:

## Recommended Chain
`Template A -> Template B -> Template C`

## Field Mapping
- `field_x` from `Template A` -> `input_y` in `Template B`
- `field_z` from `Template B` -> `input_k` in `Template C`

## Why This Chain Works
- Explain each step's role
- Explain why the field compatibility is valid

## Risks and Limitations
- Mention undocumented outputs
- Mention inferred field compatibility
- Mention missing fields or likely failure points

## Possible Enrichments
- Mention optional downstream templates that could extend the chain further

## Handling uncertainty

If evidence is incomplete, do not stop at uncertainty alone.
Still provide:
- the best available chain
- the confidence level
- the exact uncertain point

Example:
- `This chain is likely valid, but the output-to-input match is inferred from the template description because OUTPUT.md is not available.`

## What not to do

Do not:
- recommend a chain without field reasoning
- assume all listing templates output place detail URLs
- assume all details templates output emails
- assume all review templates accept listing URLs
- treat search-result URLs and detail URLs as interchangeable
- hide uncertainty when documentation is incomplete

## Success condition

This skill succeeds when the user can clearly understand:
- which templates to use
- in what order
- which fields connect each step
- what risks or missing links still exist
- how to enrich the chain further if needed
