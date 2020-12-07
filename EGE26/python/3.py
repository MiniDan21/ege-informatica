"""
Системный администратор раз в неделю создаёт архив пользовательских файлов. Однако объём
диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов.
Известно, какой объём занимает файл каждого пользователя. По заданной информации об объёме
файлов пользователей и свободном объёме на архивном диске определите максимальное число
пользователей, чьи файлы можно сохранить в архиве, а также максимальный размер имеющегося
файла, который может быть сохранён в архиве, при условии, что сохранены файлы максимально
возможного числа пользователей.
"""
# считываем файл и получаем максимальный размер архива 
file = open("../data/26-15.txt")
max_size, _ = map(int, file.readline()[:-1].split())
data = sorted([int(val) for val in file])

# находим индекс предпоследнего файла, который мы можем сохранить. Здесь работает "жадная логика"
total = 0
for i, val in enumerate(data):
	if total + val > max_size:
		sec_last_ind = i
		break
	total += val

# Допустим осталось объёма на диске - 15. Можно сохранить на него файл размеров 12 и тогда 
# останется свободного места - 3. Но дальше в массиве мог быть больший файл, например размера 14
# и он бы тоже поместился в объём 15. Именно поэтому в следующем цикле мы перибираем оставшиеся
# файлы, начиная с предпоследнего, в поисках наибольшего объёма.
max_storage = [
	val for val in data[sec_last_ind - 1:]
	if val - data[sec_last_ind] <= max_size - total
][-1]

print(sec_last_ind, max_storage)
