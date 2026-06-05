# Contributing

Thanks for helping improve `maintainer-scout`.

## Local setup

```bash
python -m pip install -e .
python -m pip install pytest ruff
pytest
ruff check .
```

## Pull requests

- Keep changes small and explain the maintenance problem they solve.
- Add or update tests for scanner behavior.
- Update `README.md` when adding user-facing CLI options.

## Rule changes

Scoring rules should be simple, explainable, and useful across many open-source projects. Avoid rules that only work for one ecosystem unless they are optional or clearly scoped.

