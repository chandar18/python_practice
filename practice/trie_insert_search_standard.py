class TrieNode():
  def __init__(self):
    self.children = [None]*26
    self.isLeaf = False

class Trie():
  def __init__(self):
    self.root = self.getNode()

  def getNode(self):
    return TrieNode()

  def _chartoindex(self, ch):
    return ord(ch) - ord('a')

  def insert(self, key):
    root = self.root
    length = len(key)
    for level in range(length):
      index = self._chartoindex(key[level])

      if not root.children[index]:
        root.children[index] = self.getNode()
      root = root.children[index]
    root.isLeaf = True

  def search(self, key):
    root = self.root
    length = len(key)

    for level in range(length):
      index = self._chartoindex(key[level])
      if not root.children[index]:
        return False
      root = root.children[index]
    return True 

def main():
  keys = ['the','there','any']

  trie = Trie()

  for key in keys:
    trie.insert(key)

  print(trie.search('ther'))
  print(trie.search('anb'))

if __name__ == '__main__':
  main()