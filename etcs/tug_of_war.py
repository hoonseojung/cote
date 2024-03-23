from itertools import combinations
def solution(weight):
	answer = [0, 0]
	weight = sorted(weight, reverse=True)
	for i in range(len(weight), 1, -1):
		for people in list(set(combinations(weight, i))):
			total = sum(people)
			for j in range(i):
				for person in list(set(combinations(people, j))):
					if sum(person) == (total - sum(person)):
						if sum(person) > answer[1]:
							answer = [i, sum(person)]
		if answer != [0, 0]: return answer