
import ast

from analyzer.ast_parser import extract_function_calls
from analyzer.taint_analysis import analyze_taint


DANGEROUS_FUNCTIONS = {
    "eval",
    "exec",
    "os.system",
    "subprocess.Popen",
    "pickle.loads"
}


def extract_features(source_code):

    tree = ast.parse(source_code)

    calls = extract_function_calls(tree)
    taint_findings = analyze_taint(tree)

    dangerous_calls = 0
    input_sources = 0
    shell_execution = 0

    for node in ast.walk(tree):

        if not isinstance(node, ast.Call):
            continue

        function_name = get_name(node.func)

        if function_name in DANGEROUS_FUNCTIONS:
            dangerous_calls += 1

        if function_name == "input":
            input_sources += 1

        for keyword in node.keywords:
            if (
                keyword.arg == "shell"
                and isinstance(keyword.value, ast.Constant)
                and keyword.value.value is True
            ):
                shell_execution += 1

    return {
        "total_function_calls": len(calls),
        "dangerous_calls": dangerous_calls,
        "input_sources": input_sources,
        "taint_findings": len(taint_findings),
        "shell_execution": shell_execution
    }


def get_name(node):

    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        parent = get_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr

    return None
