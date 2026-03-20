# Scenario Structure

Use this file when deciding what assets a new Octoparse scenario skill should include.

## Default package

Most scenario skills should start with:

```text
scenario-skill/
  SKILL.md
  references/
    request-classifier.md
    scenario-shortlist.json
    scenario-guidance.md
  evals/
    evals.json
    trigger-evals.json
```

## When to add `core` and `regional`

Split the shortlist when:

- geography materially changes the best template family
- language changes template suitability
- regional directories are first-class recommendations
- the default shortlist is starting to feel noisy or overloaded

Use:

- `scenario-shortlist-core.json`
- `scenario-shortlist-regional.json`

Keep an entry manifest only when it improves routing clarity.

## Minimum classifier expectations

The request classifier should usually decide:

- primary track
- source preference
- region or language
- whether enrichment is needed
- whether contact details are needed
- whether monitoring or review signals are needed

## Minimum shortlist fields

Each shortlisted template should usually include:

- `template_id`
- `name`
- `slug`
- `track` when already known, or enough role/context for the writer skill to infer it
- `role`
- `recommended_when`
- `key_inputs`
- `key_outputs`
- `keep_reason`

Important:

- do not require teammates to pre-label `track` if they have already grouped templates by scenario or described each template's role
- the writer skill should infer `track` when the scenario and template roles make that straightforward

## Eval asset expectations

`evals.json`:

- recommendation and workflow quality
- classifier routing
- mode selection
- invalid recommendation avoidance

`trigger-evals.json`:

- should-trigger positives
- adjacent-skill negatives
- near-miss edge cases
