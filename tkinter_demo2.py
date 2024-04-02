#this program is make for showing the image in my folder using tkinter in python 
from tkinter import*
from PIL import ImageTk,Image
import os

def rotate_image():
  global counter
  img_label.config(image=img_array[counter%len(img_array)])
  counter=counter+1
  

counter =1
root =Tk()
root.title = ("Wallpaper Viewer")

root.geometry=('600x700')
root.configure(background="black")

text_label=Label(root,text="Wallpaper Viewer",fg="#E50914",bg="black")
text_label.pack(pady=(10,10))
text_label.config(font=("Bebas Neue",24))


files=os.listdir("Wallpaper")
img_array=[]
for file in files:
  img=Image.open(os.path.join("Wallpaper",file))
  resized_img= img.resize((200,300))
  img_array.append(ImageTk.PhotoImage(resized_img))
  
img_label=Label(root,image=img_array[0])
img_label.pack(pady=(15,10))


next_btn=Button(root,text="Next",fg="black",bg="white",width=28,height=2,command=rotate_image)
next_btn.pack(pady=(15,10))

root.mainloop()
