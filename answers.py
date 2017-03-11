question = input('Вопрос: ')

def get_answer(question):
	question = str(question).lower()
	answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех!', 'пока': 'Увидимся'}
	print(answers[question])

get_answer(question)