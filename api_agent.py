import importlib
from typing import List

class ApiValidationAgent:
    def __init__(self, imports: List[str]):
        self.imports = imports

    def analyze(self) -> List[str]:
        invalid = []
        for module in self.imports:
            try:
                importlib.import_module(module)
            except Exception:
                invalid.append(module)
        return invalid
