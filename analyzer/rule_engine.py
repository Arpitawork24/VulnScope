
SECURITY_RULES = {
    "eval": {
        "rule_id": "VS001",
        "severity": "HIGH",
        "message": "eval() can execute dynamically supplied Python expressions.",
        "recommendation": "Avoid using eval() with untrusted input."
    },
    "exec": {
        "rule_id": "VS002",
        "severity": "HIGH",
        "message": "exec() can execute dynamically supplied Python code.",
        "recommendation": "Avoid executing untrusted dynamic code."
    },
    "os.system": {
        "rule_id": "VS003",
        "severity": "HIGH",
        "message": "os.system() executes operating system commands.",
        "recommendation": "Prefer subprocess with shell=False and validate inputs."
    },
    "pickle.loads": {
        "rule_id": "VS004",
        "severity": "HIGH",
        "message": "Untrusted pickle data can execute arbitrary code.",
        "recommendation": "Never deserialize untrusted pickle data."
    },
    "subprocess.Popen": {
        "rule_id": "VS005",
        "severity": "MEDIUM",
        "message": "Subprocess execution requires careful input handling.",
        "recommendation": "Avoid shell=True and validate command arguments."
    }
}


def analyze_function_calls(function_calls):
    findings = []

    for call in function_calls:
        function_name = call["function"]

        if function_name in SECURITY_RULES:
            rule = SECURITY_RULES[function_name]

            findings.append({
                "rule_id": rule["rule_id"],
                "severity": rule["severity"],
                "function": function_name,
                "line": call["line"],
                "message": rule["message"],
                "recommendation": rule["recommendation"]
            })

    return findings
