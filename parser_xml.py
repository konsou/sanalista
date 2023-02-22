import re

INPUT_FILE = "murre/osa1/01_a.xml"
OUTPUT_FILE = "kotus-sanalista-murteet.txt"
# MATCH_STRING = r"(?<=<s>).*(?=<\/s>)"  # match everything between <s> and </s>
MATCH_STRING = r"(?<=<Headword>).*(?=<\/Headword>)"  # match everything between <s> and </s>

with open(INPUT_FILE, encoding="utf-8") as f:
    contents = f.read()

matches = re.findall(MATCH_STRING, contents)


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.writelines(words)
