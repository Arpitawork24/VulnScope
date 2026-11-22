import json
import subprocess
import sys


def run_bandit(target_path):
    command = [
        sys.executable,
        "-m",
        "bandit",
        "-r",
        target_path,
        "-f",
        "json"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if not result.stdout.strip():
        raise RuntimeError(
            f"Bandit failed: {result.stderr}"
        )

    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(
            f"Could not read Bandit's JSON report: {result.stderr}"
        )

    findings = []

    for issue in report.get("results", []):
        findings.append({
            "tool": "Bandit",
            "rule_id": issue.get("test_id"),
            "severity": issue.get("issue_severity"),
            "confidence": issue.get("issue_confidence"),
            "file": issue.get("filename"),
            "line": issue.get("line_number"),
            "message": issue.get("issue_text"),
            "cwe": issue.get("issue_cwe", {}).get("id")
        })

    return findings