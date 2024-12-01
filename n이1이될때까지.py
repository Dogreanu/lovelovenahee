N,K = input("Choose N and K: ").split()
N = int(N)
K = int(K)
count = 0
while N != 0:
    if N%K==0:
        N = N//K
        count += 1
    else:
        count += (N%K)
        N = N - N%K
else:
        count -= 1 
        print(f'카운트는 {count}.')