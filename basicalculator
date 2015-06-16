from math import *
from tkinter import *
 
def calculator():
	data = box.get()
	data = str(data)
	if data == "":
		result.config(text = "Please do something!!!")
	else:
		snm = "global result2;result2 ="+data
		exec(snm)
		print(snm,"\n",result2)
		result.config(text = str(result2))
 
         
mainwindow = Tk()
mainwindow.geometry("400x200+100+100")
mainwindow.title("Basic Calculator")
 
result = Label(mainwindow)
result.config(text = "Now, you can do calculate! \n", font = "bold 23",fg = "red")
result.pack()


box = Entry(mainwindow)
box.pack()
 
buton = Button(mainwindow)
buton.config(text = "You Can Calculate!",command = calculator)
buton.pack()
buton = Button(mainwindow)
buton.config(text = "EXİT!", command = exit)
buton.pack()
mainloop()
