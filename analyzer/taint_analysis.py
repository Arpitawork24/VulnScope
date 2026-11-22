
import ast

SOURCES = {"input"}

SINKS = {
    "eval",
    "exec",
    "os.system",
    "subprocess.Popen"
}


def get_name(node):
    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        parent = get_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr

    return None


class TaintAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.tainted_variables = set()
        self.findings = []
        self.reported = set()

    def is_tainted(self, node):
        if isinstance(node, ast.Name):
            return node.id in self.tainted_variables

        if isinstance(node, ast.Call):
            if get_name(node.func) in SOURCES:
                return True

        return any(
            self.is_tainted(child)
            for child in ast.iter_child_nodes(node)
        )

    def check_sinks(self, node):

        for child in ast.walk(node):

            if not isinstance(child, ast.Call):
                continue

            function_name = get_name(child.func)

            if function_name not in SINKS:
                continue

            for argument in child.args:

                if self.is_tainted(argument):

                    variable = (
                        argument.id
                        if isinstance(argument, ast.Name)
                        else ast.unparse(argument)
                    )

                    key = (function_name, node.lineno, variable)

                    if key not in self.reported:
                        self.reported.add(key)

                        self.findings.append({
                            "function": function_name,
                            "variable": variable,
                            "line": child.lineno,
                            "message": (
                                "Untrusted input reaches "
                                "a potentially dangerous function."
                            )
                        })

    def visit_Assign(self, node):

        self.check_sinks(node.value)

        tainted = self.is_tainted(node.value)

        for target in node.targets:
            if isinstance(target, ast.Name):
                if tainted:
                    self.tainted_variables.add(target.id)
                else:
                    self.tainted_variables.discard(target.id)

        self.generic_visit(node)

    def visit_Expr(self, node):
        self.check_sinks(node.value)
        self.generic_visit(node)


def analyze_taint(tree):

    analyzer = TaintAnalyzer()
    analyzer.visit(tree)

    return analyzer.findings
