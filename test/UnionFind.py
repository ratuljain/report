__author__ = 'rjain1'

class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for i in range(n)]

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

    def printParent(self):
        print("index: ",list(range(9)))
        print("parent: ", self.parent)

uf = UnionFind(9)
uf.union(2,1)
uf.union(4,3)
uf.union(6,5)
print("\nParent array after union(2,1), union(4,3) and union(6,5):")
uf.printParent()
uf.union(2,4)
myDict = {}
for node in range(9):
    root = uf.find(node)
    if not root in myDict:
        myDict[root] = set([node])
    else:
        myDict[root].add(node)
    print("\nDisjoint sets: ")
    for mySet in myDict.values():
        print(list(mySet))