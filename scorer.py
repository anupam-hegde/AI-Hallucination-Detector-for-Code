#scorer.py

from typing import List


class HallucinationScorer:
    """
    Computes a hallucination risk score based on agent findings.
    """

    def __init__(self, invalid_imports: List[str], logic_issues: List[str]):
        self.invalid_imports = invalid_imports
        self.logic_issues = logic_issues

    def score(self) -> int:
        score = 0

        # Fake / hallucinated APIs are high risk
        score += 4 * len(self.invalid_imports)

        # Logic issues are medium-high risk
        score += 3 * len(self.logic_issues)

        # Cap the score at 10
        return min(score, 10)

    def label(self) -> str:
        score = self.score()

        if score <= 3:
            return "Low Risk"
        elif score <= 6:
            return "Medium Risk"
        else:
            return "High Risk"
