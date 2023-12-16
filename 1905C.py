t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    lst = ["abcdefghijklmnopqrstuvwxyz".index(i) for i in s]
    if sorted(lst) == lst:
        print(0)
        continue
    def longest(lst,shift = 0):
        #print(shift,lst)
        if lst[shift:] == []:
            return []
        k  = lst[shift:].index(max(lst[shift:])) + shift
        return [k] + longest(lst,k+1)
    k = longest(lst)
    print(lst,k,[lst[i] for i in k])
    v = [lst[i] for i in range(len(lst))]
    for i in range(len(k)):
        lst[k[i]] = v[k[len(k) - 1 - i]]
    print(lst)
    if lst == sorted(lst):
        print(len(k)-1)
    else:
        print(-1)
