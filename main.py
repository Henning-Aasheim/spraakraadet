import requests
from bs4 import BeautifulSoup
import json
import time
import re

def clean_text(text: str) -> str:
    # Remove spaces before punctuation .,!?;:
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)
    # Collapse multiple spaces inside the text
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

BASE_URL = 'https://sprakradet.no/spraksporsmal-og-svar/'

def get_page_links(base_url: str) -> list[str]:
    resp = requests.get(base_url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    pages_number = soup.find_all('a', class_='page-number page-numbers')
    last_page_number = int(pages_number[-1].get_text(strip=True))

    urls = []

    for page in range(1, last_page_number + 1):
        url_temp = f"{base_url}?page={page}"
        urls.append(url_temp)

    return urls



def get_content(url: str) -> list[dict]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    for block in soup.find_all('div', class_='question-dropdown'):

        # Title

        title_tag = block.find('h2', class_='font-step-1')
        if title_tag:
            title = title_tag.get_text(separator=' ', strip=True)
        else:
            title = None

        # Question

        question_div = block.find('div', class_='question-content')
        question_paragraphs = []
        if question_div:
            for p in question_div.find_all('p'):
                raw = p.get_text(separator=' ', strip=True)
                text = clean_text(raw)
                if text:
                    question_paragraphs.append(text)

        # Answer

        answer_div = block.find('div', class_='answer-content')
        answer_paragraphs = []
        if answer_div:
            for p in answer_div.find_all('p'):
                raw = p.get_text(separator=' ', strip=True)
                text = clean_text(raw)
                if text:
                    answer_paragraphs.append(text)

        data.append(
            {
                "title": title,
                "question": question_paragraphs,
                "answer": answer_paragraphs,
            }
        )
    
    return data

def main():
    all_items = []

    page_urls = get_page_links(BASE_URL)
    print(f'Found {len(page_urls)} pages.')

    for i, url in enumerate(page_urls, start=1):
        print(f'Scraping page {i}/{len(page_urls)}: {url}')
        page_items = get_content(url)
        all_items.extend(page_items)

        # SLEEP
        time.sleep(2)

    output_file = 'sprakradet.json'

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(all_items)} items to {output_file}")

if __name__ == '__main__':
    main()
