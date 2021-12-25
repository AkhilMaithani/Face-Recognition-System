from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

# class
class TrainDataSet:
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
        title_image = Image.open("Images/traindataset.png")
        title_image = title_image.resize((850,90),Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(title_image)

        # Title Image Place
        title_image_label = Label(background_label,image = self.title_image)
        title_image_label.place(x = 260, y = 25, width = 850, height = 90)

        # Under Image Load, resize
        under_image = Image.open("Images/trainunder.png")
        under_image = under_image.resize((1360,60),Image.ANTIALIAS)
        self.under_image = ImageTk.PhotoImage(under_image)

        # Under Image Place
        under_image_label = Label(background_label,image = self.under_image)
        under_image_label.place(x = 2, y = 635, width = 1360, height = 60)

        # train data button
        train_section = Image.open("Images/trainbutton.png")
        train_section = train_section.resize((295,295),Image.ANTIALIAS)
        self.train_section = ImageTk.PhotoImage(train_section)

        train_section_button = Button(background_label,command = self.trainClassifier,image = self.train_section,cursor = "hand2")
        train_section_button.place(x = 550, y = 250, width = 295, height = 295)

    # train classifier
    def trainClassifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # grey scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training Data Set",imageNp)
            cv2.waitKey(1) == 13
        
        ids = np.array(ids)
    
        # actual training loop
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training DataSets Completed!",parent = self.root)



if __name__ == "__main__":
    root = Tk()
    obj = TrainDataSet(root)
    root.mainloop()