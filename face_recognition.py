from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import requests
import os
import numpy as np
from time import strftime
from datetime import datetime
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")




        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1280,height=45)


        img_bottom=Image.open(r"college_images\face1.jpg")
        img_bottom=img_bottom.resize((550,650),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb=Label(self.root,image=self.photoimg_bottom)
        f_lb.place(x=0,y=50,width=550,height=650)
        
        img_b=Image.open(r"college_images\facial.webp")
        img_b=img_b.resize((730,650),Image.LANCZOS)
        self.photoimg_b=ImageTk.PhotoImage(img_b)

        f_lbl=Label(self.root,image=self.photoimg_b)
        f_lbl.place(x=550,y=50,width=730,height=650)

        b1_1=Button(f_lbl,text="Punch Out",command=self.Leaving, cursor="hand2",font=("times new roman",16,"bold"),bg="green",fg="white")
        b1_1.place(x=275,y=570,width=174,height=40)

        b1_2=Button(f_lbl,text="Punch In",command=self.Arriving, cursor="hand2",font=("times new roman",16,"bold"),bg="green",fg="white")
        b1_2.place(x=275,y=60,width=174,height=40)



    #============Save in Database================
    
    #===============attendence===================

    def mark_attendence(self,i,r,n,d):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
        my_cursor=conn.cursor()

        my_cursor.execute("select Id from arriving")
        i1=my_cursor.fetchall()
        i1=[row[0] for row in i1]

        if((i not in i1)):
            try:
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                my_cursor.execute("insert into arriving(Id,Name,Time,Date,Status) values(%s,%s,%s,%s,%s)",(i,n,dtString,d1,"Present"))
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                

    def mark_leave(self,i,r,n,d):
        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
        my_cursor=conn.cursor()

        my_cursor.execute("select Id from leaving")
        i1=my_cursor.fetchall()
        i1=[row[0] for row in i1]

        if((i not in i1)):
            try:
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                my_cursor.execute("insert into leaving(Id,Name,Time,Date,Status) values(%s,%s,%s,%s,%s)",(i,n,dtString,d1,"Leave_Out"))
                
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


        #===========Face recognition ==============

    def Arriving(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                

                if confidence>70:
                    cv2.putText(img,f"ID :{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"Roll no:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    self.mark_attendence(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)

                coord=[x,y,w,h]
            return coord  

        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            if ret:
                img=recognize(img, clf, faceCascade)
                cv2.imshow("Welcome", img)

                if cv2.waitKey(1)==13:
                    break
            else:
                break    

        video_cap.release()
        cv2.destroyAllWindows()

    def Leaving(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                

                if confidence>70:
                    cv2.putText(img,f"ID :{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"Roll no:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    self.mark_leave(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)

                coord=[x,y,w,h]
            return coord  

        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf=cv2.face_LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome", img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()                  
                    




if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
