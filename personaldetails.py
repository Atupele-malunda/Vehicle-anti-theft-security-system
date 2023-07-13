from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import pyttsx3
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class Personal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Vehicle Anti Theft Security System")

        #============ VAriables =================
        self.var_id=StringVar()
        self.var_Gender=StringVar()
        self.var_FirstName=StringVar()
        self.var_LastName=StringVar()
        self.var_Nationality=StringVar()
        self.var_Occupation=StringVar()
        self.var_HomeAddress=StringVar()
        self.var_PhoneNo=StringVar()
        self.var_Email=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()


        # background image
        img3 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\facedetection\facerecognition2.png")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # first image

        img = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\facedetection\facerecognition4.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=30, width=500, height=130)

        # second Image

        img1 = Image.open( r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\facedetection\facerecognition4.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=500, y=30, width=500, height=130)


        # third image

        img2 = Image.open(r"C:\Users\MALUNDA\Documents\mAIN pROJECT\Vehicle Anti theft Security System\facedetection\facerecognition2.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=1000, y=30, width=500, height=130)


        #mainframe

        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=2,y=50,width=1500,height=600)

        #left_frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Personal Information",font=("montiserat",14,'bold'))
        Left_frame.place(x=10,y=10,width=600,height=550)

        #right_frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Details", font=("montiserat", 14, 'bold'))
        Right_frame.place(x=700, y=10, width=750, height=550)

        #personal details gender frame

        personal_details_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,font=("montiserat",14))
        personal_details_frame.place(x=15,y=10,width=560,height=50)

        id_label=Label(personal_details_frame, text="id:",font=("montiserat",12,"bold"),bg="white")
        id_label.place(x=10,y=10)

        id_entry=ttk.Entry(personal_details_frame,textvariable=self.var_id, width=10,font=("montiserat",12))
        id_entry.place(x=35,y=10)

        gender_label=Label(personal_details_frame,text="Gender",font=('montiserat',12),state="active",bg="white")
        gender_label.place(x=280,y=10)

        gender_combo=ttk.Combobox(personal_details_frame,textvariable=self.var_Gender,font=("montiserat",12))
        gender_combo["values"]=("select gender","Male","Female")
        gender_combo.current(0)
        gender_combo.place(x=350,y=10)

        # personal details, firstname, surname and more frame

        more_details_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, font=("montiserat", 14))
        more_details_frame.place(x=15, y=70, width=560, height=420)

        

        #First name
        firstname_label=Label(more_details_frame, text="First Name:",font=("montiserat",12,"bold"),bg="white")
        firstname_label.grid(row=0,column=0,padx=10,sticky=W)

        firstname_entry=ttk.Entry(more_details_frame,textvariable=self.var_FirstName, width=25,font=("montiserat",12))
        firstname_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        #surname

        last_Name_label = Label(more_details_frame, text="Last Name:", font=("montiserat", 12,"bold"), bg="white")
        last_Name_label.grid(row=1, column=0, padx=10, sticky=W)

        last_Name_entry = ttk.Entry(more_details_frame,textvariable=self.var_LastName, width=25, font=("montiserat", 12))
        last_Name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #Nationality

        Nationality_label = Label(more_details_frame, text="Nationality:", font=("montiserat", 12, "bold"), bg="white")
        Nationality_label.grid(row=2, column=0, padx=10, sticky=W)

        Nationality_entry = ttk.Entry(more_details_frame,textvariable=self.var_Nationality, width=25, font=("montiserat", 12))
        Nationality_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #Occupation

        Occupation_label = Label(more_details_frame, text="Occupation:", font=("montiserat", 12, "bold"), bg="white")
        Occupation_label.grid(row=3, column=0, padx=10, sticky=W)

        Occupation_entry = ttk.Entry(more_details_frame,textvariable=self.var_Occupation, width=25, font=("montiserat", 12))
        Occupation_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        #Home address

        address_label = Label(more_details_frame, text="Home Address:", font=("montiserat", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(more_details_frame,textvariable=self.var_HomeAddress, width=25, font=("montiserat", 12))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        #phone no

        phone_label = Label(more_details_frame, text="Phone No:", font=("montiserat", 12, "bold"), bg="white")
        phone_label.grid(row=5, column=0, padx=10, sticky=W)

        phone_entry = ttk.Entry(more_details_frame,textvariable=self.var_PhoneNo, width=25, font=("montiserat", 12))
        phone_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        #Email

        Email_label = Label(more_details_frame, text="Email:", font=("montiserat", 12, "bold"), bg="white")
        Email_label.grid(row=6, column=0, padx=10, sticky=W)

        Email_entry = ttk.Entry(more_details_frame,textvariable=self.var_Email, width=25, font=("montiserat", 12))
        Email_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        #radio buttons

        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(more_details_frame,variable=self.var_radio1,command=self.generate_dataset,text="Take photo sample",value="yes")
        radionbtn1.grid(row=7, column=0)

        radionbtn2=ttk.Radiobutton(more_details_frame,variable=self.var_radio1,text="No photo sample", value="No")
        radionbtn2.grid(row=7,column=1)

        #buttons frame

        btn_frame=Frame(more_details_frame, bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=330,width=550,height=80)

        save_btn=Button(btn_frame, text="Save",command=self.add_data,width=13,font=("montiserat",12,"bold"),bg="maroon",fg="white")
        save_btn.place(x=0,y=1)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=13, font=("montiserat", 12, "bold"), bg="maroon", fg="white")
        update_btn.place(x=130,y=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=13, font=("montiserat", 12, "bold"), bg="maroon", fg="white")
        delete_btn.place(x=265, y=1)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=13, font=("montiserat", 12, "bold"), bg="maroon", fg="white")
        reset_btn.place(x=405, y=1)
       
        #take photo sample button

        Take_photo_sample_btn = Button(btn_frame, text="", width=70, font=("montiserat", 13, "bold"), bg="navy blue", fg="white")
        Take_photo_sample_btn.place(x=0,y=35)

        
        #RIGHT frame search system

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("montiserat",12))
        search_frame.place(x=10,y=15,width=723,height=70)

        search_label = Label(search_frame, text="Search By:", font=("montiserat", 12, "bold"), bg="navy blue",fg="white")
        search_label.grid(row=0, column=0, padx=10,pady=8, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("montiserat", 12),width=15 ,textvariable=self.var_search)
        search_combo["values"] = ("select","Nationality","Occupation","Home address")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2)

        search_entry = ttk.Entry(search_frame, width=18,textvariable=self.var_searchtxt, font=("montiserat", 12))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        search_btn = Button(search_frame, text="Search",command=self.search_data, width=11, font=("montiserat", 12, "bold"), bg="maroon", fg="white")
        search_btn.grid(row=0, column=3)

        searchAll_btn = Button(search_frame, text="Search All",command=self.show_all, width=11, font=("montiserat", 12, "bold"), bg="maroon", fg="white")
        searchAll_btn.grid(row=0, column=4, padx=3)

        #========== TAble Frame on the right frame=========

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=15,y=100,width=710,height=400)

        scroll_X=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.personal_details_table=ttk.Treeview(table_frame,column=("id","Gender","First Name","Last Name","Nationality","Occupation","Home Address","phone No","Email","photo"),xscrollcommand=scroll_X.set,yscrollcommand=scroll_y.set)

        scroll_X.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_X.config(command=self.personal_details_table.xview)
        scroll_y.config(command=self.personal_details_table.yview)

        self.personal_details_table.heading("id", text="id")
        self.personal_details_table.heading("Gender", text="Gender")
        self.personal_details_table.heading("First Name" , text="First Name")
        self.personal_details_table.heading("Last Name", text="Last Name")
        self.personal_details_table.heading("Nationality", text="NAtionality")
        self.personal_details_table.heading("Occupation", text="Occupation")
        self.personal_details_table.heading("Home Address", text="Home Address")
        self.personal_details_table.heading("phone No", text="Phone No")
        self.personal_details_table.heading("Email", text="Email")
        self.personal_details_table.heading("photo", text="PhotoSampleStatus")
        self.personal_details_table["show"]="headings"

        self.personal_details_table.pack(fill=BOTH,expand=1)
        self.personal_details_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    #=================== function decralation =========================

    def add_data(self):
        if self.var_Gender.get()=="Select Gender" or self.var_FirstName.get()=="" or self.var_LastName.get()=="" or self.var_Nationality.get()=="" or self.var_HomeAddress.get=="" or self.var_Occupation.get=="":
            speak_va("All fields are required")
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into intel values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_id.get(),
                                                                                   self.var_Gender.get(),
                                                                                   self.var_FirstName.get(),
                                                                                   self.var_LastName.get(),
                                                                                   self.var_Nationality.get(),
                                                                                   self.var_Occupation.get(),
                                                                                   self.var_HomeAddress.get(),
                                                                                   self.var_PhoneNo.get(),
                                                                                   self.var_Email.get(),
                                                                                
                                                                    
                                                                                   self.var_radio1.get() 
                                                                                 
                                                                                 
                                                                                 
                                                                                 
                                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Person's details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #======= fetch from database ========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from intel")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.personal_details_table.delete(*self.personal_details_table.get_children())
            for i in data:
                self.personal_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=========== get Cursor ====================================

    def get_cursor(self,event=""):
        cursor_focus=self.personal_details_table.focus()
        content=self.personal_details_table.item(cursor_focus)
        data=content["values"]

        self.var_id.set(data[0]),
        self.var_Gender.set(data[1]),
        self.var_FirstName.set(data[2]),
        self.var_LastName.set(data[3]),
        self.var_Nationality.set(data[4]),
        self.var_HomeAddress.set(data[5]),
        self.var_Occupation.set(data[6]),
        self.var_PhoneNo.set(data[7]),
        self.var_Email.set(data[8]),
        self.var_radio1.set(data[9])

    #======= Update Function =================

    def update_data(self):
        if self.var_Gender.get()=="Select Gender " or self.var_FirstName.get()=="" or self.var_LastName.get()=="":
            speak_va('All fields are required')
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this person's details",parent=self.root)
                if Update>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")
                     my_cursor=conn.cursor()
                     my_cursor.execute("update intel set    id=%s, Gender=%s,FirstName=%s,LastName=%s,Nationality=%s,Occupation=%s,HomeAddress=%s,PhoneNo=%s,Email=%s where Photo=%s",(
                     
                                                                                                                                                            self.var_id.get(),
                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                            self.var_FirstName.get(),
                                                                                                                                                            self.var_LastName.get(),
                                                                                                                                                            self.var_Nationality.get(),
                                                                                                                                                            self.var_Occupation.get(),
                                                                                                                                                            self.var_HomeAddress.get(),
                                                                                                                                                            self.var_PhoneNo.get(),
                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                            
                                                                                                                                                            self.var_radio1.get()
                                                                                                                                                             
                                                                                                                                                            
                                                                                                                                                            
                                                                                                                                        
                                                                                                                                                            
                                                                                                                            
                     
                    
                     
                     
                                                                                                                                                               ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","Person's details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==========  delete function ===========

    def delete_data(self):
        if self.var_Email.get() == "":
            messagebox.showerror("Error", "Email must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("intel Delete page", "Do you want to delete this person", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="tupsy@5050", database="details")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM intel WHERE Email = %s"
                    val = (self.var_Email.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted person's details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


#=========== RESET Function =========================

    def reset_data(self):
        self.var_id.set("")
        self.var_Gender.set("Select Gender")
        self.var_FirstName.set("")
        self.var_LastName.set("")
        self.var_Nationality.set("")
        self.var_Occupation.set("")
        self.var_HomeAddress.set("")
        self.var_PhoneNo.set("")
        self.var_Email.set("")
        self.var_radio1.set("")


# ..............Generate data set or take photo sample

# ...

   # ...



    # ...

    def generate_dataset(self):
        if self.var_Gender.get() == "Select Gender" or self.var_FirstName.get() == "" or self.var_id.get() == "":
            speak_va("All fields are mandatory")
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="tupsy@5050", database="details")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT COUNT(*) FROM intel")
                result = my_cursor.fetchone()
                id = result[0]

                sql = "UPDATE intel SET Gender=%s, FirstName=%s, LastName=%s, Nationality=%s, Occupation=%s, HomeAddress=%s, PhoneNo=%s, Email=%s, Photo=%s WHERE id=%s"
                val = (self.var_Gender.get(), self.var_FirstName.get(), self.var_LastName.get(),
                       self.var_Nationality.get(), self.var_Occupation.get(), self.var_HomeAddress.get(),
                       self.var_PhoneNo.get(), self.var_Email.get(), self.var_radio1.get(), id + 1)

                my_cursor.execute(sql, val)
                conn.commit()

                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined face frontal data from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/" + "user" + "." + str(id + 1) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 20:
                        break

                cap.release()
                cv2.destroyAllWindows()

                speak_va("Generation of dataset completed")
                messagebox.showinfo("Result", "Generation of dataset completed", parent=self.root)
            except Exception as es:
                speak_va("An exception occurred")
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ...

# ...





     # search data     
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from intel where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.personal_details_table.delete(*self.personal_details_table.get_children())
                    for i in rows:
                        self.personal_details_table.insert("",END,values=i)
                    if rows==None:
                        speak_va("Data Not Found")
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                speak_va("An Exception Occurred!")
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    # show all 
    def show_all(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")
        
        my_cursor=conn.cursor()
        my_cursor.execute("select * from intel")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.personal_details_table.delete(*self.personal_details_table.get_children())
            for i in data:
                self.personal_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


                                                                                                  


if __name__ == "__main__":
    root = Tk()
    obj = Personal(root)
    root.mainloop()