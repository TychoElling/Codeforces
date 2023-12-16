t = int(input())
for _ in range(t):
    a,b = tuple([int(i) for i in input().split()])
    print(max(a,b))
