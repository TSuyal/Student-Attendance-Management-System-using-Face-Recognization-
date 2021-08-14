import tkinter.messagebox as tmsg
from tkinter import *
from PIL import Image,ImageTk
import time
import re
import cv2

def ATTENDANCE():
    """This function make a window for taking attendance"""
    Admin_page.destroy()
    def store_data():
        """This function open files in read and append mode"""
        global roll_entry
        a="C:\\Users\\Administrator\\Desktop\\"+str(roll_entry.get())+".txt"
        op= open(a,"a+")
        op1=open("C:\\Users\\Administrator\\Desktop\\test.txt","a+")
        op.write(S_V.get())
        op1.write(S_V.get())
        op.write("        ")
        op1.write("        ")
        op.write(class_value.get())
        op1.write(class_value.get())
        op.write("        ")
        op1.write("        ")
        op.write(sub_value.get())
        op1.write(sub_value.get())
        op.write("        ")
        op1.write("       ")
        op.write(Roll_value.get())
        op1.write(Roll_value.get())
        op.write("        ")
        op1.write("        ")
        op.write(attend_value.get())
        op1.write(attend_value.get())
        op.write("        ")
        op1.write("       ")
        op.write(time.strftime("%H:%M:%S"))
        op1.write(time.strftime("%H:%M:%S"))
        op.write("        ")
        op1.write("        ")
        op.write(time.strftime("%Y-%m-%d"))
        op1.write(time.strftime("%Y-%m-%d"))
        op.write("\n")
        op1.write("\n")
        op.close()
    def HOME():
        ATD.destroy()
        admin_user()
    def clear():
        class_value.set("")
        sub_value.set("")
        attend_value.set("")
        S_V.set("")
        Roll_value.set("")
    ATD=Tk()
    global roll_entry
    class_value=StringVar()
    sub_value=StringVar()
    attend_value=StringVar()
    S_V=StringVar()
    Roll_value=StringVar()
    ATD.title=("Attendance window")
    ATD.geometry("1350x700+0+0")
    ATD.configure(background="navy blue")
    f0=Frame(ATD,bg="navy blue")
    t1=Label(f0,text="Attend To Achieve",font="algerian 50 bold",bg="navy blue")
    t1.grid(row=1,column=1)
    t2=Label(f0,text="Every Student. Every Day",font="algerian 30 bold",bg="navy blue")
    t2.grid(row=2,column=1)
    f0.place(x=120,y=200)
    Att_frame=Frame(ATD,bg="steel blue",bd=18,relief=SUNKEN)
    img=PhotoImage(file="C:\\Users\\Administrator\\Documents\\py\\attendance.png")
    img_lbl=Label(Att_frame,image=img)
    img_lbl.grid(row=0,columnspan=2,pady=20,padx=20)
    Student_Name=Label(Att_frame,text="Student Name",bd=0,bg="steel blue",font=("times new roman",15,"bold"))
    Student_Name.grid(row=1,column=0,pady=20,padx=20)
    Student_entry=Entry(Att_frame,textvariable=S_V,font=("times new roman",15))
    Student_entry.grid(row=1,column=1,pady=20,padx=20)
    roll=Label(Att_frame,text="Roll Number",bd=0,bg="steel blue",font=("times new roman",15,"bold"))
    roll.grid(row=2,column=0)
    roll_entry=Entry(Att_frame,font=("times new roman",15),textvariable=Roll_value)
    roll_entry.grid(row=2,column=1,padx=20,pady=20)
    classes=["class_1","class_2","class_3","class_4","class_5","class_6","class_7","class_8","class_9","class_10","class_11","class_12"]
    Cls=Label(Att_frame,text="Class",font=("times new roman",15,"bold"),bg='steel blue')
    Cls.grid(row=3,column=0,padx=20,pady=20)
    option=OptionMenu(Att_frame,class_value,*classes)
    option.configure(width=25)
    class_value.set("Select class")
    option.grid(row=3,column=1,padx=20,pady=20)
    Subjects=["CAO","WT","OS","Python","Cpp","EVS","OB","Maths"]
    sub=Label(Att_frame,text="Subject",font=("times new roman",15,"bold"),bg='steel blue')
    sub.grid(row=4,column=0,padx=20,pady=20)
    option=OptionMenu(Att_frame,sub_value,*Subjects)
    option.configure(width=25)
    sub_value.set("Select Subject")
    option.grid(row=4,column=1)
    Attendance=["Present","Absent"]
    Attend=Label(Att_frame,text="Attendance",font=("times new roman",15,"bold"),bg='steel blue')
    Attend.grid(row=5,column=0,padx=20,pady=20)
    option=OptionMenu(Att_frame,attend_value,*Attendance)
    option.configure(width=25)
    attend_value.set("Absent or present")
    option.grid(row=5,column=1)
    b=Button(Att_frame,text="submit",font=("times new roman",15,"bold"),bd=5,relief=RAISED,command=store_data)
    b.grid(row=6,column=0,padx=20,pady=20)
    b=Button(Att_frame,text="Clear",font=("times new roman",15,"bold"),bd=5,relief=RAISED,command=clear)
    b.grid(row=6,column=1,padx=20,pady=20)
    b=Button(ATD,text="HOME",font=("times new roman",20,"bold"),bd=5,relief=RAISED,command=HOME)
    b.grid(row=0,column=0)
    Att_frame.place(x=900,y=0)
    ATD.mainloop()

