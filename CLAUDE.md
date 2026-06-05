# CLAUDE.md

Use this alongside `AGENTS.md` when working with Claude or other coding assistants.

## Working Style

- Read `AGENTS.md` first.
- Keep changes small and reviewable.
- Prefer direct, boring solutions over clever abstractions.
- Preserve the no-runtime-dependency goal unless a dependency clearly earns its weight.
- Treat scanner output as a public contract once released.

## Good Tasks For AI Assistance

- Drafting or improving rule descriptions
- Generating test cases for repository layouts
- Summarizing scan results into release-readiness notes
- Reviewing scoring changes for false positives
- Improving documentation for maintainers

## Caution Areas

- Do not invent popularity metrics, downloads, or adoption claims.
- Do not send private repository contents to external APIs without explicit opt-in.
- Do not add security claims that the scanner cannot support.
- Do not make the score feel more precise than it is.

