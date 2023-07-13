from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox
from time import strftime
from datetime import datetime
import cv2
from detectplate import *
import mysql.connector
import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()



class detectplate:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Vehicle Anti Theft Security System")

        conn=mysql.connector.connect(host="localhost",username="root",password="tupsy@5050",database="details")

        my_str = tk.StringVar()

        #var_store
        plat_num = tk.StringVar()


        #Background image
        
       # img1 = Image.open( r"E:\Vehicle Anti theft Security System\Vehicle Anti theft Security System\img\numberplatebg.jpg")
       # img1 = img1.resize((1550, 880), Image.ANTIALIAS)
       # self.photoimg1 = ImageTk.PhotoImage(img1)

       # self.root = Label(self.root, image=self.photoimg1)
       # self.root.place(x=0, y=20, width=1530, height=850)



        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(100, time)
        lbl = Label(self.root, font=('montiserat',15,'bold'),fg='maroon',bg='white')
        lbl.place(x=650,y=10,width=130,height=50)
        time()

        #Car image

        #sel_lable = Label(text="Selected image:")
        #sel_lable.place(x=50, y=30)

        

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
        n_plate.place(x=800, y=100)

        n_plate_n = Label(self.root, textvariable=plat_num, font=15)
        n_plate_n.place(x=800, y=140)

        get_d_btn = Button(self.root, text="Get details",cursor="hand2",activebackground='maroon',activeforeground='navyblue', font=('montiserat', 15, 'bold'), fg='white',bg='maroon', command=lambda:get_results())
        get_d_btn.place(x=800, y=200)

        n_plate = Label(self.root, text="CAR OWNER DETAILS",fg='navyblue', font=("montiserat", 15, 'bold'))
        n_plate.place(x=800, y=300)

        fr = Frame(root)
        fr.place(x=800, y=340, width=500, height=200)

        

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

    




if __name__ == "__main__":
    root = Tk()
    obj = detectplate(root)
    root.mainloop()