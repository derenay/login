import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import subprocess
import sys
import os
import customtkinter as ct
from customtkinter import *
import threading


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        self.user_name_var = tk.StringVar()
        self.user_pass_var = tk.StringVar()

        img = Image.open("lisi-aerospace-FTB.png")
        resized_image = img.resize((300, 205))
        self.new_image = ImageTk.PhotoImage(resized_image)

        self.create_widgets()

    def create_widgets(self):
        img_label = Label(self.root, image=self.new_image, bg="white")
        img_label.place(x=50, y=150)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=480, y=50)

        Headling_label = Label(frame, text="Sing in", fg="#57a1f8", bg="white",
                               font=("Microsoft YaHei Light", 26, "bold"), padx=10, pady=10)
        Headling_label.place(x=170, anchor=N)

        user_holder_text = "Username"
        self.user_entry = CTkEntry(master=frame, font=("Microsoft YaHei Light", 12, "bold"), height=1, width=200,
                                   fg_color="white", border_width=1, textvariable=self.user_name_var)
        self.user_entry.insert(0, user_holder_text)
        self.user_entry.bind("<FocusIn>", self.uon_entry_click)
        self.user_entry.bind("<FocusOut>", self.uon_focus_out)
        self.user_entry.place(x=75, y=120)

        placeholder_text = "pass"
        self.pass_entry = CTkEntry(master=frame, font=("Microsoft YaHei Light", 12, "bold"), height=1, width=200,
                                   fg_color="transparent", border_width=1, textvariable=self.user_pass_var,
                                   show="\u2022", placeholder_text="pass")
        self.pass_entry.insert(0, placeholder_text)
        self.pass_entry.bind("<FocusIn>", self.on_entry_click)
        self.pass_entry.bind("<FocusOut>", self.on_focus_out)
        self.pass_entry.place(x=75, y=150)

        button = CTkButton(master=frame, text="Log in", command=self.submit)
        button.place(x=105, y=200)

    def uon_entry_click(self, event):
        if self.user_entry.get() == "Username":
            self.user_entry.delete(0, tk.END)

    def uon_focus_out(self, event):
        if self.user_entry.get() == "":
            self.user_entry.insert(0, "Username")

    def on_entry_click(self, event):
        if self.pass_entry.get() == "pass":
            self.pass_entry.delete(0, tk.END)
            self.pass_entry.configure(show="•")

    def on_focus_out(self, event):
        if self.pass_entry.get() == "":
            self.pass_entry.insert(0, "pass")
            self.pass_entry.configure(show="")

    def submit(self):
        user_name = "admin"
        password = "selam"
        User_name_var = self.user_name_var.get()
        User_pass_var = self.user_pass_var.get()

        if User_name_var == user_name and User_pass_var == password:
            self.access()
        else:
            self.reject()

        self.user_name_var.set("")
        self.user_pass_var.set("")

    def access(self):
        def run_subprocess():
            subprocess.run(["python", "main.py", "--logged_in"])

        t = threading.Thread(target=run_subprocess)
        t.start()

        print("access")
        self.root.destroy()

    def reject(self):
        print("wrong")


if __name__ == "__main__":
    login_root = Tk()
    login_app = LoginWindow(login_root)
    login_root.mainloop()
    os._exit(0)
