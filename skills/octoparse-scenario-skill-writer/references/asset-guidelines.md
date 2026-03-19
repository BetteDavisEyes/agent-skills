# Asset Guidelines

Use this file when deciding where to place scenario-skill logic.

## Keep `SKILL.md` focused on workflow

The main `SKILL.md` should carry:

- purpose
- triggers
- workflow
- evidence priority
- collaboration rules
- response contract

Move bulky domain detail out of the main file when it starts to slow retrieval or duplicate references.

## Suggested asset roles

### `request-classifier.md`

Put:

- routing dimensions
- decision matrix
- examples
- regional trigger rules

### shortlist JSON files

Put:

- kept templates only
- role of each template
- key inputs and outputs
- recommendation hints

Do not put long prose here.

### guidance markdown

Put:

- recommended defaults
- common chains
- regional notes
- exceptions

### `evals/evals.json`

Put:

- task-style prompts
- expected outputs
- assertions

### `evals/trigger-evals.json`

Put:

- should-trigger and should-not-trigger queries
- grouping labels when helpful

## Anti-patterns

Avoid:

- repeating the same rule in three files
- storing the full catalog when only a shortlist is needed
- turning JSON indexes into prose documents
- putting implementation detail into trigger eval files
