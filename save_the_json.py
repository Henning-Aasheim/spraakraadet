import json
import re

def clean_text(text: str) -> str:
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

input_file = "sprakradet.json"
output_file = "sprakradet_clean.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    if "title" in item and isinstance(item["title"], str):
        item["title"] = clean_text(item["title"])

    if "question" in item and isinstance(item["question"], list):
        item["question"] = [clean_text(q) for q in item["question"]]

    if "answer" in item and isinstance(item["answer"], list):
        item["answer"] = [clean_text(a) for a in item["answer"]]

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)