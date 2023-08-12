N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min_value = 2000000000

for i in range(N):
    for j in range(N):
        if a[i] + b[j] < K:
            continue
        if a[i] + b[j] < min_value:
            min_value = a[i] + b[j]

print(min_value)