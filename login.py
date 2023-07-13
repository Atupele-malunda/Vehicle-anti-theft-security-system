from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from Main import vehicle_anti_theft_security_system
from personaldetails import Personal
from facerecognition import Recognise
from numberplatedetection import detectplate
from detectplate import *
from train import TRAIN
from time import strftime
from datetime import datetime
import numpy as np
import mysql.connector
import cv2
import os
import re
import tkinter
import pyttsx3
from mysql.connector import cursor
from os import close





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        


        #Background image
        img1 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\ai-robot.jpg")
        img1 = img1.resize((1550, 880), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=10, width=1530, height=850)

        frame = Frame(self.root, bg="maroon", borderwidth=1)
        frame.place(x=800, y=170, width=340, height=450)
        
        #LOGO
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\LOGO.png")
        left_lbl = Label(self.root, image=self.bg1,bg='white')
        left_lbl.place(x=400, y=170, width=400, height=450,)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(100, time)
        lbl = Label(self.root, font=('montiserat',15,'bold'),fg='maroon',bg='white')
        lbl.place(x=700,y=120,width=130,height=50)
        time()


        #Logo on the login page
        img2 = Image.open(r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\2.jpg")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, borderwidth=0)
        lblimg2.place(x=900, y=175, width=100, height=100)

       
        # labels
        username_lbl = Label(frame, text="Username", font=( "montiserat", 15, "bold"), bg="maroon", fg="white")
        username_lbl.place(x=65, y=152)

        self.txtuser = ttk.Entry(frame, font=("montiserat", 13, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=("montiserat", 15, "bold"), bg="maroon", fg="white")
        password_lbl.place(x=65, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("montiserat", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        #iconz

        img3 = Image.open(r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\2.jpg")
        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="maroon", borderwidth=0)
        lblimg3.place(x=840, y=325, width=25, height=25)

       
        img4 = Image.open(r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\3.jpg")
        img4 = img4.resize((20, 20), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(image=self.photoimage4, bg="maroon", borderwidth=0)
        lblimg4.place(x=840, y=397, width=25, height=25)

         # loginBuutton
        loginbtn = Button(frame, text="Login", command=self.login,font=("montiserat", 15, "bold"), bd=3, relief=RIDGE, bg="maroon", fg="white",cursor="hand2")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registrationButton
        registerbtn = Button(frame, text="Register",command=self.register_window, font=( "montiserat", 10, "bold"), borderwidth=0, bg="maroon", fg="white", activebackground="maroon",cursor="hand2")
        registerbtn.place(x=0, y=350, width=160)

        # forgetpasswordButton
        forgetbtn = Button(frame, text="Forget Password?",command=self.forgot_password_window,font=("montiserat", 10, "bold"), borderwidth=0, bg="maroon", fg="white", activebackground="maroon",cursor="hand2")
        forgetbtn.place(x=30, y=370, width=160)



        ##### calling the register window =================


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    #================== LOGIN WINDOW====================    

    def login(self):
            if self.txtuser.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "all field required")
            elif self.txtuser.get() == "admin" or "ADMIN" and self.txtpass.get() == "@1234":
                
                #speak_va("Welcome to vehicle anti theft security system")
                #messagebox.showinfo("success", "welcome to vehicle anti theft security system")
                self.new_window=(self.root)
                
                self.app=vehicle_anti_theft_security_system(self.new_window)
                
                
            else:
                conn = mysql.connector.connect(host="localhost", user="root", password="tupsy@5050", database="details")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s and pass=%s",(
                    self.txtuser.get(),
                    self.txtpass.get()

                        ))
                row=my_cursor.fetchone()
                
                if row==None:
                    speak_va("Invalid username and password!")
                    messagebox.showerror("Error","Invalid username and password")
                else:
                    open_main=messagebox.askyesno("Success","Enter vehicle anti theft security system?")
                    if open_main>0:
                        self.new_window=(self.root)
                        self.app=vehicle_anti_theft_security_system(self.new_window)
                        
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
                #self.root.destroy()
                # self.root.destroy()


    #************************************Reset password button ko lagi*******************
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
                messagebox.showerror("Error","select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
                messagebox.showerror("Error","select your answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
                messagebox.showerror("Error","please enter your new password",parent=self.root2) 
        else:
            
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="details")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
           # my_cursor.execute(query,value)
            #my_cursor.execute("select * from register where email=%s and securityQ=%s and securityA=%s "(
            #self.txtuser.get(),
            #self.combo_security_Q.get(),
            #self.txt_security.get()

             #         ))
            row=my_cursor.fetchone()
            if row==None:
                speak_va("Wrong Security Answer")
                messagebox.showerror("Error","Invalid security answer")
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                speak_va("Your password has been reset successfully.")
                messagebox.showinfo("Info","your password has been reset , please login new password",parent=self.root2)
            conn.commit()
            conn.close()
            self.root2.destroy()

    #   ************************forget password****************
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="tupsy@5050", database="details")
            my_cursor = conn.cursor()
            query=("select *from register where email=%s")   ##### <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< see thissssssss
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"),bg="white", fg="red")
                l.place(x=0,y=0,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "your dad name", "your mother name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="orange",fg="green")
                btn.place(x=100,y=300)



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1600x800+0+0")

        # ***************variabletr
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background img
        
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\9.jpg")
        lbl_lbl = Label(self.root, image=self.bg)
        lbl_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # #left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\LOGO.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=30, y=100, width=500, height=550)
        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ***lebal and entry
        # column 1
        
        Register_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="REGISTER HERE",font=("times new roman",20,"bold"), fg="blue")
        Register_frame.place(x=5,y=5,width=670,height=400)

        

        fname=Label(Register_frame,text="First and Middle Name",font=("times new roman",15,"bold"),bg="white")
        fname.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        fname_entry=ttk.Entry(Register_frame,textvariable=self.var_fname,width=25,font=("times new roman",13,"bold"))
        fname_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        validate_fname=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_fname,'%P'))

        # lname = Label(frame, text="Last Name", font=(
        #     "times new roman", 15, "bold"), bg="white")
        # lname.place(x=370, y=100)

        # self.txt_lname = ttk.Entry(
        #     frame, textvariable=self.var_lname, font=("times new roman", 15))
        # self.txt_lname.place(x=370, y=130, width=250)

        lname=Label(Register_frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        lname_entry=ttk.Entry(Register_frame,textvariable=self.var_lname,width=25,font=("times new roman",13,"bold"))
        lname_entry.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        validate_lname=self.root.register(self.checklname)
        fname_entry.config(validate='key',validatecommand=(validate_lname,'%P'))


       
        contact=Label(Register_frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        contact_entry=ttk.Entry(Register_frame,textvariable=self.var_contact,width=25,font=("times new roman",13,"bold"))
        contact_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        validate_phone=self.root.register(self.checkphone)
        contact_entry.config(validate='key',validatecommand=(validate_phone,'%P'))

        email=Label(Register_frame,text="Email or Username",font=("times new roman",15,"bold"),bg="white")
        email.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(Register_frame,textvariable=self.var_email,width=25,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        email=Label(Register_frame,text="*Please enter valid email: ex123@gmail.com",font=("times new roman",8,"bold"),fg="red",bg="white")
        # pswd.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        email.place(x=250, y=139)



       

        security_Q=Label(Register_frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        Security_combo=ttk.Combobox(Register_frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly",width=23)
        Security_combo["values"]=("Select Security Question","Your Dad's Name","Your Mom's name")
        Security_combo.current(0)
        Security_combo.grid(row=7,column=1,padx=5,pady=10,sticky=W)

       

        security_A=Label(Register_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.grid(row=6,column=2,padx=10,pady=5,sticky=W)

        security_entry=ttk.Entry(Register_frame,textvariable=self.var_securityA,width=25,font=("times new roman",13,"bold"))
        security_entry.grid(row=7,column=2,padx=10,pady=5,sticky=W)


       
        pswd=Label(Register_frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.grid(row=8,column=1,padx=10,pady=5,sticky=W)

        pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_pass,width=25,font=("times new roman",13,"bold"))
        pswd_entry.grid(row=9,column=1,padx=10,pady=5,sticky=W)


        pswd=Label(Register_frame,text="*Please enter strong password",font=("times new roman",10,"bold"),fg="red",bg="white")
        # pswd.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        pswd.place(x=35, y=305)



    


        confirm_pswd=Label(Register_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.grid(row=8,column=2,padx=10,pady=5,sticky=W)

        confirm_pswd_entry=ttk.Entry(Register_frame,textvariable=self.var_confpass,width=25,font=("times new roman",13,"bold"))
        confirm_pswd_entry.grid(row=9,column=2,padx=10,pady=5,sticky=W)

        # ......check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I am Agree with terms and conditions", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=370)

        # button================BUTTONS TO REGISTER AND LOGINTO THE SYSTEM ==============

        
        img = Image.open(r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\7.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        
        img1 = Image.open(r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\8.jpg")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login,borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)


    def checkname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checklname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
        return True

    def checkphone(self,phone):
        if len(phone) <=10:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
            messagebox.showerror('Invalid','Invalid entry. Please enter phone (example:9846200045)', parent=self.root)
            return False
            
        else:
            messagebox.showwarning('Alert','invalid phone. Please enter phone (example:9846200045)',parent=self.root)
            return False



        
       
       



# ................fuction

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "password and confirm password must be same",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and conditions",parent=self.root)

        elif not ("@" or ".com") in self.var_email.get():
            messagebox.showerror("Error",'Invalid email Enter valid email like atupelemalunda@gmail.com ',parent=self.root)

        # elif not  (".org" or ".edu" or ".com" or ".net") in self.var_email.get():
        #     messagebox.showerror("Error",'Invalid email Enter valid email like keshav123@gmail.com ',parent=self.root)
        
        elif not ("@" or "!" or "$" or "-" or "." or "#" ) in self.var_pass.get():
            messagebox.showerror("Error",'Invalid password Please Enter Strong password like tupsy@123 ',parent=self.root)

    
        # def checkemail(self,email):
        #     if len(email)>=7:not
        # elif self.var_email.get()=="re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)([a-zA-z]{2,5})$")!=None":
        #     messagebox.showerror("Error",'Invalid email Enter valid email like keshav123@gmail.com ',pare"nt=self.root)

            # return True
            # else:
            #     messagebox.showwarning('Alert','Invalid email Enter valid email like keshav123@gmail.com ')
            #     return False
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="details")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")   ### <<<<<<<<<<<<<<<<<<seee
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "user already exists ,try another email", parent=self.root )
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (

                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                
                messagebox.showinfo("Success", "Register Successfully", parent=self.root )
            conn.commit()
            conn.close()
            # self.root.destroy()
    def return_login(self):
        self.root.destroy()


class vehicle_anti_theft_security_system:
    def __init__(self, root):
        
        self.root = root
        
        self.root.geometry("1550x800+0+0")
        self.root.title("Vehicle Anti Theft Security System")
     
        #Background image
        img1 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\mainbg.jpg")
        img1 = img1.resize((1550, 880), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=10, width=1530, height=850)
       
        

       
       
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(100, time)
        lbl = Label(self.root, font=('montiserat',15,'bold'),fg='maroon',bg='white')
        lbl.place(x=700,y=10,width=130,height=40)
        time()

        conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")

        my_str = tk.StringVar()

        #var_store
        plat_num = tk.StringVar()


      

        

        #Label for uploading the file============

        b1_1 = Button(self.root,text="Upload Photo",cursor="hand2",font=("montiserat", 11, "bold"), bg='maroon', fg="white",command=lambda:upload_file())
        b1_1.place(x=50, y=420, width=100, height=30)

        #=======LABEL2===========

        label2=tk.Label(self.root, textvariable=my_str,fg='maroon')
        label2.place(x=150,y=420, height=30)
        my_str.set("Select file")

        #done = Button(self.root, text="Upload file", font=('montiserat', 10, 'bold'))
        #done.place(x=50, y=470)

        #Results segement

        n_plate = Label(self.root, text="Result:", font=("montiserat", 15, 'bold'))
        n_plate.place(x=50, y=460)

        n_plate_n = Label(self.root, textvariable=plat_num, font=15)
        n_plate_n.place(x=180, y=460)

        get_d_btn = Button(self.root, text="Get details",cursor="hand2",activebackground='maroon',activeforeground='navyblue', font=('montiserat', 15, 'bold'), fg='white',bg='maroon', command=lambda:get_results())
        get_d_btn.place(x=50, y=500)

        n_plate = Label(self.root, text="CAR OWNER DETAILS",fg='navyblue',bg='white', font=("montiserat", 15, 'bold'))
        n_plate.place(x=50, y=550)

        frame=Frame(bg_img)
        frame.place(x=2,y=0,width=2000,height=2000)

        Left_frame = LabelFrame(frame, bd=2, bg="white", relief=RIDGE, text="Number Plate Detection & Recognition",fg='maroon', font=("montiserat", 14, 'bold'))
        Left_frame.place(x=5, y=10, width=750, height=770)

       


        fr = Frame(Left_frame,bg='white')
        fr.place(x=40, y=540, width=500, height=200)

        

        def upload_file():
            global file
            file=filedialog.askopenfile(initialdir='"C:/Users/MALUNDA/Documents/mAIN pROJECT/Vehicle Anti theft Security System/cars"', filetypes=[("png files","*.png"),("All types","*.*")])
            
            if(file):
                my_str.set(file.name)
                pic = Image.open(file.name)
                img = ImageTk.PhotoImage(pic)

                labe = Label(self.root, image=img)

                labe.image = img
                labe.place(x=50, y=120, width=500, height=300)
                #plat_num.set("Hello")

                ext_num = extract_num(file.name)
                plat_num.set("")

                # Clear previous entries
                for widget in fr.winfo_children():
                    widget.destroy()

                #display    licenseplate
              
                ext_num = extract_num(file.name)
                plat_num.set(ext_num)
        # take the data
        

                
       
        def get_results():
            if file is None:
                speak_va("No file selected")
                messagebox.showerror("Error", "No file selected")
                return

            ext_num = extract_num(file.name)

            icursor = conn.cursor()
            icursor.execute("SELECT * FROM car INNER JOIN profile ON car.Licenceplate='%s' AND car.Owner=profile.id" % ext_num)
            result = icursor.fetchall()

            if len(result) == 0:
                
                messagebox.showinfo("Oops", "CAR OWNER DETAILS NOT AVAILABLE")
            else:

                for widget in fr.winfo_children():
                    widget.destroy()
                lst = [
                    ('License plate:', result[0][1]),
                    ('Owner Name:', result[0][7]),
                    ('Contact:', result[0][3]),
                    ('EmailAddress:', result[0][4]),
                    ('HomeAddress:', result[0][5]),
                    #('Email', result[0][8]),
                    #('Address', result[0][9])
                ]

                # Rest of your code to display the details
                # Clear previous labels

                
            for child in fr.winfo_children():
                child.destroy()

            # Display the new details
            row_index = 0
            for item in lst:
                label = Label(fr, text=item[0], font=('montiserat', 14, 'bold'),fg='maroon', anchor='w')
                label.grid(row=row_index, column=0, sticky='w', padx=10, pady=5)

                value = Label(fr, text=item[1], font=('montiserat', 14), anchor='w')
                value.grid(row=row_index, column=1, sticky='w', padx=10, pady=5)

                row_index += 1

                print(result)

            
            
        #####=======FILE OPENER ==================
       

        
        #Personal Details
        img3 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\facedetection\persoanl2.png")
        img3 = img3.resize((300, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1=Button(self.root,image=self.photoimg3,cursor="hand2",command=self.personal_details)
        b1.place(x=770,y=100,width=300,height=300)

        b1_1=Button(self.root,text="Personal Details",cursor="hand2",font=("montiserat", 17,"bold"),bg='maroon',fg="white")
        b1_1.place(x=770,y=370,width=300,height=40)

        

        #Face Recognition

        img4 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\facedetection\robotface.png")
        img4 = img4.resize((300, 300), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root,image=self.photoimg4, cursor="hand2",command=self.face_recognition)
        b1.place(x=770, y=470, width=300, height=300)

        b1_1 = Button(self.root,text="Face Recognition",cursor="hand2", font=("montiserat", 17, "bold"), bg='maroon', fg="white")
        b1_1.place(x=770, y=750, width=300, height=40)

       

        #Train Data
        img6 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\face-recognition-attendance.jpg")
        img6 = img6.resize((300, 300), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(self.root,image=self.photoimg6,cursor="hand2",command=self.train)
        b1.place(x=1200,y=100,width=300,height=300)

        b1_1=Button(self.root,text="Data Training",cursor="hand2",font=("montiserat", 17,"bold"),bg='maroon',fg="white")
        b1_1.place(x=1200,y=370,width=300,height=40)

        #Exit System Button
        img12 = Image.open("Img/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((250, 250), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(self.root, image=self.photoimg12, cursor="hand2" ,command=self.iexit)
        btn8.place(x=1200, y=500, width=250, height=250)

        
   
        
    def open_img(self):
        os.startfile("data")
   #================= Functions Button To switch to personal details window=========

    def personal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Personal(self.new_window)
    
    # ===================================

    #function to switch to face recognition module

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognise(self.new_window)
 # ========================================================


 #======== function to switch to number plate detection ==========

    def number_plate_detection(self):
        self.new_window=Toplevel(self.root)
        self.app=detectplate(self.new_window)

 #======= FUNCTION TO SWITCH TO TRAIN DATA ======

    def train(self):
        self.new_window = Toplevel(self.root)
        self.app = TRAIN(self.new_window)
    #function to exit the system

    def iexit(self):
        #speak_va(" Are you sure you want to exit vehicle anti theft security System?")
        self.iexit=tkinter.messagebox.askyesno("Vehicle anti theft security system","Are you sure you want to exit this system?",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
       

       

                                                                                                 
if __name__ == "__main__":
    main()
    # root= Tk()
    # app=login_window(root)
    # root.mainloop()