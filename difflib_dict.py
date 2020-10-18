#!/usr/bin/env python3

from difflib import SequenceMatcher
from difflib import get_close_matches

check = SequenceMatcher(None, "chinna", "china")
print(check.ratio())

print(get_close_matches("chinnna", ["china", "france", "india", "usa"]))
