class Trie:
    def __init__(self):
        self.child=[0 for i in range(27)]
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp=self.child
        for i in word:
            if temp[ord(i)-ord('a')]==0:
                temp[ord(i)-ord('a')]=[0 for i in range(27)]
            temp=temp[ord(i)-ord('a')]
        temp[26]=1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp=self.child
        for i in word:
            if temp[ord(i)-ord('a')]==0:
                return False
            temp=temp[ord(i)-ord('a')]
        if(temp and temp[26]==1):
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp=self.child
        for i in prefix:
            if temp[ord(i)-ord('a')]==0:
                return False
            temp=temp[ord(i)-ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
