#!/usr/bin/python
__author__ = "DDENG"

import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
from tkinter import font

win = tk.Tk()
win.wm_title("排球隊熱情招生中!")                 # 設定抬頭名稱
win.minsize(width=500, height=450)             # 視窗最小為寬度 666 高度 480
win.maxsize(width=1024, height=768)            # 視窗最大為寬度 666 高度 480
win.resizable(width=True, height=True)
background_image = ImageTk.PhotoImage(Image.open("03.jpg"))
background_label = tk.Label(win, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def event1():
    global entry1       # Entry 輸入框的變數
    global entry2       # Entry 輸入框的變數
    global label1Str    # Label1 的文字 變數
    global choosen
    t1=entry1.get()     #取得用戶所輸入的文字
    t1=int(t1)
    t2=entry2.get()
    t2=str(t2)
    position=choosen.get()

    if position=='舉球員' and t1<=170 and t1>=150:
        answer="安啦!你非常適合!"
    elif position=='舉球員' and t1<150:
        answer="你要不要考慮一下當自由球員吧!"
    elif position=='舉球員'and t1>170:
        answer="你這麼高!!打攔中或主攻啦"
    elif position=='攔中' and t1<=175 and t1>160:
        answer="你可以來打主攻唷~"
    elif position == '攔中' and t1 <= 175 and t1<160:
        answer="嗯...要不要考慮打舉球呢"
    elif position=='攔中' and t1>175:
        answer="你身高不錯! 以後靠你啦!"
    elif position=='主攻' and t1<=180 and t1>=155:
        answer="主攻很適合你~"
    elif position=='主攻' and t1<155:
        answer="你要不要考慮打舉球或自由?"
    elif position=='主攻' and t1>180:
        answer="你這身高~來啦!打攔中"

    label1Str.set("嗨"+t2+"!\n"+str(answer))    #設定 Label1 的文字

def event2():
    result = tkMessageBox.askyesno("warning!", "Do you want to quit?")
    if result == True:
        quit()


menubar = tk.Menu(win)   #選單條
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=win.quit)
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)

label0 =tk.Label(win,text="排球隊熱情招生中!!!快來測測你適合哪個位置吧~",bg="#DDDDDD",
                 fg="#CC0000", font=('Courier',15))    #印出"排球隊熱情招生中!!!快來測測你適合哪個位置吧~"
label0.place(x=25,y=15)
label1 =tk.Label(win,text="選擇想要的位置:",bg="#DCDCDC",fg="black",font=('Courier',10))  #印出"選擇想要的位置"
label1.place(x=30,y=120)
label2 =tk.Label(win,text="輸入身高(cm):",bg="#DCDCDC",fg="black",font=('Courier',10))  #印出"輸入身高"
label2.place(x=30,y=180)
label3 =tk.Label(win,text="姓名or暱稱:",bg="#DCDCDC",fg="black",font=('Courier',10))  #印出"輸入身高"
label3.place(x=30,y=70)
label4 =tk.Label(win,bg="#DCDCDC",text="您適合位置為:",fg="black")   #印出"適合的位置"
label4.place(x=30,y=240)

label1Str=StringVar()  #適合位置的輸出元件變數
label5=tk.Label(win,bg="#DDDDDD",fg="black",text="ooooo",textvariable=label1Str,
                font=('Courier',10))
label5.place(x=40,y=300)

v1=tk.StringVar()  #性別選項元件變數
gender1 = tk.Radiobutton(win, text='男',bg="#DCDCDC", variable=v1, value='A')
gender1.place(x=230,y=70)
gender2= tk.Radiobutton(win, text='女',bg="#DCDCDC", variable=v1, value='B')
gender2.place(x=280,y=70)

entry1=tk.Entry(win,width=12)     #取得輸入數字(身高)
entry1.place(x=135,y=180)
entry2=tk.Entry(win,width=12)    #取得輸入字串(姓名)
entry2.place(x=120,y=70,width=80,height=20)

btn1 =tk.Button(win,text="確定",bg="#DDDDDD",command=event1)  #確定按鈕
btn1.place(x=240,y=175)

bt2=tk.Button(win,text="結束(Quit)",activebackground="yellow",activeforeground="red",
              bg="#DCDCDC",fg="purple",width=10,height=1,command=event2)   #離開按鈕及視窗
bt2.place(x=50,y=400)


# Combobox creation
n = tk.StringVar()
choosen = ttk.Combobox(win, width=8, textvariable=n)
# Adding combobox drop down list
choosen['values'] = ('--選擇位置--','舉球員','攔中','主攻')                #下拉攔 選擇位置
choosen.place(x=150,y=120)
choosen.current()

win.config(menu=menubar)
win.mainloop()


