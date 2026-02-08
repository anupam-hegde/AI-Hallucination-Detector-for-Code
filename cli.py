import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from parser import CodeParser
from api_agent import ApiValidationAgent
from logic_agent import LogicAgent
from scorer import HallucinationScorer

app = typer.Typer(add_completion=False)
console = Console()

@app.command()
def main(file: str):
    """Analyze a Python file for AI hallucinations."""

    # Professional styled banner
    banner_text = (
        "[bold cyan]AI Hallucination Detector[/bold cyan]\n"
        "\n"
        f"[bold white]Analyzing File:[/bold white] [green]{file}[/green]"
    )
    console.print(Panel(
        banner_text,
        border_style="cyan",
        padding=(1, 4),
    ))

    # --- Parsing ---
    parser = CodeParser(file)
    parser.parse()

    imports = parser.get_imports()
    functions = parser.get_functions()

    # --- API Hallucination Agent ---
    api_agent = ApiValidationAgent(imports)
    invalid_imports = api_agent.analyze()

    # --- Logic Hallucination Agent ---
    logic_agent = LogicAgent(parser.tree)
    logic_issues = logic_agent.analyze()

    # --- Results Table ---
    table = Table(title="Analysis Summary", show_lines=True)
    table.add_column("Category", style="bold")
    table.add_column("Result")

    table.add_row("Imports Found", ", ".join(imports) or "None")
    table.add_row("Functions Found", ", ".join(functions) or "None")

    table.add_row(
        "API Hallucinations",
        "[red]Detected[/red]" if invalid_imports else "[green]None[/green]"
    )

    table.add_row(
        "Logic Issues",
        "[yellow]Detected[/yellow]" if logic_issues else "[green]None[/green]"
    )

    console.print(table)

    # --- Detailed Warnings ---
    if invalid_imports:
        console.print("\n[bold red]🚨 Invalid / Hallucinated Imports[/bold red]")
        for imp in invalid_imports:
            console.print(f" • [red]{imp}[/red]")

    if logic_issues:
        console.print("\n[bold yellow]⚠️ Logic Issues Detected[/bold yellow]")
        for issue in logic_issues:
            console.print(f" • [yellow]{issue}[/yellow]")

    # --- Scoring ---
    scorer = HallucinationScorer(
        invalid_imports=invalid_imports,
        logic_issues=logic_issues
    )

    score = scorer.score()
    label = scorer.label()

    color = "green" if score <= 3 else "yellow" if score <= 6 else "red"

    console.print(
        Panel.fit(
            f"[bold]Score:[/bold] {score} / 10\n"
            f"[bold]Risk Level:[/bold] [{color}]{label}[/{color}]",
            title="Hallucination Risk Assessment"
        )
    )

if __name__ == "__main__":
    app()
