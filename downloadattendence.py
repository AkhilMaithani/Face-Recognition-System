from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from time import strftime
from datetime import date, datetime
import mysql.connector
import numpy as np
import cv2
import csv
from tkinter import filedialog


# global variable 
mydata = []

# class
class DownloadAttendence:
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
        title_image = Image.open("Images/downladattendencetile.png")
        title_image = title_image.resize((850,90),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 90)

        # Import CSV button
        import_csv = Image.open("Images/importcsv.png")
        import_csv = import_csv.resize((283,73),Image.ANTIALIAS)
        self.import_csv = ImageTk.PhotoImage(import_csv)

        import_csv_button = Button(background_label,command = self.importCsv,image = self.import_csv,cursor = "hand2")
        import_csv_button.place(x = 150, y = 615, width = 283, height = 73)

        # Export CSV button
        export_csv = Image.open("Images/exportcsv.png")
        export_csv = export_csv.resize((283,73),Image.ANTIALIAS)
        self.export_csv = ImageTk.PhotoImage(export_csv)

        export_csv_button = Button(background_label,command = self.exportCsv,image = self.export_csv,cursor = "hand2")
        export_csv_button.place(x = 900, y = 615, width = 283, height = 73)

        # frame to show attendence
        register_frame = Frame(background_label,bg = "white",highlightbackground="black",highlightthickness=3)
        register_frame.place(x = 80, y = 200, width = 1200, height = 400)

        # scroll bars
        scroll_x = ttk.Scrollbar(register_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(register_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(register_frame,column = ("ID","Name","RollNo","Section","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill= X)
        scroll_y.pack(side = RIGHT,fill= Y)

        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text = "ID")
        self.AttendanceReportTable.heading("Name",text = "Name")
        self.AttendanceReportTable.heading("RollNo",text = "RollNo")
        self.AttendanceReportTable.heading("Section",text = "Section")
        self.AttendanceReportTable.heading("Time",text = "Time")
        self.AttendanceReportTable.heading("Date",text = "Date")
        self.AttendanceReportTable.heading("Attendance",text = "Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("ID",width = 100)
        self.AttendanceReportTable.column("Name",width = 100)
        self.AttendanceReportTable.column("RollNo",width = 100)
        self.AttendanceReportTable.column("Section",width = 100)
        self.AttendanceReportTable.column("Time",width = 100)
        self.AttendanceReportTable.column("Date",width = 100)
        self.AttendanceReportTable.column("Attendance",width = 100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand = 1)

    # fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent = self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
     # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1 :
                messagebox.showerror("NoData","No Data found to be export",parent = self.root)
                return False

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent = self.root)
            with open(fln,mode="w",newline ="") as myfile:
                exp_write = csv.writer(myfile,delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data exported","Your data exported successfully")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    

if __name__ == "__main__":
    root = Tk()
    obj = DownloadAttendence(root)
    root.mainloop()