class Node:
    def __init__(self, key=None):
        self.key = key
        self.child = {}
        self.data = ""


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur = self.head
        for s in string:
            if s not in cur.child:
                cur.child[s] = Node(s)
            cur = cur.child[s]
        cur.data = string

    def search(self, string):
        cur = self.head
        for s in string:
            if cur.data != "":
                return False
            cur = cur.child[s]
        return True


T = int(input())
for _ in range(T):
    check = True
    N = int(input())
    phone = [int(input()) for _ in range(N)]

    trie = Trie()
    for ph in phone:
        trie.insert(str(ph))

    for ph in phone:
        if not trie.search(str(ph)):
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")

