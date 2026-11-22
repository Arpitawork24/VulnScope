from pathlib import Path
from analyzer.ast_parser import parse_source, extract_function_calls

file_path = Path("sample_codes/vulnerable_code.py")

code = file_path.read_text(encoding="utf-8")

tree = parse_source(code)
calls = extract_function_calls(tree)

print("\nFUNCTION CALLS FOUND:\n")

for call in calls:
    print(call)