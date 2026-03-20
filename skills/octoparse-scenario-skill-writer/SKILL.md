---
name: octoparse-scenario-skill-writer
description: Create or redesign Octoparse scenario skills that turn a business workflow into a reusable skill package. Use this skill whenever the user wants to build a new Octoparse scenario skill such as lead generation, competitor monitoring, market research, e-commerce intelligence, or social media intelligence; when they want to turn a proven workflow into a skill; or when they need help designing a classifier, shortlist, evals, trigger-evals, or core/regional split for an Octoparse scenario.
---

# Octoparse Scenario Skill Writer

Use this skill to design Octoparse scenario skills that sit above individual templates and MCP tools.

This is a skill-writing workflow, not a task-execution workflow.

Use it when the user wants to create a reusable scenario skill for a business outcome such as:

- lead generation
- competitor monitoring
- market research
- e-commerce intelligence
- social media intelligence

## What this skill produces

This skill helps produce a scenario skill package with:

- `SKILL.md`
- `references/request-classifier.md`
- `references/<scenario>-shortlist.json`
- optional:
  - `references/<scenario>-shortlist-core.json`
  - `references/<scenario>-shortlist-regional.json`
- `references/<scenario>-guidance.md`
- `evals/evals.json`
- `evals/trigger-evals.json`

Read `references/scenario-structure.md` when deciding what files the new scenario should include.
Read `references/input-requirements.md` to determine what the user should provide before generation.
Read `references/delivery-modes.md` before deciding how far to take implementation and git actions.

## When not to use this skill

Do not use this skill for:

- creating a single Octoparse task
- configuring parameters for one template
- validating one specific output-to-input template chain

Use these instead:

- `octoparse-template-task`
- template-specific docs
- `octoparse-link-template`

## Evidence priority

Use sources in this order:

1. the user's scenario goal and constraints
2. existing Octoparse scenario skill patterns in this repo
3. `references/scenario-structure.md`
4. `references/input-requirements.md`
5. `references/delivery-modes.md`
6. `references/asset-guidelines.md`
7. `octoparse-link-template` when the scenario needs multi-template workflow rules
8. Octoparse MCP tools and official template/category pages, when shortlist design needs source evidence

## Workflow

Copy this checklist and track progress:

```text
Task Progress:
- [ ] Step 1: Define the scenario boundary
- [ ] Step 2: Decide whether this is a true scenario skill
- [ ] Step 3: Identify internal tracks
- [ ] Step 4: Design the request classifier
- [ ] Step 5: Design the shortlist strategy
- [ ] Step 6: Define chain-validation rules
- [ ] Step 7: Draft SKILL.md
- [ ] Step 8: Draft references
- [ ] Step 9: Draft evals and trigger-evals
- [ ] Step 10: Decide delivery mode and repository actions
- [ ] Step 11: Check for weight, overlap, and anti-patterns
```

### Step 1: Define the Scenario Boundary

State clearly:

- what business workflow the scenario skill should cover
- what it should not cover
- how it differs from a category page, an MCP tool, and a template-task skill

If the scenario is too broad, narrow it before writing anything else.

### Step 1.5: Collect the Input Contract

Before generating files, determine whether the user has provided enough scenario data.

Use `references/input-requirements.md` to classify what is available:

- required inputs
- strongly recommended inputs
- optional but useful inputs

If important inputs are missing:

- identify exactly what is missing
- make the smallest reasonable assumption only when it is low risk
- otherwise stop at design mode instead of forcing a partial package

### Step 2: Decide Whether This Is a True Scenario Skill

Only continue if the user needs a reusable scenario-level workflow.

Good candidates:

- the user wants a curated workflow above many templates
- the user wants to route from business intent to recommended templates
- the user wants reusable classifier and shortlist logic

Bad candidates:

- the user just needs one template configured
- the user only wants one template chain validated

### Step 3: Identify Internal Tracks

Check whether the scenario naturally splits into distinct subtracks.

Examples:

- local business vs B2B company
- brand monitoring vs product monitoring
- marketplace research vs direct-site research

If tracks exist, define them before writing the shortlist.

### Step 4: Design the Request Classifier

Create a `request-classifier.md` that routes user intent before template selection.

