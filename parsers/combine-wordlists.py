import json

INPUT_FILE_1 = "../processed-wordlists/kotus-sanalista.json"
INPUT_FILE_2 = "../processed-wordlists/kotus-sanalista-murre.json"
OUTPUT_FILE = "../processed-wordlists/kotus-sanalista-yhdistetty.json"

all_words = []

for filename in (INPUT_FILE_1, INPUT_FILE_2):
    with open(filename, encoding="utf-8") as f:
        loaded_words = json.load(f)
        print(f"Loaded {len(loaded_words)} words from {filename}")
        all_words.extend(loaded_words)
print(f"Loaded a total of {len(all_words)} words")

print(f"Removing duplicates and sorting")
all_words = list(set(all_words))
all_words = sorted(all_words)
print(f"Words after duplicate removal: {len(all_words)}")

print(f"Saving words to {OUTPUT_FILE}")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(all_words, f, indent=2, ensure_ascii=False)
