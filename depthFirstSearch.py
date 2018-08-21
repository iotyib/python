#-*-coding:utf-8-*-

def preorder(self,root):
    '''递归实现先序遍历'''
    if root == None:
        return
    print root.elem
    self.preorder(root.lchild)
    self.preorder(root.rchild)


def inorder(self,root):
    '''递归实现中序遍历'''
    if root == None:
        return
    self.inorder(root.lchild)
    print root.elem
    self.inorder(root.rchild)


def postorder(self,root):
    '''递归实现后序遍历'''
    if root == None:
        return
    self.postorder(root.lchild)
    self.postorder(root.rchild)
    print root.elem
