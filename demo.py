#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : demo.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/4/16
from comtypes import client
from time import  sleep
lw = client.CreateObject("lw.lwsoft3")
print(lw.ver())

hwnd=lw.FindWindow("多开器1","")
hwnd1=hwnd
print(hwnd)
hwnd=lw.FindSonWindow(hwnd,"TheRender","RenderWindow")
print(hwnd)
ret = lw.IsBind(hwnd)
print(ret)
if ret==0:
    binwindow=lw.BindWindow(hwnd,4,1,256,0)
    print(binwindow)
lw.MoveTo (629,104)
lw.LeftClick()
ret = lw.Capture(0,0,2000,2000,"screen.bmp")
sleep(4)
ret = lw.SetWindowState(hwnd1,2)
ret = lw.SetDict(0,"xindongdict.txt")
ret = lw.FindStrEx(0,0,2000,2000,"开始按钮","c7e0ea-381F15",1.0)

print(ret)

if ret!=None:
    ret = ret.split("|")
    if len(ret)==1:
        ret=(ret[0].split(",")[1],ret[0].split(",")[2])
        print(ret)
        lw.MoveTo(int(ret[0]),int(ret[1]))
        lw.LeftClick()

sleep(2)
ret= lw.findpicex(0, 0, 2000, 2000, "心动女友脚本/字库保存的图片/签到.bmp")
print(ret)
if ret!=None:
    ret = ret.split("|")
    if len(ret)==1:
        ret=(ret[0].split(",")[1],ret[0].split(",")[2])
        print(ret)
        lw.MoveTo(int(ret[0]),int(ret[1]))
        lw.LeftClick()
        sleep(2)
        lw.MoveTo(658,565)
        lw.LeftClick()
        sleep(2)
        lw.moveto(980,146)
        lw.leftclick()