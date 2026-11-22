from analyzer.ast_parser import (
    parse_source,
    extract_function_calls
)
from analyzer.rule_engine import analyze_function_calls
from analyzer.taint_analysis import analyze_taint
from analyzer.bandit_runner import run_bandit


def analyze_project(target_path):

    bandit_findings = run_bandit(target_path)

    rule_findings = []
    taint_findings = []

    from pathlib import Path

    for file_path in Path(target_path).rglob("*.py"):

        code = file_path.read_text(encoding="utf-8")
        tree = parse_source(code)

        calls = extract_function_calls(tree)

        rules = analyze_function_calls(calls)
        taint = analyze_taint(tree)

        for finding in rules:
            finding["file"] = str(file_path)

        for finding in taint:
            finding["file"] = str(file_path)

        rule_findings.extend(rules)
        taint_findings.extend(taint)

    return {
        "rule_based": rule_findings,
        "taint_analysis": taint_findings,
        "bandit": bandit_findings
    }