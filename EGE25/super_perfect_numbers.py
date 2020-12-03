# Число называется суперсовершенным, если сумма всех делителей
# суммы всех его делителей равна произведению самого числа на 2. например, число 16 суперсовершенное.
# Его делители: 1, 2, 4, 8, 16. Их сумма равна 31. Делители числа 31: 1+31=32. 32=16*2.
# Выведите каждое суперсовершенное число из диапазона [2; 80000] в порядке возрастания по одному в строке.

# Импортируем функцию корня из модуля math
from math import sqrt


# Создаем функцию sum_divs нахождения суммы всех делителей числа num
def sum_divs(num):
	# Пустой список для делителей числа
	list_divs = []
	# округленный до целого числа корень числа num
	q = round(sqrt(num))
	# Добавляем в список делителей, если извлеченный квадратный корень целый
	if q ** 2 == num:
		list_divs.append(q)
	# Запускаем цикл с перебором всех делителей от 1(включая) до корня(не включая)
	for j in range(1, q):
		# Если делится - добавляем
		if num % j == 0:
			# Если делится, то при делении даст и второй делитель
			# Добавим эти два делителея в список
			list_divs += [j, num // j]

	# Завершаем функцию и возвращаем сумму всех делителей
	return sum(list_divs)


# Перебор чисел в заданном диапазоне
for i in range(2, 80001):
	# Число Суперсовершенное, если сумма делителей суммы делителей числа есть само число умноженное на 2
	if i * 2 == sum_divs(sum_divs(i)):
		# Если так и есть, то выводим число
		print(i)
