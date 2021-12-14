class Node(object):
    def __init__(self, data, count=0):
        self.count = count
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        now = self.root

        for s in string:
            if s not in now.child:
                now.child[s] = Node(s)
            now = now.child[s]
            now.count += 1

    def search(self, string):
        now = self.root
        cnt = 0

        for s in string:
            if now.count == 1:
                break
            now = now.child[s]
            cnt += 1

        return cnt

def solution(words):                    #Trie 알고리즘 사용
    answer = 0
    trie = Trie()

    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)
    return answer