# Delivery Modes

Use this file to decide how far the writer skill should go.

## Supported delivery modes

### `design-only`

Use when:

- the scenario is still being defined
- key inputs are missing
- the user only wants the framework

Output:

- scenario boundary
- file plan
- classifier plan
- shortlist plan
- open input gaps

### `draft-package`

Use when:

- the scenario is defined
- enough inputs exist to draft files
- the user wants a first pass but not final repo actions yet

Output:

- draft `SKILL.md`
- draft references
- draft evals

### `full-package`

Use when:

- the required inputs are present
- the repo path is known
- the user wants the actual skill package created

Output:

- files written into the repo
- basic validation completed

### `package-and-commit`

Use when:

- full-package conditions are met
- the user wants git actions performed

Output:

- files written
- `git add`
- `git commit`

### `PR-ready`

Use when:

- the package has already been created
- the branch context is ready
- the user wants a handoff that is ready to push and open as a PR

Output:

- package written
- committed changes
- push instructions
- concise PR summary

## Git action guardrails

Only perform git actions when:

- the repo path is explicit
- the target branch is explicit or safe to create
- the user has approved repository changes

Do not assume PR creation itself is always available from the current environment.

If direct PR creation is unavailable, stop at PR-ready and provide the next commands.
