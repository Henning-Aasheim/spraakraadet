import requests
from bs4 import BeautifulSoup

url = 'https://sprakradet.no/spraksporsmal-og-svar/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

pages_number = soup.find_all('a', class_='page-number page-numbers')[-1].get_text()

urls = []

for page in range(1, int(pages_number)):
    url_temp = f"https://sprakradet.no/spraksporsmal-og-svar/?page={page}"
    urls.append(url_temp)


for url in urls:
    response_temp = requests.get(url)
    soup_temp = BeautifulSoup(response_temp.text, 'html.parser')
    container = soup_temp.find_all('div', )


# Title can be found as <h1></h1> under <div class = "top-wrapper" />
# Spørsmål finnes i <p></p> under <div class = "question-content" />
# Svar finnes i <p></p> under <div class = "answer-content" />