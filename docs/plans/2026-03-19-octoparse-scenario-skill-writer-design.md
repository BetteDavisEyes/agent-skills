# Octoparse Scenario Skill Writer Design

## Goal

Create a reusable writer skill that helps build Octoparse scenario skills such as:

- lead-generation
- competitor-monitoring
- market-research
- e-commerce-intelligence
- social-media-intelligence

The writer skill should not execute Octoparse tasks directly. Its purpose is to turn a business scenario into a maintainable workflow skill package.

## Why this skill exists

Octoparse already has:

- template categories
- template-detail and task-execution MCP tools
- template-task and link-template skills

What is still missing is a repeatable way to create scenario-level skills that:

- narrow a large template catalog into a defensible shortlist
- classify user requests before recommending templates
- decide when multi-template workflows are valid
- define how to test recommendation quality and trigger quality

This writer skill captures that process so future scenario skills do not need to be invented from scratch.

## Scope

Use this skill when the user wants to create or redesign an Octoparse scenario skill.

Examples:

- create a competitor-monitoring skill
- design a market-research scenario skill
- turn our e-commerce intelligence workflow into a reusable skill
- build a social-media intelligence skill with regional variants

Do not use this skill for:

- creating a single Octoparse task
- configuring one template's inputs
- validating one specific template chain

Those belong to:

- `octoparse-template-task`
- template-specific docs
- `octoparse-link-template`

## Required outputs

The writer skill should guide the model to produce a scenario skill package with these default parts:

- `SKILL.md`
- `references/request-classifier.md`
- `references/<scenario>-shortlist.json`
- optional split references:
  - `references/<scenario>-shortlist-core.json`
  - `references/<scenario>-shortlist-regional.json`
- `references/<scenario>-guidance.md`
- `evals/evals.json`
- `evals/trigger-evals.json`

## Standard workflow

The writer skill should follow this workflow:

1. Define scenario boundaries
- what the scenario solves
- what it does not solve
- how it differs from a category page, an MCP tool, and a task-execution skill

2. Identify internal tracks
- determine whether the scenario needs internal subtracks
- examples:
  - `local-business-leads` vs `b2b-company-leads`
  - brand monitoring vs product monitoring
  - marketplace intelligence vs direct-site intelligence

3. Design a request classifier
- define the minimum routing dimensions needed before recommending templates
- common dimensions:
  - primary track
  - source preference
  - region or language
  - whether enrichment is needed
  - whether reviews or monitoring signals are needed

4. Build a shortlist
- avoid starting from the full template catalog
- define a curated shortlist first
- split into `core` and `regional` when geography or language materially changes recommendations

5. Define chain rules
- identify when a single template is enough
- identify when a multi-template workflow is needed
- require `octoparse-link-template` for validating any real output-to-input chain

6. Write the scenario `SKILL.md`
- keep workflow and selection logic in the main skill
- move template-heavy detail into `references/`

7. Write evaluation assets
- `evals.json` for recommendation logic, mode selection, and workflow choice
- `trigger-evals.json` for should-trigger and should-not-trigger coverage

8. Review for weight and maintainability
- remove duplicated guidance
- ensure `references/` files have clear roles
- ensure the main skill stays compact and points to the right reference files

## Scenario skill structure

Recommended output structure:

```text
scenario-skill/
  SKILL.md
  references/
    request-classifier.md
    scenario-shortlist.json
    scenario-shortlist-core.json
    scenario-shortlist-regional.json
    scenario-guidance.md
  evals/
    evals.json
    trigger-evals.json
```

Not every scenario must split into `core` and `regional`, but the writer skill should explicitly decide whether that split is needed.

## Guidance for `SKILL.md`

The generated scenario `SKILL.md` should usually contain:

- `name`
- `description`
- scenario purpose
- prerequisites
- internal tracks
- evidence priority
- recommendation rules
- output preferences
- workflow
- response contract
- what not to do
- success condition

The writer skill should keep the main `SKILL.md` concise and move bulky template detail into `references/`.

## Guidance for the classifier

The classifier should route requests before template selection.

Minimum recommended dimensions:

- primary track
- source preference
- region or language
- whether contact details are required
- whether enrichment is required
- whether review or monitoring signals are required

The classifier should also define the conditions under which the regional shortlist must be loaded.

## Guidance for the shortlist

Each shortlisted template should usually include:

- `template_id`
- `name`
- `slug`
- `track`
- `role`
- `recommended_when`
- `key_inputs`
- `key_outputs`
- `keep_reason`

The writer skill should prefer a small, defensible shortlist over exhaustive coverage.

## Guidance for evals

`evals.json` should test:

- track selection
- source routing
- mode selection
- shortlist choice
- regional fallback
- chain choice
- avoidance of invalid recommendations

`trigger-evals.json` should test:

- positive cases for each major track
- negative cases that should belong to adjacent skills
- near-miss prompts that might incorrectly trigger

Useful trigger groups:

- `positive-<track>`
- `negative-template-task`
- `negative-link-template`
- `negative-skill-maintenance`

## Collaboration rules with other Octoparse skills

The writer skill should explicitly guide the model to:

- use `octoparse-link-template` for validating multi-template chains
- leave template execution to `octoparse-template-task` or MCP tools
- avoid merging chain validation, task execution, and scenario selection into one giant skill

## Common anti-patterns

Avoid these:

- stuffing the full template catalog into `SKILL.md`
- using category pages as a substitute for a shortlist
- skipping the request classifier
- assuming similar inputs imply a valid template chain
- writing `evals.json` but skipping trigger coverage
- leaving too much domain logic inside the main `SKILL.md`

## Recommended next step

When this design is implemented as a skill, the first real target should be a scenario with clear internal tracks and regional variants so the writer skill can exercise:

- classifier design
- shortlist design
- core/regional splitting
- trigger eval design

That makes it a strong template for future Octoparse scenario skills.
