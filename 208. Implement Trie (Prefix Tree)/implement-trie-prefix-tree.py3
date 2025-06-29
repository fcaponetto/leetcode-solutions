# 208. Implement Trie (Prefix Tree) (2/22/57464)
# Runtime: 50 ms (42.49%) Memory: 32.22 MB (25.92%) 

# Time Complexity O(n) where n is the length of the word to search or insert
# Space Complexity O(n) where n is the length of the word


class Trie:

    class TrieNode:
        def __init__(self):
            self.children = {} # hash map
            self.endWord = False

    def __init__(self):
        self.root = self.TrieNode()        

    def insert(self, word: str) -> None:
        currNode = self.root

        for c in word:
            # if not present, add it
            if c not in currNode.children:
                currNode.children[c] = self.TrieNode()
            # otherwise retrive it
            currNode = currNode.children[c]
        currNode.endWord = True

    def search(self, word: str) -> bool:
        currNode = self.root

        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]

        return currNode.endWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root

        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)