def Student_Record_page():
    """This function store the attendance of students"""
    global root
    global user_entry
    admin_user_window.destroy()
    root=Tk()
    root.geometry("1350x700+0+0")
    root.title("Login System")
    def HOME1():
        root.destroy()
        admin_user()
    def Show_Student_record():
        global root
        global user
        def HOME4():
            showRCD.destroy()
            admin_user()
        user=user_entry.get()
        root.destroy()
        showRCD=Tk()
        showRCD.geometry("1350x700+0+0")
        showRCD.title("Student Attendance record")
        f0=Frame(showRCD,bg="navy blue",bd=5,relief=SUNKEN)
        txt=Label(f0,text="ATTENDANCE RECORD",font="algerian 45 bold",bg="navy blue")
        txt.grid(row=0,column=0,padx=28,pady=2)
        f0.place(x=0,y=0)
        f1=Frame(showRCD)
        p=Label(f1,text="Advancing Student Success",font="algerian 25 bold",fg="green")
        p.grid(row=8,column=10,pady=10)
        p=Label(f1,text="By",font="algerian 25 bold",fg="green")
        p.grid(row=9,column=10,pady=10)
        p=Label(f1,text="Reducing Chronic Absence",font="algerian 25 bold",fg="green")
        p.grid(row=10,column=10,pady=10)
        f=Label(f1,text="Attendance Works",font="algerian 25 italic",fg="red")
        f.grid(row=11,column=10,pady=10)
        f1.place(x=805,y=200)
        b=Button(showRCD,text="HOME",font=("times new roman",20,"bold"),bd=5,relief=SUNKEN,command=HOME4)
        b.pack(anchor="ne")
        yscrollbar=Scrollbar(showRCD)
        u="C:\\Users\\Administrator\\Desktop\\"+user+".txt"
        try:
            p=Listbox(showRCD,bg="black",fg="white",yscrollcommand=yscrollbar.set,width=70,height=40,font=("times new roman",15,"italic" ))
            fr=open(u,"r")
            line=fr.readline()
            while line:
                p.insert(END,line)
                line=fr.readline()
            p.place(x=0,y=84)
            yscrollbar.pack(side=RIGHT,fill=Y)
            yscrollbar.config(command=p.yview)
            fr.close()
        except:
            tmsg.showerror("Error","File is Empty")
    def VUD():
        """This function varify username and password"""
        global user
        if (uservalue.get()) =="":
            tmsg.showinfo("Information","Please Enter Valid Username")
        elif passvalue.get() =="":
            tmsg.showinfo("Information","Please Enter Valid password")
        elif passvalue.get()!="MERI":
            tmsg.showerror("Error","Incorrect Password")
        elif passvalue.get()=="MERI":
            Show_Student_record()
            tmsg.showinfo("Information","Congratulation, Login Success")
        else:
            Show_Student_record()
            tmsg.showinfo("Information","Congratulation, Login Success")
            
    def clear_detail():
        """This function clear the values of username and password in Student login window"""
        passvalue.set("") 
        uservalue.set("")
    
    root.configure(background="navy blue")
    admin_logo=PhotoImage(file="C:\\Users\\Administrator\\Documents\\py\\admin.png")
    pass_logo=PhotoImage(file="C:\\Users\\Administrator\\Documents\\py\\capture4.png")
    user_logo=PhotoImage(file="C:\\Users\\Administrator\\Documents\\py\\capture.png")
    passvalue=StringVar()
    uservalue=StringVar()
    f0=Frame(root,bg="white",bd=15,relief=RAISED)
    title=Label(f0,text="Login System",bg="white",fg="black",font=("times new roman",40, "bold"))
    title.grid(row=0,columnspan=2)
    _admin_=Label(f0,image=admin_logo,bd=0)
    _admin_.grid(row=1,columnspan=2)
    _user_=Label(f0,text="username",image=user_logo,compound=LEFT,font=("times new roman",18),bd=0,bg="white")
    _user_.grid(row=2,column=0,pady=20,padx=20)
    user_entry=Entry(f0,textvariable=uservalue,bd=5,font=("times new roman",15))
    user_entry.grid(row=2,column=1,padx=20)
    _pass_=Label(f0,text="password",image=pass_logo,compound=LEFT,bg="white",bd=0,font=("times new roman",18))
    _pass_.grid(row=3,column=0)
    pass_entry=Entry(f0,textvariable=passvalue,bd=5,font=("times new roman",15)).grid(row=3,column=1)
    b=Button(f0,text="Sign in",font=("",15),bd=5,relief=SUNKEN,command=VUD)
    b.grid(row=4,column=0,pady=20)
    b=Button(f0,text="Clear",font=("",15),bd=5,relief=SUNKEN,command=clear_detail)
    b.grid(row=4,column=1,padx=50)
    f0.place(x=480,y=100)
    b=Button(root,text="HOME",font=("times new roman",20,"bold"),bd=5,relief=SUNKEN,command=HOME1)
    b.grid(row=0,column=0)
    root.mainloop()

