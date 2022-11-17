import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
from PIL import ImageTk, Image
import os

def create_test_image_frame(container):

    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(frame, text="Test Image", style="Subheading02.TLabel")
    labelTestImage.grid(row=0, sticky="W")

    # File dan folder dari test image
    file = 'no_image01.png'
    folder = 'assets'
    # Open dan show image
    dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img = Image.open(dir).resize((360, 360),Image.Resampling.LANCZOS)
    resizedImg = ImageTk.PhotoImage(img)
    labelImg = ttk.Label(frame, image=resizedImg)
    labelImg.grid(row=1)
    labelImg.image = resizedImg
    return frame

def create_other_closest_result(container):
    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(frame, text="Other Closest Results", style="Subheading02.TLabel")
    labelTestImage.grid(row=0, sticky="W", columnspan=3)

    # File dan folder closest result 1
    file = 'no_image02.png'
    folder = 'assets'
    # Open dan show image closest result 1
    dir01 = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img01 = ImageTk.PhotoImage(Image.open(dir01))
    labelImg = ttk.Label(frame, image=img01)
    labelImg.grid(row=1, column=0, sticky='W')
    labelImg.image = img01

    # File dan folder closest result 2
    file = 'no_image02.png'
    folder = 'assets'
    # Open dan show image closest result 1
    dir02 = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img02 = ImageTk.PhotoImage(Image.open(dir02))
    labelImg = ttk.Label(frame, image=img02)
    labelImg.grid(row=1, column=1)
    labelImg.image = img02

    # File dan folder closest result 3
    file = 'no_image02.png'
    folder = 'assets'
    # Open dan show image closest result 1
    dir03 = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img03 = ImageTk.PhotoImage(Image.open(dir03))
    labelImg = ttk.Label(frame, image=img03)
    labelImg.grid(row=1, column=2)
    labelImg.image = img03

    return frame
    

def create_result_image_frame(container):

    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(frame, text="Closest Result", style="Subheading02.TLabel")
    labelTestImage.grid(row=0, sticky="W")

    # File dan folder result image
    file = 'no_image01.png'
    folder = 'assets'
    # Open dan show image
    dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file))
    img = Image.open(dir).resize((360, 360),Image.Resampling.LANCZOS)
    resizedImg = ImageTk.PhotoImage(img)
    labelImg = ttk.Label(frame, image=resizedImg)
    labelImg.grid(row=1, sticky='W')
    labelImg.image = resizedImg

    # Other closest result
    other_closest_result = create_other_closest_result(frame)
    other_closest_result.grid(row=2, pady=(8, 0))

    return frame

def chooseFolder():
    root = Tk()
    root.directory = fd.askdirectory()
    root.withdraw()
    return root.directory

def create_choose_folder_button(container):
    dir_choose_folder_inactive = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'button_choose_folder_inactive.png'))
    choose_folder_inactive = ImageTk.PhotoImage(Image.open(dir_choose_folder_inactive))
    dir_choose_folder_active = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'button_choose_folder_active.png'))
    choose_folder_active = ImageTk.PhotoImage(Image.open(dir_choose_folder_active))

    def on_enter(event):
        button_choose_folder.config(image=choose_folder_active)
        button_choose_folder.image = choose_folder_active

    def on_leave(enter):
        button_choose_folder.config(image=choose_folder_inactive)
        button_choose_folder.image = choose_folder_inactive

    # Masukkin chooseFolder as command di button ini
    
    button_choose_folder = ttk.Button(container, image=choose_folder_inactive,command=chooseFolder)
    button_choose_folder.image = choose_folder_inactive

    button_choose_folder.bind("<Enter>", on_enter)
    button_choose_folder.bind("<Leave>", on_leave)

    return button_choose_folder

# def chooseFile():

def create_choose_file_button(container):
    dir_choose_file_inactive = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'button_choose_file_inactive.png'))
    choose_file_inactive = ImageTk.PhotoImage(Image.open(dir_choose_file_inactive))
    dir_choose_file_active = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'button_choose_file_active.png'))
    choose_file_active = ImageTk.PhotoImage(Image.open(dir_choose_file_active))

    def on_enter(event):
        button_choose_file.config(image=choose_file_active)
        button_choose_file.image = choose_file_active

    def on_leave(enter):
        button_choose_file.config(image=choose_file_inactive)
        button_choose_file.image = choose_file_inactive

    # Masukkin chooseFile as command di button ini
    button_choose_file = ttk.Button(container, image=choose_file_inactive)
    button_choose_file.image = choose_file_inactive

    button_choose_file.bind("<Enter>", on_enter)
    button_choose_file.bind("<Leave>", on_leave)

    return button_choose_file

# def openCamera():

def create_open_camera_button(container):
    dir_open_camera_inactive = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'button_open_camera_inactive.png'))
    open_camera_inactive = ImageTk.PhotoImage(Image.open(dir_open_camera_inactive))
    dir_open_camera_active = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'button_open_camera_active.png'))
    open_camera_active = ImageTk.PhotoImage(Image.open(dir_open_camera_active))

    def on_enter(event):
        button_open_camera.config(image=open_camera_active)
        button_open_camera.image = open_camera_active

    def on_leave(enter):
        button_open_camera.config(image=open_camera_inactive)
        button_open_camera.image = open_camera_inactive

    # Masukkin openCamera as command di button ini
    button_open_camera = ttk.Button(container, image=open_camera_inactive)
    button_open_camera.image = open_camera_inactive

    button_open_camera.bind("<Enter>", on_enter)
    button_open_camera.bind("<Leave>", on_leave)

    return button_open_camera

