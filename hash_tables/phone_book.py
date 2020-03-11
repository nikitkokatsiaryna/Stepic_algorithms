# 1 the decision through the loop

num = int(input())
requests = [input().split() for el in range(num)]
phone_book = {}

for el in requests:
    if 'add' in el:
        phone_book[el[1]] = el[2]
    elif 'find' in el:
        if el[1] not in phone_book:
            print('not found')
        else:
            print(phone_book[el[1]])
    else:
        if el[1] not in phone_book:
            continue
        else:
            del phone_book[el[1]]



# 2 the decision through the methods
book = {}


def add_number(number_and_name):
    number, name = number_and_name.split()
    book[number] = name


def del_number(number):
    if book.get(number):
        del book[number]


def find_number(number):
    if book.get(number):
        print(book[number])
    else:
        print('not found')


commands = {
        'add': add_number,
        'del': del_number,
        'find': find_number
    }


def main():
    for line in range(int(input())):
        line = input()
        command, number_and_name = line.split(',', 1)
        action = commands.get(command)
        action(number_and_name)


if __name__ == "__main__":
    main()


# 3 the decision through the class
class PhoneBook:
    def __init__(self):
        self._dict = dict()

    def add_contact(self, contact):
        number, name = contact.split()
        self._dict[number] = name
        return self._dict

    def del_contact(self, contact):
        if contact in self._dict:
            del self._dict[contact]

    def find_contact(self, contact):
        if contact in self._dict:
            return self._dict[contact]
        else:
            return "not found"


def main():
    pb = PhoneBook()
    for index in range(int(input())):
        line = input()
        command, contact = line.split(' ', 1)
        if command == 'add':
            pb.add_contact(contact)
        elif command == 'find':
            contact_name = pb.find_contact(contact)
            print(contact_name)
        else:
            pb.del_contact(contact)

if __name__ == "__main__":
    main()

