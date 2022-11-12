import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
import os



def create_test_image_frame(container):

    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(frame, text="Test Image")
    labelTestImage.grid(row=0, sticky="W")

    file = 'Adriana Lima0_0.jpg'
    folder = 'test'
    dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img = Image.open(dir).resize((448, 448),Image.ANTIALIAS)
    resizedImg = ImageTk.PhotoImage(img)
    labelImg = ttk.Label(frame, image=resizedImg)
    labelImg.grid(row=1)
    labelImg.image = resizedImg

    return frame

def create_result_image_frame(container):

    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(frame, text="Closest Result")
    labelTestImage.grid(row=0, sticky="W")

    file = 'Adriana Lima0_0.jpg'
    folder = 'test'
    dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img = Image.open(dir).resize((448, 448),Image.ANTIALIAS)
    resizedImg = ImageTk.PhotoImage(img)
    labelImg = ttk.Label(frame, image=resizedImg)
    labelImg.grid(row=1)
    labelImg.image = resizedImg

    return frame


def create_info_frame(container):

    frame = ttk.Frame(container)

    # grid layout
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=2)

    frame.rowconfigure(0, weight=2)
    frame.rowconfigure(1, weight=2)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=2)
    frame.rowconfigure(4, weight=2)
    frame.rowconfigure(5, weight=1)
    frame.rowconfigure(6, weight=2)
    frame.rowconfigure(7, weight=2)
    frame.rowconfigure(8, weight=1)
    frame.rowconfigure(9, weight=2)

    # def chooseFolder():

    # def chooseFile():
        
    insertDataset = ttk.Label(frame, text="Insert Your Dataset", style='Subheading.TLabel')
    insertDataset.grid(column=0, row=0, columnspan=2, sticky='W')
    chooseFolder = ttk.Button(frame, text="Choose Folder", command=frame.destroy)
    chooseFolder.grid(column=0)
    folderName = ttk.Label(frame, text="No file chosen")
    folderName.grid(column=1, row=1)

    insertTestImage = ttk.Label(frame, text="Insert Your Test Image", style='Subheading.TLabel')
    insertTestImage.grid(column=0, row=3, columnspan=2, sticky='W')
    chooseFile = ttk.Button(frame, text="Choose File", command=frame.destroy)
    chooseFile.grid(column=0, row=4, sticky='W')
    fileName = ttk.Label(frame, text="No file chosen")
    fileName.grid(column=1, row=4)

    result = ttk.Label(frame, text="Result", style='Subheading.TLabel')
    result.grid(column=0, row=6, columnspan=2,sticky='W')
    resultName = ttk.Label(frame, text="None")
    resultName.grid(column=0, row=7,columnspan=2,sticky='W')

    executionTime = ttk.Label(frame, text="Execution time: 01:00")
    executionTime.grid(column=0, row=9, columnspan=2,sticky='W')

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('recognice')
    root.minsize(1280, 720)
    root.config(bg = '#FFFFFF')

    # Layout on the root window
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=6)

    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=4)
    root.columnconfigure(2, weight=4)

    # logo

    # title
    ttk.Label(root, text="Recognize Face using Eigenface Method", style="Heading1.TLabel").grid(row=1,column=0,columnspan=3)

    # test image
    test_image_frame = create_test_image_frame(root)
    test_image_frame.grid(column=0, row=2)

    # result
    result_image_frame = create_result_image_frame(root)
    result_image_frame.grid(column=1, row=2)

    # info 
    info_frame = create_info_frame(root)
    info_frame.grid(column=2,row=2)

    # style
    s = ttk.Style()
    s.theme_use('alt')
    s.configure('.', font=('Dubai'))
    s.configure('Heading1.TLabel', font=('Dubai 32 bold'), foreground='#6C56C2')
    s.configure('Subheading.TLabel', font=('Dubai', 20), foreground='#6C56C2')
    s.configure('TButton', background = '#FFD04D', foreground='#FFFFFF', relief='flat')
    s.map('TButton', background=[('active','#FEBF10')], relief='flat')
    s.configure('TFrame', background = '#FFFFFF')
    s.configure('TLabel', background = '#FFFFFF')

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()

if __name__ == "__main__":
    create_main_window()
