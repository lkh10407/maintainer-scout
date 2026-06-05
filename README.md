# maintainer-scout

`maintainer-scout` is a small CLI for open-source maintainers who want a quick, repeatable check of repository maintenance signals before a release, contributor push, or funding application.

It scans a local repository and produces a concise health report covering documentation, governance, security, automation, packaging, and test signals.

## Why this exists

Maintainers often know what is missing from a project, but that knowledge lives in their head. This tool turns common maintenance expectations into a report that can be shared in issues, pull requests, release planning notes, or onboarding docs.

## Features

- Scores repository maintenance readiness from `0` to `100`
- Detects common OSS files such as `LICENSE`, `README`, `CONTRIBUTING`, `SECURITY`, and `CODE_OF_CONDUCT`
- Checks for CI workflows, issue templates, release notes, package metadata, and test directories
- Finds common maintenance markers such as `TODO`, `FIXME`, and `XXX`
- Emits either Markdown or JSON
- Has no runtime dependencies

## Install

```bash
python -m pip install git+https://github.com/lkh10407/maintainer-scout.git
```

For local development:

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
maintainer-scout .
maintainer-scout ~/src/my-project --format json
maintainer-scout . --fail-under 75
```

Example Markdown output:

```markdown
# Maintainer Scout Report

Score: 82/100

## Strengths
- README found
- License found
- CI workflow found

## Improvements
- Add SECURITY.md
- Add issue templates
```

## Exit Codes

- `0`: scan completed and score met `--fail-under`
- `1`: scan completed but score was below `--fail-under`
- `2`: invalid input or unsupported path

## Development

```bash
python -m pip install pytest ruff
pytest
ruff check .
```

## AI-Assisted Maintenance

This repository includes lightweight working rules for AI coding agents:

- `AGENTS.md`: project workflow, safety rules, and verification expectations
- `CLAUDE.md`: assistant-specific collaboration notes
- `docs/current-state.md`: current implementation status
- `docs/roadmap.md`: planned improvements
- `docs/sprints/`: plans for larger changes

## Roadmap

- Language-specific checks for Python, JavaScript, Rust, and Go
- GitHub API mode for issue and pull request freshness signals
- SARIF output for code scanning integrations
- Suggested GitHub Actions annotations

## Contributing

Contributions are welcome. Please open an issue first for larger changes so we can keep the scope clear and maintainable.

## License

MIT
