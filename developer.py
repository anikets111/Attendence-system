from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Developer")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1280,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1280,height=650)


        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=450,height=600)

        img_t=Image.open(r"college_images\Aniket.jpg")
        img_t=img_t.resize((140,210),Image.ANTIALIAS)
        self.photoimg_t=ImageTk.PhotoImage(img_t)

        f_lbl=Label(main_frame,image=self.photoimg_t)
        f_lbl.place(x=305,y=0,width=140,height=210)

#==========Developer Information=========
        dev_lbl=Label(main_frame,text="Hello my name is Aniket Rajput",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_lbl.place(x=0,y=5)

        dev_lbl=Label(main_frame,text="I am a student of Rama University",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_lbl.place(x=0,y=40)


        





if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()