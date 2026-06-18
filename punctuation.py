import matplotlib.pyplot as plt
from functions import read_json


filename = 'sprakradet_clean.json'

text = read_json(filename=filename, sections=('answer', 'question'))

count_periods = text.count('.')
count_commas = text.count(',')
count_questionmarks = text.count('?')

print(f'There are {count_periods} periods, {count_commas} commas, and {count_questionmarks} question marks')

text_answers = read_json(filename=filename, sections='answer')

count_answers_questionmarks = text_answers.count('?')
count_answers_periods = text_answers.count('.')
count_answers_commas = text_answers.count(',')

print(f'There are {count_answers_periods} periods, {count_answers_commas} commas, and {count_answers_questionmarks} question marks')

text_questions = read_json(filename=filename, sections='question')

text_queries_periods = text_questions.count('.')
text_queries_commas = text_questions.count(',')
text_queries_questionmarks = text_questions.count('?')

print(f'There are {text_queries_periods} periods, {text_queries_commas} commas, and {text_queries_questionmarks} question marks')

