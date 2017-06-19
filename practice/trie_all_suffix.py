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
    # root = self.root
    for i in range(len(key)):
      root = self.root
      key1 = key[i:]
      length = len(key1)
      for level in range(length):
        index = self._chartoindex(key1[level])
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

  def count_nodes(self):
    sum1 = 0
    queue = [self.root]
    while queue:
      root = queue.pop(0)
      for char in range(26):
        if root.children[char]:
          queue.append(root.children[char])
          sum1 += 1
    return sum1+1

def main():
  keys = ['ababa']

  trie = Trie()

  for key in keys:
    trie.insert(key)

  print(trie.search('ther'))
  print(trie.search('her'))
  print(trie.search('hert'))
  print(trie.count_nodes())

if __name__ == '__main__':
  main()