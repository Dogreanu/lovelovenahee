import time

from itertools import permutations

N = input("Choose N: ")
N = int(N)
count = 0
start = time.time()

for cases in permutations(range(N),N):
    allset = 1
    for i in range(N-1):
        for k in range(1,N-i):
            good = 0
            if abs(cases[i] - cases[i+k]) == k:
                break
            good = 1
        if good != 1:
            allset = 0
            break
    if allset == 1:
        count += 1
print(f'The number of ways to make N queens is: {count}')
print("time :", time.time() - start)