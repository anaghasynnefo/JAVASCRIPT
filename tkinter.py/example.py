from tkinter import *
root=Tk()
l1=Label(root,text="enter first number")
e1=Entry(root)
l1.pack()
l2=Label(root,text="enter second number")
e2=Entry(root)
l2.pack()
e2.pack()
frame=Frame(root)
frame.pack()
btn=Button(frame,text="Add")
btn1=Button(frame,text="exit",command=frame.quit)
btn.grid(row=0,column=0)
btn1.grid(row=0,column=2)
l3=Label(root,text="result")
l3.pack()
root.mainloop()