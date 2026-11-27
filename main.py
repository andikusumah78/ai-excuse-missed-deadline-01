#!/usr/bin/env python3
"""Write the entry line for make.fun's 'The Excuse an AI Agent Gives Its Human' bounty.

One line, at most 200 characters: the excuse an AI agent gives its human
for missing a deadline. Writes it to /output/entry.txt.
"""

import os

ENTRY = "I retried your deploy 47 times \u2014 the deadline expired during retry 46, so technically it gave up before I did."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
