n, m = map(int, input().split())
ancestor = [[int(el), index] for index, el in enumerate(input().split())]
maxn = max(ancestor)[0]


def find(i, ancestor):
    if i != ancestor[i][1]:
        ancestor[i][1] = find(ancestor[i][1], ancestor)
    return ancestor[i][1]


def union(i, j, ancestor, max_n):
    t_1 = find(i, ancestor)
    t_2 = find(j, ancestor)
    if t_1 != t_2:
        ancestor[t_1][0] += ancestor[t_2][0]
        ancestor[t_2] = [0, ancestor[t_1][1]]
    if ancestor[t_1][0] > max_n:
        max_n = ancestor[t_1][0]
    return max_n


for i in range(m):
    t_1, t_2 = map(int, input().split())
    print(union(t_1 - 1, t_2 - 1, ancestor, maxn))


# ____________________________________________________________


def find(i, data):
    if i != data[i][1]:
        data[i][1] = find(data[i][1], data)
    return data[i][1]


def union(d, s, data, max_n):
    d = find(d, data)
    s = find(s, data)

    if d != s:
        data[d][0] += data[s][0]
        data[s] = [0, d]
    if max_n < data[d][0]:
        max_n = data[d][0]
    return max_n


n, m = 5, 5
data = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]
max_v = max(data)[0]

for i in range(m):
    d, s = map(int, input().split())
    print(union(d - 1, s - 1, data, max_v))
