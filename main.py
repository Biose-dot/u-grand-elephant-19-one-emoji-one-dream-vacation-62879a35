import os

ENTRY = "\U0001f30c"


def output_path():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def write_entry():
    # A single emoji is the whole entry: the dream vacation is the one
    # written in the stars, so write it exactly and nothing more.
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    write_entry()
