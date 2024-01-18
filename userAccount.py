import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.logged_in = True
            return True
        else:
            return False

    def logout(self):
        self.logged_in = False

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self)
        self.login_button["text"] = "Login"
        self.login_button["command"] = self.login
        self.login_button.pack()

        self.logout_button = tk.Button(self, text="Logout", command=self.logout, state=tk.DISABLED)
        self.logout_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if user.login(username, password):
            messagebox.showinfo("Login info", "Login successful")
            self.logout_button["state"] = tk.NORMAL
        else:
            messagebox.showinfo("Login info", "Username or password is incorrect")

    def logout(self):
        user.logout()
        self.logout_button["state"] = tk.DISABLED
        messagebox.showinfo("Logout info", "Logged out successfully")

user = User("admin", "password")
root = tk.Tk()
app = Application(master=root)
app.mainloop()