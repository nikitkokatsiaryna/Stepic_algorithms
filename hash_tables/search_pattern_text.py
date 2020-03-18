# variant 1
def custom_hash(string):
    return sum(ord(l) for l in list(string))


def search_substring(string, sub_string):
    matches = []

    str_length = len(string)
    sub_str_length = len(sub_string)

    base_hash = custom_hash(string[:sub_str_length:])
    sub_str_hash = custom_hash(sub_string)

    for i in range(0, str_length - sub_str_length + 1):
        next_idx = sub_str_length + i
        prev = 0 if i == 0 else ord(string[i - 1])
        last = 0 if i == 0 else ord(string[next_idx - 1])
        base_hash = base_hash - prev + last
        if base_hash == sub_str_hash and sub_string == string[i:next_idx]:
            matches.append(i)

    return matches


def main():
    sub_string = input()
    string = input()
    print(*search_substring(string, sub_string))


if __name__ == '__main__':
    main()


# variant 2
#исходные строки, сразу переводим коды, с учетом ord('A') == 65
pattern = [ord(s) - 65 for s in input()]
text = [ord(s) - 65 for s in input()]

#константы
m, n = len(pattern), len(text)
x, p = 59, 67 # простые

#степени x от 1 до m-1 по модулю p (чтобы не пересчитывать)
x_pows = [1]
for i in range(1, m):
    x_pows.append(x_pows[-1] * x % p)

#хеш паттерна в обратную сторону (тогда вывод идет в прямом порядке):
#pattern[0] * x ^ (m-1)  + pattern[1] * x ^ (m-2) + ... pattern[m-1]
pattern_hash = sum([pattern[i] * x_pows[m-i-1] for i in range(m)]) % p

#последние мономы в хеше: text[i] * x ^ (m-1)
last_monoms = [text[i] * x_pows[-1] % p for i in range(n - m + 1)]

#хеш первой подстроки, тоже в обратную сторону
cur_hash = (last_monoms[0] + sum([text[i] * x_pows[m-i-1] for i in range(1, m)])) % p

#цикл в прямом порядке
for i in range(n - m):

    #проверяем совпадение хеша и подстроки
    if pattern_hash == cur_hash and pattern == text[i:(i+m)]:
        print(i, end = ' ')

    #пересчет хеша (в начале выталкиваем макс. степень, в конце прибавляем 0-вую
    cur_hash = ((cur_hash - last_monoms[i]) * x + text[i + m]) % p

#последняя подстрока, если добавить в цикл, то в пересчете хеша выйдем за границы массива
if pattern_hash == cur_hash and pattern == text[(n-m):]:
    print(n - m, end = ' ')


# variant 3. Failed in the 6 test
class PatternText:
    def __init__(self, pattern):
        self.pattern = pattern
        self._size = len(pattern)
        self._p = 1000000007
        self._x = 263

    def _get_hash(self, value):
        total = 0
        x_mult = 1
        for char in value:
            total = total + ord(char) * x_mult * self._x
            total += ord(char) * x_mult
            x_mult *= self._x
            hash_char = ((total % self._p) + self._p) % self._size
            return hash_char


def main():
    table = PatternText(input())
    text = input()
    pattern = table.pattern
    pattern_len = len(table.pattern)
    hash_pattern = table._get_hash(table.pattern)
    index_list = set()

    for el in range(len(text)):
        part_text = text[el:el + pattern_len]
        hash_part_text = table._get_hash(part_text)

        if hash_part_text == hash_pattern:
            for i in range(len(text) - pattern_len + 1):
                if pattern == text[i: i + pattern_len]:
                    index_list.add(i)
    print(*index_list)


if __name__ == '__main__':
    main()
