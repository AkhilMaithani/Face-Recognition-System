from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from register import Register
import tkinter
from tkinter import messagebox
from markattendence import MarkAttendence

# class
class Support:
    # constructor of a class
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Background Image Load, resize
        background = Image.open("Images/StudentBackground.jpg")
        background = background.resize((1366,768),Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(background)

        # Background Image Place
        background_label = Label(self.root,image = self.background)
        background_label.place(x = 0, y = 0, width = 1366, height = 768)

        # Title Image Load, resize
        title_image = Image.open("Images/supportportal.png")
        title_image = title_image.resize((850,90),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 90)

        # Under Image Load, resize
        under_image = Image.open("Images/supportportalunder.png")
        under_image = under_image.resize((1360,50),Image.ANTIALIAS)
        self.under_image = ImageTk.PhotoImage(under_image)

        # Under Image Place
        under_image_label = Label(background_label,image = self.under_image)
        under_image_label.place(x = 2, y = 650, width = 1360, height = 50)

        # student support
        support_image = Image.open("Images/studentsupport.png")
        support_image = support_image.resize((455,255),Image.ANTIALIAS)
        self.support_image = ImageTk.PhotoImage(support_image)

        support_image_label = Label(background_label,image = self.support_image)
        support_image_label.place(x = 150, y = 260, width = 455, height = 255)

        # Admin support
        admin_image = Image.open("Images/adminsupport.png")
        admin_image = admin_image.resize((455,255),Image.ANTIALIAS)
        self.admin_image = ImageTk.PhotoImage(admin_image)

        admin_image_label = Label(background_label,image = self.admin_image)
        admin_image_label.place(x = 800, y = 260, width = 455, height = 255)


if __name__ == "__main__":
    root = Tk()
    obj = Support(root)
    root.mainloop()