# def resultName():

# def countExecutionTime():

def create_info_frame(container):

    frame = ttk.Frame(container)

    # grid layout
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=2)

    # Insert Dataset
    insertDataset = ttk.Label(frame, text="Insert Your Dataset", style='Subheading.TLabel')
    insertDataset.grid(column=0, row=0, columnspan=2, sticky='W')
    # Choose Folder Button
    choose_folder_button = create_choose_folder_button(frame)
    choose_folder_button.grid(column=0, row=1)
    # Folder Name Chosen
    folderName = ttk.Label(frame, text="No file chosen")
    folderName.grid(column=1, row=1)

    # Insert Test Image
    insertTestImage = ttk.Label(frame, text="Insert Your Test Image", style='Subheading.TLabel')
    insertTestImage.grid(column=0, row=2, columnspan=2, sticky='W', pady=(24, 0))
    # Choose File Button
    choose_file_button = create_choose_file_button(frame)
    choose_file_button.grid(column=0, row=3, sticky='W')
    # File Name Chosen
    fileName = ttk.Label(frame, text="No file chosen")
    fileName.grid(column=1, row=3)

    # or divider
    dir_or = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'or_divider.png'))
    img_or_divider = ImageTk.PhotoImage(Image.open(dir_or))
    orDivider = ttk.Label(frame, image=img_or_divider)
    orDivider.grid(column = 0, columnspan=2, row=4)
    orDivider.image = img_or_divider

    # Open Camera Button
    open_camera_button = create_open_camera_button(frame)
    open_camera_button.grid(columnspan=2, row=5, sticky='W')

    # Result
    result = ttk.Label(frame, text="Result", style='Subheading.TLabel')
    result.grid(column=0, row=6, columnspan=2,sticky='W', pady=(24, 0))
    resultName01 = ttk.Label(frame, text="None")
    resultName01.grid(column=0, row=7,columnspan=2,sticky='W')
    resultName02 = ttk.Label(frame, text="None")
    resultName02.grid(column=0, row=8,columnspan=2,sticky='W')
    resultName03 = ttk.Label(frame, text="None")
    resultName03.grid(column=0, row=9,columnspan=2,sticky='W')
    resultName04 = ttk.Label(frame, text="None")
    resultName04.grid(column=0, row=10,columnspan=2,sticky='W')

    # Execution Time
    executionTime = ttk.Label(frame, text="Execution time: 01:00")
    executionTime.grid(column=0, row=11, columnspan=2,sticky='W', pady=(24, 0))

    return frame


def create_main_window():
    root = tk.Tk()
    root.title('recognice - Face Recognition')
    root.minsize(1440, 900)
    root.config(bg = '#FFFFFF')
    dirLogo = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets','logo.ico'))
    root.iconbitmap(dirLogo)

    # background
    dir_background = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'background.png'))
    background = ImageTk.PhotoImage(Image.open(dir_background))
    background_container = ttk.Label(root, image=background)
    background_container.image = background
    background_container.place(rely=1, relx=0.5, anchor='s')

    # Create main frame
    mainFrame = ttk.Frame(root)
    mainFrame.place(relx=.5, rely=.47, anchor="c")

    # Layout on the main frame
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=4)

    # logo
    dir_logo_full = os.path.join(os.path.dirname(os.path.dirname(__file__)), os.path.join('assets', 'logo_full.png'))
    logo_full = ImageTk.PhotoImage(Image.open(dir_logo_full))
    logo_full_container = ttk.Label(root, image=logo_full)
    logo_full_container.image = logo_full
    logo_full_container.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=40)

    # title
    ttk.Label(mainFrame, text="Recognize Face using Eigenface Method", style="Heading1.TLabel").grid(row=0,column=0,columnspan=3, pady=(20, 40))

    # test image
    test_image_frame = create_test_image_frame(mainFrame)
    test_image_frame.grid(column=0, row=2, sticky='N')

    # result
    result_image_frame = create_result_image_frame(mainFrame)
    result_image_frame.grid(column=1, row=2, sticky='N', padx=50)

    # info 
    info_frame = create_info_frame(mainFrame)
    info_frame.grid(column=2,row=2)

    # style
    s = ttk.Style()
    s.theme_use('alt')
    s.configure('.', font=("Futura Bk BT", 18), foreground="#2F2D2D")
    s.configure('Heading1.TLabel', font=("Futura Md BT", 36), foreground='#6C56C2')
    s.configure('Subheading.TLabel', font=("Futura Md BT", 24), foreground='#6C56C2')
    s.configure('Subheading02.TLabel', font=("Futura Md BT", 20), foreground='#2F2D2D')
    s.configure('TButton', background = '#FFFFFF', foreground='#FFFFFF', relief='flat')
    s.map('TButton', relief='flat', background=[('active','#FFFFFF')])
    s.configure('TFrame', background = '#FFFFFF')
    s.configure('TLabel', background = '#FFFFFF')

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()

if __name__ == "__main__":
    create_main_window()
