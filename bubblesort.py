import random
import datetime

test = []
for x in range(1,101):
	test.append(random.randint(0, 10000))

start = datetime.datetime.now()
def bubbleSort(list):
	for i in range(0, len(list)-1):
		for j in range(0, len(list)-i-1):
			if list[j] > list[j+1]:
				(list[j], list[j+1]) = (list[j+1], list[j])
	return list
print bubbleSort(test)

print datetime.datetime.now() - start