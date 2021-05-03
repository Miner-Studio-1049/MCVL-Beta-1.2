########################
### JRRP.py          ###
### 原作者: 熊熊糖果 ###
### 版本号: 2.0.0    ###
########################
'''
====调用方式=======================================================
import JRRP            # 导入JRRP文件
JRRP.Jrrp()            # 自动根据时间和识别码计算人品
Jrrp.jrrp(code,time)   # 手动提供识别码计算人品，时间，要求int类型，8位数
Jrrp.getcode()         # 获取识别码
Jrrp.writecode()       # 写入识别码
-----一些不重要的小功能--------------
Jrrp.read_reg(dir,key) # 读注册表，dir:注册表文件夹路径，key:键名
Jrrp.cmd(command)      # 后台运行cmd不弹窗
-------------------------------------
===================================================================
'''

from time import strftime,localtime
from random import randint
import winreg
from subprocess import run
def read_reg(l,s):
    location = l
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, location)
    i = 0
    while True:
        try:
            a=winreg.EnumValue(key, i)
            if a[0]==s:
                return a[1]
            i += 1
        except OSError as error:
            winreg.CloseKey(key)
            break
def cmd(c):
    run(c,shell=True)
def writecode(code):
    cmd(f'reg add "HKCU\\Software\\MCVL" /v Code /t REG_DWORD /d {str(code)} /f')
def getcode():
    code=str(read_reg(r"Software\\MCVL","Code"))
    return code
def jrrp(code,time):
    data=int(code)+time
    d=data
    c=code
    try:
        j=(((d+1324)*(((d+154)*(c+1))%(c+3421)+((d+879)*(c+34))%((c+413)%(9*(((d+87)*(c+213))%((c+45)+76))))))+(((d+1)*(c+43))%(c+1)+((d+234)*(c+654))%((c+32)%(453*(((d+5362)*(c+532))%((c+86)+234)))))+91312)%101
    except:
        data=data*2
        j=jrrp(data,time)
    return j
def Jrrp():
    try:
        code=int(getcode())
    except:
        code=randint(10000000,99999999)
        c=str(code)
        writecode(c)
    time=int(strftime("%Y%m%d",localtime()))
    return jrrp(code,time)
