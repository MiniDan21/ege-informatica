from itertools import product


text = (open('k7-75.txt').read().split('\n'))

text = list(map(int, text))

amount = text.pop(0)

amount_even = set([i for i in text if i % 2 == 0])
amount_odd = set([i for i in text if i % 2 != 0])

del text

set_of_couples = list(product(amount_odd, amount_even))
print((39, 12) in set_of_couples)
count = 0
for n1, n2 in set_of_couples:
	if n1 % 13 == 0 or n2 % 13 == 0:
		count += 1

print(count)