Typical classifier dimensions:

- primary track
- source preference
- region or language
- whether enrichment is required
- whether contact details are required
- whether reviews or monitoring signals are required

The classifier should also decide whether a regional shortlist is needed.

Do not require the user to hand-label tracks if the scenario can infer them from template roles or scenario goals.

### Step 5: Design the Shortlist Strategy

Do not start from the full template catalog.

First decide:

- what the core shortlist should contain
- whether a regional shortlist is necessary
- what makes a template worth keeping in the shortlist

Use a core/regional split when:

- geography changes the recommended source
- language changes template suitability
- regional directories materially outperform global defaults

If the user has already provided a curated shortlist:

- use it as the primary source
- do not widen to the full catalog unless the shortlist is clearly incomplete

### Step 6: Define Chain-Validation Rules

If the scenario recommends multi-template workflows:

- use `octoparse-link-template` to validate output-to-input chains
- separate true chains from paired strategies
- do not assume similar inputs imply a valid chain

If no multi-template workflow is needed, say so explicitly.

### Step 7: Draft `SKILL.md`

The scenario `SKILL.md` should usually include:

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

Keep the main skill lean. Move template-heavy details into `references/`.

### Step 8: Draft References

Create focused references rather than one giant file.

Read `references/asset-guidelines.md` for the default responsibilities of:

- `request-classifier.md`
- shortlist files
- guidance files
- eval assets

Prefer a small number of files with clear roles over a large number of overlapping files.

### Step 10: Decide Delivery Mode and Repository Actions

Use `references/delivery-modes.md` to choose how far to go.

Supported delivery levels:

- design-only
- draft-package
- full-package
- package-and-commit
- PR-ready

Only perform repository actions when:

- the repo path is known
- the target branch is known or can be safely created
- the user wants files generated in the repo
- the required scenario inputs are sufficient

If repository actions are allowed, the skill may:

- create files
- update references
- run basic validation
- `git add`
- `git commit`
- give push and PR-ready instructions

### Step 9: Draft Evals and Trigger-Evals

Create:

- `evals/evals.json`
- `evals/trigger-evals.json`

`evals.json` should test:

- track selection
- source routing
- mode selection
- shortlist choice
- regional fallback
- chain choice
- avoidance of invalid recommendations

`trigger-evals.json` should test:

- should-trigger prompts for each major track
- near-miss negatives that belong to adjacent skills
- negative cases for task execution, chain validation, and skill maintenance

### Step 11: Check for Weight, Overlap, and Anti-Patterns

Before finishing, check:

- is the main `SKILL.md` too heavy?
- should some detail move into `references/`?
- are there duplicated rules across files?
- does the skill overlap too much with `octoparse-template-task` or `octoparse-link-template`?

Read `references/asset-guidelines.md` again if the package feels too heavy.

## Response contract

When helping the user design a new scenario skill, always provide:

### Scenario Boundary
- what the skill should cover
- what it should not cover

### Proposed Tracks
- the internal tracks, if any

### Classifier Plan
- what dimensions the request classifier should use

### Shortlist Plan
- whether to keep one shortlist or split into core/regional
- how templates will be selected

### Asset Plan
- what files will be created

### Input Requirements
- what the user must still provide
- what was inferred

### Delivery Mode
- whether the result stops at design
- or continues through package generation and git-ready output

### Risks
- overlap risks
- weight risks
- evaluation gaps

## What not to do

Do not:

- stuff the full template catalog into one `SKILL.md`
- skip the classifier when the scenario clearly needs routing
- assume every scenario needs core/regional splitting
- merge chain validation into the scenario skill when `octoparse-link-template` should do it
- treat `evals.json` as enough without trigger coverage
- require perfect template metadata from the user before making any progress
- require the user to hand-label `track` when the writer can infer it from scenario structure and template roles

## Success condition

This skill succeeds when the user ends up with a scenario skill package that:

- has a clear boundary
- has a usable classifier
- has a defensible shortlist
- has realistic evals and trigger-evals
- clearly states what inputs were required from the user
- can stop at design or continue to git-ready delivery when appropriate
- stays compact enough for reliable retrieval and maintenance
