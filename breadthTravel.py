#-*-coding:utf-8-*-

def breadthTravel(self,root):
    '''利用队列实现树的遍历'''
    if root == None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print node.elem
        if node.lchild != None:
            queue.append(node.lchild)
        if node.rchild == None:
            queue.append(node.rchild)
        