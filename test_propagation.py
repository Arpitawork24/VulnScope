from pathlib import Path

from analyzer.ast_parser import parse_source
from analyzer.taint_analysis import analyze_taint

code = Path(
    "sample_codes/propagation_test.py"
).read_text(encoding="utf-8")

tree = parse_source(code)

findings = analyze_taint(tree)

for finding in findings:
    print(finding)

print("\nTotal findings:", len(findings))