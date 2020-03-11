def find(i, parents):
    while i != parents[i]:
        i = parents[i]
    return i


def union(i, j, parent, rank, size=None, max_s=None):
    i_id = find(i, parent)
    j_id = find(j, parent)

    if i_id == j_id:
        return

    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
        if size:
            size[i_id] += size[j_id]
            max_s = max(max_s, size[i_id])
    else:
        parent[i_id] = j_id
        if size:
            size[j_id] += size[i_id]
            max_s = max(max_s, size[j_id])

        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1

    return max_s


n, e, d = map(int, input().split())
parent = [el for el in range(n)]
ranks = [0] * n
result = 1

for el in range(e):
    i, j = map(int, input().split())
    union(i - 1, j - 1, parent, ranks)

for el in range(d):
    di, dj = map(int, input().split())
    if find(di - 1, parent) == find(dj - 1, parent):
        result = 0

print(result)

