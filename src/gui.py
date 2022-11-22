import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import *
from PIL import ImageTk, Image
import os
import training, recognition
from webcam import *
import threading, utils


class programState:
    def __init__(self):
        self.trainingFolderPath = ""
        self.newImageFilePath = ""
        self.trainingImageMatrices = None
        self.trainingImageMean = None
        self.eigenFaces = None
        self.mostSimilarFacesPaths = []
        self.traningImagePaths = []
        self.sortedTraningImagePaths = []
        self.programInteractable = True

        self.testImageLabel = None
        self.resultImageLabel0 = None
        self.resultImageLabel1 = None
        self.resultImageLabel2 = None
        self.resultImageLabel3 = None

        self.execTime = 0
        self.timerLabel = None
        self.tkRoot = None

        self.similarity = 0
        self.similarityLabel = None
        self.eucDist = 0
        self.eucDistLabel = None
        self.projDist = 0
        # ========== THRESHOLD ==============
        self.projThreshold = 0
        self.similarityThreshold = 115

        self.errorMsgLabel = None

        self.folderNameLabel = None
        self.fileNameLabel = None

    def trainImages(self):
        self.errorMsgLabel.configure(text="Program is running")
        self.programInteractable = False
        (
            self.eigenFaces,
            self.trainingImageMean,
            self.trainingImageMatrices,
        ) = training.trainFromFolder(self.trainingFolderPath)
        self.programInteractable = True
        self.errorMsgLabel.configure(text="")

        self.traningImagePaths = []
        for filename in os.listdir(self.trainingFolderPath):
            f = os.path.join(self.trainingFolderPath, filename)
            if os.path.isfile(f):
                self.traningImagePaths.append(f)

    def runExecTimer(self):
        if self.eigenFaces == None:
            ss = self.execTime % 60
            mm = self.execTime // 60
            self.timerLabel.configure(text=f"Execution time: {mm:02d}:{ss:02d}")
            self.execTime += 1
            self.tkRoot.after(1000, self.runExecTimer)

    def startTraining(self):
        self.eigenFaces = None
        self.execTime = 0
        self.runExecTimer()

        thread = threading.Thread(target=self.trainImages)

        thread.start()

    def recognizeMostSimilar(self):
        if self.trainingFolderPath != "" or self.newImageFilePath != "":
            unkownImageVector = training.normalizeImage(self.newImageFilePath)
            (
                self.sortedTraningImagePaths,
                self.projDist,
                self.similarity,
                self.eucDist,
            ) = recognition.getSimilarImagesPathSorted(
                unkownImageVector,
                self.trainingImageMean,
                self.trainingImageMatrices,
                self.traningImagePaths,
                self.eigenFaces,
                self.similarityThreshold,
            )

            self.projThreshold = (
                len(self.sortedTraningImagePaths) * 4
                + (len(self.sortedTraningImagePaths) * 100) * 100
            )

            if (
                self.eucDist <= self.similarityThreshold
                and self.projDist <= self.projThreshold
            ):
                imgTest = ImageTk.PhotoImage(
                    Image.open(self.newImageFilePath).resize(
                        (360, 360), Image.Resampling.LANCZOS
                    )
                )
                self.testImageLabel.configure(image=imgTest)
                self.testImageLabel.image = imgTest

                img0 = ImageTk.PhotoImage(
                    Image.open(self.sortedTraningImagePaths[0]).resize(
                        (360, 360), Image.Resampling.LANCZOS
                    )
                )
                self.resultImageLabel0.configure(image=img0)
                self.resultImageLabel0.image = img0

                img1 = ImageTk.PhotoImage(
                    Image.open(self.sortedTraningImagePaths[1]).resize(
                        (120, 120), Image.Resampling.LANCZOS
                    )
                )
                self.resultImageLabel1.configure(image=img1)
                self.resultImageLabel1.image = img1

                img2 = ImageTk.PhotoImage(
                    Image.open(self.sortedTraningImagePaths[2]).resize(
                        (120, 120), Image.Resampling.LANCZOS
                    )
                )
                self.resultImageLabel2.configure(image=img2)
                self.resultImageLabel2.image = img2

                img3 = ImageTk.PhotoImage(
                    Image.open(self.sortedTraningImagePaths[3]).resize(
                        (120, 120), Image.Resampling.LANCZOS
                    )
                )
                self.resultImageLabel3.configure(image=img3)
                self.resultImageLabel3.image = img3

                self.similarityLabel.configure(
                    text=f"Similarity: {self.similarity * 100:.2f}%"
                )
                self.eucDistLabel.configure(
                    text=f"Euclidean Distance: {self.eucDist:.2f}"
                )
            elif self.projDist > self.projThreshold:
                imgTest = ImageTk.PhotoImage(
                    Image.open(self.newImageFilePath).resize(
                        (360, 360), Image.Resampling.LANCZOS
                    )
                )
                self.testImageLabel.configure(image=imgTest)
                self.testImageLabel.image = imgTest

                self.errorMsgLabel.configure(text="Image not recognized as a face")

                self.sortedTraningImagePaths = []
                self.similarity = 0
                self.eucDist = 0
                self.projDist = 0

                self.resetResults()
            else:
                imgTest = ImageTk.PhotoImage(
                    Image.open(self.newImageFilePath).resize(
                        (360, 360), Image.Resampling.LANCZOS
                    )
                )
                self.testImageLabel.configure(image=imgTest)
                self.testImageLabel.image = imgTest

                self.errorMsgLabel.configure(text="Face not found in training images")

                self.sortedTraningImagePaths = []
                self.similarity = 0
                self.eucDist = 0
                self.projDist = 0

                self.resetResults()

        else:
            print("please choose folder")

    def resetImages(self):
        # File dan folder dari test image
        file = "no_image01.png"
        folder = "assets"
        # Open dan show image
        imagepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
        )

        imgTest = ImageTk.PhotoImage(
            Image.open(imagepath).resize((360, 360), Image.Resampling.LANCZOS)
        )
        self.testImageLabel.configure(image=imgTest)
        self.testImageLabel.image = imgTest

        img0 = ImageTk.PhotoImage(
            Image.open(imagepath).resize((360, 360), Image.Resampling.LANCZOS)
        )
        self.resultImageLabel0.configure(image=img0)
        self.resultImageLabel0.image = img0

        file = "no_image02.png"
        folder = "assets"
        # Open dan show image
        imagepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
        )

        img1 = ImageTk.PhotoImage(
            Image.open(imagepath).resize((120, 120), Image.Resampling.LANCZOS)
        )
        self.resultImageLabel1.configure(image=img1)
        self.resultImageLabel1.image = img1

        img2 = ImageTk.PhotoImage(
            Image.open(imagepath).resize((120, 120), Image.Resampling.LANCZOS)
        )
        self.resultImageLabel2.configure(image=img2)
        self.resultImageLabel2.image = img2

        img3 = ImageTk.PhotoImage(
            Image.open(imagepath).resize((120, 120), Image.Resampling.LANCZOS)
        )
        self.resultImageLabel3.configure(image=img3)
        self.resultImageLabel3.image = img3

    def resetResults(self):
        self.similarityLabel.configure(text="Similarity: ")
        self.eucDistLabel.configure(text="Euclidean Distance: ")

    def resetInfoFrame(self):
        self.errorMsgLabel.configure(text="")
        self.folderNameLabel.configure(text="No folder chosen")
        self.fileNameLabel.configure(text="No file chosen")
        self.timerLabel.configure(text="Execution time: 00:00")
        self.resetResults()


