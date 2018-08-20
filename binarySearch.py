#-*-coding:utf-8-*-

'''
def binarySearch(alist,item):
    #非递归实现
    first = 0
    last = len(alist)-1
    while first <= last:
        midpoint = (first+last)/2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False
'''
def binarySearch(alist,item):
    '''递归实现'''
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

if __name__ == '__main__':
    alist = [0,1,2,8,13,17,19,32,43]
    print binarySearch(alist,3)
    print binarySearch(alist,13)