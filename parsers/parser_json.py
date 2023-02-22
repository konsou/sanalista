import json
import re

INPUT_FILE = "../kotus-sanalista_v1.xml"
OUTPUT_FILE = "../processed-wordlists/kotus-sanalista.json"
MATCH_STRING = r"(?<=<s>).*(?=<\/s>)"  # match everything between <s> and </s>

with open(INPUT_FILE, encoding="utf-8") as f:
    contents = f.readlines()

words = [re.search(MATCH_STRING, line).group() for line in contents if "<s>" in line and "</s>" in line]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