def Registeration_form():
    """This function creates a window for registration"""
    def HOME3():
        Register.destroy()
        admin_user()
    Admin_page.destroy()
    Register=Tk()
    Register.geometry("1350x700+0+0")
    F_value=StringVar()
    Phone_value=StringVar()
    email_value=StringVar()
    gen_value=IntVar()
    Classes_value=StringVar()
    Father_value=StringVar()
    Mother_value=StringVar()
    Address_value=StringVar()
    def store():
        """This function open a txt file in append mode to store the registered data"""
        op=open("C:\\Users\\Administrator\\Desktop\\New folder\\registration.txt","a")
        op.write(F_value.get())
        op.write("          ")
        op.write(str(Phone_value.get()))
        op.write("          ")
        op.write(email_value.get())
        op.write("          ")
        op.write(Classes_value.get())
        op.write("          ")
        op.write(Father_value.get())
        op.write("          ")
        op.write(Mother_value.get())
        op.write("          ")
        op.write(Address_value.get())
        op.write("          ")
        op.write(k)
        op.write("\n")
        op.close()

    def Validdetails():
        """This function is for valid details for registration"""
        if F_value.get()=="":
            tmsg.showinfo("Information","Please Enter Full Name")
        elif Phone_value.get()=="":
            tmsg.showinfo("Information","Please Enter Phone Number")
        elif email_value.get()=="":
            tmsg.showinfo("Information","Please Enter Gmail")
        elif Classes_value.get()=="Select class":
            tmsg.showinfo("Information","Please Enter Class")
        elif Father_value.get()=="":
            tmsg.showinfo("Information","Please Enter Father's Name")
        elif Mother_value.get()=="":
            tmsg.showinfo("Information","Please Enter Mother's Name")
        elif Address_value.get()=="":
            tmsg.showinfo("Information","Please Enter Address")
        elif gen_value.get()==0:
            tmsg.showinfo("Information","Please Select Your Gender")
        elif email_value.get()!="":
            status=validemail(email_value.get())
            if(status):
                store()
                tmsg.showinfo("Information","User Registered Successfully!!!")
        else:
            store()
            tmsg.showinfo("Information","User Registered Successfully!!!")

    def validPhone(user_phoneno):
            if user_phoneno.isdigit():
                return True
            elif user_phoneno=="":
                return True
            else:
                tmsg.showinfo("Information","Only digits are allowed")
    def validemail(user_mail):
        if email_value.get()!="":
            if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",user_mail)!=None:
                return True
            else:
                tmsg.showinfo("Information","This is not a valid email address")
                return False
    def Clear():
        F_value.set("")
        Phone_value.set("")
        email_value.set("")
        Classes_value.set("Select class")
        gen_value.set(0)
        Father_value.set("")
        Mother_value.set("")
        Address_value.set("")

    Register.title("Registeration Form")
    Register.configure(background="dark blue")
    Register_frame=Frame(Register,bg="steel blue")
    text=Label(Register_frame,text="Registeration Form",font=("times new roman",30,"bold"),bg="steel blue")
    text.grid(row=0,columnspan=3,pady=5)
    Register_frame.place(x=530,y=25)
    F_name=Label(Register_frame,text="Full Name",font=("times new roman",15,"bold"),bg='steel blue')
    F_name.grid(row=1,column=0,padx=15,pady=15)
    F_entry=Entry(Register_frame,font=("times new roman",18),bd=5,relief=SUNKEN,textvariable=F_value)
    F_entry.grid(row=1,column=1,padx=15,pady=10)

    phone=Label(Register_frame,text="Phone Number",font=("times new roman",15,"bold"),bg='steel blue')
    phone.grid(row=2,column=0,padx=15,pady=5)
    phone_entry=Entry(Register_frame,font=("times new roman",18),bd=5,relief=SUNKEN,textvariable=Phone_value)
    phone_entry.grid(row=2,column=1,padx=15,pady=5)
    phoneno=Register.register(validPhone)
    phone_entry.config(validate="key",validatecommand=(phoneno,"%p"))

    Gmail=Label(Register_frame,text="Gmail",font=("times new roman",15,"bold"),bg='steel blue')
    Gmail.grid(row=3,column=0,padx=15,pady=5)
    Gmail_entry=Entry(Register_frame,font=("times new roman",18),bd=5,relief=SUNKEN,textvariable=email_value)
    Gmail_entry.grid(row=3,column=1,padx=15,pady=5)

    classes=["class_1","class_2","class_3","class_4","class_5","class_6","class_7","class_8","class_9","class_10","class_11","class_12"]
    Cls=Label(Register_frame,text="Class",font=("times new roman",15,"bold"),bg='steel blue')
    Cls.grid(row=4,column=0,padx=15,pady=5)
    option=OptionMenu(Register_frame,Classes_value,*classes)
    option.configure(width=35)
    Classes_value.set("Select class")
    option.grid(row=4,column=1)

    Father=Label(Register_frame,text="Father's name",font=("times new roman",15,"bold"),bg='steel blue')
    Father.grid(row=5,column=0,padx=15,pady=5)
    Father_entry=Entry(Register_frame,font=("times new roman",18),bd=5,relief=SUNKEN,textvariable=Father_value)
    Father_entry.grid(row=5,column=1,padx=15,pady=5)

    Mother=Label(Register_frame,text="Mother's name",font=("times new roman",15,"bold"),bg='steel blue')
    Mother.grid(row=6,column=0,padx=15,pady=5)
    Mother_entry=Entry(Register_frame,font=("times new roman",18),bd=5,relief=SUNKEN,textvariable=Mother_value)
    Mother_entry.grid(row=6,column=1,padx=15,pady=5)

    Address=Label(Register_frame,text="Address",font=("times new roman",15,"bold"),bg='steel blue')
    Address.grid(row=7,column=0,padx=15,pady=5)
    Address_entry=Entry(Register_frame,font=("times new roman",18),bd=5,relief=SUNKEN,textvariable=Address_value)
    Address_entry.grid(row=7,column=1,padx=15,pady=5)

    gender=Label(Register_frame,text="Gender",font=("times new roman",15,"bold"),bg='steel blue')
    gender.grid(row=8,column=0,padx=15,pady=5)
    gen=Radiobutton(Register_frame,variable=gen_value,text="Male",value=1,font=("times new roman",15,"bold"),bg="steel blue")
    gen.grid(row=8,column=1)
    gen=Radiobutton(Register_frame,variable=gen_value,text="Female",value=2,font=("times new roman",15,"bold"),bg="steel blue")
    gen.grid(row=8,column=2,padx=15,pady=5)

    b=Button(Register_frame,bd=5,relief=SUNKEN,text="Register",font=("times new roman",15,"bold"),command=Validdetails)
    b.grid(row=9,column=0,pady=25)

    b=Button(Register_frame,bd=5,relief=SUNKEN,text="Clear",font=("times new roman",15,"bold"),command=Clear)
    b.grid(row=9,column=2,pady=25)

    b=Button(Register,bd=5,relief=SUNKEN,text="HOME",font=("times new roman",20,"bold"),command=HOME3)
    b.grid(row=0,column=0)


    if gen_value.get()==1:
        k=str(gen_value.get())
    else:
        k=str(gen_value.get())
    
    Register_frame.place(x=350,y=30)
    Register.mainloop()
