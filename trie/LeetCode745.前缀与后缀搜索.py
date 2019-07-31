'''
给定多个 words，words[i] 的权重为 i 。

设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。这个函数将返回具有前缀 prefix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。

例子:

输入:
WordFilter(["apple"])
WordFilter.f("a", "e") // 返回 0
WordFilter.f("b", "") // 返回 -1

注意:

    words的长度在[1, 15000]之间。
    对于每个测试用例，最多会有words.length次对WordFilter.f的调用。
    words[i]的长度在[1, 10]之间。
    prefix, suffix的长度在[0, 10]之前。
    words[i]和prefix, suffix只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prefix-and-suffix-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路:
Node增加一个权重属性，插入词同时赋予权重，
fprefix()，接受前缀，返回该前缀的最后一个字符代表的node
finprefixwords(),接受前缀，fprefix()返回的node，words用于存储所有含有该前缀的词和权重，返回words
f(),接受前缀、后缀，调用fprefix，finprefixwords，对返回的words，
调用endswith方法（这里偷懒了，是否应该再建一个后缀树，）筛选出以后缀结尾的词的权重存入list，
最后返回list中最大权重

'''

class Node():
    def __init__(self):
       self.children = {}  
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