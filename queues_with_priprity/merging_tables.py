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


if __name__ == '__main__':
    n, m = map(int, input().split())
    sizes = [int(el) for el in input().split()]
    max_size = max(sizes)
    parents = [el for el in range(n)]
    ranks = [0] * n

    for el in range(m):
        dest, source = map(int, input().split())
        max_size_tmp = union(dest - 1, source - 1, parents, ranks, sizes, max_size)
        max_size = max_size_tmp or max_size
        print(max_size)