def ADMIN():
    global Admin_page
    admin_user_window.destroy()
    Admin_page=Tk()
    def HOME2():
        Admin_page.destroy()
        admin_user()
    def destroy():
        Admin_page.destroy()
    Admin_page.geometry("1350x700+0+0")
    Admin_page.title("Admin Page")
    Admin_page.configure(background="navy blue")
    Admin_frame=Frame(Admin_page,bg="steel blue")

    Admin_icon=PhotoImage(file="C:\\Users\\Administrator\\Documents\\py\\Admin2.png")
    Admin_icon_frame=Label(Admin_frame,image=Admin_icon,bd=0)
    Admin_icon_frame.grid(row=0,columnspan=3,pady=20)
    Admin_text=Label(Admin_frame,text="What do you want to do?",font=("times new roman",20,"bold"),bg="steel blue",fg="dark grey")
    Admin_text.grid(row=1,columnspan=3,pady=20,padx=20)

    b=Button(Admin_frame,text="Registeration",font=("times new roman",18,"bold"),bd=5,relief=SUNKEN,command=Registeration_form)
    b.grid(row=2,column=0,padx=20,pady=10)

    b=Button(Admin_frame,text="Mark Attendance",font=("times new roman",18,"bold"),bd=5,relief=SUNKEN,command=ATTENDANCE)
    b.grid(row=2,column=1,padx=20,pady=10)

    b=Button(Admin_page,text="HOME",font=("times new roman",20,"bold"),bd=5,relief=SUNKEN,command=HOME2)
    b.grid(row=0,column=0)


    Admin_frame.place(x=460,y=100)
    Admin_page.mainloop()

