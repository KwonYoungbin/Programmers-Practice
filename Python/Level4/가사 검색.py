from collections import defaultdict

class Node(object):
    def __init__(self, data, count=0):
        self.count = count
        self.child = {}
        self.datalist = []

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        now = self.root

        for s in string:
            if s not in now.child:
                now.child[s] = Node(s)
            now = now.child[s]
            now.datalist.append(len(string))
            now.count += 1

    def search(self, string, length):
        now = self.root

        for s in string:
            if s in now.child:
                now = now.child[s]
            else:
                return 0

        return now.datalist.count(length)

def solution(words, queries):                       # Trie 알고리즘 사용
    answer = []
    trie = Trie()
    r_trie = Trie()
    len_list = defaultdict(int)

    for word in words:
        trie.insert(word)
        r_trie.insert(word[::-1])
        len_list[len(word)] += 1

    for q in queries:
        if q == '?' * len(q):
            answer.append(len_list[len(q)])
        elif q[0] == '?':
            string = q[::-1].split('?')[0]
            answer.append(r_trie.search(string, len(q)))
        elif q[0] != '?':
            string = q.split('?')[0]
            answer.append(trie.search(string, len(q)))
    return answer