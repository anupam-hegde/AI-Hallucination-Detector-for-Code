# logic_agent.py

import ast
from typing import List


class LogicAgent:
    """
    Detects logical / algorithmic hallucinations
    using simple AST-based heuristics.
    """

    def __init__(self, tree: ast.AST):
        self.tree = tree

    def analyze(self) -> List[str]:
        issues = []

        if self._has_nested_loops():
            issues.append(
                "Possible O(n^2) complexity detected due to nested loops"
            )

        return issues

    def _has_nested_loops(self) -> bool:
        """
        Detects nested for/while loops using AST traversal.
        """
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.For, ast.While)):
                for child in ast.walk(node):
                    if child is not node and isinstance(child, (ast.For, ast.While)):
                        return True
        return False
