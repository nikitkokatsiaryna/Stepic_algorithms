from array import array


class Something():

    def __init__(self):

        self.parent = {}
        self.rank = {}

    def makeSet(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

        # while i != self.parent[i]:
        #     i = self.parent[i]
        # return i
        #

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


Something = Something()

n, e, d = map(int, input().split())

z = 1

for x in range(1, n + 1):
    Something.makeSet(x)

for x in range(e):
    i, j = map(int, input().split())
    Something.union(i, j)

for x in range(d):
    i, j = map(int, input().split())
    if Something.find(i) == Something.find(j):
        z = 0

print(z)

# Something.union(3, 5)
# print(Something.parent)
# print(Something.rank)