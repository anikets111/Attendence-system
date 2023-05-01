from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog




mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x700+0+0")
        self.root.title("Attendence SYSTEM")
        #=========== Text Variables==========
        self.var_attenid=StringVar()
        self.var_attenroll=StringVar()
        self.var_attenname=StringVar()
        self.var_attendep=StringVar()
        self.var_attentime=StringVar()
        self.var_attendate=StringVar()
        self.var_attenda=StringVar()






        img1=Image.open(r"college_images\att.jpg")
        img1=img1.resize((640,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=640,height=150)

        img2=Image.open(r"college_images\clg.jpg")
        img2=img2.resize((640,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=640,y=0,width=640,height=150)

        title_lbl=Label(self.root,text="Attendence Management System  ",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=150,width=1280,height=45)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=8,y=200,width=1255,height=480)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=2,width=610,height=470)

        img_left=Image.open(r"college_images\images1.jpeg")
        img_left=img_left.resize((600,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=600,height=120)

        m_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        m_frame.place(x=3,y=130,width=600,height=310)

        attendenceId=Label(m_frame,text="AttendenceID:",font=("times new roman",12,"bold"),bg="white")
        attendenceId.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        attendenceI=ttk.Entry(m_frame,width=20,textvariable=self.var_attenid,font=("times new roman",12,"bold"))
        attendenceI.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        rollLabel=Label(m_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        rollL=ttk.Entry(m_frame,width=20,textvariable=self.var_attenroll,font=("times new roman",12,"bold"))
        rollL.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        nameLabel=Label(m_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        nameL=ttk.Entry(m_frame,width=20,textvariable=self.var_attenname,font=("times new roman",12,"bold"))
        nameL.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        depLabel=Label(m_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        depL=ttk.Entry(m_frame,width=20,textvariable=self.var_attendep,font=("times new roman",12,"bold"))
        depL.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        timeLabel=Label(m_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=2,pady=10,sticky=W)
        timeL=ttk.Entry(m_frame,width=20,textvariable=self.var_attentime,font=("times new roman",12,"bold"))
        timeL.grid(row=2,column=1,padx=2,pady=10,sticky=W)


        dateLabel=Label(m_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=2,pady=10,sticky=W)
        dateL=ttk.Entry(m_frame,width=20,textvariable=self.var_attendate,font=("times new roman",12,"bold"))
        dateL.grid(row=2,column=3,padx=2,pady=10,sticky=W)


        attendenceLab=Label(m_frame,text="Attendence Status:",font=("times new roman",12,"bold"),bg="white")
        attendenceLab.grid(row=3,column=0,padx=2,pady=10,sticky=W)
        
        self.atten_status=ttk.Combobox(m_frame,width=16,textvariable=self.var_attenda,font=("comicsansns",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=10)
        self.atten_status.current(0)

        btn_frame=Frame(m_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=260,width=590,height=35)

        save_btn=Button(btn_frame,text="Import csv",width=15,command=self.importCsv,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",width=16,command=self.exportCsv,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)
        








        # Right Label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=2,width=610,height=470)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=595,height=430)

        #====scroll bar table===========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence Id")      
        self.AttendenceReportTable.heading("roll",text="Roll No")
        self.AttendenceReportTable.heading("name",text="Name")        
        self.AttendenceReportTable.heading("department",text="Department")       
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence Status")

        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=150)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)



    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)



    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully") 

        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attenid.set(rows[0])
        self.var_attenroll.set(rows[1])
        self.var_attenname.set(rows[2])
        self.var_attendep.set(rows[3])
        self.var_attentime.set(rows[4])
        self.var_attendate.set(rows[5])
        self.var_attenda.set(rows[6])

    def reset_data(self,):
        self.var_attenid.set("")
        self.var_attenroll.set("")
        self.var_attenname.set("")
        self.var_attendep.set("")
        self.var_attentime.set("")
        self.var_attendate.set("")
        self.var_attenda.set("Status")














if __name__ =="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()