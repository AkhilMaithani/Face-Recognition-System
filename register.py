from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


# class
class Register:
    # constructor of a class
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_sname = StringVar()
        self.var_id = StringVar()
        self.var_cname = StringVar()
        self.var_unro = StringVar()
        self.var_ro = StringVar()
        self.var_sec = StringVar()
        self.var_sem = StringVar()
        self.var_dep = StringVar()
        self.var_gen = StringVar()
        self.var_dob = StringVar()
        self.var_mo = StringVar()
        

        # Background Image Load, resize
        background = Image.open("Images/StudentBackground.jpg")
        background = background.resize((1366,768),Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(background)

        # Background Image Place
        background_label = Label(self.root,image = self.background)
        background_label.place(x = 0, y = 0, width = 1366, height = 768)

        # Title Image Load, resize
        title_image = Image.open("Images/registrationportal.png")
        title_image = title_image.resize((850,70),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 70)

        # registeration frame
        register_frame = Frame(background_label,bg = "white",highlightbackground="black",highlightthickness=3)
        register_frame.place(x = 83, y = 130, width = 1200, height = 550)

        # Student Name
        student_name = Label(register_frame,text = "Student Name: ",font = ("Comic Sans MS",13,"bold"))
        student_name.grid(row = 0,column = 0,padx = 10,pady = 10,sticky = W)
        student_name_entry = ttk.Entry(register_frame,textvariable = self.var_sname,width = 20,font = ("Comic Sans MS",13))
        student_name_entry.grid(row = 0,column = 1,padx = 10,pady = 10,sticky = W)

        # Student Id
        student_id = Label(register_frame,text = "Student Id: ",font = ("Comic Sans MS",13,"bold"))
        student_id.grid(row = 0,column = 2,padx = 10,pady = 10,sticky = W)
        student_id_entry = ttk.Entry(register_frame,textvariable = self.var_id,width = 20,font = ("Comic Sans MS",13))
        student_id_entry.grid(row = 0,column = 3,padx = 10,pady = 10,sticky = W)

        # Course Name
        course_name = Label(register_frame,text = "Course Name: ",font = ("Comic Sans MS",13,"bold"))
        course_name.grid(row = 0,column = 4,padx = 10,pady = 10,sticky = W)
        course_name_entry = ttk.Entry(register_frame,textvariable = self.var_cname,width = 20,font = ("Comic Sans MS",13))
        course_name_entry.grid(row = 0,column = 5,padx = 10,pady = 10,sticky = W)

        # University Roll Number
        university_roll_no = Label(register_frame,text = "Uni. Roll Number: ",font = ("Comic Sans MS",13,"bold"))
        university_roll_no.grid(row = 1,column = 0,padx = 10,pady = 10,sticky = W)
        university_roll_no_entry = ttk.Entry(register_frame,textvariable = self.var_unro,width = 20,font = ("Comic Sans MS",13))
        university_roll_no_entry.grid(row = 1,column = 1,padx = 10,pady = 10,sticky = W)

        # Class Roll Number
        class_roll_no = Label(register_frame,text = "Roll Number: ",font = ("Comic Sans MS",13,"bold"))
        class_roll_no.grid(row = 1,column = 2,padx = 10,pady = 10,sticky = W)
        class_roll_no_entry = ttk.Entry(register_frame,textvariable = self.var_ro,width = 20,font = ("Comic Sans MS",13))
        class_roll_no_entry.grid(row = 1,column = 3,padx = 10,pady = 10,sticky = W)

        # Section
        section = Label(register_frame,text = "Section: ",font = ("Comic Sans MS",13,"bold"))
        section.grid(row = 1,column = 4,padx = 10,pady = 10,sticky = W)
        section_entry = ttk.Entry(register_frame,textvariable = self.var_sec,width = 20,font = ("Comic Sans MS",13))
        section_entry.grid(row = 1,column = 5,padx = 10,pady = 10,sticky = W)

        # Department
        department = Label(register_frame,text = "Department: ",font = ("Comic Sans MS",13,"bold"))
        department.grid(row = 2,column = 0,padx = 10,pady = 10,sticky = W)
        department_entry = ttk.Entry(register_frame,textvariable = self.var_dep,width = 20,font = ("Comic Sans MS",13))
        department_entry.grid(row = 2,column = 1,padx = 10,pady = 10,sticky = W)

        # Current Semester
        semester = Label(register_frame,text = "Semester: ",font = ("Comic Sans MS",13,"bold"))
        semester.grid(row = 2,column = 2,padx = 10,pady = 10,sticky = W)
        semester_entry = ttk.Entry(register_frame,textvariable = self.var_sem,width = 20,font = ("Comic Sans MS",13))
        semester_entry.grid(row = 2,column = 3,padx = 10,pady = 10,sticky = W)

        # Gender
        gender = Label(register_frame,text = "Gender: ",font = ("Comic Sans MS",13,"bold"))
        gender.grid(row = 2,column = 4,padx = 10,pady = 10,sticky = W)
        gender_entry = ttk.Entry(register_frame,textvariable = self.var_gen,width = 20,font = ("Comic Sans MS",13))
        gender_entry.grid(row = 2,column = 5,padx = 10,pady = 10,sticky = W)

        # DOB
        dob = Label(register_frame,text = "DOB: ",font = ("Comic Sans MS",13,"bold"))
        dob.grid(row = 3,column = 0,padx = 10,pady = 10,sticky = W)
        dob_entry = ttk.Entry(register_frame,textvariable = self.var_dob,width = 20,font = ("Comic Sans MS",13))
        dob_entry.grid(row = 3,column = 1,padx = 10,pady = 10,sticky = W)

        # Mobile Number
        mobile_no = Label(register_frame,text = "Mobile Number: ",font = ("Comic Sans MS",13,"bold"))
        mobile_no.grid(row = 3,column = 2,padx = 10,pady = 10,sticky = W)
        mobile_no_entry = ttk.Entry(register_frame,textvariable = self.var_mo,width = 20,font = ("Comic Sans MS",13))
        mobile_no_entry.grid(row = 3,column = 3,padx = 10,pady = 10,sticky = W)
        
        # add photo section
        photo_section = Image.open("Images/addphotosample.png")
        photo_section = photo_section.resize((403,103),Image.ANTIALIAS)
        self.photo_section = ImageTk.PhotoImage(photo_section)

        photo_section_button = Button(register_frame,command = self.generateDataSet,image = self.photo_section,cursor = "hand2")
        photo_section_button.place(x = 400, y = 250, width = 403, height = 103)
        
        # save button
        save = Image.open("Images/save.png")
        save = save.resize((203,63),Image.ANTIALIAS)
        self.save = ImageTk.PhotoImage(save)

        save_button = Button(register_frame,command = self.addData,image = self.save,cursor = "hand2")
        save_button.place(x = 100, y = 450, width = 203, height = 63)

        # reset button
        reset = Image.open("Images/reset.png")
        reset = reset.resize((203,63),Image.ANTIALIAS)
        self.reset = ImageTk.PhotoImage(reset)

        reset_button = Button(register_frame,command = self.resetData,image = self.reset,cursor = "hand2")
        reset_button.place(x = 900, y = 450, width = 203, height = 63)

    
    # add data function
    def addData(self):
        if self.var_sname.get() == "" or self.var_id.get() == "" or self.var_unro.get() == "" or self.var_ro.get() == "":
            messagebox.showwarning("Warning","Some Fields are Empty!",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root", password = "1234",database = "face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( self.var_sname.get(), self.var_id.get(), self.var_cname.get(), self.var_unro.get(), self.var_ro.get(), self.var_sec.get(), self.var_dep.get(), self.var_sem.get(), self.var_gen.get(), self.var_dob.get(), self.var_mo.get()))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully!",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent = self.root)

    # reset function
    def resetData(self):
        self.var_sname.set("")
        self.var_id.set("")
        self.var_cname.set("")
        self.var_unro.set("")
        self.var_ro.set("")
        self.var_sec.set("")
        self.var_dep.set("")
        self.var_sem.set("")
        self.var_gen.set("")
        self.var_dob.set("")
        self.var_mo.set("")

    # generate data set and upload photos
    def generateDataSet(self):
        if self.var_sname.get() == "" or self.var_id.get() == "" or self.var_unro.get() == "" or self.var_ro.get() == "":
            messagebox.showwarning("Warning","Some Fields are Empty!",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",username = "root", password = "1234",database = "face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult =my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set StudentName = %s,CourseName = %s, UniRollNo = %s, RollNo = %s, Section = %s, Department = %s, Semester = %s, Gender = %s, DOB = %s, MobileNo = %s where StudentId = %s",(self.var_sname.get(),self.var_id.get()==id+1,self.var_cname.get(),self.var_unro.get(),self.var_ro.get(),self.var_sec.get(),self.var_dep.get(),self.var_sem.get(),self.var_gen.get(),self.var_dob.get(),self.var_mo.get()))

                conn.commit()
                conn.close()

                # load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor =1.3
                    # Minimum neighbour = 5

                    for (x,y,w,h) in faces :
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

                
                

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()