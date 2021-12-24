from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from register import Register
import tkinter
from tkinter import messagebox
from support import Support
from markattendence import MarkAttendence

# class
class Student:
    # constructor of a class
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Background Image Load, resize
        background = Image.open("Images/Background.png")
        background = background.resize((1366,768),Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(background)

        # Background Image Place
        background_label = Label(self.root,image = self.background)
        background_label.place(x = 0, y = 0, width = 1366, height = 768)

        # Title Image Load, resize
        title_image = Image.open("Images/student.png")
        title_image = title_image.resize((850,90),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 90)

        # Under Image Load, resize
        under_image = Image.open("Images/student_under.png")
        under_image = under_image.resize((1360,50),Image.ANTIALIAS)
        self.under_image = ImageTk.PhotoImage(under_image)

        # Under Image Place
        under_image_label = Label(background_label,image = self.under_image)
        under_image_label.place(x = 2, y = 650, width = 1360, height = 50)

        # Buttons Register Yourself
        register_yourself = Image.open("Images/registeryourself.png")
        register_yourself = register_yourself.resize((150,150),Image.ANTIALIAS)
        self.register_yourself = ImageTk.PhotoImage(register_yourself)

        button1 = Button(background_label,image = self.register_yourself,command = self.registerYourself,cursor = "hand2")
        button1.place(x = 150,y = 200,width = 150,height = 150)
        button1_label = Label(background_label,text = "Register Yourself")
        button1_label.place(x = 150,y = 325,width = 150,height = 25)

        # Button Mark Attendence
        mark_attendence = Image.open("Images/markattendence.png")
        mark_attendence = mark_attendence.resize((150,150),Image.ANTIALIAS)
        self.mark_attendence = ImageTk.PhotoImage(mark_attendence)

        button2 = Button(background_label,command = self.markAttendence_f,image = self.mark_attendence,cursor = "hand2")
        button2.place(x = 605,y = 200,width = 150,height = 150)
        button2_label = Label(background_label,text = "Mark Attendence")
        button2_label.place(x = 605,y = 325,width = 150,height = 25)

        # Button Logout
        log_out = Image.open("Images/logout.jpg")
        log_out = log_out.resize((150,150),Image.ANTIALIAS)
        self.log_out = ImageTk.PhotoImage(log_out)

        button3 = Button(background_label,command = self.logout,image = self.log_out,cursor = "hand2")
        button3.place(x = 1025,y = 200,width = 150,height = 150)
        button3_label = Label(background_label,text = "Log Out")
        button3_label.place(x = 1025,y = 325,width = 150,height = 25)

        # Button Help
        support_section = Image.open("Images/support.png")
        support_section = support_section.resize((150,150),Image.ANTIALIAS)
        self.support_section = ImageTk.PhotoImage(support_section)

        button4 = Button(background_label,command = self.support_f,image = self.support_section,cursor = "hand2",bg = "white")
        button4.place(x = 605,y = 450,width = 150,height = 150)
        button4_label = Label(background_label,text = "Support")
        button4_label.place(x = 605,y = 575,width = 150,height = 25)
        
    # Register Yourself Function
    def registerYourself(self):
        self.new_window = Toplevel(self.root)
        self.app1 = Register(self.new_window)

    # Mark Attendence Function
    def markAttendence_f(self):
        self.new_window = Toplevel(self.root)
        self.app1 = MarkAttendence(self.new_window)

    # support Function
    def support_f(self):
        self.new_window = Toplevel(self.root)
        self.app1 = Support(self.new_window)

    # logout function
    def logout(self):
        self.iexit = tkinter.messagebox.askyesno("Exit Window","Are you sure you want to exit!",parent = self.root)

        if self.iexit > 0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()