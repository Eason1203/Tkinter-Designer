import  os
import  time
import datetime
import pyautogui as pag
from time import sleep
import keyboard
import tkinter as tk
from PIL import Image, ImageTk
import random
import pyperclip #處理複製的功能
import subprocess
from plyer import notification





# while True:
#     if keyboard.is_pressed('w'):
#         x = datetime.datetime.now()
#         #s1 = x.strftime("%d/%m/%Y, %H:%M:%S")
#         s1 = x.strftime("%y%m%d_%H%M%S")
#         print(s1)
#         myScreenshot = pag.screenshot(region=(9,267, 938, 528,))
#         myScreenshot.save(f'D:\\Pictures\\{s1}.png')
#     elif keyboard.is_pressed('s'):
#         print('Backward')
#     elif keyboard.is_pressed('a'):
#         print('Left')
#     elif keyboard.is_pressed('d'):
#         print('Right')
#     elif keyboard.is_pressed('enter'):  # if key 'enter' is pressed 
#         print('You pressed enter!')
#     elif keyboard.is_pressed('q'):
#         print('Quit!')
#         break

def screenshot():
    x = datetime.datetime.now()
    s1 = x.strftime("%y%m%d_%H%M%S")
    myScreenshot = pag.screenshot(region=(180,180, 1200, 750))
    myScreenshot.save(f'D:\\Pictures\\{s1}.png')
    notification.notify(
    title = 'screenshoted',
    message = f'{s1}.png',
    app_icon = None,
    timeout = 5,)

def getEn():
    text = en.get()
    lb.config(text=text)

def explorer():
    subprocess.Popen('explorer "C:\"')

    

    


window = tk.Tk()
window.title('Screenshot')
window.geometry('600x700+100+200')
# window.minsize(width=400, height=400)
# window.maxsize(width=1000, height=678)
window.resizable(False, False) 
#window.iconbitmap("\screenshot.ico")
#window.configure(bg="#373737")
window.config(padx=40, pady=20, bg="#373737")
window.attributes("-alpha", 0.85) #1-0  1=100% 0=0%
window.attributes("-topmost",1) #置頂
#image
img = tk.PhotoImage(file="screenshot.png")
#buttom
btn = tk.Button(text="click")
# btn.config(bg="#777777", width=10, height=1)
btn.config(image=img)
btn.config(command=screenshot)
btn.pack() # 封裝
#Label
lb = tk.Label(bg="#373737", fg="white",text="Please cleck the button")
lb.config(font="Calibri 20")
lb.pack()

en = tk.Entry()
en.pack()
btn= tk.Button(text="ok", command=getEn)
btn.pack()


def gen_xy():
    min_val= int(min_en.get())
    max_val= int(max_en.get())
    x = str(random.randint(min_val,max_val))
    y = str(random.randint(min_val,max_val))
    x_show.config(text="X: "+x)
    y_show.config(text="Y: "+y)

def copy():
    xy = x_show.cget("text") +"\n"+ y_show.cget("text")
    pyperclip.copy(xy)



min_en = tk.Entry()
min_en.pack()
max_en = tk.Entry()
max_en.pack()

x_show = tk.Label(bg="#373737", fg="white",text="")
x_show .config(font="Calibri 20")
x_show .pack()

y_show = tk.Label(bg="#373737", fg="white",text="")
y_show .config(font="Calibri 20")
y_show .pack()

gen_btn = tk.Button(text="generation", command=gen_xy)
gen_btn.pack()
copy_btn = tk.Button(text="copy", command=copy)
copy_btn.pack()

open_btn = tk.Button(text="explorer", command=explorer)
open_btn.pack()




window.mainloop()


# canvas = tk.Canvas(window, width=600, height=150, bg="#555555")
# canvas.create_text(10, 0, text='hello', anchor='nw')
# canvas.create_text(20, 20, text='world', anchor='nw', font=('Arial', 20))
# canvas.create_text(30, 40, text='I am\nOXXO', anchor='nw', fill='#f00', font=('Arial', 30, 'bold'))
# canvas.create_text(40, 110, text='中文測試', anchor='nw', fill='#0a0', font=('Arial', 30, 'bold','italic','underline'))
# canvas.pack()



#window.iconbitmap('icon.ico')

# myScreenshot = pag.screenshot(region=(9,267, 938, 528,))
# myScreenshot.save(f'D:\\Pictures\\{s1}.png')


# for i in range(5):
#     time.sleep(2)
#     time
#     #myScreenshot = pag.screenshot(region=(9,267, 949, 796,))
#     myScreenshot = pag.screenshot(region=(9,267, 938, 528,))
#     myScreenshot.save(f'./test{i}.png')
   