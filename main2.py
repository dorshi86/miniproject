import tkinter as tk

class project:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.label1 = tk.Label(self.frame, text='Dor Shiloni Mini Project', font=('Arial Bold', 24))
        self.label1.pack()
        self.button1 = tk.Button(self.frame, text = 'Register', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Login', width = 25, command = self.new_window)
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Register(self.newWindow)

class Register:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = project(root)
    root.mainloop()

if __name__ == '__main__':
    main()