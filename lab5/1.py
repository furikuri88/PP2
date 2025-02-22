import re
import textwrap

with open("row.txt", 'r', encoding='utf-8') as tx:
    txt=tx.read()

def match_pattern(string):
    pattern = r'^ab*$'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
t=txt.split()
strings = ["a", "ab", "abb", "abbb", "b", "ba", "abc"]
for s in strings:
    print(f"'{s}': {match_pattern(s)}")
print("\n","second: ")
for s in t:
    print(f"'{s}': {match_pattern(s)}")
