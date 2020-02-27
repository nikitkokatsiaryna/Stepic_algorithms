n, m = map(int, input().split())
processes = [[0, i] for i in range(n)]  # инициализированная куча с процессорами
tasks = [int(s) for s in input().split()]  # задачи количества m
# n, m = 3, 11
# processes = [[0, 0], [0, 1], [0, 2]]  # инициализированная куча с процессорами
# tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # задачи количества m


def SiftDown(i):
    min_index = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and processes[l] < processes[min_index]:
        min_index = l
    if r < n and processes[r] < processes[min_index]:
        min_index = r
    if i != min_index:
        processes[i], processes[min_index] = processes[min_index], processes[i]
        SiftDown(min_index)


current_time = 0
for task_j in tasks:
    current_time = processes[0][0]
    print(processes[0][1], current_time)
    processes[0][0] += task_j
    SiftDown(0)
