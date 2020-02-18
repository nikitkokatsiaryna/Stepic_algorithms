from collections import defaultdict

num = int(input('Input num: '))
tops = list(map(int, input().split()))
tops_dict = defaultdict(list)

for index, el in enumerate(tops):
    tops_dict[el].append(index)
    if el == -1:
        top_index = index

queue = [top_index]
tops_height = [0] * num
tops_height[top_index] = 1

while len(queue) > 0:
    queue_end = queue.pop()
    for el in tops_dict[queue_end]:
        tops_height[el] = tops_height[queue_end] + 1
        queue.append(el)

print(max(tops_height))