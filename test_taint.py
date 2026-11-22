
from pathlib import Path

from analyzer.ast_parser import parse_source
from analyzer.taint_analysis import analyze_taint


code = Path(
    "sample_codes/vulnerable_code.py"
).read_text(encoding="utf-8")

tree = parse_source(code)

findings = analyze_taint(tree)

print("\nVULNSCOPE TAINT ANALYSIS REPORT")
print("=" * 50)

for finding in findings:
    print(f"\nFunction: {finding['function']}")
    print(f"Variable: {finding['variable']}")
    print(f"Line: {finding['line']}")
    print(f"Problem: {finding['message']}")

print("\nTotal taint findings:", len(findings))
