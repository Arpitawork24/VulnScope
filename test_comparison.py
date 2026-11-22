from analyzer.comparison import analyze_project

results = analyze_project("sample_codes")

for tool, findings in results.items():

    print(f"\n{tool.upper()} RESULTS")
    print("=" * 50)

    for finding in findings:
        print(finding)

    print("Total findings:", len(findings))