from pathlib import Path

LINE = (
    "One star. My bowl was empty for four whole minutes this morning. "
    "Four. I have filed a formal complaint with the dog. He agrees."
)


def run():
    if not 0 < len(LINE) < 201:
        raise SystemExit("line must be 1-200 characters long")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("line must be a single non-blank line")
    out = Path("/output") / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


raise SystemExit(run())
