from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from personaldetails import Personal
from facerecognition import Recognise
from numberplatedetection import detectplate
from time import strftime
from datetime import datetime 
from tkinter import messagebox
import tkinter
import cv2
import pyttsx3
import os
import re


class vehicle_anti_theft_security_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Vehicle Anti Theft Security System")


        
     
        
       
        

        title_lbl=Label(text="VEHICLE ANTI THEFT SECURITY SYSTEM",fg='maroon',font=("montiserat)",30,'bold'),bg='white')
        title_lbl.place(x=0,y=0,width=1530,height=100)
       
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(100, time)
        lbl = Label(title_lbl, font=('montiserat',13,'bold'),fg='maroon',bg='white')
        lbl.place(x=0,y=25,width=110,height=50)
        time()



        
        #Personal Details
        img3 = Image.open( r"C:\Users\USER\Downloads\Vehicle Anti theft Security System\Vehicle Anti theft Security System\facedetection\persoanl2.png")
        img3 = img3.resize((300, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1=Button(self.root,image=self.photoimg3,cursor="hand2")
        b1.place(x=100,y=200,width=300,height=300)

        b1_1=Button(self.root,text="Personal Details",command=self.personal_details,cursor="hand2",font=("montiserat", 13,"bold"),bg='maroon',fg="white")
        b1_1.place(x=100,y=500,width=300,height=40)

        

        #Face Recognition

        img4 = Image.open( r"C:\Users\USER\Downloads\Vehicle Anti theft Security System\Vehicle Anti theft Security System\facedetection\robotface.png")
        img4 = img4.resize((300, 300), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root,image=self.photoimg4, cursor="hand2")
        b1.place(x=630, y=200, width=300, height=300)

        b1_1 = Button(self.root,text="Face Recognition",command=self.face_recognition,cursor="hand2", font=("montiserat", 13, "bold"), bg='maroon', fg="white")
        b1_1.place(x=630, y=500, width=300, height=40)

        #number plate recognition

        img5 = Image.open( r"C:\Users\USER\Downloads\Vehicle Anti theft Security System\Vehicle Anti theft Security System\facedetection\detectednumberplate.png")
        img5 = img5.resize((300, 300), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(self.root,image=self.photoimg5, cursor="hand2")
        b1.place(x=1150, y=200, width=300, height=300)

        b1_1 = Button(self.root,text="Number plate detection & recognition",command=self.number_plate_detection, cursor="hand2", font=("montiserat", 13, "bold"), bg='maroon', fg="white")
        b1_1.place(x=1150, y=500, width=300, height=40)

        
        
        #Exit System Button
        img12 = Image.open("Img/exit-sign-neon-style_77399-144.jpg")
        img12 = img12.resize((195, 195), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        btn8 = Button(self.root, image=self.photoimg12, cursor="hand2")
        btn8.place(x=1150, y=500, width=195, height=195)

        btn8_8 = Button(self.root, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white" ,command=self.iexit)   
        btn8_8.place(x=1150, y=500, width=195, height=40)
        

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
        
    #function to exit the system

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Vehicle anti theft security system","Are you sure you want to exit this project?",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
       








if __name__ == "__main__":
    root = Tk()
    obj = vehicle_anti_theft_security_system(root)
    root.mainloop()