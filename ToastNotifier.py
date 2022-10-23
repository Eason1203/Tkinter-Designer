from win10toast import ToastNotifier 
from time import strftime
import PIL.Image
import os
import keyboard

icon = PIL.Image.open("Testpng.png")
icon.save("Testpng.ico")

seconds = [10,20,30,40,50,59]
while True:
    sec = strftime("%S")
    if int(sec) in seconds:
        a = ToastNotifier()
        a.show_toast(
            title=f"{sec} notificaiton",
            msg=f"Sir the seconds on {sec}",
            icon_path ="Testpng.ico",
            duration=5
        )
    elif keyboard.is_pressed('q'):
        print('Quit!')
        break
    
    # elif key == 27: #ESC
    #     print("You pressed ESC")
    #     break

