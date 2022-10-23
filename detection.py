import  os
import  time
import pyautogui as pag
from time import sleep

try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  #獲取螢幕的尺寸
        print(screenWidth,screenHeight)
        x,y = pag.position()   #獲取當前滑鼠的位置
        posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
        print(posStr)
        time.sleep(0.5)
        os.system('cls')   #清除螢幕
except KeyboardInterrupt:
    print('end....')