#-*-coding:utf-8-*-

def quickSort(alist,start,end):
    '''快速排序'''

    #退出递归的条件
    if start >= end:
        return

    #设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    #low为序列左边的由左至右的游标
    low = start

    #high为序列右边的从右至左的游标
    high = end

    while  low < high:
        #如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        #将high指向的元素放到low位置上
        alist[low] = alist[high]

        #如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        #将low指向的元素放到high位置上
        alist[high] = alist[low]

    #退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    #将基准元素放到该位置
    alist[low] = mid

    #将基准元素左边的子序列进行快速排序
    quickSort(alist,start,low-1)

    #对基准元素右边的子序列进行快速排序
    quickSort(alist,low+1,end)

if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    quickSort(alist,0,len(alist)-1)
    print alist