isCameraOpened = False


def create_test_image_frame(container, state: programState):

    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(frame, text="Test Image", style="Subheading02.TLabel")
    labelTestImage.grid(row=0, sticky="W")

    # File dan folder dari test image
    file = "no_image01.png"
    folder = "assets"
    # Open dan show image
    dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
    )
    img = Image.open(dir).resize((360, 360), Image.Resampling.LANCZOS)
    resizedImg = ImageTk.PhotoImage(img)
    labelImg = ttk.Label(frame, image=resizedImg)
    labelImg.grid(row=1)
    labelImg.image = resizedImg
    state.testImageLabel = labelImg

    return frame


def create_other_closest_result(container, state):
    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(
        frame, text="Other Closest Results", style="Subheading02.TLabel"
    )
    labelTestImage.grid(row=0, sticky="W", columnspan=3)

    # File dan folder closest result 1
    file = "no_image02.png"
    folder = "assets"
    # Open dan show image closest result 1
    dir01 = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
    )
    img01 = ImageTk.PhotoImage(Image.open(dir01))
    labelImg = ttk.Label(frame, image=img01)
    labelImg.grid(row=1, column=0, sticky="W")
    labelImg.image = img01
    state.resultImageLabel1 = labelImg

    # File dan folder closest result 2
    file = "no_image02.png"
    folder = "assets"
    # Open dan show image closest result 1
    dir02 = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
    )
    img02 = ImageTk.PhotoImage(Image.open(dir02))
    labelImg = ttk.Label(frame, image=img02)
    labelImg.grid(row=1, column=1)
    labelImg.image = img02
    state.resultImageLabel2 = labelImg

    # File dan folder closest result 3
    file = "no_image02.png"
    folder = "assets"
    # Open dan show image closest result 1
    dir03 = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
    )
    img03 = ImageTk.PhotoImage(Image.open(dir03))
    labelImg = ttk.Label(frame, image=img03)
    labelImg.grid(row=1, column=2)
    labelImg.image = img03
    state.resultImageLabel3 = labelImg

    return frame


