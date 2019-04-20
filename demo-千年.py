#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : demo-千年.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/4/16
from comtypes import client
from time import  sleep
lw = client.CreateObject("lw.lwsoft3")
print(lw.ver())
hwnd=lw.FindWindow("星辰千年","")
print(hwnd)
ret = lw.IsBind(hwnd)
print(ret)
if ret==0:
    binwindow=lw.BindWindow(hwnd,4,1,1,0,0)
    print(binwindow)
ret = lw.SetWindowState(hwnd,1)
sleep(1)


for i in range(200):
    lw.MoveTo(776, 508)
    lw.LeftClick()
    sleep(0.1)
