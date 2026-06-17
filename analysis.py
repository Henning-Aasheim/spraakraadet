import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import nltk
import spacy
import nb_core_news_sm

# Only need to run once
# nltk.download('stopwords')

from nltk.corpus import stopwords

#df = pd.read_json('sprakradet_clean.json')
#print(df.head())

with open('sprakradet_clean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

all_text = []

for item in data:
    questions = ' '.join(item.get('question', []))
    answers = ' '.join(item.get('answer', []))

    all_text.append(questions)
    all_text.append(answers)

raw_text = ' '.join(all_text)

# Stopwords and lemmatisation

norwegian_stopwords = set(stopwords.words('norwegian'))

nlp = nb_core_news_sm.load()

def chunk_text(text, max_chars=200_000):
    for i in range(0, len(text), max_chars):
        yield text[i:i + max_chars]

lemmas = []

for chunk in chunk_text(raw_text, max_chars=200_000):
    doc = nlp(chunk)
    lemmas.extend(
        token.lemma_.lower()
        for token in doc if not token.is_punct and not token.is_space
    )

filtered_lemmas = [w for w in lemmas if w not in norwegian_stopwords]
filtered_text = ' '.join(filtered_lemmas)


wc = WordCloud(
    width=1200,
    height= 800,
    background_color='white',
    max_words=100,
    colormap='viridis'
)

wordcloud = wc.generate(filtered_text)

plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()