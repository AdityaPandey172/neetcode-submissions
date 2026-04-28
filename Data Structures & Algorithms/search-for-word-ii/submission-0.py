from collections import Counter
from itertools import chain, product
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.refcnt = 0
        self.is_word = False
        self.is_rev = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, rev):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
            node.refcnt += 1
        node.is_word = True
        node.is_rev = rev
    
    def remove(self, word):
        node = self.root
        for i, c in enumerate(word):
            parent = node
            node = node.children[c]

            if node.refcnt == 1:
                path = [(parent, c)]
                for c in word[i + 1 :]:
                    path.append((node, c))
                    node = node.children[c]
                for parent, c in path:
                    parent.children.pop(c)
                return
            node.refcnt -= 1
        node.is_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        n, m = len(board), len(board[0])
        trie = Trie()

        boardcnt = Counter(chain(*board))

        for w, wrdcnt in ((w, Counter(w))for w in words):
            if any(wrdcnt[c] > boardcnt[c]for c in wrdcnt):
                continue
            if wrdcnt[w[0]] < wrdcnt[w[-1]]:
                trie.insert(w, False)
            else:
                trie.insert(w[::-1], True)
        
        def dfs(r, c, parent) -> None:
            if not (node := parent.children.get(board[r][c])):
                return
            path.append(board[r][c])
            board[r][c] = '#'

            if node.is_word:
                word = "".join(path)
                res.append(word[::-1] if node.is_rev else word)
                trie.remove(word)
            
            if r > 0:
                dfs(r - 1, c, node)
            if r < n -1:
                dfs(r + 1, c, node)
            if c > 0:
                dfs(r, c - 1, node)
            if c < m -1:
                dfs(r, c + 1, node)
            
            board[r][c] = path.pop()
        
        path = []
        for r, c in product(range(n), range(m)):
            dfs(r, c, trie.root)
        return res









        