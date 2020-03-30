# class BinaryTree:
#
#     def __init__(self, tree):
#         self.tree = tree
#         self.result = list()
#
#     def in_order(self, node):
#         if node == -1:
#             return
#         self.in_order(self.tree[node][1])
#         self.result.append(self.tree[node][0])
#         self.in_order(self.tree[node][2])
#         return self.result
#
#     def pre_order(self, node):
#         if node == -1:
#             return
#         self.result.append(self.tree[node][0])
#         self.pre_order(self.tree[node][1])
#         self.in_order(self.tree[node][2])
#         return self.result
#
#     def post_order(self, node):
#         if node == -1:
#             return
#         self.post_order(self.tree[node][1])
#         self.in_order(self.tree[node][2])
#         self.result.append(self.tree[node][0])
#         return self.result
#
#     def implementation(self):
#         print(*self.in_order(0))
#         self.result.clear()
#         print(*self.pre_order(0))
#         self.result.clear()
#         print(*self.post_order(0))
#
#
# def main():
#     str_num = int(input())
#     list_node = [[]] * str_num
#
#     for num in range(str_num):
#         key, left_index, right_index = list(map(int, input().split()))
#         list_node[num] = [key, left_index, right_index]
#     node = BinaryTree(list_node)
#     node.implementation()
#
#
# if __name__ == '__main__':
#     main()


class BinaryTree:
    def __init__(self, tree):
        self.tree = tree
        self.result = list()

    def in_order(self, node):
        if node == -1:
            return
        self.in_order(self.tree[node]["left"])
        self.result.append(self.tree[node]["key"])
        self.in_order(self.tree[node]["right"])
        return self.result

    def pre_order(self, node):
        if node == -1:
            return
        self.result.append(self.tree[node]["key"])
        self.pre_order(self.tree[node]["left"])
        self.pre_order(self.tree[node]["right"])
        return self.result

    def post_order(self, node):
        if node == -1:
            return
        self.post_order(self.tree[node]["left"])
        self.post_order(self.tree[node]["right"])
        self.result.append(self.tree[node]["key"])
        return self.result

    def implementation(self):
        print(*self.in_order(0))
        self.result.clear()
        print(*self.pre_order(0))
        self.result.clear()
        print(*self.post_order(0))


def main():
    tree = list()
    n = (int(input()))
    for node in range(n):
        tree.append({"key": None, "left": None, "right": None})
        tree[node]["key"], tree[node]["left"], tree[node]["right"] = list(map(int, input().split()))
    t = BinaryTree(tree)
    t.implementation()


if __name__ == "__main__":
    main()
