from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from colorama import Cursor
import cv2
from tkinter import messagebox
import os
import numpy as np
import mysql.connector
import tkinter
import tkinter as tk
from time import strftime
from datetime import datetime 
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()



class TRAIN:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Vehicle Anti Theft Security System")
               
       #Background image
        img1 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\img\trainbg.jpg")
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
        lbl.place(x=680,y=350,width=130,height=50)
        time()

        

        
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2", font=("montiserat", 30, "bold"), bg='maroon', fg="white")
        b1_1.place(x=600, y=400, width=300, height=60)
        
        #data_Training code


    def train_classifier(self):
        # data_dir=(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\data")
        # data_dir = (r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\data")
        data_dir = (r"E:\Vehicle Anti theft Security System\Vehicle Anti theft Security System\data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # grAY SCALE image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        #speak_va("Data Training completed successfully!")
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)
        # self.root.destroy()


        
    

if __name__ == "__main__":
    root = Tk()
    obj = TRAIN(root)
    root.mainloop()