def create_result_image_frame(container, state):

    frame = ttk.Frame(container)

    labelTestImage = ttk.Label(
        frame, text="Closest Result", style="Subheading02.TLabel"
    )
    labelTestImage.grid(row=0, sticky="W")

    # File dan folder result image
    file = "no_image01.png"
    folder = "assets"
    # Open dan show image
    dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.path.join(folder, file)
    )
    img = Image.open(dir).resize((360, 360), Image.Resampling.LANCZOS)
    resizedImg = ImageTk.PhotoImage(img)
    labelImg = ttk.Label(frame, image=resizedImg)
    labelImg.grid(row=1, sticky="W")
    labelImg.image = resizedImg
    state.resultImageLabel0 = labelImg

    # Other closest result
    other_closest_result = create_other_closest_result(frame, state)
    other_closest_result.grid(row=2, pady=(8, 0))

    return frame


def chooseTrainingFolder(state: programState):
    if state.programInteractable:
        root = Tk()
        root.directory = fd.askdirectory()
        root.withdraw()

        if root.directory == "":
            return

        state.newImageFilePath = ""
        state.trainingFolderPath = ""
        state.execTime = 0
        state.resetInfoFrame()
        state.resetImages()

        if utils.trainingFolderValid(root.directory):
            state.trainingFolderPath = root.directory
            state.folderNameLabel.configure(text=os.path.basename(root.directory))
            state.errorMsgLabel.configure(text="")
            state.startTraining()
        else:
            state.errorMsgLabel.configure(text="Folder must only contain images")


def create_choose_folder_button(container, state):
    dir_choose_folder_inactive = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "button_choose_folder_inactive.png"),
    )
    choose_folder_inactive = ImageTk.PhotoImage(Image.open(dir_choose_folder_inactive))
    dir_choose_folder_active = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "button_choose_folder_active.png"),
    )
    choose_folder_active = ImageTk.PhotoImage(Image.open(dir_choose_folder_active))

    def on_enter(event):
        button_choose_folder.config(image=choose_folder_active)
        button_choose_folder.image = choose_folder_active

    def on_leave(enter):
        button_choose_folder.config(image=choose_folder_inactive)
        button_choose_folder.image = choose_folder_inactive

    # Masukkin chooseFolder as command di button ini

    button_choose_folder = ttk.Button(
        container,
        image=choose_folder_inactive,
        command=lambda: chooseTrainingFolder(state),
    )
    button_choose_folder.image = choose_folder_inactive

    button_choose_folder.bind("<Enter>", on_enter)
    button_choose_folder.bind("<Leave>", on_leave)

    return button_choose_folder


def chooseImageFile(state: programState):
    if state.trainingFolderPath == "":
        state.errorMsgLabel.configure(text="Choose dataset first")
        return
    if state.programInteractable:
        root = Tk()
        state.newImageFilePath = fd.askopenfilename(
            title="Choose a file",
            filetypes=[
                ("image files", ".png"),
                ("image files", ".jpg"),
                ("image files", ".jpeg"),
            ],
        )
        root.withdraw()

        if state.newImageFilePath == "":
            return

        state.fileNameLabel.configure(text="No file chosen")
        state.resetImages()
        state.resetResults()

        if utils.isImageFile(state.newImageFilePath):
            state.errorMsgLabel.configure(text="")
            state.fileNameLabel.configure(text=os.path.basename(state.newImageFilePath))
            state.recognizeMostSimilar()
        else:
            state.newImageFilePath = ""
            state.errorMsgLabel.configure(text="Image file invalid")


