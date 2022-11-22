# Tugas Besar 2 IF 2123 Algeo - Eigenfaces for Face Recognition

Recognice is a face recognition application that use Eigen Value to search for the most similar face. You can watch our live demo [_here_](https://www.youtube.com/watch?v=JrZH4j8tW3A).

## Table of Contents

-   [General Info](#general-information)
-   [How to Run](#technologies-used)
-   [Screenshots](#screenshots)
-   [Program Structure](#program-structure)

## General Information

Within recognice you can add your own folder dataset as training images. While the test image can be chosen from your file or taken from webcam. Recognice performs the best with a lot of images per identities. It is better to have your dataset already aligned and crop to their face.

## Team Members

| **NIM**  |       **Nama**        |
| :------: | :-------------------: |
| 13521094 | Angela Livia Arumsari |
| 13521134 |     Rinaldy Adin      |
| 13521139 |   Nathania Callista   |

## How to Run

1. Install fonts needed for application by opening and installing font from `FutuBk.ttf` and `FutuMd.ttf`

2. Install dependencies needed by running this command in root folder

```
$ pip install -r requirements.txt
```

3. Run `main.py` by using this command

```
$ python main.py
```

## Screenshots

![App Interface](https://github.com/liviaarumsari/Algeo02-21094/blob/main/assets/screenshot01.png)
![Error when the input is not an image](https://github.com/liviaarumsari/Algeo02-21094/blob/main/assets/screenshot02.png)
![Error when there is no matching face](https://github.com/liviaarumsari/Algeo02-21094/blob/main/assets/screenshot03.png)
![Succesful recognition](https://github.com/liviaarumsari/Algeo02-21094/blob/main/assets/screenshot04.png)

## Program Structure

```
.
│   .gitignore
│   FutuBk.ttf
│   FutuMd.ttf
│   main.py
│   README.md
│   requirements.txt
│
├───assets
│       background.png
│       button_choose_file_active.png
│       button_choose_file_inactive.png
│       button_choose_folder_active.png
│       button_choose_folder_inactive.png
│       button_open_camera_active.png
│       button_open_camera_inactive.png
│       logo.ico
│       logo_full.png
│       no_image01.png
│       no_image02.png
│       or_divider.png
│
└───src
        gui.py
        my-face.png
        qrMethod.py
        recognition.py
        requirements.txt
        training.py
        utils.py
        webcam.py
        __init__.py
```
