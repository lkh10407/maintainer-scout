# Current State

## What Works

- Local repository scanning
- Markdown report output
- JSON report output
- Score threshold with `--fail-under`
- Detection for common OSS files:
  - README
  - LICENSE
  - CONTRIBUTING
  - SECURITY
  - CODE_OF_CONDUCT
  - issue templates
  - changelog
  - package metadata
  - tests
- Maintenance marker counting for comment-style `TODO`, `FIXME`, and `XXX`

## Current Constraints

- No network scan mode
- No GitHub API integration
- No ecosystem-specific dependency analysis
- No SARIF or GitHub annotation output
- Scoring is intentionally simple and broad
- GitHub Actions workflow is not committed yet because the current push token does not include `workflow` scope

## Verification

Current baseline:

```bash
python3 -m pytest
PYTHONPATH=src python3 -m maintainer_scout . --fail-under 80
```
