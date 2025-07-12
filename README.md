# 🤖 Automated Job Application Bot for Naukri.com

This is a Django + Playwright-powered automation tool that auto-applies to jobs on [Naukri.com](https://naukri.com) based on your search criteria.  
It’s designed to mimic human behavior while navigating the job listings and applying with minimal manual effort.

---

## 🚀 Features

- 🔍 **Search & Apply** to jobs automatically using your job title and location
- 🔹 Supports multiple application flows:
  - **Direct Apply** — Clicks “Apply” on jobs that allow instant applications
  - **I’m Interested** — Handles soft apply flows with one click
  - **Apply on Company Site** — Skips and opens external job postings for manual action
- 🧠 Smartly detects and skips complex applications or captchas

---

## 🛠️ Tech Stack

- 🐍 Python 3
- 🧪 Playwright (Browser Automation)
- 🌐 Django (Web interface for triggering the bot)

---

## 💻 How to Run This Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/murtuza2905ali/naukri-autoapply-pilot.git
cd naukri-autoapply-pilot
2️⃣ Set Up Virtual Environment
bash

python -m venv venv
venv\Scripts\activate    # On Windows
3️⃣ Install Requirements
bash

pip install django playwright pandas openpyxl

4️⃣ Install Playwright Browsers
bash

playwright install
5️⃣ Run the Django Server
bash

cd jobapply_project
python manage.py runserver
Now open your browser and go to:
📍 http://127.0.0.1:8000/

6️⃣ Enter Login Credentials
In the web interface:

Type your email and password used for Naukri.com

Click the “Start Applying” button

🧠 Your credentials will be passed securely to the Playwright bot (no storage unless coded).

📸 How It Works
Once triggered:

Opens Chrome browser in controlled mode (CDP)

Logs into your Naukri profile using the given credentials

Searches for jobs based on your title & location

Applies automatically using matching application paths

Skips complicated or external applications gracefully

📂 Folder Structure
bash

naukri-autoapply-pilot/
├── jobapply_project/        # Django Project Code
│   ├── manage.py
│   ├── templates/
│   └── test_click_job.py    # Main Playwright automation script
├── requirements.txt
└── README.md
📌 Note
For first-time login, manual CAPTCHA solving may be required.

The bot does not store your credentials unless explicitly added.

External job sites (Apply on Company Site) are skipped for safety.

🙋‍♂️ Author
Murtuza Ali
🔗 GitHub
📬 DM for questions or collaboration
