# Falls on 10 test
def add_string(string, index, empty_list):
    if string != [] and string not in empty_list[index]:
        empty_list[index].insert(0, string)
    elif string not in empty_list:
        empty_list[index] = [string]


def del_string(text, index, list):
    for el in list:
        if text in el:
            el.remove(text)


def find_string(find_text, index, list):
    answer = 'no'
    for el in list:
        if find_text in el:
            answer = 'yes'
    print(answer)


def check_list(text, index, list):
    if list[int(text)] == []:
        print(' ')
    else:
        print(' '.join(list[int(text)]))


commands = {
    'add': add_string,
    'del': del_string,
    'find': find_string,
    'check': check_list,
}


def get_hash(value, size):
        total = 0
        x_mult = 1
        simple_number = 1000000007
        x = 263
        for char in value:
            total += ord(char) * x_mult
            x_mult *= x
        return (total % simple_number) % size


def main_func():
    size = int(input())
    count_requests = int(input())
    empty_list = [[] for el in range(size)]
    for el in range(count_requests):
        command, text = input().split(' ')
        text_index = get_hash(text, size)

        action = commands.get(command)
        action(text, text_index, empty_list)


if __name__ == "__main__":
    main_func()



# Without mistakes
class HashChainTable:
    def __init__(self, size):
        self._table = [None] * size
        self._size = size
        self._p = 1000000007
        self._x = 263

    def _get_hash(self, item):
        total = 0
        x_mult = 1
        for char in item:
            total += ord(char) * x_mult
            x_mult *= self._x
        return (total % self._p) % self._size

    def add(self, value):
        value_hash = self._get_hash(value)
        if not self._find(value, value_hash):
            if self._table[value_hash]:
                self._table[value_hash].append(value)
            else:
                self._table[value_hash] = [value]

    def remove(self, value):
        value_hash = self._get_hash(value)
        if self._find(value, value_hash):
            self._table[value_hash].remove(value)

    def _find(self, value, value_hash):
        return self._table[value_hash] and value in self._table[value_hash]

    def ffind(self, value):
        str_hash = self._get_hash(value)
        print('yes' if self._find(value, str_hash) else 'no')

    def check(self, value):
        lst = self._table[int(value)]
        print(' '.join(reversed(lst)) if lst else '')


def main():
    table = HashChainTable(int(input()))
    funcs = {'add': table.add,
             'del': table.remove,
             'find': table.ffind,
             'check': table.check}

    for _ in range(int(input())):
        cmd, value = input().split()
        funcs[cmd](value)


if __name__ == "__main__":
    main()