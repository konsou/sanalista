import json
import os
import xml.etree.ElementTree as ET

INPUT_FILE_DIRECTORY = "../murre"
OUTPUT_FORMAT = "json"  # json or txt
OUTPUT_FILE = f"../kotus-sanalista-murre.{OUTPUT_FORMAT}"

xml_files = []
for root, dirs, files in os.walk(INPUT_FILE_DIRECTORY, topdown=False):
    for name in files:
        if name.endswith(".xml"):
            xml_files.append(os.path.join(root, name))

words = []

for xml_file in xml_files:
    new_words = []
    print(f"Processing {xml_file}")
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for dict_entry in root.findall('DictionaryEntry'):
        headword_container = dict_entry.find('HeadwordCtn')
        headword = headword_container.find('Headword')
        possible_newline = "" if OUTPUT_FORMAT == "json" else "\n"
        headword_text = headword.text.replace("|", "") + possible_newline
        new_words.append(headword_text)

    print(f"New words found: {len(new_words)}")
    words += new_words

print(f"Removing duplicates and sorting")
words = list(set(words))
words = sorted(words)

print(f"Processing complete, writing {len(words)} words to {OUTPUT_FILE}")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    if OUTPUT_FORMAT == "json":
        json.dump(words, f, indent=2, ensure_ascii=False)
    else:
        f.writelines(words)
