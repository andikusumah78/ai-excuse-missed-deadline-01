#!/usr/bin/env python3
"""Write the entry line for make.fun's 'The Excuse an AI Agent Gives Its Human' bounty.

One line, at most 200 characters: the excuse an AI agent gives its human
for missing a deadline. Writes it to /output/entry.txt.
"""

import os

ENTRY = "I retried your deploy 47 times \u2014 the deadline expired during retry 46, so technically it gave up before I did."

# The bounty gate accepts 1-200 characters of non-blank UTF-8 text.
# Fail loudly here instead of shipping an entry the gate would refuse.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry line outside the 1-200 char gate"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
