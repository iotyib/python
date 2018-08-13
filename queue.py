#!/usr/bin/env/python
#-*-coding:utf-8-*-

from multiprocessing import Queue,Process
import os,time,random

def write(q):
    for value in ['A','B','C']:
        print 'Put %s in queue...'%value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while not q.empty():
        value = q.get(True)
        print 'Get %s in queue...'%value
        time.sleep(random.random())

if __name__ == '__main__':
    # 父进程创建Queue并传递给各个子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动pw子进程，写入
    pw.start()
    # 等待pw结束
    pw.join()
    # 启动pr子进程，读取
    pr.start()
    # pr进程是死循环，无法等待结束，只能强制结束
    pr.join()
    print ''
    print '所有数据都已写入并且读完...'