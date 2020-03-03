n, m = map(int, input().split())
ancestor = [[int(el), index] for index, el in enumerate(input().split())]
maxn = max(ancestor)[0]


def find(i, ancestor):
    while i != ancestor[i][1]:
        ancestor[i][1] = find(ancestor[i][1])
    return ancestor[i][1]


def union(i, j, ancestor, max_n):

    t_1 = find(i, ancestor)
    t_2 = find(j, ancestor)
    if t_1 != t_2:
        ancestor[t_1][0] += ancestor[t_2][0]
        ancestor[t_2] = [0, ancestor[t_1][1]]
    if ancestor[t_1][0] > max_n:
        max_n = ancestor[t_1][0]


for i in range(m):
    t_1, t_2 = map(int, input().split())
    print(union(t_1 - 1, t_2 - 1, ancestor, maxn))
