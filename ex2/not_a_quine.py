# Este script imprime ele mesmo, com syntax highlight
from rich.console import Console
from rich.syntax import Syntax

console = Console()

with open(__file__, "r") as f:
    contents = f.read()
    syntax = Syntax(contents, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
