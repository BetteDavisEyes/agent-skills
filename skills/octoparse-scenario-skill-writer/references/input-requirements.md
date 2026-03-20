# Input Requirements

Use this file to decide what the user must provide before the scenario skill package can be generated.

## Goal

The writer skill should help Octoparse teammates understand:

- what they must provide
- what is strongly recommended
- what is optional
- what the writer skill can infer on its own

## Required inputs

These are the minimum inputs needed to produce a useful scenario skill design:

- scenario name
- scenario goal
- scenario boundary
  - what the skill should cover
  - what it should not cover
- an initial curated template list
  - even if small
- a short explanation of what each kept template is for

Without these, the writer skill should usually stop at design discussion rather than generating a full package.

## Strongly recommended inputs

These make package generation much more reliable:

- stable template data or a stable template list
- template IDs, names, slugs, or URLs
- known default recommendations
- known exclusions
  - templates that should not be recommended
- regional or language distinctions
- known valid or invalid template chains
- example user requests

## Optional but useful inputs

These improve package quality but should not be treated as blockers:

- template output-field spreadsheets
- official category links
- example template pages
- internal FAQ notes
- previous scenario docs
- preferred output modes
  - quick answer
  - task setup
  - run and sample
  - export-ready

## What the writer skill may infer

The writer skill may infer these when evidence is strong enough:

- internal tracks
- whether a core/regional split is needed
- whether a template is discovery, enrichment, or review oriented
- whether a template belongs in the shortlist
- `track` values for shortlist records

Do not force teammates to provide these manually if the scenario and template roles already make them obvious.

## Recommended teammate handoff format

If the teammate has structured data, recommend a sheet or JSON with:

- `template_name`
- `template_id`
- `template_slug` or `template_url`
- `role`
- `recommended_when`
- `key_inputs`
- `key_outputs`
- `notes`

`track` is optional.

## Fallback rule

If some recommended inputs are missing:

- generate the highest-confidence package possible
- clearly label what was inferred
- clearly list what the teammate should provide next to improve the package
