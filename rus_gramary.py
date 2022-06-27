def rus_gramary(number: int) -> str:
	if int(str(number)[-1]) == 1 and number != 11: #если последний символ 1 и не равно 11, то файл
		return 'файл'
	if (int(str(number)[-1]) == 2 or int(str(number)[-1]) == 3 or int(str(number)[-1]) == 4) and (number != 12 and number != 13 and number != 14):
	#если меньше 10, больше 15 и последний символ 2,3,4, то файла
		return 'файла'
	else: #иначе файлов, включая последний символ 11, или последний символ 0, то файлов
		return 'файлов'

if __name__ == '__main__':
	while True:
		x = input('Enter the number: ')
		if x != 'exit':
			if x.isnumeric():
				print(rus_gramary(int(x)))
			else:
				continue
		else:
			break
