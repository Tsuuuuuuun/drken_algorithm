N, v = map(int, input().split())
a = list(map(int, input().split()))

exist = False
for i in range(N):
    if a[i] == v:
        exist = True
print('Yes' if exist else 'No')