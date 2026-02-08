# GitHub Copilot CLI Usage Log

This project demonstrates the use of GitHub Copilot CLI as a development
and reasoning assistant while building an AI Hallucination Detector for code.
Copilot was used to accelerate implementation, clarify concepts, and debug
CLI issues. All suggestions were manually reviewed and validated.

---

## 1. AST Parsing (Code Structure Analysis)

Prompt used:
```bash
copilot suggest "Write Python code using ast to extract imports and function definitions"

## 2. API Hallucination Detection

Prompt used:
```bash
copilot suggest "How to safely check if a Python module exists without executing user code?"

##3. Logic Hallucination Detection

Prompt used:
```bash
copilot explain "How to detect nested loops using Python AST?"

## 4. CLI Debugging (Typer Issues)

Prompt used:
```bash
copilot explain "Why does Typer show 'Got unexpected extra argument' or 'Missing command' errors?"

## 5. Scoring Design

Prompt used:
```bash
copilot suggest "Design a simple weighted scoring system to combine multiple code analysis signals"






