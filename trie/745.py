class Node():
    def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
       self.children = {}  # mapping from character ==> Node
       self.isword = False
       self.index = 0

class WordFilter:

    def __init__(self, words):
        self.root = Node()
        l = len(words)
        for i in range(l):
            word = words[i]
            node = self.root
            for s in word:
                if s not in node.children:
                    node.children[s] = Node()
                node = node.children[s]
            node.isword = True
            node.index = i
    
    
    def fprefix(self,str,node):
        for s in str:
            if s in node.children:
                node = node.children[s]
            else:
                return -1
        return node
    
    #找到trie中所有已str为前缀的词
    def finprefixwords(self,str,node,words={}):
        '''
        str：前缀
        node：该前缀代表的节点
        words：所有trie中存储的已该前缀开头的词

        str和node 由fprefix函数得到
        '''
        l = len(node.children)
        if l == 0:
            words[str]=node.index
        else:
            if node.isword:
                words[str]=node.index
            for key in node.children:
                self.finprefixwords(str+key,node.children[key],words)

        return words
    
    def f(self, prefix: str, suffix: str) -> int:
        node = self.root
        t = self.fprefix(prefix,node)
        if t == -1:
            return -1
        else:
            words = self.finprefixwords(prefix,t,words={})
            m = []
            for key in words:
                if key.endswith(suffix):
                    m.append(words[key])
            if m == []:
                return -1
            else:
                return max(m)

    


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)