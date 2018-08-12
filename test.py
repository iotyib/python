#!/usr/bin/env/python
#-*-coding:utf-8-*-

import os

pid = os.fork()

if pid < 0:
    print '调用失败'
elif pid == 0:
    print '我是子进程%s,我的父进程是%s'%(os.getpid(),os.getppid())
else:
    print '我是父进程%s，我的子进程是%s'%(os.getpid(),pid)