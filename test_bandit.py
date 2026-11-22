from analyzer.bandit_runner import run_bandit

findings = run_bandit("sample_codes")

print("\nVULNSCOPE - BANDIT BASELINE REPORT")
print("=" * 50)

for finding in findings:
    print(f"\nTool: {finding['tool']}")
    print(f"Rule: {finding['rule_id']}")
    print(f"Severity: {finding['severity']}")
    print(f"Confidence: {finding['confidence']}")
    print(f"File: {finding['file']}")
    print(f"Line: {finding['line']}")
    print(f"Problem: {finding['message']}")

print("\nTotal Bandit findings:", len(findings))