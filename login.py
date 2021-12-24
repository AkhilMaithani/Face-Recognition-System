# for making GUI
from tkinter import *
# for stylish tool kits 
from tkinter import ttk
# for images [Python Imaging Library]
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import student
import admin


# class
class FaceRecognitionSystem:
    # constructor of a class
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_workspace = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()


        # Background Image Load, resize
        background = Image.open("Images/loginbackground.png")
        background = background.resize((1366,768),Image.ANTIALIAS)
        self.background = ImageTk.PhotoImage(background)

        # Background Image Place
        background_label = Label(self.root,image = self.background)
        background_label.place(x = 0, y = 0, width = 1366, height = 768)

        # Title Image Load, resize
        title_image = Image.open("Images/facerecognitionsystem.png")
        title_image = title_image.resize((855,75),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 855, height = 75)

        # registeration frame
        register_frame = Frame(background_label,bg = "white",highlightbackground="black",highlightthickness=3)
        register_frame.place(x = 500, y = 200, width = 400, height = 400)

        # image login
        login_image = Image.open("Images/loginicon.png")
        login_image = login_image.resize((380,380),Image.ANTIALIAS)
        self.login_image = ImageTk.PhotoImage(login_image)

        login_image_label = Label(register_frame,image = self.login_image)
        login_image_label.place(x = 0, y = 0, width = 380, height = 380)


        # Select Workplace
        work_place = Label(register_frame,text = "Workplace: ",font = ("Comic Sans MS",13,"bold"))
        work_place.grid(row = 10,column = 0,padx = 10,pady = 10,sticky = W)
        work_place_entry = ttk.Entry(register_frame,textvariable = self.var_workspace,width = 20,font = ("Comic Sans MS",13))
        work_place_entry.grid(row = 10,column = 1,padx = 10,pady = 10,sticky = W)

        # Select Workplace
        user_name = Label(register_frame,text = "Username: ",font = ("Comic Sans MS",13,"bold"))
        user_name.grid(row = 13,column = 0,padx = 10,pady = 10,sticky = W)
        user_name_entry = ttk.Entry(register_frame,textvariable = self.var_username,width = 20,font = ("Comic Sans MS",13))
        user_name_entry.grid(row = 13,column = 1,padx = 10,pady = 10,sticky = W)

        # Select Workplace
        password_en = Label(register_frame,text = "Password: ",font = ("Comic Sans MS",13,"bold"))
        password_en.grid(row = 16,column = 0,padx = 10,pady = 10,sticky = W)
        password_en_entry = ttk.Entry(register_frame,textvariable = self.var_password,width = 20,font = ("Comic Sans MS",13))
        password_en_entry.grid(row = 16,column = 1,padx = 10,pady = 10,sticky = W)

        # login button
        login_button = Image.open("Images/loginbutton.png")
        login_button = login_button.resize((255,75),Image.ANTIALIAS)
        self.login_button = ImageTk.PhotoImage(login_button)

        login_button_bu = Button(login_image_label,command = self.login_f,image = self.login_button,cursor = "hand2")
        login_button_bu.place(x = 70, y = 250, width = 255, height = 75)

    # login function
    def login_f(self):
        if ((self.var_workspace.get()).lower() == "student") and ((self.var_username.get()).lower() == "user1") and ((self.var_password.get()) == "1234"):
            messagebox.showinfo("Success","Login into Student Portal!")
            student.Student(root)
        elif ((self.var_workspace.get()).lower() == "admin") and ((self.var_username.get()).lower() == "user2") and ((self.var_password.get()) == "5678"):
            messagebox.showinfo("Success","Login into Admin Portal!")
            admin.Admin(root)
        else:
            messagebox.showerror("Error","Wrong Credentials!")


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()