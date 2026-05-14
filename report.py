import json
import os
from datetime import datetime
from typing import Dict

def save_report(report: Dict, format: str = "markdown") -> str:
    project_name = report.get("project_name", "unknown").replace(" ", "-").lower()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    if format == "json":
        filename = f"report-{project_name}-{timestamp}.json"
        content = json.dumps(report, indent=2)
    else:
        filename = f"report-{project_name}-{timestamp}.md"
        content = _format_markdown(report)

    with open(filename, "w") as f:
        f.write(content)

    return filename

def _format_markdown(report: Dict) -> str:
    score = report["trust_score"]
    if score >= 80:
        emoji = "🟢"
    elif score >= 60:
        emoji = "🟡"
    elif score >= 40:
        emoji = "🟠"
    else:
        emoji = "🔴"

    lines = [
        f"# TrustMech Report: {report['project_name']}",
        f"",
        f"URL: {report['url']}",
        f"Trust Score: {emoji} {report['trust_score']}/100",
        f"Generated: {datetime.now().isoformat()}",
        f"",
        f"## Summary",
        f"{report['summary']}",
        f"",
        f"## Red Flags 🚩",
    ]

    if report["red_flags"]:
        for flag in report["red_flags"]:
            lines.append(f"- {flag}")
    else:
        lines.append("- None detected")

    lines += [
        f"",
        f"## Green Flags ✅",
    ]

    if report["green_flags"]:
        for flag in report["green_flags"]:
            lines.append(f"- {flag}")
    else:
        lines.append("- None detected")

    lines += [
        f"",
        f"## Social Links",
    ]

    for platform, link in report.get("social_links", {}).items():
        lines.append(f"- {platform}: {link}")

    return "\n".join(lines)
