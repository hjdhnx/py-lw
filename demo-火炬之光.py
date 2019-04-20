#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : demo-火炬之光.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/4/17

from comtypes import client
from time import  sleep
lw = client.CreateObject("lw.lwsoft3")
print(lw.ver())
game_runner="开始挑战"


def ClickFind(ret,name):
    if ret != None:
        ret = ret.split("|")
        if len(ret) == 1:
            ret = (ret[0].split(",")[1], ret[0].split(",")[2])
            #print(ret)
            global game_runner
            if name=="准备":
                getcengshu()
                game_runner="准备"
            elif name=="开始挑战":
                game_runner="爬塔结算"
            elif name=="作战":
                game_runner="远征结算"
            elif name=="爬塔结算":
                game_runner="确定"
            elif name=="远征结算":
                game_runner="远征返回"
            elif name=="远征返回":
                game_runner="作战"
            elif name=="确定":
                game_runner="挑战判断"
            elif name=="挑战判断":
                tiaozhanpanduan()
            elif name=="继续挑战":
                game_runner="结算"
            elif name=="返回主城":
                game_runner="结束"
            lw.MoveTo(int(ret[0]), int(ret[1]))
            lw.LeftClick()
            print("点击一次%s "%name,ret)


def jiesuan():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "立即结算", "B5C993-322345", 1.0)
    ClickFind(ret,"结算")
def zhunbei():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "准备", "9FB9BB-5E4543", 1.0)
    ClickFind(ret,"准备")
def queding():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "确定", "B1B2AD-4E4D51", 1.0)
    ClickFind(ret,"确定")
def fanhui():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "返回主城", "B0B0AE-4F4F51", 1.0)
    #9FB9BB-5E4543
    print("返回主城按钮的位置",ret)
    ClickFind(ret,"返回主城")
def getcengshu():
    ret = lw.Ocr(0,0,2000,2000,"B1B2AD-4E4D51",1.0)
    print("找到字符串",ret)
def kaishitiaozhan():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "开始挑战", "B1B2AD-4E4D51", 1.0)
    ClickFind(ret, "开始挑战")
def jixutiaozhan():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "继续挑战", "B1B2AD-4E4D51", 1.0)
    ClickFind(ret, "继续挑战")
def tiaozhanpanduan():
    global game_runner
    ret = lw.FindStrEx(0, 0, 2000, 2000, "禁止继续挑战", "B0B0AE-4F4F51", 1.0)
    if ret!=None:
        game_runner="返回主城"
        print("战力没解锁，返回并结束")
    else:
        game_runner="可以继续挑战，继续挑战"
def zuozhan():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "作战", "B0B0AE-4F4F51", 1.0)
    ClickFind(ret, "作战")
def yuanzhengfanhui():
    ret = lw.FindStrEx(0, 0, 2000, 2000, "远征返回", "DBA7A3-245154", 1.0)
    ClickFind(ret, "远征返回")
def 单人爬塔():
    global game_runner
    if game_runner=="开始挑战":
        kaishitiaozhan()
    elif game_runner=="爬塔结算":
        jiesuan()
    elif game_runner=="确定":
        queding()
    elif game_runner=="继续挑战":
        jixutiaozhan()
    elif game_runner=="返回主城":
        fanhui()
    elif game_runner=="结束":
        ret = lw.UnBindWindow()
        exit()

def 远征():
    global game_runner
    if game_runner=="作战":
        zuozhan()
    elif game_runner=="远征结算":
        jiesuan()
    elif game_runner=="远征返回":
        yuanzhengfanhui()
if __name__ == '__main__':

    hwnd=lw.FindWindow("多开器1","")
    hwnd1=hwnd
    print(hwnd)
    hwnd=lw.FindSonWindow(hwnd,"TheRender","RenderWindow")
    print(hwnd)
    ret = lw.IsBind(hwnd)
    print(ret)
    if ret==0:
        lw. EnableSwitchWindow(1)#禁止绑定前激活窗口
        binwindow=ret = lw.BindWindow(hwnd,5,1,1,0,0)
        print(binwindow)
    sleep(1)
    #ret = lw.SetWindowState(hwnd,3)
    ret = lw.Capture(0,0,2000,2000,"screen.bmp")
    ret = lw.SetDict(0,"huojudict.txt")
    ret = lw.UseDict(0)
    sleep(0.5)
    game_runner="作战"
    #ret=lw.UnBindWindow()
    #print("解绑效果:",ret)
    lw.MoveTo(719,7)
    while True:
        # 单人爬塔()
        #远征()
        lw.LeftClick()
        sleep(1)