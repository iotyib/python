#-*-coding:utf-8-*-

class Deque(object):
    '''双端队列：双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端执行。双端队列可以在队列任意一端入队和出队'''
    def __init__(self):
        self.items = []

    def is_empey(self):
        '''判断队列是否为空'''
        return self.items == []

    def addFront(self,item):
        '''在队头添加元素'''
        self.items.insert(0,item)

    def addRear(self,item):
        '''在队尾添加元素'''
        self.items.append(item)

    def removeFront(self):
        '''队头删除元素'''
        return self.items.pop(0)

    def removeRear(self):
        '''队尾删除元素'''
        return self.items.pop()

    def size(self):
        '''返回队列大小'''
        return len(self.items)

if __name__ == '__main__':
    deque = Deque()
    deque.addFront(1)
    deque.addFront(2)
    deque.addRear(3)
    deque.addRear(4)
    print deque.size()
    print deque.removeFront()
    print deque.removeFront()
    print deque.removeRear()
    print deque.removeRear()