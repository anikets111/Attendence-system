from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Student Details")


#===========variables==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #first image
        img=Image.open(r"college_images\images.jpeg")
        img=img.resize((410,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=410,height=120)

        #Second image
        img1=Image.open(r"college_images\download.jpeg")
        img1=img1.resize((430,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=410,y=0,width=430,height=120)

        #third image
        img2=Image.open(r"college_images\download1.jpeg")
        img2=img2.resize((440,120),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=440,height=120)

        #bg image
        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1280,650),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1280,height=650)

        title_lbl=Label(bg_img,text="Student Management System  ",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=8,y=55,width=1255,height=500)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=480)

        #left label image
        img_left=Image.open(r"college_images\images1.jpeg")
        img_left=img_left.resize((600,40),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=600,height=40)

#current Course
        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Details",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=43,width=600,height=100)

#Department
        dep_label=Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","E&T","Nursing","Medical","ParaMedical","Others")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

#Course
        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","MCA","BCA","BSc","B.Tech","MBA","MBBS","Others")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

#Year
        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","Others")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

#semester
        semester_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8","Others")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)
        
#Class Student Information
        Student_info=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Student_info.place(x=5,y=145,width=600,height=310)

#Student Id
        stID_label=Label(Student_info,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        stID_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        stID_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_id,font=("times new roman",12,"bold"))
        stID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

#Student Name
        stName_label=Label(Student_info,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        stName_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        stName_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        stName_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

#Class Division
        cd_label=Label(Student_info,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        cd_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        cd_combo=ttk.Combobox(Student_info,textvariable=self.var_div,font=("times new roman",12,"bold"),width=13,state="readonly")
        cd_combo["values"]=("Select Division","A","B","C","D")
        cd_combo.current(0)
        cd_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#Roll No
        roll_label=Label(Student_info,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        roll_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

#Gender
        gender_label=Label(Student_info,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=2,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Student_info,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=13,state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

#DOB
        dob_label=Label(Student_info,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        dob_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W) 

#Email
        email_label=Label(Student_info,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2,pady=5,sticky=W)

        email_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W) 

#Phone No
        phno_label=Label(Student_info,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phno_label.grid(row=3,column=2,padx=2,pady=5,sticky=W)

        phno_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phno_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)                      

#address
        address_label=Label(Student_info,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2,pady=5,sticky=W)

        address_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

#Teacher Name
        teacher_label=Label(Student_info,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=2,pady=5,sticky=W)

        teacher_entry=ttk.Entry(Student_info,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

#Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Student_info,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        
        radiobtn2=ttk.Radiobutton(Student_info,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

#Buttons Frame        
        btn_frame=Frame(Student_info,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=580,height=35)

        save_btn=Button(btn_frame,text="Save",width=15,command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        btn_frame1=Frame(Student_info,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=580,height=35)
        
        Take_btn=Button(btn_frame1,text="Take a Photo sample",command=self.generate_dataset,width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Take_btn.grid(row=0,column=0)

        up_btn=Button(btn_frame1,text="Update Photo sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        up_btn.grid(row=0,column=1)


 # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=10,width=610,height=480)

        img_right=Image.open(r"college_images\images (1).jpeg")
        img_right=img_right.resize((600,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=600,height=120)
        
        #===========Search System==============

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=125,width=600,height=60)

        search_lbl=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_lbl.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone No.","Student name","ID","Others")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=18,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        show_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",11,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4,padx=2)

        #==========Table Frame=========
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=190,width=600,height=265)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Adderss")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #=======Function Decl========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_id.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                                

                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Details saved succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
           
    #===========Fetchdata=========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #=============get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #   Update Buton

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                Upadate=messagebox.askyesno("update","Do you want to update the details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,student_id=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s ",(


                                                                                                                                                                                   self.var_dep.get(),
                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                   self.var_id.get(),
                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                   self.var_name.get(),
                                                                                                                                                                                   self.var_div.get(),
                                                                                                                                                                                   self.var_roll.get(),
                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                   self.var_dob.get(),
                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                   self.var_teacher.get(),
                                                                                                                                                                                   self.var_radio1.get(),
                                                                                                                                                                                   self.var_id.get(),

                                                                                                                                                                                     ))

                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Update Successfully",parent=self.root)   
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     

    # Delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

    #  reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")



    #===========  Generate Data set Take a sample   ===============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("select * from student")
               myresult=my_cursor.fetchall()
               ide=0
               for x in myresult:
                   ide+=1
               my_cursor.execute("update student set dep=%s,course=%s,year=%s,student_id=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(


                                                                                                                                                                                   self.var_dep.get(),
                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                   self.var_id.get(),
                                                                                                                                                                                   self.var_semester.get(),                                                                                                                                                                              
                                                                                                                                                                                   self.var_name.get(),
                                                                                                                                                                                   self.var_div.get(),
                                                                                                                                                                                   self.var_roll.get(),
                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                   self.var_dob.get(),
                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                   self.var_teacher.get(),
                                                                                                                                                                                   self.var_radio1.get(),
                                                                                                                                                                                   self.var_id.get()==ide+1

                                                                                                                                                                                     ))
               conn.commit()
               self.fetch_data()
               self.reset_data()
               conn.close()
               #load data on frontal face cv2
               face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

               def face_cropped(img):
                   gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                   faces=face_classifier.detectMultiScale(gray,1.3,5)

                   for (x,y,w,h) in faces:
                       face_cropped=img[y:y+h,x:x+w]
                       return face_cropped
                   
               cap=cv2.VideoCapture(0)
               img_id=0
               while True:
                   ret,myframe=cap.read()
                   if face_cropped(myframe) is not None:
                       img_id+=1
                       face=cv2.resize(face_cropped(myframe),(450,450))
                       face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                       file_name="data/user."+str(ide)+"."+str(img_id)+".jpg"
                       cv2.imwrite(file_name,face)
                       cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                       cv2.imshow("Cropped Face",face)

                   if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
               cap.release()
               cv2.destroyAllWindows()

               messagebox.showinfo("Result","Generating data set Completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   



if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()