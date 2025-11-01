# 👤 Face Attendance System

A **Python-based Face Recognition Attendance System** that automates attendance marking using real-time face detection and recognition.  
Built using **OpenCV**, **NumPy**, and **Pandas**, it captures faces from a webcam feed, recognizes them, and logs attendance automatically in a CSV file.

---

## 🚀 Features

- 🎥 **Real-time Face Detection** — Detects multiple faces simultaneously using OpenCV.
- 🧠 **Face Recognition** — Recognizes known faces using the LBPH (Local Binary Pattern Histogram) algorithm.
- 🗓️ **Automatic Attendance Logging** — Saves name, date, and time to CSV files automatically.
- 🧾 **Daily Attendance Reports** — Creates a new CSV for every date.
- 💻 **Simple GUI** — Easy-to-use interface for both capturing and recognizing faces.
- ⚡ **Fast & Lightweight** — Works smoothly on most systems with a standard webcam.

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Language** | Python 3.x |
| **Libraries** | OpenCV, NumPy, Pandas |
| **Storage** | CSV Files |
| **Tools / IDE** | VS Code / PyCharm |
| **OS Support** | Windows / Linux |

---

## 📁 Project Structure

faceattendance/
├── image/ # Folder for storing training images
├── 2024-12-11.csv # Attendance records (auto-generated)
├── 2024-12-20.csv
├── 2025-07-20.csv
├── attendance.py # Main script file
├── .gitignore # Ignores CSV, PPT, and image data
└── Introducing-the-Face-Attendance-System.pptx (ignored)

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Shu2003bh/Face-Attendance-System.git
cd Face-Attendance-System
2️⃣ Install Required Libraries
bash
Copy code
pip install opencv-python numpy pandas
3️⃣ Run the Project
bash
Copy code
python attendance.py
4️⃣ Allow Camera Access
Ensure your webcam is working and accessible.
The app will open a live camera window for face recognition.

🧠 How It Works
🧩 Step 1: Capture Faces
The system captures multiple images of each user using the webcam.

Each image is stored in the image/ folder with a unique name or ID.

🧩 Step 2: Train Model
The LBPH (Local Binary Pattern Histogram) algorithm is used to train facial recognition data.

The model saves encodings for all captured faces.

🧩 Step 3: Recognize Faces
When a known face appears on camera, it matches with the stored data.

Displays Name, ID, and Time on the screen in real-time.

🧩 Step 4: Mark Attendance
Recognized users are logged automatically in a CSV file:

css
Copy code
YYYY-MM-DD.csv
Each row includes:
| Name | ID | Date | Time |

📸 Example Output
Name	ID	Date	Time
Shubham Bajpai	101	2025-07-20	10:23:45

✅ Automatically saved in the root folder with that day’s date as the filename.

💡 Tips for Best Accuracy
Capture 20–30 images per user in good lighting.

Keep your face straight and clear during training.

Avoid blurry images.

Ensure the background is plain for better detection.

🔐 Data Privacy
All data (images and CSVs) are stored locally — nothing is uploaded online.

The .gitignore file ensures personal data files like:

CSV attendance logs

Presentation files

Image dataset
are not uploaded to GitHub.

🔮 Future Improvements
🌐 Integrate cloud storage (Firebase/MySQL) for centralized attendance data.

📊 Add a dashboard to visualize daily/weekly reports.

🔊 Add voice feedback on successful recognition.

🧩 Deploy with Flask or Streamlit for a web-based interface.

🧑‍💻 Developer
Shubham Bajpai
📍 Kanpur, India
📧 shubhambajpai592@gmail.com
🔗 LinkedIn | GitHub

⭐ If you found this project helpful, don’t forget to star the repo!




