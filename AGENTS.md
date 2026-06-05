# AGENTS.md

This file is the working guide for AI coding agents and human maintainers working on `maintainer-scout`.

## Project Purpose

`maintainer-scout` helps open-source maintainers audit repository maintenance readiness. Keep the project focused on practical, explainable checks that reduce maintainer burden.

## Project Structure

- `src/maintainer_scout/`: CLI, scanner, and report rendering code
- `tests/`: focused tests for scanner and CLI behavior
- `docs/`: roadmap, current state, sprint plans, and application notes
- `.github/`: issue and pull request templates

## How To Work

### Small Work

For work expected to take under one hour, implement directly:

- Bug fixes
- Test additions
- README or documentation edits
- Small scoring rule changes
- CLI help text improvements

Before finishing, run the smallest useful verification command, usually:

```bash
python3 -m pytest
```

### Big Work

For work expected to take more than one day, create a sprint plan before implementation:

1. Copy `docs/sprints/_template.md`
2. Create `docs/sprints/NN-short-title.md`
3. Fill in goals, done criteria, affected files, risks, and rollout plan
4. Ask for user approval before coding
5. Keep the checklist updated as work progresses
6. Update `docs/current-state.md` and `docs/roadmap.md` when the work lands

## Rule Design Principles

- Prefer checks that are useful across many open-source projects.
- Keep findings explainable in one sentence.
- Avoid ecosystem-specific assumptions unless they are optional or clearly scoped.
- Do not require network access for the default local scan.
- Keep runtime dependencies minimal.

## Stop The Line

Ask the user before:

- Adding a paid API or external SaaS integration
- Logging repository contents, secrets, or personally identifiable information
- Sending scanned source code to a remote service
- Making destructive Git history changes on `main`
- Deleting `AGENTS.md`, `CLAUDE.md`, or core documentation
- Changing scoring semantics in a way that breaks existing JSON output

## Commit Style

Use concise conventional commits:

```text
feat(scanner): add security policy check
fix(cli): return status 2 for invalid paths
docs(roadmap): add triage assistant milestone
test(scanner): cover ignored directories
```

Common types:

- `feat`
- `fix`
- `docs`
- `refactor`
- `test`
- `chore`

## Verification

Before final handoff:

- Run tests when code changed
- Run the CLI against this repository when scanner/reporting changed
- Mention any verification that could not be run
- Keep final summaries short and specific