def create_choose_file_button(container, state):
    dir_choose_file_inactive = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "button_choose_file_inactive.png"),
    )
    choose_file_inactive = ImageTk.PhotoImage(Image.open(dir_choose_file_inactive))
    dir_choose_file_active = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "button_choose_file_active.png"),
    )
    choose_file_active = ImageTk.PhotoImage(Image.open(dir_choose_file_active))

    def on_enter(event):
        button_choose_file.config(image=choose_file_active)
        button_choose_file.image = choose_file_active

    def on_leave(enter):
        button_choose_file.config(image=choose_file_inactive)
        button_choose_file.image = choose_file_inactive

    # Masukkin chooseFile as command di button ini
    button_choose_file = ttk.Button(
        container, image=choose_file_inactive, command=lambda: chooseImageFile(state)
    )
    button_choose_file.image = choose_file_inactive

    button_choose_file.bind("<Enter>", on_enter)
    button_choose_file.bind("<Leave>", on_leave)

    return button_choose_file


def openCamera(state: programState):
    if state.trainingFolderPath == "":
        state.errorMsgLabel.configure(text="Choose dataset first")
        return
    if state.programInteractable:
        result_path = os.path.join(os.path.dirname(__file__), "my-face.png")

        if os.path.exists(result_path):
            os.remove(result_path)

        state.programInteractable = False
        openWebcam()
        state.programInteractable = True

        state.errorMsgLabel.configure(text="")
        state.newImageFilePath = ""

        if os.path.exists(result_path):
            state.newImageFilePath = result_path
            state.recognizeMostSimilar()
        else:
            state.errorMsgLabel.configure(text="Webcam was not able to find face")


def create_open_camera_button(container, state):
    dir_open_camera_inactive = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "button_open_camera_inactive.png"),
    )
    open_camera_inactive = ImageTk.PhotoImage(Image.open(dir_open_camera_inactive))
    dir_open_camera_active = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "button_open_camera_active.png"),
    )
    open_camera_active = ImageTk.PhotoImage(Image.open(dir_open_camera_active))

    def on_enter(event):
        button_open_camera.config(image=open_camera_active)
        button_open_camera.image = open_camera_active

    def on_leave(enter):
        button_open_camera.config(image=open_camera_inactive)
        button_open_camera.image = open_camera_inactive

    # Masukkin openCamera as command di button ini
    button_open_camera = ttk.Button(
        container, image=open_camera_inactive, command=lambda: openCamera(state)
    )
    button_open_camera.image = open_camera_inactive

    button_open_camera.bind("<Enter>", on_enter)
    button_open_camera.bind("<Leave>", on_leave)

    return button_open_camera


