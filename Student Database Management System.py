import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

root=Tk()

class Student(tk.Frame):
     def __init__(self,root):
        
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        self.canvas = tk.Canvas(self.root,bd=4,relief=RIDGE,bg="brown")
        self.canvas.place(x=5,y=100,width=600,height=700)

        self.Manage_Frame=tk.Frame(self.canvas,bd=4,relief=RIDGE,bg="maroon")
        self.Manage_Frame.place(x=5,y=100,width=600,height=700)

        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.create_window((4,4), window=self.Manage_Frame, anchor="nw", tags="self.Manage_Frame")
        self.Manage_Frame.bind("<Configure>",self.onFrameConfigure)
        self.populate()

        
        title=Label(self.canvas,text="Student Management System", bd=10, relief=GROOVE ,font=("times new roman",39),bg="maroon",fg="white")
        title.pack(side=TOP,fill=X)
                

#==========MANAGE FRAME========== 

        
     def populate(self):

        self.USN_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Semester_var=StringVar()
        self.Age_var=StringVar()
        self.Semid_var=StringVar()
        self.Subject1_var=StringVar()
        self.Marks11_var=StringVar()
        self.Marks12_var=StringVar()
        self.Marks13_var=StringVar()
        self.Average1_var=IntVar()
        self.Subject2_var=StringVar()
        self.Marks21_var=StringVar()
        self.Marks22_var=StringVar()
        self.Marks23_var=StringVar()
        self.Average2_var=IntVar()
        self.Subject3_var=StringVar()
        self.Marks31_var=StringVar()
        self.Marks32_var=StringVar()
        self.Marks33_var=StringVar()
        self.Average3_var=IntVar()
        self.Subject4_var=StringVar()
        self.Marks41_var=StringVar()
        self.Marks42_var=StringVar()
        self.Marks43_var=StringVar()
        self.Average4_var=IntVar()
        self.Guardian_var=StringVar()
        self.Relationship_var=StringVar()
        self.Pno_var=StringVar()


        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.search_by1=StringVar()
        self.search_txt1=StringVar()

        m_title=Label(self.Manage_Frame,text="Manage Students",bg="maroon", fg="white",font=("Copperplate Gothic Bold",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_USN=Label(self.Manage_Frame,text="USN:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_USN.grid(row=1,column=0,pady=10, padx=20, sticky="w")

        txt_USN=Entry(self.Manage_Frame,textvariable=self.USN_var,font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_USN.grid(row=1,column=1 ,pady=10, padx=20, sticky="w")

        lbl_name=Label(self.Manage_Frame,text="Name:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10, padx=20, sticky="w")

        txt_name=Entry(self.Manage_Frame,textvariable=self.Name_var,font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1 ,pady=10, padx=20, sticky="w")

        lbl_email=Label(self.Manage_Frame,text="Email:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10, padx=20, sticky="w")

        txt_email=Entry(self.Manage_Frame,textvariable=self.Email_var,font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1 ,pady=10, padx=20, sticky="w")

        lbl_gender=Label(self.Manage_Frame,text="Gender:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(self.Manage_Frame,textvariable=self.Gender_var,font=("Copperplate Gothic Bold",15,"bold"), state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10, padx=20, sticky="w")

        lbl_sem=Label(self.Manage_Frame,text="Semester:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_sem.grid(row=5,column=0,pady=10, padx=20, sticky="w")

        txt_sem=Entry(self.Manage_Frame,textvariable=self.Semester_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_sem.grid(row=5,column=1 ,pady=10, padx=20, sticky="w")

        lbl_age=Label(self.Manage_Frame,text="Age:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_age.grid(row=6,column=0,pady=10, padx=20, sticky="w")

        txt_age=Entry(self.Manage_Frame,textvariable=self.Age_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_age.grid(row=6,column=1 ,pady=10, padx=20, sticky="w")

        lbl_sub1=Label(self.Manage_Frame,text="Subject 1:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_sub1.grid(row=7,column=0,pady=10, padx=20, sticky="w")

        txt_sub1=Entry(self.Manage_Frame,textvariable=self.Subject1_var,font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_sub1.grid(row=7,column=1 ,pady=10, padx=20, sticky="w")

        lbl_marks11=Label(self.Manage_Frame,text="CIE 1:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks11.grid(row=8,column=0,pady=10, padx=20, sticky="w")

        txt_marks11=Entry(self.Manage_Frame,textvariable=self.Marks11_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks11.grid(row=8,column=1,pady=10, padx=20, sticky="w")

        lbl_marks12=Label(self.Manage_Frame,text="CIE 2:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks12.grid(row=9,column=0,pady=10, padx=20, sticky="w")

        txt_marks12=Entry(self.Manage_Frame,textvariable=self.Marks12_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks12.grid(row=9,column=1,pady=10, padx=20, sticky="w")

        lbl_marks13=Label(self.Manage_Frame,text="CIE 3:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks13.grid(row=10,column=0,pady=10, padx=20, sticky="w")

        txt_marks13=Entry(self.Manage_Frame,textvariable=self.Marks13_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks13.grid(row=10,column=1,pady=10, padx=20, sticky="w")

        lbl_avg1=Label(self.Manage_Frame,text="Average:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_avg1.grid(row=11,column=0,pady=10, padx=20, sticky="w")

        txt_avg1=Entry(self.Manage_Frame,textvariable=self.Average1_var,font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_avg1.grid(row=11,column=1,pady=10, padx=20, sticky="w")
           
        lbl_sub2=Label(self.Manage_Frame,text="Subject 2:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_sub2.grid(row=12,column=0,pady=10, padx=20, sticky="w")

        txt_sub2=Entry(self.Manage_Frame,textvariable=self.Subject2_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_sub2.grid(row=12,column=1 ,pady=10, padx=20, sticky="w")

        lbl_marks21=Label(self.Manage_Frame,text="CIE 1:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks21.grid(row=13,column=0,pady=10, padx=20, sticky="w")

        txt_marks21=Entry(self.Manage_Frame,textvariable=self.Marks21_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks21.grid(row=13,column=1,pady=10, padx=20, sticky="w")

        lbl_marks22=Label(self.Manage_Frame,text="CIE 2:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks22.grid(row=14,column=0,pady=10, padx=20, sticky="w")

        txt_marks22=Entry(self.Manage_Frame,textvariable=self.Marks22_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks22.grid(row=14,column=1,pady=10, padx=20, sticky="w")

        lbl_marks23=Label(self.Manage_Frame,text="CIE 3:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks23.grid(row=15,column=0,pady=10, padx=20, sticky="w")

        txt_marks23=Entry(self.Manage_Frame,textvariable=self.Marks23_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks23.grid(row=15,column=1,pady=10, padx=20, sticky="w")

        lbl_avg2=Label(self.Manage_Frame,text="Average:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_avg2.grid(row=16,column=0,pady=10, padx=20, sticky="w")

        txt_avg2=Entry(self.Manage_Frame,textvariable=self.Average2_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_avg2.grid(row=16,column=1,pady=10, padx=20, sticky="w")

        lbl_sub3=Label(self.Manage_Frame,text="Subject 3:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_sub3.grid(row=17,column=0,pady=10, padx=20, sticky="w")

        txt_sub3=Entry(self.Manage_Frame,textvariable=self.Subject3_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_sub3.grid(row=17,column=1 ,pady=10, padx=20, sticky="w")

        lbl_marks31=Label(self.Manage_Frame,text="CIE 1:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks31.grid(row=18,column=0,pady=10, padx=20, sticky="w")

        txt_marks31=Entry(self.Manage_Frame,textvariable=self.Marks31_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks31.grid(row=18,column=1,pady=10, padx=20, sticky="w")

        lbl_marks32=Label(self.Manage_Frame,text="CIE 2:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks32.grid(row=19,column=0,pady=10, padx=20, sticky="w")

        txt_marks32=Entry(self.Manage_Frame,textvariable=self.Marks32_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks32.grid(row=19,column=1,pady=10, padx=20, sticky="w")

        lbl_marks33=Label(self.Manage_Frame,text="CIE 3:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks33.grid(row=20,column=0,pady=10, padx=20, sticky="w")

        txt_marks33=Entry(self.Manage_Frame,textvariable=self.Marks33_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks33.grid(row=20,column=1,pady=10, padx=20, sticky="w")

        lbl_avg3=Label(self.Manage_Frame,text="Average:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_avg3.grid(row=21,column=0,pady=10, padx=20, sticky="w")

        txt_avg3=Entry(self.Manage_Frame,textvariable=self.Average3_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_avg3.grid(row=21,column=1,pady=10, padx=20, sticky="w")

        lbl_sub4=Label(self.Manage_Frame,text="Subject 4:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_sub4.grid(row=22,column=0,pady=10, padx=20, sticky="w")

        txt_sub4=Entry(self.Manage_Frame,textvariable=self.Subject4_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_sub4.grid(row=22,column=1 ,pady=10, padx=20, sticky="w")

        lbl_marks41=Label(self.Manage_Frame,text="CIE 1:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks41.grid(row=23,column=0,pady=10, padx=20, sticky="w")

        txt_marks41=Entry(self.Manage_Frame,textvariable=self.Marks41_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks41.grid(row=23,column=1,pady=10, padx=20, sticky="w")

        lbl_marks42=Label(self.Manage_Frame,text="CIE 2:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks42.grid(row=24,column=0,pady=10, padx=20, sticky="w")

        txt_marks42=Entry(self.Manage_Frame,textvariable=self.Marks42_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks42.grid(row=24,column=1,pady=10, padx=20, sticky="w")

        lbl_marks43=Label(self.Manage_Frame,text="CIE 3:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_marks43.grid(row=25,column=0,pady=10, padx=20, sticky="w")

        txt_marks43=Entry(self.Manage_Frame,textvariable=self.Marks43_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_marks43.grid(row=25,column=1,pady=10, padx=20, sticky="w")

        lbl_avg4=Label(self.Manage_Frame,text="Average:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_avg4.grid(row=26,column=0,pady=10, padx=20, sticky="w")

        txt_avg4=Entry(self.Manage_Frame,textvariable=self.Average4_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_avg4.grid(row=26,column=1,pady=10, padx=20, sticky="w")

        lbl_guardian=Label(self.Manage_Frame,text="Guardian Name:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_guardian.grid(row=27,column=0,pady=10, padx=20, sticky="w")

        txt_guardian=Entry(self.Manage_Frame,textvariable=self.Guardian_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_guardian.grid(row=27,column=1,pady=10, padx=20, sticky="w")

        lbl_relationship=Label(self.Manage_Frame,text="Relationship:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_relationship.grid(row=28,column=0,pady=10, padx=20, sticky="w")

        txt_relationship=Entry(self.Manage_Frame,textvariable=self.Relationship_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_relationship.grid(row=28,column=1,pady=10, padx=20, sticky="w")

        lbl_pno=Label(self.Manage_Frame,text="Guardian Ph.No:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_pno.grid(row=29,column=0,pady=10, padx=20, sticky="w")

        txt_pno=Entry(self.Manage_Frame,textvariable=self.Pno_var, font=("Copperplate Gothic Bold",15,"bold"),bd=5,relief=GROOVE)
        txt_pno.grid(row=29,column=1,pady=10, padx=20, sticky="w")

        lbl_blank=Label(self.Manage_Frame)
        lbl_blank.grid(row=30,column=0,pady=10, padx=20, sticky="w")

        lbl_blank1=Label(self.Manage_Frame)
        lbl_blank.grid(row=31,column=0,pady=10, padx=20, sticky="w")
        
     def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
                

#==========BUTTON FRAME==========  


        btn_Frame=Frame(self.canvas,bd=4,relief=RIDGE, bg="brown")
        btn_Frame.place(x=50,y=750,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        
#==========DETAIL FRAME==========


        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="maroon")
        Detail_Frame.place(x=570,y=90,width=945,height=700)

        lbl_search=Label(Detail_Frame,text="Search By:",bg="maroon", fg="white",font=("Copperplate Gothic Bold",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",15,"bold"), state='readonly')
        combo_search['values']=("usn","name","semester","average1","average2","average3","average4")
        combo_search.grid(row=0,column=1,pady=10, padx=20, sticky="w")

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2 ,pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by1,width=10,font=("times new roman",15,"bold"), state='readonly')
        combo_search['values']=("usn","name","semester","average1","average2","average3","average4")
        combo_search.grid(row=1,column=1,pady=10, padx=20, sticky="w")

        txt_search1=Entry(Detail_Frame,textvariable=self.search_txt1,width=15,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search1.grid(row=1,column=2 ,pady=10, padx=20, sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data1).grid(row=1,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=1,column=4,padx=10,pady=10)


#==========TABLE FRAME==========  
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="black")
        Table_Frame.place(x=10,y=120,width=900,height=570)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("USN","Name","Email","Gender","Semester","Age","Subject 1","CIE 1.1","CIE 1.2","CIE 1.3","Average 1","Subject 2","CIE 2.1","CIE 2.2","CIE 2.3","Average 2","Subject 3","CIE 3.1","CIE 3.2","CIE 3.3","Average 3","Subject 4","CIE 4.1","CIE 4.2","CIE 4.3","Average 4","Guardian","Relationship","Phone Number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("USN",text="USN")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Semester",text="Semester")
        self.Student_table.heading("Age",text="Age")
        self.Student_table.heading("Subject 1",text="Subject 1")
        self.Student_table.heading("CIE 1.1",text="CIE 1")
        self.Student_table.heading("CIE 1.2",text="CIE 2")
        self.Student_table.heading("CIE 1.3",text="CIE 3")
        self.Student_table.heading("Average 1",text="Average 1")
        self.Student_table.heading("Subject 2",text="Subject 2")
        self.Student_table.heading("CIE 2.1",text="CIE 1")
        self.Student_table.heading("CIE 2.2",text="CIE 2")
        self.Student_table.heading("CIE 2.3",text="CIE 3")
        self.Student_table.heading("Average 2",text="Average 2")
        self.Student_table.heading("Subject 3",text="Subject 3")
        self.Student_table.heading("CIE 3.1",text="CIE 1")
        self.Student_table.heading("CIE 3.2",text="CIE 2")
        self.Student_table.heading("CIE 3.3",text="CIE 3")
        self.Student_table.heading("Average 3",text="Average 3")
        self.Student_table.heading("Subject 4",text="Subject 4")
        self.Student_table.heading("CIE 4.1",text="CIE 1")
        self.Student_table.heading("CIE 4.2",text="CIE 2")
        self.Student_table.heading("CIE 4.3",text="CIE 3")
        self.Student_table.heading("Average 4",text="Average 4")
        self.Student_table.heading("Guardian",text="Guardian")
        self.Student_table.heading("Relationship",text="Relationship")
        self.Student_table.heading("Phone Number",text="Phone Number")

        self.Student_table['show']='headings'
        self.Student_table.column("USN",width=180)
        self.Student_table.column("Name",width=200)
        self.Student_table.column("Email",width=250)
        self.Student_table.column("Gender",width=120)
        self.Student_table.column("Semester",width=120)
        self.Student_table.column("Age",width=120)
        self.Student_table.column("Subject 1",width=120)
        self.Student_table.column("CIE 1.1",width=120)
        self.Student_table.column("CIE 1.2",width=120)
        self.Student_table.column("CIE 1.3",width=120)
        self.Student_table.column("Average 1",width=120)
        self.Student_table.column("Subject 2",width=120)
        self.Student_table.column("CIE 2.1",width=120)
        self.Student_table.column("CIE 2.2",width=120)
        self.Student_table.column("CIE 2.3",width=120)
        self.Student_table.column("Average 2",width=120)
        self.Student_table.column("Subject 3",width=120)
        self.Student_table.column("CIE 3.1",width=120)
        self.Student_table.column("CIE 3.2",width=120)
        self.Student_table.column("CIE 3.3",width=120)
        self.Student_table.column("Average 3",width=120)
        self.Student_table.column("Subject 4",width=120)
        self.Student_table.column("CIE 4.1",width=120)
        self.Student_table.column("CIE 4.2",width=120)
        self.Student_table.column("CIE 4.3",width=120)
        self.Student_table.column("Average 4",width=120)
        self.Student_table.column("Guardian",width=120)
        self.Student_table.column("Relationship",width=120)
        self.Student_table.column("Phone Number",width=250)
        

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.fetch_data()






     def add_students(self):
        if self.USN_var.get()=="" or self.Name_var.get()=="" or self.Semester_var.get()=="" or self.Guardian_var.get()=="" or self.Pno_var.get()=="":
                messagebox.showerror("Error","All fields are required!!")
        else:
                con=pymysql.Connect(host="localhost",user="root",password="",database="stm2")
                cur=con.cursor()
                
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.USN_var.get(),
                                                                                         self.Name_var.get(),
                                                                                         self.Age_var.get(),
                                                                                         self.Gender_var.get(),
                                                                                         self.Email_var.get(),
                                                                                         self.Semester_var.get(),
                                                                                         self.Subject1_var.get(),
                                                                                         self.Subject2_var.get(),
                                                                                         self.Subject3_var.get(),
                                                                                         self.Subject4_var.get()
                                                                                         ))


                con.commit()
        


        
                cur.execute("insert into marks values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.USN_var.get(),
                                                                                                                        self.Subject1_var.get(),
                                                                                                                        self.Marks11_var.get(),                                                                                     
                                                                                                                        self.Marks12_var.get(),
                                                                                                                        self.Marks13_var.get(),
                                                                                                                        self.Average1_var.get(),
                                                                                                                        self.Subject2_var.get(),
                                                                                                                        self.Marks21_var.get(),
                                                                                                                        self.Marks22_var.get(),
                                                                                                                        self.Marks23_var.get(),
                                                                                                                        self.Average2_var.get(),
                                                                                                                        self.Subject3_var.get(),
                                                                                                                        self.Marks31_var.get(),
                                                                                                                        self.Marks32_var.get(),
                                                                                                                        self.Marks33_var.get(),
                                                                                                                        self.Average3_var.get(),
                                                                                                                        self.Subject4_var.get(),
                                                                                                                        self.Marks41_var.get(),
                                                                                                                        self.Marks42_var.get(),
                                                                                                                        self.Marks43_var.get(),
                                                                                                                        self.Average4_var.get()
                                                                                                                        ))


                con.commit()
        
                cur.execute("insert into guardian values(%s,%s,%s,%s)",(self.USN_var.get(),
                                                                        self.Guardian_var.get(),
                                                                        self.Relationship_var.get(),
                                                                        self.Pno_var.get()
                                                                        ))
                                                                        
                                                                        

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Congratulations! The data has been recorded")

     def fetch_data(self):
         
        con=pymysql.Connect(host="localhost",user="root",password="",database="stm2")
        cur=con.cursor()
        cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where S.usn=M.roll and S.usn=G.rollnum")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        
        con.close()

     def clear(self):
        self.USN_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Semester_var.set("")
        self.Age_var.set("")
        self.Subject1_var.set("")
        self.Marks11_var.set("")
        self.Marks12_var.set("")
        self.Marks13_var.set("")
        self.Average1_var.set("")
        self.Subject2_var.set("")
        self.Marks21_var.set("")
        self.Marks22_var.set("")
        self.Marks23_var.set("")
        self.Average2_var.set("")
        self.Subject3_var.set("")
        self.Marks31_var.set("")
        self.Marks32_var.set("")
        self.Marks33_var.set("")
        self.Average3_var.set("")
        self.Subject4_var.set("")
        self.Marks41_var.set("")
        self.Marks42_var.set("")
        self.Marks43_var.set("")
        self.Average4_var.set("")
        self.Guardian_var.set("")
        self.Relationship_var.set("")
        self.Pno_var.set("")

     def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.USN_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Semester_var.set(row[4])
        self.Age_var.set(row[5])
        self.Subject1_var.set(row[6])
        self.Marks11_var.set(row[7])
        self.Marks12_var.set(row[8])
        self.Marks13_var.set(row[9])
        self.Average1_var.set(row[10])
        self.Subject2_var.set(row[11])
        self.Marks21_var.set(row[12])
        self.Marks22_var.set(row[13])
        self.Marks23_var.set(row[14])
        self.Average2_var.set(row[15])
        self.Subject3_var.set(row[16])
        self.Marks31_var.set(row[17])
        self.Marks32_var.set(row[18])
        self.Marks33_var.set(row[19])
        self.Average3_var.set(row[20])
        self.Subject4_var.set(row[21])
        self.Marks41_var.set(row[22])
        self.Marks42_var.set(row[23])
        self.Marks43_var.set(row[24])
        self.Average4_var.set(row[25])
        self.Guardian_var.set(row[26])
        self.Relationship_var.set(row[27])
        self.Pno_var.set(row[28])

     def update_data(self):
        con=pymysql.Connect(host="localhost",user="root",password="",database="stm2")
        cur=con.cursor()
        
        cur.execute("update student set name=%s,age=%s,gender=%s,email=%s,semester=%s,subject1=%s,subject2=%s,subject3=%s,subject4=%s where usn=%s",(
                                                                                                                                                self.Name_var.get(),
                                                                                                                                                self.Age_var.get(),
                                                                                                                                                self.Gender_var.get(),
                                                                                                                                                self.Email_var.get(),
                                                                                                                                                self.Semester_var.get(),
                                                                                                                                                self.Subject1_var.get(),
                                                                                                                                                self.Subject2_var.get(),
                                                                                                                                                self.Subject3_var.get(),
                                                                                                                                                self.Subject4_var.get(),
                                                                                                                                                self.USN_var.get()
                                                                                                                                                ))


        con.commit()
       


       
        cur.execute("update marks set sub1=%s,cie11=%s,cie12=%s,cie13=%s,average1=%s,sub2=%s,cie21=%s,cie22=%s,cie23=%s,average2=%s,sub3=%s,cie31=%s,cie32=%s,cie33=%s,average3=%s,sub4=%s,cie41=%s,cie42=%s,cie43=%s,average4=%s where roll=%s",(
                                                                                                                                                                                                                                             self.Subject1_var.get(),
                                                                                                                                                                                                                                             self.Marks11_var.get(),                                                                                     
                                                                                                                                                                                                                                             self.Marks12_var.get(),
                                                                                                                                                                                                                                             self.Marks13_var.get(),
                                                                                                                                                                                                                                             self.Average1_var.get(),
                                                                                                                                                                                                                                             self.Subject2_var.get(),
                                                                                                                                                                                                                                             self.Marks21_var.get(),
                                                                                                                                                                                                                                             self.Marks22_var.get(),
                                                                                                                                                                                                                                             self.Marks23_var.get(),
                                                                                                                                                                                                                                             self.Average2_var.get(),
                                                                                                                                                                                                                                             self.Subject3_var.get(),
                                                                                                                                                                                                                                             self.Marks31_var.get(),
                                                                                                                                                                                                                                             self.Marks32_var.get(),
                                                                                                                                                                                                                                             self.Marks33_var.get(),
                                                                                                                                                                                                                                             self.Average3_var.get(),
                                                                                                                                                                                                                                             self.Subject4_var.get(),
                                                                                                                                                                                                                                             self.Marks41_var.get(),
                                                                                                                                                                                                                                             self.Marks42_var.get(),
                                                                                                                                                                                                                                             self.Marks43_var.get(),
                                                                                                                                                                                                                                             self.Average4_var.get(),
                                                                                                                                                                                                                                             self.USN_var.get()
                                                                                                                                                                                                                                             ))


        con.commit()
       
        cur.execute("update guardian set gname=%s,relationship=%s,phonenumber=%s where rollnum=%s",(
                                                                                               self.Guardian_var.get(),
                                                                                               self.Relationship_var.get(),
                                                                                               self.Pno_var.get(),
                                                                                               self.USN_var.get(),
                                                                                               ))
                                                                                                  
                                                                   

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

     def delete_data(self):
         
        con=pymysql.Connect(host="localhost",user="root",password="",database="stm2")
        cur=con.cursor()
        cur.execute("delete from student where usn=%s",self.USN_var.get())
        con.commit()
        cur.execute("delete from marks where roll=%s",self.USN_var.get())
        con.commit()
        cur.execute("delete from guardian where rollnum=%s",self.USN_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

     def search_data(self):
         
        con=pymysql.Connect(host="localhost",user="root",password="",database="stm2")
        cur=con.cursor()
        if self.search_by.get()=="average1" or self.search_by.get()=="average2" or self.search_by.get()=="average3" or self.search_by.get()=="average4":
            cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where "+str(self.search_by.get())+" < "+str(self.search_txt.get())+" and S.usn=M.roll and S.usn=G.rollnum")
        else:
            cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%' and S.usn=M.roll and S.usn=G.rollnum")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
     
        con.close()

     def search_data1(self):

        con=pymysql.Connect(host="localhost",user="root",password="",database="stm2")
        cur=con.cursor()

        if self.search_by.get()=="semester" and self.search_by1.get()=="average1":
            cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%' and "+str(self.search_by1.get())+" < "+str(self.search_txt1.get())+" and S.usn=M.roll and S.usn=G.rollnum")
        elif self.search_by.get()=="semester" and self.search_by1.get()=="average2":
            cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%' and "+str(self.search_by1.get())+" < "+str(self.search_txt1.get())+" and S.usn=M.roll and S.usn=G.rollnum")
        elif self.search_by.get()=="semester" and self.search_by1.get()=="average3":
            cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%' and "+str(self.search_by1.get())+" < "+str(self.search_txt1.get())+" and S.usn=M.roll and S.usn=G.rollnum")
        elif self.search_by.get()=="semester" and self.search_by1.get()=="average4":
            cur.execute("select usn,name,email,gender,semester,age,sub1,cie11,cie12,cie13,average1,sub2,cie21,cie22,cie23,average2,sub3,cie31,cie32,cie33,average3,sub4,cie41,cie42,cie43,average4,gname,relationship,phonenumber from student S,marks M,guardian G where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%' and "+str(self.search_by1.get())+" < "+str(self.search_txt1.get())+" and S.usn=M.roll and S.usn=G.rollnum")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()

        con.close()
    










ob=Student(root)
root.mainloop()
