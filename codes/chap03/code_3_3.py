N = int(input())
a = list(map(int, input().split()))
min_value = 2000000000

for i in range(N):
    if a[i] < min_value:
        min_value = a[i]
print(min_value)