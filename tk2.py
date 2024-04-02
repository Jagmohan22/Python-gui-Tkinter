from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import re

def handle_login():
    email = email_input.get()
    password = pass_input.get()

    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        if email == "jagmohannegi@gmail.com" and password == "jagmohan1234":
            messagebox.showinfo("Success", "Successfully logged in")
        else:
            messagebox.showerror("Login failed", "Invalid email or password")
    else:
        messagebox.showerror("Invalid email", "Please enter a valid email address")

def on_email_click(event):
    if email_input.get() == "Enter Email":
        email_input.delete(0, END)
        email_input.config(fg='black')

def on_pass_click(event):
    if pass_input.get() == "Enter Password":
        pass_input.delete(0, END)
        pass_input.config(fg='black')
        pass_input.config(show='*')

root = Tk()
root.title("Login form")
root.iconbitmap("hacker.ico")
root.geometry('400x500')
root.configure(background="#047BD5")

img = Image.open("image2.png")
resized_img = img.resize((100, 100))
img = ImageTk.PhotoImage(resized_img)
img_lable = Label(root, image=img)
img_lable.pack(pady=(10, 10))

text_lable = Label(root, text="flipkart", fg="white", bg="#047BD5")
text_lable.pack()
text_lable.config(font=("verdana", 24))

email_lable = Label(root, text="Enter Email", fg="white", bg="#047BD5")
email_lable.pack(pady=(20, 5))
email_lable.config(font=("verdana", 12))

email_input = Entry(root, width=50, fg='grey')
email_input.pack(ipady=6, pady=(1, 15))
email_input.insert(0, 'Enter Email')
email_input.bind("<FocusIn>", on_email_click)

pass_lable = Label(root, text="Enter Password", fg="white", bg="#047BD5")
pass_lable.pack(pady=(20, 5))
pass_lable.config(font=("verdana", 12))

pass_input = Entry(root, width=50, fg='grey')
pass_input.pack(ipady=6, pady=(1, 15))
pass_input.insert(0, 'Enter Password')
pass_input.bind("<FocusIn>", on_pass_click)

login_btn = Button(root, text="Login Here", bg='white', fg='black', width=15, height=2, command=handle_login)
login_btn.pack(pady=(10, 20))
login_btn.config(font=("verdana", 9))


root.mainloop()
