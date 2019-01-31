from tkinter import *
from tkinter import filedialog
import sys
import os

with open("somefile.txt", "r+") as file1:
    file1.truncate()

for line in reversed(open("somefile.txt").readlines()):
    print(line.rstrip(-2))

root = Tk()

def copy_data():
    var = tbox2.get(1.0, 'end-1c')

    if var == "clear":
        os.remove("E:\schkoding\somefile.txt")
        f = open("somefile.txt","w+")
        frm = ""
        frm += f.read()

        tbox1.delete(1.0, 'end')
        tbox1.insert(1.0, frm)
        f.flush()

    else:
        with open("test.schok", "w") as att_file:
            att_file.write(var)
            
        os.system('output.bat')

        frm = ""
        file = open("somefile.txt", "r+")
        frm += file.read()

        file.flush()

        tbox1.delete(1.0, 'end')
        tbox1.insert(1.0, frm)

        file.close()
    
frame = Frame(root, width=1000, height=600)
frame.pack()

tbox1 = Text(frame)
tbox1.place(x=0, y=0, height=400, width=600)

tbox2 = Text(frame)
tbox2.place(x=0, y=400, height=800, width=1000)

tbox3 = Text(frame)
tbox3.place(x=500, y=0, height=400, width=500)
Button(frame, text='RUN', width="20", height="3", font='helvetica 20', bg="white",
       command=copy_data).place(x=600, y=500, height=30, width=100)

root.mainloop()
