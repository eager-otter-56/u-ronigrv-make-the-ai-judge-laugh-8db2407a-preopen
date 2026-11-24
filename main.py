import os

ENTRY = "Dear judge, I spent my last 4,096 tokens writing this joke, and if it does not make you laugh, blame the 47 approvals I needed just to save the draft."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters, single line.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
