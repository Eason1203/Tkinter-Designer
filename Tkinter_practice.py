import tkinter as tk

window = tk.Tk()
window.title('Screenshot')
window.geometry('600x700+100+200')

Label = tk.Label(window, text='This is TK', bg='Green', font=('Arial,12'), width=15, height=2)
Label.pack()
window.mainloop 

