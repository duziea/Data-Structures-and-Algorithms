class Node():
    def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
       self.children = {}  # mapping from character ==> Node
       self.isword = False
       self.isprefix = 0
       self.isweight = 0

class Trie():
    def __init__(self):
        self.root = Node()
    
    # def getNode(self):
    #     return Node()

    def insert(self,strs,w ):
        node = self.root
        for s in strs:
            if s not in node.children:
                node.children[s] = Node()
            node.isprefix += 1
            node = node.children[s]
        
        node.isprefix += 1
        node.isword= True
        node.isweight = w

    def find(self,strs):
        node = self.root
        for s in strs:
            if s in node.children:
                node = node.children[s]
                
            else:
                return False
        # return node.isword
        return [node.isword,node]
    
    def fprefix(self,strs,node):
        for s in strs:
            if s in node.children:
                node = node.children[s]
            else:
                return -1
        return [node,strs]

    #找到trie中所有已strs为前缀的词
    def finprefixwords(self,str,node,words=[]):
        '''
        str：前缀
        node：该前缀代表的节点
        words：所有trie中存储的已该前缀开头的词

        str和node 由fprefix函数得到
        '''
        l = len(node.children)
        if l == 0:
            words.append(str)
        # if l == 0:
        #     if node.isword:
        #         words.append(str)
        else:
            if node.isword:
                words.append(str)
            for key in node.children:
                # str=str+key
                self.finprefixwords(str+key,node.children[key],words)

        return words
    
    def prefixnum(self,prefix):
        node = self.root
        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else:
                return 0
        return node.isprefix

    #前后缀
    def f(self, prefix: str, suffix: str) -> int:
        rnode = self.fprefix(prefix,self.root)
        if rnode:
            nodes = self.getsuffixfirst(rnode,suffix[0])
            for node in nodes:
                t = self.fprefix(suffix[1:],node)
                if t == -1:
                    return -1
                return t.isweight
            
        else:
            return -1


    #递归求node节点分支下所有xnode的
    def getsuffixfirst(self,node,x,f=[]):
        l = len(node.children)
        if l == 0:
            return False
        else:
            for key in node.children:
                if key == x:
                    f.append(node.children[key])
                self.getsuffixfirst(node.children[key],x,f)

            return f
            
#递归求叶子节点个数          
# r = 0
# def getrootchildrenlen(trie):
#     l = len(trie.children)
#     global r
#     r = r + l
#     if l == 0:
#         return 
#     else:
#         for key in trie.children:
#             print(key)
#             getrootchildrenlen(trie.children[key])
    
#     return r


def finprefixwords(str,node,words=[]):
    '''
    str：前缀
    node：该前缀代表的节点
    words：所有trie中存储的已该前缀开头的词

    str和node 由fprefix函数得到
    '''
    l = len(node.children)
    if l == 0:
        words.append(str)
    # if l == 0:
    #     if node.isword:
    #         words.append(str)
    else:
        if node.isword:
            words.append(str)
        for key in node.children:
            # str=str+key
            finprefixwords(str+key,node.children[key],words)

    return words

#递归求node节点分支下所有xnode的
    # def getsuffixfirst(self,node,x,f=[]):
    #     l = len(node.children)
    #     if l == 0:
    #         return False
    #     else:
    #         for key in node.children:
    #             if key == x:
    #                 f.append(node.children[key])
    #             self.getsuffixfirst(node.children[key],x,f)

    #         return f



if __name__ == "__main__":
    

    trie = Trie()

    Sampleinput=['banana','band','bann','ban','bana','bee','absolute','acm']


    w = 0
    for i in Sampleinput:
        trie.insert(i,w)
        w += 1

    # print(getstrinleaves(trie.root,'a'))
    # t = trie.getsuffixfirst(trie.root.children['b'],'a')
    # print(t)
    # print(trie.f('a','e'))
    f = trie.fprefix('ban',trie.root)
    words = finprefixwords(f[1],f[0])
    words1 = trie.finprefixwords(f[1],f[0])
    print(words)
    print(words1)