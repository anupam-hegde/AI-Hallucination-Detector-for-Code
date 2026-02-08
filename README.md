# AI Hallucination Detector CLI

A lightweight CLI that inspects Python files for hallucinated imports and suspect logic using fast AST heuristics and a simple risk scorer.


[▶ Watch CLI demo on YouTube](https://www.youtube.com/watch?v=40PZU8grB-8)

## Features
- Rich, single-command terminal UI with summary and risk panel
- API hallucination checks via import validation
- Logic heuristics (nested loop detection as a starter rule)
- Simple scoring model with Low/Medium/High labels
- Zero external API calls; everything runs locally

## Quickstart
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
Analyze a Python file:
```bash
python cli.py sample.py
```

Example output:
```

                                                                              
    AI Hallucination Detector                                                 
                                                                              
    Analyzing File: sample.py                                                 
                                                                              

          Analysis Summary           

 Category            Result       

 Imports Found       sklearn.fake 

 Functions Found     search       

 API Hallucinations  Detected     

 Logic Issues        Detected     


Invalid / Hallucinated Imports
  sklearn.fake

Logic Issues Detected
  Possible O(n^2) complexity detected due to nested loops
 Hallucination Risk Assessment 
 Score: 7 / 10                   
 Risk Level: High Risk           

```

## How it works
- Parser (`parser.py`): AST parses the target file and extracts imports and function names.
- API agent (`api_agent.py`): Attempts to import each module; failures are treated as hallucinations.
- Logic agent (`logic_agent.py`): Scans the AST for nested loops as a simple complexity heuristic.
- Scorer (`scorer.py`): Assigns weights to findings and caps the risk score at 10.
- CLI (`cli.py`): Orchestrates agents, renders tables/panels with `rich`, and outputs the final risk level.

## Extending
- Add more heuristics in `logic_agent.py` (e.g., unused branches, dead code, suspicious constant comparisons).
- Add extra API validation rules (e.g., validate specific symbols, not just modules) in `api_agent.py`.
- Tune scoring weights or labels in `scorer.py`.
- Swap the banner/table styles by editing the `rich` components in `cli.py`.

## Project layout
```
cli.py              # Entry point CLI
parser.py           # AST parser and extractors
api_agent.py        # Import validation agent
logic_agent.py      # Logic heuristics agent
scorer.py           # Risk scoring
sample.py           # Example target file (stub)
requirements.txt    # Dependencies
```

## Troubleshooting
- `ModuleNotFoundError: typer`: Activate the venv and install deps: `.\.venv\Scripts\activate && pip install -r requirements.txt`.
- `File not found`: Ensure the path you pass exists (relative paths are resolved from repo root).
- Windows PowerShell execution policy issues: run PowerShell as Admin and `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` if needed.
