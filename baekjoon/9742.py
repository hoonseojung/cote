import itertools
from sys import stdin
while 1:
    input_data = stdin.readline().rstrip().split()
    if len(input_data) != 2:
        break
    string, n = input_data
    n = int(n)
    npr = list(itertools.permutations(list(string), len(string)))
    if len(npr) < n:
        print("{} {} = No permutation".format(string, n))
    else:
        print("{} {} = {}".format(string, n, ''.join(npr[n-1])))