import tkinter as tk
import time
import os
import pyautogui as pag
from time import sleep

def onGo():
    print("go go go!")
    print(var.get())

def gettime():
    var.set(time.strftime("%H:%M:%S"))  # 獲取當前時間
    root.after(1000, gettime)  # 每隔1s調用函數 gettime 自身獲取時間

def getXY():
    try:
        while True:
            #print("Press Ctrl-C to end")
            screenWidth, screenHeight = pag.size()  #獲取螢幕的尺寸
            print(screenWidth,screenHeight)
            x,y = pag.position()   #獲取當前滑鼠的位置
            posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
            text = en.get()
            lb.config(text=text)
            #print(posStr)
            time.sleep(1)
            os.system('cls')   #清除螢幕
    except KeyboardInterrupt:
        print('end....')

root =tk.Tk()
root.title('入門案例')

var=tk.StringVar()
w =tk.Label(root, text="Hello Python!",textvariable=var,fg='blue',font=("微軟雅黑",40))
var.set("Hello Python!")
w.pack()

en = tk.Entry()
en.pack()

goBtn = tk.Button(text="測試",command=getXY,fg='blue',font=("黑體",20))
goBtn.pack()

lb = tk.Label(bg="#373737", fg="white",text="Please cleck the button")
lb.config(font="Calibri 20")
lb.pack()

root.mainloop()