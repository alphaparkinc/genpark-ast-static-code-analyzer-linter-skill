"""Python AST Static Code Analyzer & Linter.
100% Python Standard Library.
"""

import ast

class ASTCodeLinter(ast.NodeVisitor):
    """AST syntax visitor inspecting code complexity, security, and quality."""
    def __init__(self):
        self.issues = []
        self.defined_funcs = set()
        self.called_funcs = set()
        self.complexity = 1

    def visit_FunctionDef(self, node):
        self.defined_funcs.add(node.name)
        if not ast.get_docstring(node):
            self.issues.append(f"Function '{node.name}' at line {node.lineno} missing docstring")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.called_funcs.add(node.func.id)
            if node.func.id in ["eval", "exec"]:
                self.issues.append(f"Dangerous call '{node.func.id}' detected at line {node.lineno}")
        self.generic_visit(node)

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    @classmethod
    def analyze_source(cls, code_str):
        tree = ast.parse(code_str)
        linter = cls()
        linter.visit(tree)
        return {
            "complexity": linter.complexity,
            "issues": linter.issues,
            "functions": list(linter.defined_funcs)
        }
