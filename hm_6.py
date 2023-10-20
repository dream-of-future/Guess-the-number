import tkinter as tk
import random
number=random.randint(0,1024)     # 随机数范围
running=True                      # 判断是否执行
num=0                             # 猜的次数
nmaxn=1024                        # 最大值
nminn=0                           # 最小值

times = 1
def eBtnClose(event):             # 关闭
    root.destroy()
    print('您一共玩了',times,'次')


def eBtnGuess(event):             # 游戏主程序
    global nmaxn
    global nminn
    global num
    global running                # 设置全局变量
    if running:                   # 判断是否运行
        val_a=int(entry_a.get())
        if val_a==number:         # 判断输入
            labelqval("恭喜答对了！")
            num+=1
            running=False         # 终止主程序（if为假）
            numGuess()
        elif val_a<number:
            if val_a>nminn:
                nminn=val_a       # 将最小改为输入值
                num+=1
                labelqval("小了哦，请输入"+str(nminn)+"到"+str(nmaxn)+"之间任意整数：")
        else:
            if val_a<nmaxn:
                nmaxn=val_a       # 将最大改为输入值
                num+=1
                labelqval("大了哦，请输入"+str(nminn)+"到"+str(nmaxn)+"之间的任意整数：")
    else:
        labelqval('你已经答对了！')


def numGuess():                   # 提示信息
    if num==1:
        labelqval('真棒，一次就答对了')
    elif num<10:
        labelqval('不错喔，十次以内答对了牛。。。尝试次数：'+str(num))
    else:
        labelqval('好吧，你都尝试超过10次了。。。尝试次数：'+str(num))
def labelqval(vText):
    label_val_q.config(label_val_q,text=vText)


def reset(event):                       # 重开一把
    global times
    times += 1
    global nmaxn
    global nminn
    global num
    global running
    global number
    number = random.randint(0, 1024)
    running = True
    num = 0
    nmaxn = 1024
    nminn = 0
    eBtnGuess(event)



root=tk.Tk(className="猜数字游戏")
root.geometry("400x90+200+200")
label_val_q=tk.Label(root,width="80")
label_val_q.pack(side="top")
entry_a=tk.Entry(root,width='40')
btnGuess=tk.Button(root,text="猜")
entry_a.pack(side="left")
entry_a.bind('<Return>',eBtnGuess)
btnGuess.bind("<Button-1>",eBtnGuess)
btnGuess.pack(side="left")

btnAgain=tk.Button(root,text='重开')  # 自己加的代码
btnAgain.bind('<Button-1>',reset)
btnAgain.pack(side="left")

btnClose=tk.Button(root,text='关闭')
btnClose.bind('<Button-1>',eBtnClose)
btnClose.pack(side="right")
labelqval("请输入0~1024之间的任意整数：")
entry_a.focus_set()
print(number)
root.mainloop()
