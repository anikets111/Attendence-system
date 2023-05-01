from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Helpdesk
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Face Recognition System By AR")


        #first image
        img=Image.open(r"college_images\download.jpg")
        img=img.resize((410,120),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=410,height=120)

        #Second image
        img1=Image.open(r"college_images\download (4).jpg")
        img1=img1.resize((430,120),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=410,y=0,width=430,height=120)

        #third image
        img2=Image.open(r"college_images\download (1).jpg")
        img2=img2.resize((440,120),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=440,height=120)

        
        #bg image
        img3=Image.open(r"college_images\backimg.jpg")
        img3=img3.resize((1280,650),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1280,height=650)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE  ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1280,height=40)

        #======Time=======
        def time():
             string=strftime('%H:%M:%S %p')
             lbl.config(text = string)
             lbl.after(1000, time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg='white',fg='black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()     



        #Student button
        img4=Image.open(r"college_images\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4, cursor="hand2")
        b1.place(x=50,y=50,width=220,height=220)


        b1_1=Button(bg_img,command=self.student_details,text="Student Details", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=50,y=250,width=220,height=40)


        #Detect Face button
        img5=Image.open(r"college_images\FaceD.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=350,y=50,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=250,width=220,height=40)

        #attendence button
        img6=Image.open(r"college_images\Attendence.jpeg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6, cursor="hand2",command=self.attendence_data)
        b1.place(x=650,y=50,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence", cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=250,width=220,height=40)

        #Help Desk button
        img7=Image.open(r"college_images\Help.png")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_data, cursor="hand2")
        b1.place(x=950,y=50,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=250,width=220,height=40)



        #Train button
        img8=Image.open(r"college_images\Train.jpeg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=50,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=50,y=520,width=220,height=40)


        #Photos button
        img9=Image.open(r"college_images\Photos.jpeg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=350,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",command=self.open_img, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=520,width=220,height=40)

        #Developer button
        img10=Image.open(r"college_images\Developer.png")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b1.place(x=650,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650,y=520,width=220,height=40)


        #Exit button
        img11=Image.open(r"college_images\Exit.webp")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11, command=self.iExit,cursor="hand2")
        b1.place(x=950,y=320,width=220,height=220)

        b1_1=Button(bg_img,text="Exit", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=520,width=220,height=40)

    def open_img(self):
        os.startfile("data")



        #===========Function Buttons=================
    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)
   
   
    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)


    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendence(self.new_window)

    def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)

    def help_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Helpdesk(self.new_window)

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face recognition","Are you sure exit this project",parent=self.root)
         if self.iExit>0:
              self.root.destroy()
         else:
              return
              





if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
