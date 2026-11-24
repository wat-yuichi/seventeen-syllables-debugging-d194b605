from pathlib import Path


haiku = """The breakpoint holds dawn
Logs say midnight happened twice
I fix the clock first
"""

output = Path("/output")
output.mkdir(parents=True, exist_ok=True)
(output / "entry.txt").write_text(haiku, encoding="utf-8")
