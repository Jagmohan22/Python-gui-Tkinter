from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
  email = email_input.get()
  password = pass_input.get()
  if(email == "jagmohannegi@gamil.com" and password == "jagmohan1234"):
    # print("Succefully logged in")
    messagebox.showinfo("Succefully logged in")
  else:
    # print("Login failed")
    messagebox.showerror("Login failed")
  
  

root = Tk()
root.title("Login form")
root.iconbitmap("Python-gui-Tkinter/hacker.ico")
root.geometry('400x500')
# root.minsize(500,500)
root.configure(background="#047BD5")

img=Image.open("Python-gui-Tkinter/image2.png")
resized_img= img.resize((100,100))
img= ImageTk.PhotoImage(resized_img)
# img=ImageTk.PhotoImage(Image.open("Python-gui-Tkinter/image2.png"))
img_lable =Label(root,image=img)
img_lable.pack(pady=(10,10))

text_lable =Label(root,text="flipkart",fg="white",bg="#047BD5")
text_lable.pack()
text_lable.config(font=("verdana",24))

email_lable=Label(root,text="Enter Email",fg="white",bg="#047BD5")
email_lable.pack(pady=(20,5))
email_lable.config(font=("verdana",12))
email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))


pass_lable=Label(root,text="Enter Password",fg="white",bg="#047BD5")
pass_lable.pack(pady=(20,5))
pass_lable.config(font=("verdana",12))

pass_input=Entry(root,width=50)
pass_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root, text="Login Here",bg='white',fg='black',width=15,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",9))


root.mainloop()

