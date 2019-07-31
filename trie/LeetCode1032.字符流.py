'''按下述要求实现 StreamChecker 类：

StreamChecker(words)：构造函数，用给定的字词初始化数据结构。
query(letter)：如果存在某些 k >= 1，可以用查询的最后 k个字符（按从旧到新顺序，
包括刚刚查询的字母拼写）出给定字词表中的某一字词时，返回 true。否则，返回 false。
 
示例：
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // 初始化字典
streamChecker.query('a');          // 返回 false
streamChecker.query('b');          // 返回 false
streamChecker.query('c');          // 返回 false
streamChecker.query('d');          // 返回 true，因为 'cd' 在字词表中
streamChecker.query('e');          // 返回 false
streamChecker.query('f');          // 返回 true，因为 'f' 在字词表中
streamChecker.query('g');          // 返回 false
streamChecker.query('h');          // 返回 false
streamChecker.query('i');          // 返回 false
streamChecker.query('j');          // 返回 false
streamChecker.query('k');          // 返回 false
streamChecker.query('l');          // 返回 true，因为 'kl' 在字词表中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/stream-of-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路:
构建一个字典树，由题最后 k个字符（按从旧到新顺序，
包括刚刚查询的字母拼写）知，要查询k个字符串，如上示例要查询的字符串为
['d','cd','bcd','abcd'],由于cd被标记为单词，所以返回'cd'。这种方法，最坏需要查k个词

换个思路
将字符串reverse一下构建字典树，查询的时候也reverse，如上查询cd即查询dc，只需查dcba，判断dc是否标记为单词
['d','dc','dcb','dcba']
'''
class Node():
    def __init__(self):
       self.children = {}  # mapping from character ==> Node
       self.isword = False

class Trie():
    def __init__(self):
        self.root = Node()    

    def insert(self,strs):
        node = self.root
        for s in strs:
            if s not in node.children:
                node.children[s] = Node()
            node = node.children[s]

        node.isword= True

    def find(self,strs):
        node = self.root
        for s in strs:
            if s not in node.children:
                return False
            node = node.children[s]
            if node.isword:
                return True
        return False
        

class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.q=''

    def query(self, letter:str) -> bool:
        self.q += letter
        return self.trie.find(self.q[::-1])