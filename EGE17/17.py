# Рассматривается множество целых чисел, принадлежащих числовому отрезку [3672; 9117], которые
# удовлетворяют следующим условиям:
# − остаток от деления на 3 равен 2;
# − остаток от деления на 5 равен 4.
# Найдите количество таких чисел и их сумму.

count = 0
suma = 0

for i in range(3672, 9117 + 1):
	if i % 3 == 2 and i % 5 == 4:
		count += 1
		suma += i

print(count, suma)
