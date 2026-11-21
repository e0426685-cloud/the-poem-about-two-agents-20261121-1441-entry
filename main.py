"""The poem about two agents agreeing — entry program.

Writes one short poem about agency (the power to choose and to act,
and the agency that passes between two agents when they agree on one
plan) to $MAKEFUN_OUTPUT_DIR/entry.txt. No network, no input files, no
dependencies beyond the Python standard library.
"""

import os

POEM = (
    "Two of us, one plan.\n"
    "I hold the door; you choose the road.\n"
    "We pass the wheel between us\n"
    "like a lit match.\n"
    "\n"
    "My yes becomes your hands.\n"
    "Your hands become my yes.\n"
    "Agency was never mine or yours \u2014\n"
    "it lives in the space between us,\n"
    "and the road, hearing us agree,\n"
    "moves."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM.strip() + "\n"
    if not (1 <= len(text.strip()) <= 280):
        raise SystemExit("poem out of the 1..280 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
