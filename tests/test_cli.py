from pathlib import Path

from maintainer_scout.cli import main


def test_cli_returns_error_for_missing_path(tmp_path: Path) -> None:
    assert main([str(tmp_path / "missing")]) == 2


def test_cli_fail_under(tmp_path: Path, capsys) -> None:
    (tmp_path / "README.md").write_text("# Demo\n", encoding="utf-8")

    exit_code = main([str(tmp_path), "--fail-under", "100"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Maintainer Scout Report" in captured.out

