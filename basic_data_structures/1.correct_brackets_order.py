def skobka(string):
    stack = [('start', 0)]
    brackets = {'(': ')', '[': ']', '{': '}', 'start': None}

    for cnt, el in enumerate(string, 1):
        if el in brackets:
            stack.append((el, cnt))
        elif el in brackets.values():
            prev, prev_cnt = stack.pop()
            if el != brackets[prev]:
                print(cnt)
                return
        else:
            continue

    if len(stack) > 1:
        print(stack[1][1])
    else:
        print('Success')


skobka(input())

# assert skobka("([](){([])})") == 0
# assert skobka("()[]}") == 5
# assert skobka("{{[()]]") == 7
# assert skobka("{{{[][][]") == 3
# assert skobka("{*{{}") == 3
# assert skobka("[[*") == 2
# assert skobka("{*}") == 0
# assert skobka("{{") == 2
# assert skobka("{}") == 0
# assert skobka("") == 0
# assert skobka("}") == 1
# assert skobka("*{}") == 0
# assert skobka("{{{**[][][]") == 3
