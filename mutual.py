#!/usr/bin/env/python
#-*-coding:utf-8-*-

from threading import Lock,Thread

g_num = 0
def test1():
    global g_num
    for i in range(100):
        mutualFlag = mutual.acquire(True)
        if mutualFlag:
            g_num += 1
            mutual.release()
    print 'test1%d'%g_num

def test2():
    global g_num
    for i in range(100):
        mutualFlag = mutual .acquire(True)
        if mutualFlag:
            g_num += 1
            mutual.release()
    print 'test2%d'%g_num
mutual = Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()
print g_num