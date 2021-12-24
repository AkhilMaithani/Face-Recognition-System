from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from tkinter import messagebox
import os
from support import Support
from train import TrainDataSet
from downloadattendence import DownloadAttendence

# class
class Admin:
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
        title_image = Image.open("Images/admin.png")
        title_image = title_image.resize((850,90),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 90)

        # Under Image Load, resize
        under_image = Image.open("Images/admin_under.png")
        under_image = under_image.resize((1360,50),Image.ANTIALIAS)
        self.under_image = ImageTk.PhotoImage(under_image)

        # Under Image Place
        under_image_label = Label(background_label,image = self.under_image)
        under_image_label.place(x = 2, y = 650, width = 1360, height = 50)

        # Buttons Photo Data Set
        all_photos = Image.open("Images/photos.png")
        all_photos = all_photos.resize((150,150),Image.ANTIALIAS)
        self.all_photos = ImageTk.PhotoImage(all_photos)

        button1 = Button(background_label,command = self.open_Photos,image = self.all_photos,cursor = "hand2")
        button1.place(x = 150,y = 200,width = 150,height = 150)
        button1_label = Label(background_label,text = "Photo's DataSet")
        button1_label.place(x = 150,y = 325,width = 150,height = 25)

        # Button Train Data Set
        train_dataset = Image.open("Images/taindata.jpg")
        train_dataset = train_dataset.resize((150,150),Image.ANTIALIAS)
        self.train_dataset = ImageTk.PhotoImage(train_dataset)

        button2 = Button(background_label,command = self.trainDataSet_f,image = self.train_dataset,cursor = "hand2")
        button2.place(x = 605,y = 200,width = 150,height = 150)
        button2_label = Label(background_label,text = "Train DataSet")
        button2_label.place(x = 605,y = 325,width = 150,height = 25)

        # Button Download Attendence
        download_attendence = Image.open("Images/checkattendence.jpg")
        download_attendence = download_attendence.resize((150,150),Image.ANTIALIAS)
        self.download_attendence = ImageTk.PhotoImage(download_attendence)

        button3 = Button(background_label,command = self.downlaod_attendance_f,image = self.download_attendence,cursor = "hand2")
        button3.place(x = 1025,y = 200,width = 150,height = 150)
        button3_label = Label(background_label,text = "Download Attendence")
        button3_label.place(x = 1025,y = 325,width = 150,height = 25)
        
        # Button Logout
        log_out = Image.open("Images/logout.jpg")
        log_out = log_out.resize((150,150),Image.ANTIALIAS)
        self.log_out = ImageTk.PhotoImage(log_out)

        button3 = Button(background_label,command = self.logout,image = self.log_out,cursor = "hand2")
        button3.place(x = 375,y = 450,width = 150,height = 150)
        button3_label = Label(background_label,text = "Log Out")
        button3_label.place(x = 375,y = 575,width = 150,height = 25)

        # Button Help
        support_section = Image.open("Images/support.png")
        support_section = support_section.resize((150,150),Image.ANTIALIAS)
        self.support_section = ImageTk.PhotoImage(support_section)

        button4 = Button(background_label,command = self.support_f,image = self.support_section,cursor = "hand2",bg = "white")
        button4.place(x = 820,y = 450,width = 150,height = 150)
        button4_label = Label(background_label,text = "Support")
        button4_label.place(x = 820,y = 575,width = 150,height = 25)

    # open photos
    def open_Photos(self):
        os.startfile("data")
    
    # train dataset
    def trainDataSet_f(self):
        self.new_window = Toplevel(self.root)
        self.app2 = TrainDataSet(self.new_window)

    # support Function
    def support_f(self):
        self.new_window = Toplevel(self.root)
        self.app1 = Support(self.new_window)

    # downloa Attendance Function
    def downlaod_attendance_f(self):
        self.new_window = Toplevel(self.root)
        self.app1 = DownloadAttendence(self.new_window)

    # logout function
    def logout(self):
        self.iexit = tkinter.messagebox.askyesno("Exit Window","Are you sure you want to exit!",parent = self.root)

        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    
if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()