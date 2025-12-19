# 📁 AI Based Directory Management System

An **AI-powered directory management system** built using **Python** that automatically organizes files and folders in real time.
The system uses **Machine Learning**, **file system monitoring**, and a **GUI dashboard** to classify and manage files intelligently.

---

## 🚀 Project Overview

Managing messy folders is a common problem. This project solves it by:

* Automatically classifying files using **Machine Learning**
* Organizing files into predefined folders
* Monitoring directories **in real time**
* Cleaning up empty folders
* Providing a **user-friendly GUI**

This project is developed as part of an **Operating Systems course project**.

---

## 🧠 Key Features

* 🔍 **AI-based file classification** using Naive Bayes
* 📂 **Automatic folder creation** (Documents, Images, Music, etc.)
* 🔄 **Real-time directory monitoring** using Watchdog
* 🧹 **Auto cleanup of empty folders**
* 🖥️ **GUI dashboard** built with Tkinter
* 📝 **Live logging** of all actions
* ⚡ Handles already existing files and newly added files

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI
* **Scikit-learn** – Machine Learning
* **Watchdog** – File system monitoring
* **Pickle** – Model storage
* **OS & Shutil** – File operations
* **Threading** – Background monitoring

---

## 📂 Folder Structure

```
AI_Directory_Manager/
│
├── gui.py           # Main GUI application
├── scanner.py       # Real-time folder monitoring
├── organizer.py     # File organizing logic
├── ml_model.py      # ML model training & prediction
├── model.pkl        # Trained ML model
├── logs.txt         # Action logs
└── README.md        # Project documentation
```

---

## 🧠 How the AI Works

* Uses **Naive Bayes (MultinomialNB)**
* Trained on file names and extensions
* Predicts the correct category:

  * Documents
  * Images
  * Music
  * Code
  * Executables
  * Shortcuts
* Unknown files are placed into the **Others** folder

---

## 🖥️ GUI Dashboard Features

* 📂 Selected Folder display
* 🧠 AI Status (ON / OFF)
* 📊 Number of files organized
* 🕒 Last action performed
* ▶ Start Monitoring button
* 📁 Browse Folder option

---

## ⚙️ Installation & Setup

### 1️⃣ Install Python

Download Python from:
[https://www.python.org/](https://www.python.org/)

### 2️⃣ Install Required Libraries

```bash
pip install scikit-learn watchdog
```

---

## ▶️ How to Run the Project

1. Open terminal in the project folder
2. Run the GUI file:

```bash
python gui.py
```

3. Click **Browse Folder**
4. Select the folder you want to organize
5. Click **Start Monitoring**
6. Files will be organized automatically

---

## 📝 Logging

* All actions are saved in `logs.txt`
* Includes:

  * File movements
  * Skipped files
  * Folder deletions
  * Errors (if any)

---

## 🧪 Example Output

```
resume.pdf → Documents
photo.png → Images
song.mp3 → Music
Deleted folder: certificates
Cleaned parent folder: Downloads
```

---

## 📌 Advantages

* Saves time
* Keeps directories clean
* No manual sorting needed
* Beginner-friendly GUI
* Practical Operating Systems implementation

---

## 🚧 Limitations

* Works mainly based on file names
* Limited predefined categories
* Requires Python to be installed

---

## 🔮 Future Enhancements

* Content-based file classification
* User-defined custom categories
* Web-based interface
* Cloud integration
* Improved AI accuracy

---

## 👨‍🎓 Author

**Name:** Kovid
**Role:** Engineering Student
**Subject:** Operating Systems
**Project Type:** Academic + AI-based

---

## ⭐ Final Note

This project demonstrates the **practical use of AI in Operating Systems** by combining:

* File systems
* Process monitoring
* Machine learning
* GUI programming

---
