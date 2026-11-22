import ast


def get_function_name(node):
    """Extract the full name of a function call."""

    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        parent = get_function_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr

    return None


def parse_source(code):
    """Convert Python source code into an Abstract Syntax Tree."""
    return ast.parse(code)


def extract_function_calls(tree):
    """Extract function calls, arguments, and line numbers."""

    function_calls = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):

            function_calls.append({
                "function": get_function_name(node.func),
                "arguments": [
                    ast.unparse(argument) for argument in node.args
                ],
                "line": node.lineno
            })

    return function_calls