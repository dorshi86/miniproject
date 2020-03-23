import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from user import User

# Main class for the program UI
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text='Register', width=25, command=self.open_register)
        self.button1.pack()
        self.button2 = Button(self.frame, text='Login', width=25, command=self.open_login)
        self.button2.pack()
        self.frame.pack()

    def open_register(self):
        self.newWindow = Toplevel(self.master)
        self.app = Register(self.newWindow)

    def open_login(self):
        self.newWindow = Toplevel(self.master)
        self.app = Login(self.newWindow)

# Class for the register process
class Register:
    # Register window
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.user_firstname_label = Label(self.master, text="First Name:")
        self.user_firstname_label.pack()

        self.user_firstname_text_box = Entry(self.master, bd=1)
        self.user_firstname_text_box.pack()

        self.user_lastname_label = Label(self.master, text="Last Name:")
        self.user_lastname_label.pack()

        self.user_lastname_text_box = Entry(self.master, bd=1)
        self.user_lastname_text_box.pack()

        self.user_email_label = Label(self.master, text="Email:")
        self.user_email_label.pack()

        self.user_email_text_box = Entry(self.master, bd=1)
        self.user_email_text_box.pack()

        self.user_gender_label = Label(self.master, text="Gender:")
        self.user_gender_label.pack()

        self.user_gender_combo = Combobox(self.master)
        self.user_gender_combo['values'] = ('Male','Female')
        self.user_gender_combo.pack()

        self.user_id_label = Label(self.master, text="User ID:")
        self.user_id_label.pack()

        self.user_id_text_box = Entry(self.master, bd=1)
        self.user_id_text_box.pack()

        self.user_pass_label = Label(self.master, text="User Password:")
        self.user_pass_label.pack()

        self.user_pass_text_box = Entry(self.master, bd=1)
        self.user_pass_text_box.pack()

        self.enter_button = Button(self.master, text="Enter", command=self.submit)
        self.enter_button.pack()
    # Submit process
    def submit(self):
        user_firstname = self.user_firstname_text_box.get()
        user_lastname = self.user_lastname_text_box.get()
        user_email = self.user_email_text_box.get()
        user_gender = self.user_gender_combo.get()
        user_id = self.user_id_text_box.get()
        user_pass = self.user_pass_text_box.get()
        Submit=User(user_firstname, user_lastname, user_email, user_gender, user_id, user_pass)
        messagebox.showinfo(title=Register, message=Submit.create_user())

# Class for the Login process
class Login:
    # Login Window
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.user_id_label = Label(self.master, text="User ID:")
        self.user_id_label.pack()

        self.user_id_text_box = Entry(self.master, bd=1)
        self.user_id_text_box.pack()

        self.user_pass_label = Label(self.master, text="User Password:")
        self.user_pass_label.pack()

        self.user_pass_text_box = Entry(self.master, bd=1)
        self.user_pass_text_box.pack()

        self.enter_button = Button(self.master, text="Enter", command=self.submit)
        self.enter_button.pack()
    # Submit process
    def submit(self):
        user_id = self.user_id_text_box.get()
        user_pass = self.user_pass_text_box.get()
        Submit=User(0,0,0,0,user_id,user_pass)
        messagebox.showinfo(title=Login, message=Submit.validate_user())

root = Tk()
app = MainWindow(root)
root.mainloop()