def create_info_frame(container, state: programState):

    frame = ttk.Frame(container)

    # grid layout
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=2)

    # Insert Dataset
    insertDataset = ttk.Label(
        frame, text="Insert Your Dataset", style="Subheading.TLabel"
    )
    insertDataset.grid(column=0, row=0, columnspan=2, sticky="W")
    # Choose Folder Button
    choose_folder_button = create_choose_folder_button(frame, state)
    choose_folder_button.grid(column=0, row=1)
    # Folder Name Chosen
    folderName = ttk.Label(frame, text="No folder chosen")
    folderName.grid(column=1, row=1, sticky="W")
    state.folderNameLabel = folderName

    # Insert Test Image
    insertTestImage = ttk.Label(
        frame, text="Insert Your Test Image", style="Subheading.TLabel"
    )
    insertTestImage.grid(column=0, row=2, columnspan=2, sticky="W", pady=(24, 0))
    # Choose File Button
    choose_file_button = create_choose_file_button(frame, state)
    choose_file_button.grid(column=0, row=3, sticky="W")
    # File Name Chosen
    fileName = ttk.Label(frame, text="No file chosen")
    fileName.grid(column=1, row=3, sticky="W")
    state.fileNameLabel = fileName

    # or divider
    dir_or = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "or_divider.png"),
    )
    img_or_divider = ImageTk.PhotoImage(Image.open(dir_or))
    orDivider = ttk.Label(frame, image=img_or_divider)
    orDivider.grid(column=0, columnspan=2, row=4)
    orDivider.image = img_or_divider

    # Open Camera Button
    open_camera_button = create_open_camera_button(frame, state)
    open_camera_button.grid(columnspan=2, row=5, sticky="W")

    # Result
    result = ttk.Label(frame, text="Result", style="Subheading.TLabel")
    result.grid(column=0, row=6, columnspan=2, sticky="W", pady=(24, 0))
    resultSimilarty = ttk.Label(frame, text="Similarity: ")
    resultSimilarty.grid(column=0, row=7, columnspan=2, sticky="W")
    resultDistance = ttk.Label(frame, text="Euclidean Distance: ")
    resultDistance.grid(column=0, row=8, columnspan=2, sticky="W")
    state.similarityLabel = resultSimilarty
    state.eucDistLabel = resultDistance

    # Execution Time
    executionTime = ttk.Label(frame, text="Execution time: 00:00")
    executionTime.grid(column=0, row=9, columnspan=2, sticky="W", pady=(24, 0))
    state.timerLabel = executionTime

    # Error message
    errorMsg = ttk.Label(frame, text="", style="Error.TLabel")
    errorMsg.grid(column=0, row=10, columnspan=2, sticky="W", pady=(24, 0))
    state.errorMsgLabel = errorMsg

    return frame


def quit_root(root):
    root.quit()
    root.destroy()


def create_main_window(state: programState):
    root = tk.Tk()
    root.title("recognice - Face Recognition")
    root.minsize(1440, 900)
    root.config(bg="#FFFFFF")
    dirLogo = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.path.join("assets", "logo.ico")
    )
    root.iconbitmap(dirLogo)
    root.protocol("WM_DELETE_WINDOW", lambda: quit_root(root))
    state.tkRoot = root

    # background
    dir_background = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "background.png"),
    )
    background = ImageTk.PhotoImage(Image.open(dir_background))
    background_container = ttk.Label(root, image=background)
    background_container.image = background
    background_container.place(rely=1, relx=0.5, anchor="s")

    # Create main frame
    mainFrame = ttk.Frame(root)
    mainFrame.place(relx=0.5, rely=0.47, anchor="c")

    # Layout on the main frame
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=4)

    # logo
    dir_logo_full = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.path.join("assets", "logo_full.png"),
    )
    logo_full = ImageTk.PhotoImage(Image.open(dir_logo_full))
    logo_full_container = ttk.Label(root, image=logo_full)
    logo_full_container.image = logo_full
    logo_full_container.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=40)

    # title
    ttk.Label(
        mainFrame, text="Recognize Face using Eigenface Method", style="Heading1.TLabel"
    ).grid(row=0, column=0, columnspan=3, pady=(20, 40))

    # test image
    test_image_frame = create_test_image_frame(mainFrame, state)
    test_image_frame.grid(column=0, row=2, sticky="N")

    # result
    result_image_frame = create_result_image_frame(mainFrame, state)
    result_image_frame.grid(column=1, row=2, sticky="N", padx=50)

    # info
    info_frame = create_info_frame(mainFrame, state)
    info_frame.grid(column=2, row=2)

    # style
    s = ttk.Style()
    s.theme_use("alt")
    s.configure(".", font=("Futura Bk BT", 18), foreground="#2F2D2D")
    s.configure("Heading1.TLabel", font=("Futura Md BT", 36), foreground="#6C56C2")
    s.configure("Subheading.TLabel", font=("Futura Md BT", 24), foreground="#6C56C2")
    s.configure("Error.TLabel", font=("Futura Md BT", 20), foreground="#eb4034")
    s.configure("Subheading02.TLabel", font=("Futura Md BT", 20), foreground="#2F2D2D")
    s.configure("TButton", background="#FFFFFF", foreground="#FFFFFF", relief="flat")
    s.map("TButton", relief="flat", background=[("active", "#FFFFFF")])
    s.configure("TFrame", background="#FFFFFF")
    s.configure("TLabel", background="#FFFFFF")

    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()


def initGUI():
    state = programState()
    create_main_window(state)
