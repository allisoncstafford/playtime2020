#!/usr/bin/env python3
import re

print("Output #1: I'm excited to learn Python.")

string = 'The quick brown fox jumps over the lazy dog.'
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print(f"Output #38: count = {count}")