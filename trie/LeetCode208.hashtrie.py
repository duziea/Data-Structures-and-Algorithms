class Node():
    '''
    Node类： Trie中的节点
    实例node的属性 children：
    这里采用python的字典来映射，{str:Node}   Node：当前节点的子节点；str：子节点Node代表的字符。
    实例node的属性 isword：
    True：代表从根节点到当前节点经过的字符组成的字符串存在于Trie中。
    False：代表从根节点到当前节点经过的字符组成的字符串不存在于Trie中。
    '''
    def __init__(self):
        self.children = {} 
        self.isword = False
    
class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self,strs):
        '''插入原理：
        1将字符串分为单个字符，
        2取根节点和第一个字符
        3判断当前节点的children属性中是否存在该字符，
            3.1若存在，则进入该字符对应的节点，重复步骤3判断下一个字符
            3.2若有字符不存在,在children属性中为该字符映射新节点，进入新节点，重复步骤3判断下个字符
        4直至所有字符判断结束，最后一个节点isword属性设为true，表示该strs已插入成功
        '''
        node = self.root
        for s in strs:
            if s not in node.children:
                node.children[s] = Node()
            node = node.children[s]
        node.isword = True
        
    def find(self,strs):
        ''' 查找原理：
        1将字符串分为单个字符，
        2取根节点和第一个字符
        3判断当前节点的children属性中是否存在该字符，
            3.1若存在，则进入该字符对应的节点，重复步骤3判断下一个字符，直至所有字符判断结束
                3.1.1 末节点的属性isword=True，则strs在Trie中，结果为找到
                3.1.2 isword=False，则不在，结果为未找到
            3.2若有字符不存在则strs不在trie中，结果为未找到
        4返回查找结果
        '''
        node = self.root
        for s in strs:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return node.isword