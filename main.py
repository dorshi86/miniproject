#from user import User
from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Radiobutton, Button

root = Tk()

# root.geometry('480x150')
root.resizable(width=False, height=False)
root.title('Mini Project')

can1=Canvas(root, width=500, height=500, bg="blue")
can1.pack(expand=False, fill=X)

lbl1 = Label(can1, text="Dor Shiloni", bg='blue' , fg='white', font=('Arial Bold', 24))
lbl1.grid(column=1, row=0)
lbl2 = Label(can1, text="INT Python Course", bg='blue', fg='white', font=('Arial Bold', 24))
lbl2.grid(column=1, row=1)

b1 = Button(can1, text="Register")
b1.grid(column=0,row=3)

b1 = Button(can1, text="Login")
b1.grid(column=3,row=3)



#
# combo = Combobox(window)
# combo['values'] = (1,2,3,4,5,6, 'Text')
#
# combo.current(0)
# combo.grid(column=1, row=1)
#
# chk = Checkbutton(window, text='check')
# chk.grid(column=1, row=2)
#
# rad1 = Radiobutton(window, text='first', value=1)
# rad2 = Radiobutton(window, text='second', value=2)
# rad3 = Radiobutton(window, text='third', value=4)
#
# rad1.grid(column=0, row=3)
# rad2.grid(column=0, row=3)
# rad3.grid(column=0, row=3)

# myVar = combo.get()

root.mainloop()