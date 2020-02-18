num = int(input())

commands = [input().split() for com in range(num)]

stack = [0]

for el in commands:
    if el[-1].isdigit():
        stack.append(max(stack[-1], int(el[-1])))
    elif el[-1] == 'pop':
        stack.pop()
    else:
        print(stack[-1])
