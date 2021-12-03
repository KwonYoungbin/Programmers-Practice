import sys
from collections import deque

sys.setrecursionlimit(10 ** 4)  # 파이썬의 recursion 한계 조절

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(pre, node):
    q = deque([node])
    while q:
        now = q.popleft()
        pre.append(now.data[2])
        if now.right:
            q.appendleft(now.right)
        if now.left:
            q.appendleft(now.left)


def postorder(post, node):
    if node.left:
        postorder(post, node.left)
    if node.right:
        postorder(post, node.right)
    post.append(node.data[2])


def solution(nodeinfo):
    answer = [[] for _ in range(2)]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    root = None
    for node in nodeinfo:
        if not root:
            root = Tree(node)
        else:
            cur = root
            while True:
                if node[0] < cur.data[0]:
                    if cur.left:
                        cur = cur.left
                        continue
                    else:
                        cur.left = Tree(node)
                        break
                if node[0] > cur.data[0]:
                    if cur.right:
                        cur = cur.right
                        continue
                    else:
                        cur.right = Tree(node)
                        break
                break
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer