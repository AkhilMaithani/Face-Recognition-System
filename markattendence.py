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

# class
class MarkAttendence:
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
        title_image = Image.open("Images/markattendencetitle.png")
        title_image = title_image.resize((850,90),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 90)

        # Under Image Load, resize
        under_image = Image.open("Images/markattendenceunder.png")
        under_image = under_image.resize((1360,60),Image.ANTIALIAS)
        self.under_image = ImageTk.PhotoImage(under_image)

        # Under Image Place
        under_image_label = Label(background_label,image = self.under_image)
        under_image_label.place(x = 2, y = 635, width = 1360, height = 60)

        # mark attendence button
        mark_attendence_section = Image.open("Images/markattendencebutton.png")
        mark_attendence_section = mark_attendence_section.resize((305,305),Image.ANTIALIAS)
        self.mark_attendence_section = ImageTk.PhotoImage(mark_attendence_section)

        mark_attendence_section_button = Button(background_label,command = self.mark_attendence_fun,image = self.mark_attendence_section,cursor = "hand2")
        mark_attendence_section_button.place(x = 550, y = 250, width = 305, height = 305)

    
    # attendence in csv file
    def attendence_csv(self,i,r,n,s):
        with open("student_attendence.csv","r+",newline = "\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if(i not in name_list):
                now = datetime.now()
                date_curr = now.strftime("%d/%m/%Y")
                time_curr = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{r},{s},{time_curr},{date_curr},Present")

            
    # mark attendence main function
    def mark_attendence_fun(self):
        def details(img,classifier,scalefactor,minneighbour,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scalefactor,minneighbour)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = "localhost",username = "root", password = "1234",database = "face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("select StudentName from Student where StudentId = " + str(id))
                n = my_cursor.fetchone()
                na = ''.join(n)
                
                my_cursor.execute("select StudentId from Student where StudentId = " + str(id))
                i = my_cursor.fetchone()
                idd = ''.join(i)

                my_cursor.execute("select RollNo from Student where StudentId = " + str(id))
                r = my_cursor.fetchone()
                ro = ''.join(r)

                my_cursor.execute("select Section from Student where StudentId = " + str(id))
                s = my_cursor.fetchone()
                sec = ''.join(s)

                if confidence > 77:
                    cv2.putText(img,f"Name: {na}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),1)
                    cv2.putText(img,f"StudentId: {idd}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),1)
                    cv2.putText(img,f"RollNo: {ro}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),1)
                    cv2.putText(img,f"Section: {sec}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),1)
                    self.attendence_csv(idd,ro,na,sec)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face Detected",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),1)
                
                coord = [x,y,w,y]
            
            return coord
        

        def check(img,clf,faceCascade):
            coord = details(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = check(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = MarkAttendence(root)
    root.mainloop()