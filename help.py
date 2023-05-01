from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Help Desk")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        img_top=Image.open(r"college_images\HelpDesk.jpg")
        img_top=img_top.resize((1280,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1280,height=650)

        t_lbl=Label(f_lbl,text="Email: anikets22222@gmail.com",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        t_lbl.place(x=350,y=300)
        t_lbl=Label(f_lbl,text="Mobile No: 9997289847",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
        t_lbl.place(x=430,y=370)


if __name__ =="__main__":
    root=Tk()
    obj=Helpdesk(root)
    root.mainloop()