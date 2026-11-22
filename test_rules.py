
from pathlib import Path

from analyzer.ast_parser import (
    parse_source,
    extract_function_calls
)

from analyzer.rule_engine import analyze_function_calls


file_path = Path("sample_codes/vulnerable_code.py")

code = file_path.read_text(encoding="utf-8")

tree = parse_source(code)

calls = extract_function_calls(tree)

findings = analyze_function_calls(calls)

print("\nVULNSCOPE SECURITY REPORT")
print("=" * 50)

for finding in findings:
    print(f"\nRule ID: {finding['rule_id']}")
    print(f"Severity: {finding['severity']}")
    print(f"Function: {finding['function']}")
    print(f"Line: {finding['line']}")
    print(f"Problem: {finding['message']}")
    print(f"Recommendation: {finding['recommendation']}")

print("\nTotal potential issues:", len(findings))
