import json
from collections.abc import Iterable

def read_json(filename, sections=('question', 'answer')):

    if isinstance(sections, str):
        sections = [sections]

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_text = []

    for item in data:
        for section in sections:
            text = ' '.join(item.get(section, []))
            all_text.append(text)

    raw_text = ' '.join(all_text)

    return(raw_text)