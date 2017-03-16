question = input('Вопрос: ')

def get_answer(question):
	question = str(question).lower()
	answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех!', 'пока': 'Увидимся'}
	print(answers[question])

if __name__ == '__main__':
	get_answer(question)