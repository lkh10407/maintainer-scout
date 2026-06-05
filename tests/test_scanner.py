from pathlib import Path

from maintainer_scout.reporting import render_markdown
from maintainer_scout.scanner import scan_repository


def test_scan_scores_common_oss_signals(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Demo\n", encoding="utf-8")
    (tmp_path / "LICENSE").write_text("MIT\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("[project]\nname='demo'\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()

    report = scan_repository(tmp_path)

    assert report.score == 46
    assert any(finding.category == "documentation" and finding.passed for finding in report.findings)
    assert any(finding.category == "security" and not finding.passed for finding in report.findings)


def test_marker_count_ignores_git_directory(tmp_path: Path) -> None:
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "app.py").write_text("# TODO: ship it\n", encoding="utf-8")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "ignored.py").write_text("# TODO: ignore\n", encoding="utf-8")

    report = scan_repository(tmp_path)

    assert report.markers == {"TODO": 1}


def test_markdown_report_lists_improvements(tmp_path: Path) -> None:
    report = scan_repository(tmp_path)

    markdown = render_markdown(report)

    assert "# Maintainer Scout Report" in markdown
    assert "Add a README.md" in markdown
    assert "Score: **0/100**" in markdown

