from tkinter import *

def sal():
    num3.configure(state=NORMAL)
    num4.configure(state=NORMAL)
    num5.configure(state=NORMAL)
    num6.configure(state=NORMAL)
    inp1 = str(num1.get())
    inp2 = int(num2.get())
    comm = inp2 * 10/100
    num3.delete(0, END)
    num3.insert(0, comm)
    hra = inp2 * 15/100
    num4.delete(0, END)
    num4.insert(0, hra)
    pf = inp2 * 3/100
    num5.delete(0, END)
    num5.insert(0, pf)
    netsal = inp2 + comm + hra - pf
    num6.delete(0, END)
    num6.insert(0, netsal)

    num3.configure(state=DISABLED)
    num4.configure(state=DISABLED)
    num5.configure(state=DISABLED)
    num6.configure(state=DISABLED)


root = Tk()
root.geometry("700x700")
root.title("Star Code With Mo Arshad...")

lbl1 = Label(root, text="Emp Name:")
lbl2 = Label(root, text="Salary:")
lbl3 = Label(root, text="Comm:")
lbl4 = Label(root, text="HRA:")
lbl5 = Label(root, text="PF:")

num1 = Entry(root)
num2 = Entry(root)
num3 = Entry(root, state=DISABLED)
num4 = Entry(root,state=DISABLED)
num5 = Entry(root,state=DISABLED)
num6 = Entry(root, state=DISABLED)

btn = Button(root, text="Netpay", command=sal)

lbl1.place(x=10, y=10)
num1.place(x=80, y=10)

lbl2.place(x=10, y=50)
num2.place(x=80, y=50)

lbl3.place(x=10, y=90)
num3.place(x=80, y=90)

lbl4.place(x=10, y=130)
num4.place(x=80, y=130)

lbl5.place(x=10, y=170)
num5.place(x=80, y=170)

btn.place(x=80, y=210)

num6.place(x=80, y=250)


root.mainloop()