def FACERECOGNIZER():
    face_cascade=cv2.CascadeClassifier("C:\\Users\\Administrator\\Documents\\py\\haarcascade_frontalface_default.xml")
    rec=cv2.face.LBPHFaceRecognizer_create() 
    rec.read("C:\\Users\\Administrator\\Desktop\\recognizer\\TrainingData.yml")
    ID=0

    cap=cv2.VideoCapture(0)
    while(cap.isOpened):
        ret,img=cap.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.9,minNeighbors=4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            ID,conf=rec.predict(gray[y:y+h,x:x+w])
            if ID==1:
                ID="Tanya"
            elif ID==2 or ID==3 or ID==4:
                ID="unknown"
            else:
                ID="unknown"
            cv2.putText(img,str(ID),(x,y+h),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0),2)
            cv2.imshow("img",img)
            if ID=="Tanya":
                
                ADMIN()
                #cap.release()
                #cv2.destroyAllWindows()
            else:
                tmsg.showinfo("Error","Invaid Admin")
                #cv2.destroyAllWindows()

        cv2.imshow("img",img)
        if cv2.waitKey(100)==27:
           break
    cap.release()
    cv2.destroyAllWindows()

def admin_user():
    global admin_user_window
    admin_user_window=Tk()
    admin_user_window.geometry("1350x700+0+0")
    admin_user_window.title("Student's Management System")
    admin_user_window.configure(background="navy blue")

    image=PhotoImage(file="C:\\Users\\Administrator\\Documents\\py\\admin1.png")

    frame1=Frame(admin_user_window,bg="navy blue")

    txt=Label(frame1,text="Meri College",font="algerian 25 bold",bg="navy blue")
    txt.grid(row=0,column=0)

    txt=Label(frame1,text="Of",font="algerian 25 bold",bg="navy blue")
    txt.grid(row=1,column=0)

    txt=Label(frame1,text="Engineering And Technology",font="algerian 25 bold",bg="navy blue")
    txt.grid(row=2,column=0)

    frame1.place(x=96,y=250)

    frame_lbl=Frame(admin_user_window,bg="steel blue",bd=20,pady=10,relief=GROOVE)
    welcome_text=Label(frame_lbl,text="Welcome",font=("times new roman",25,"bold"),bg="steel blue")
    welcome_text.grid(row=1,columnspan=3,padx=10)

    to_text=Label(frame_lbl,text="To",font=("times new roman",25,"bold"),bg="steel blue")
    to_text.grid(row=2,columnspan=3)

    SAMS_text=Label(frame_lbl,text="Student's Attendance Management System",font=("times new roman",25,"bold"),bg="steel blue")
    SAMS_text.grid(row=3,columnspan=3)

    image_lbl=Label(frame_lbl,image=image,bd=0,bg="steel blue")
    image_lbl.grid(row=4,columnspan=3,pady=25,padx=10)

    title=Label(frame_lbl,text="ARE YOU ADMIN OR USER?",font=("times new roman",18,"bold"),bd=0,pady=10,bg="steel blue",fg="red")
    title.grid(row=5,columnspan=3)

    b=Button(frame_lbl,text="USER",font=("times new roman",20,"bold"),bd=5,relief=SUNKEN,command=Student_Record_page)
    b.grid(row=6,column=0,pady=25,padx=10)

    b=Button(frame_lbl,text="ADMIN",font=("times new roman",20,"bold"),bd=5,relief=SUNKEN,command=FACERECOGNIZER)
    b.grid(row=6,column=1,pady=25,padx=10)

    b=Button(frame_lbl,text="EXIT",font=("times new roman",20,"bold"),bd=5,relief=SUNKEN,command=quit)
    b.grid(row=6,column=2,pady=25,padx=10)


    frame_lbl.place(x=702,y=0)
    admin_user_window.mainloop()

admin_user()
    




