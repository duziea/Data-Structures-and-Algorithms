'''
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)

search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def find(self,strs):
        node = self.root
        for s in strs:
            if s in node.children:
                node = node.children[s]
                
            else:
                return False
思路：
本质是trie树find字符串升级，
'.'代表万能字符
当遇到'.'时，遍历当前node.children的key
    继续判断node.children[key].children和'.'后的字符
    def match(self,node=self.root ,words,index=0):    定义一个方法，接收node(初始为root)，words，index(下标，用来取words的每个字符，初始为0)
        l = len(words)                          
        if index == l:
            return Node.isword
        word = words[index]
        if word == '.':                                 遇到'.'
            for key in node.children:                   遍历当前node.children的key，调用self.match(node.children[key],words,index+1)
                if self.match(node.children[key],words,index+1):       这里要if语句判断是否找到，若找到则返回True，退出for循环。
                    return True
            
        else:
            if word in node.children:
                match(node.children[word],words,index+1)
            else:
                return False

'''



class Node():
    def __init__(self):
       self.children = {}  
       self.isword = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = Node()
            node = node.children[s]
        
        node.isword= True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(self.root,word,0)

    def match(self,node,word,index):
        if index == len(word):
            return node.isword
        i = word[index]
        if i == '.':
            for x in node.children:
                if self.match(node.children[x],word,index+1):
                    return True
            return False
        else:
            if i not in node.children:
                return False
            return self.match(node.children[i],word,index+1)
                


