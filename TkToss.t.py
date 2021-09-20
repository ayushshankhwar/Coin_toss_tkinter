from tkinter import *
import random
def tss():
    # number = int(input("Number of times to flip coin: "))
    recordList = []
    heads = 0
    tails = 0
    for i in range(0, 1):
        # print("in loop")
        flip = random.randint(0, 1)
        if (flip == 0):
            # print("Heads")
            recordList.append("Heads")
        else:
            # print("Tails")
            recordList.append("Tails")

    # print(str(recordList))
    aaalabel = Label(win, text=recordList)
    aaalabel.pack()
win = Tk()
win.geometry("300x400")
win.title(" Coin Toss ")
menu = Menu(win)
win.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Flip",command=tss)
subMenu.add_command(label="Toss",command=tss)
subMenu.add_command(label="Exit",command=quit)
alabel = Label(win,text="_ Click the button below to toss the coin _")
alabel.pack()
button = Button(win,text="...TOSS...", command=tss)
button.pack()
win.mainloop()
