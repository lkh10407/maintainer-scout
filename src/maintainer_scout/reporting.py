from __future__ import annotations

from .scanner import Report


def render_markdown(report: Report) -> str:
    lines = [
        "# Maintainer Scout Report",
        "",
        f"Repository: `{report.root}`",
        f"Score: **{report.score}/100**",
        "",
        "## Strengths",
    ]

    passed = [finding for finding in report.findings if finding.passed]
    if passed:
        lines.extend(f"- {finding.message}" for finding in passed)
    else:
        lines.append("- No strong maintenance signals found yet.")

    lines.extend(["", "## Improvements"])
    failed = [finding for finding in report.findings if not finding.passed]
    if failed:
        lines.extend(
            f"- **{finding.category}**: {finding.message} ({finding.weight} pts)"
            for finding in failed
        )
    else:
        lines.append("- No improvements detected by the current rules.")

    if report.markers:
        lines.extend(["", "## Maintenance Markers"])
        for marker, count in sorted(report.markers.items()):
            lines.append(f"- `{marker}`: {count}")

    lines.extend(
        [
            "",
            "## Next Steps",
            "- Pick the highest-weight missing signal and add it before the next release.",
            "- Re-run this report in CI to keep maintenance basics visible.",
        ]
    )
    return "\n".join(lines)

