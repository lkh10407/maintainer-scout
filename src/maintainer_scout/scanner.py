from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

TEXT_EXTENSIONS = {
    ".cfg",
    ".go",
    ".js",
    ".json",
    ".md",
    ".py",
    ".rs",
    ".toml",
    ".ts",
    ".txt",
    ".yaml",
    ".yml",
}

IGNORED_DIRS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "__pycache__",
    "dist",
    "node_modules",
}


@dataclass(frozen=True)
class Finding:
    category: str
    message: str
    passed: bool
    weight: int

    def to_dict(self) -> dict[str, object]:
        return {
            "category": self.category,
            "message": self.message,
            "passed": self.passed,
            "weight": self.weight,
        }


@dataclass(frozen=True)
class Report:
    root: str
    score: int
    findings: list[Finding]
    markers: dict[str, int]

    def to_dict(self) -> dict[str, object]:
        return {
            "root": self.root,
            "score": self.score,
            "findings": [finding.to_dict() for finding in self.findings],
            "markers": self.markers,
        }


def scan_repository(root: Path) -> Report:
    findings = [
        _check_any(root, "documentation", "README found", "Add a README.md", 16, ["README.md"]),
        _check_any(root, "licensing", "License found", "Add a LICENSE file", 14, ["LICENSE", "LICENSE.md"]),
        _check_any(
            root,
            "contributors",
            "Contributing guide found",
            "Add CONTRIBUTING.md",
            10,
            ["CONTRIBUTING.md", ".github/CONTRIBUTING.md"],
        ),
        _check_any(
            root,
            "security",
            "Security policy found",
            "Add SECURITY.md",
            10,
            ["SECURITY.md", ".github/SECURITY.md"],
        ),
        _check_any(
            root,
            "governance",
            "Code of conduct found",
            "Add CODE_OF_CONDUCT.md",
            6,
            ["CODE_OF_CONDUCT.md", ".github/CODE_OF_CONDUCT.md"],
        ),
        _check_any(
            root,
            "automation",
            "CI workflow found",
            "Add a GitHub Actions workflow",
            14,
            [".github/workflows/ci.yml", ".github/workflows/ci.yaml"],
        ),
        _check_any(
            root,
            "support",
            "Issue template found",
            "Add GitHub issue templates",
            6,
            [".github/ISSUE_TEMPLATE/bug_report.md", ".github/ISSUE_TEMPLATE/config.yml"],
        ),
        _check_any(
            root,
            "releases",
            "Changelog found",
            "Add CHANGELOG.md",
            8,
            ["CHANGELOG.md", "HISTORY.md", "RELEASES.md"],
        ),
        _check_any(
            root,
            "packaging",
            "Package metadata found",
            "Add package metadata such as pyproject.toml or package.json",
            8,
            ["pyproject.toml", "package.json", "Cargo.toml", "go.mod"],
        ),
        _check_any(root, "tests", "Tests found", "Add tests", 8, ["tests", "test"]),
    ]
    score = sum(finding.weight for finding in findings if finding.passed)
    return Report(root=str(root), score=min(score, 100), findings=findings, markers=_count_markers(root))


def _check_any(
    root: Path,
    category: str,
    passed_message: str,
    failed_message: str,
    weight: int,
    candidates: list[str],
) -> Finding:
    passed = any((root / candidate).exists() for candidate in candidates)
    return Finding(
        category=category,
        message=passed_message if passed else failed_message,
        passed=passed,
        weight=weight,
    )


def _count_markers(root: Path) -> dict[str, int]:
    counts = {"TODO": 0, "FIXME": 0, "XXX": 0}
    for path in _iter_text_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line in lines:
            if not _looks_like_comment(line):
                continue
            for marker in counts:
                counts[marker] += line.count(marker)
    return {marker: count for marker, count in counts.items() if count}


def _looks_like_comment(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith(("#", "//", "/*", "*", "<!--"))


def _iter_text_files(root: Path):
    for path in root.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            yield path
