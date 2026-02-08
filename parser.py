import ast
from typing import List

class CodeParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.tree = ast.parse(f.read())

    def get_imports(self) -> List[str]:
        imports = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
        return imports

    def get_functions(self) -> List[str]:
        return [
            node.name
            for node in ast.walk(self.tree)
            if isinstance(node, ast.FunctionDef)
        ]
