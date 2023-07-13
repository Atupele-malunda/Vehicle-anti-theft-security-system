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



class Recognise:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Vehicle Anti Theft Security System")
               
       #Background image
        img1 = Image.open( r"E:\Vehicle Anti theft Security System\Vehicle Anti theft Security System\img\face_scan_Adobe.jpg")
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
        lbl.place(x=720,y=45,width=130,height=50)
        time()

        #Recognise

        img4 = Image.open( r"E:\Vehicle Anti theft Security System\Vehicle Anti theft Security System\img\facedetector.png")
        img4 = img4.resize((500, 500), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root,image=self.photoimg4, cursor="hand2",command=self.face_recog)
        b1.place(x=550, y=100, width=500, height=500)

        b1_1 = Button(self.root,text="RECOGNISE FACE",cursor="hand2", command=self.face_recog,font=("montiserat", 15, "bold"), bg='maroon', fg="white")
        b1_1.place(x=550, y=600, width=500, height=40)
        
        


    # face recognition  command=self.face_recog
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w + 20, y + h + 20), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h + 20, x:x + w + 20])

        # Rest of your code
        # ...


    # Rest of your code
    # ...

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h+20,x:x+w+20])
                
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")
                
                my_cursor=conn.cursor()

                query = "SELECT FirstName FROM intel WHERE Email = %s"
                my_cursor.execute(query, (str(id),))
                n = my_cursor.fetchone()

                n = str(n)
                print(n)
                # n="+".join(n)

                query = "SELECT LastName FROM intel WHERE Email = %s"
                my_cursor.execute(query, (str(id),))
                r = my_cursor.fetchone()
                r = str(r)
                # r = "+".join(r)

                
                query = "SELECT Occupation FROM intel WHERE Email = %s"
                my_cursor.execute(query, (str(id),))
                d = my_cursor.fetchone()
                d = str(d)
                # d = "+".join(d)

                query = "SELECT HomeAddress FROM intel WHERE Email = %s"
                my_cursor.execute(query, (str(id),))
                i = my_cursor.fetchone()
                i=my_cursor.fetchone()
                #i = str(i)
                #i = "+".join(i)
                #print(id)
                # new code for accuracy calculation
                #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                
                #result = id.predict(img)

                if predict < 500:  
                 #if result[1] < 500:
                    confidence=int((100*(1-predict/300)))
                    #str2 = str(confidence)
                    #confidence = int(100 * (1 - (result[1])/300))
                    #display_string = str(confidence)+'% confidence it is user'
                    #cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-100), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)



                if confidence> 70:
                    cv2.putText(img,f"FirstName: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0 ,0,128),3)

                    cv2.putText(img,f"LastName:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,128),3)

                    cv2.putText(img,f"Occupation:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,128),3)
                    
                    cv2.putText(img,f"HomeAddress:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,128),3)
                    #self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,0,255),3)
            
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord 
            
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            # speak_va("Welcome to Face Recognition World")
            cv2.imshow("Welcome to face Recognition",img)


            if cv2.waitKey(1)==13:
                
                break
        video_cap.release()
        cv2.destroyAllWindows()


        # df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen23.csv")
        #df_state = pd.read_csv(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Teamkyzen23.csv")
    
        # Dup_Rows = df_state[df_state.duplicated()]

       # DF_RM_DUP = df_state.drop_duplicates(keep=False) 

        # print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

        # DF_RM_DUP = df_state.drop_duplicates(keep=False)
    # writer=csv.writer(DF_RM_DUP.head(n=1))

    # pahilaaaa koooooooooooooooo display
#    .............. # [[  data = DF_RM_DUP.head(n=1)
    # #    ((((((Pahilaaa koooo yo)))))) # data.to_csv('teamkyzen1.csv',encoding='utf-8', index=True)
    #     with open("test.csv", "wt") as fp:
    #         writer = csv.writer(fp)
    # # writer.writerow(["your", "header", "foo"])  # write header
    #         writer.writerow(data)
    
        # DF_RM_DUP.to_csv('test.csv', index=False) 
       # DF_RM_DUP.to_csv('test1.csv', index=False) 


       


        



        



        
    #     df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen2.csv")
    
    #     # Dup_Rows = df_state[df_state.duplicated()]

    #     DF_RM_DUP = df_state.drop_duplicates(keep=False) 

    #     # print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

    #     # DF_RM_DUP = df_state.drop_duplicates(keep=False)
    # # writer=csv.writer(DF_RM_DUP.head(n=1))


    # # print('\n\nResult DataFrame after duplicate removal :\n', DF_RM_DUP.head(n=1))
    #     data = str(DF_RM_DUP.head(n=1))

        
    

if __name__ == "__main__":
    root = Tk()
    obj = Recognise(root)
    root.mainloop()