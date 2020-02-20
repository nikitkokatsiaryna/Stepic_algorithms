n = int(input())
lst = [int(i) for i in input().split()]
m = int(input())

left, right, answer, prev = [], [], [], -1
for _ in range(n):
    if len(left) < m - 1:
        left.append((lst[0], max(prev, lst[0])))
        prev = max(prev, lst[0])
        del lst[0]
        if right:
            answer.append(max(prev, right.pop()[1]))
    else:
        left.append((lst[0], max(prev, lst[0])))
        answer.append(max(prev, lst[0]))
        del lst[0]
        prev = -1
        while left:
            el = left.pop()[0]
            right.append((el, max(prev, el)))
            prev = max(prev, el)
        right.pop()
        prev = -1
print(*answer)