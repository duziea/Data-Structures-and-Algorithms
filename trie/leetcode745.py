class Node():
    def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
       self.children = {}  # mapping from character ==> Node
       self.isword = False
       self.index = -1

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
        node = self.root
        for s in str:
            if s in node.children:
                node = node.children[s]
            else:
                return -1
        return [str,node]
    
    #找到trie中所有已str为前缀的词
    def finprefixwordss(self,str,node,wordss={}):
        '''
        str：前缀
        node：该前缀代表的节点
        wordss：所有trie中存储的已该前缀开头的词

        str和node 由fprefix函数得到
        '''
        l = len(node.children)
        if l == 0:
            wordss[str]=node.index
        # if l == 0:
        #     if node.isword:
        #         wordss.append(str)
        else:
            if node.isword:
                wordss[str]=node.index
            for key in node.children:
                self.finprefixwordss(str+key,node.children[key],wordss)

            return wordss
    
    def f(self, prefix: str, suffix: str,wordss={}) -> int:
        node = self.root
        t = self.fprefix(prefix,node)
        if t == -1:
            return -1
        else:
            pre = t[0]
            node = t[1]
            wordss = self.finprefixwordss(pre,node,wordss={})
            m = []
            for key in wordss:
                if key.endswith(suffix):
                    m.append(wordss[key])
            if m == []:
                return -1
            else:
                
                return max(m)
                
def f(trie,prefix: str, suffix: str,wordss={}) -> int:
    node = trie.root
    t = trie.fprefix(prefix,node)
    if t == -1:
        return -1
    else:
        pre = t[0]
        node = t[1]
        wordss = trie.finprefixwordss(pre,t[1],wordss={})

        m = []
        for key in wordss:
            if key.endswith(suffix):
                m.append(wordss[key])
        if m == []:
            return -1
        else:
            
            return max(m)
            
    
if __name__ == "__main__":
    
    words=["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]
    listf = [["babbab",""],["","abaa"],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
    #["WordFilter","f","f","f","f","f","f","f","f","f","f"]
    #[[["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]],["","abaa"],["babbab",""],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]

    
    
    
    obj = WordFilter(words)
    result = []

    for i in listf:
        p = obj.f(i[0],i[1])
        result.append(p)
        print(result)
    
    # p = obj.f(f[1][0],f[1][1])
    # print(p)


    # obj = WordFilter(words)
    # result = []
    
    # for i in listf:
    #     p = f(obj,i[0],i[1])
    #     result.append(p)
    #     print(result)


    # print(obj.finprefixwordss(listf[1][0],obj.root,wordss={}))
    # print(obj.finprefixwordss(listf[2][0],obj.root,wordss={}))
    # print(obj.finprefixwordss(listf[1][0],obj.root,wordss={}))

