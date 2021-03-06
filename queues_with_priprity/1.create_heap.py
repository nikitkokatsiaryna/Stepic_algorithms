def heapify(h, i):
    min_index = i
    l = 2 * i + 1
    r = 2 * i + 2
    per_indexes = []

    if l < len(h) and h[l] < h[min_index]:
        min_index = l

    if r < len(h) and h[r] < h[min_index]:
        min_index = r

    if i != min_index:
        per_indexes.append((i, min_index))
        h[i], h[min_index] = h[min_index], h[i]
        per_indexes += heapify(h, min_index)

    return per_indexes


num = int(input())
tree = [int(el) for el in input().split()]

a = []
for index in reversed(range(len(tree) // 2)):
    result = heapify(tree, index)
    for el in result:
        if len(el) > 0:
            a.append(el)

print(len(a))
for el in a:
    print(*el)

