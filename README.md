🎬 Valentiflix

Valentiflix is a Netflix-themed, cinematic web experience designed as a romantic surprise for Valentine's Week. It features a daily "content unlock" system where specific messages and memories become available only on their respective days (Rose Day, Propose Day, etc.), building anticipation until the season finale on February 14th.

✨ Features

Cinematic UI: Dark mode, hero banners, and horizontal scrolling rows inspired by Netflix.

Time-Locked Content: Episodes (Rose, Propose, Chocolate, etc.) only unlock on specific dates.

Authentication: A login screen to keep your messages private.

Interactive Elements: Secret codes to unlock hidden messages, confetti effects, and a "Season Finale" surprise.

Responsive: Works beautifully on mobile and desktop.

🛠️ Prerequisites

Python 3.7+

Pip (Python Package Manager)

🚀 Quick Start

1. Clone/Download

Download the project files or unzip the valentiflix_project.zip.

2. Create a Virtual Environment (Recommended)

Open your terminal/command prompt in the project folder:

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

You only need Flask and Werkzeug:

pip install Flask werkzeug


4. Run the Application

python app.py


Visit http://127.0.0.1:5000 in your browser.

Default Username: love

Default Password: you

⚙️ Customization (Make it Yours!)

This app is a template. You must customize it to make it special. Open app.py in any text editor (VS Code, Notepad++, etc.).

1. Change Credentials

Find the USERS dictionary near the top of app.py:

USERS = {
    "your_nickname": generate_password_hash("your_password")
}


Note: To generate a new hash, you can use python in terminal: from werkzeug.security import generate_password_hash; print(generate_password_hash("password"))

2. Personalize Content

Edit the CONTENT_DATA list in app.py.

Images: Replace image URLs with direct links to your photos (hosted on Imgur, Dropbox, or placed in a static/images folder).

Messages: Change description and memory_text to your personal memories.

Secrets: Change secret_answer. The user must type this specific word in the episode view to trigger the confetti.

3. Testing Mode (DEV_MODE)

By default, content is locked until the real dates (Feb 7 - Feb 14). To see how everything looks right now:

Change this line in app.py:

DEV_MODE = True  # Set to True to unlock everything


Don't forget to set it back to False before sharing it!

📅 The Schedule

The app is hardcoded for 2026 (per your request), but you can change the year in CONTENT_DATA dates in app.py:

Feb 7: Rose Day

Feb 8: Propose Day

Feb 9: Chocolate Day

Feb 10: Teddy Day

Feb 11: Promise Day

Feb 12: Hug Day

Feb 13: Kiss Day

Feb 14: Valentine's Day (The Finale)

🌐 Deployment

To share this with your partner, you need to host it online.

Option A: PythonAnywhere (Easiest & Free)

Sign up for a free account at PythonAnywhere.

Upload your files via the "Files" tab.

Open a generic Web App, select Flask, and point it to your app.py.

Option B: Render.com

Create a requirements.txt file: pip freeze > requirements.txt.

Push code to GitHub.

Connect GitHub to Render and deploy as a Web Service.

❤️ License

Built with love. Free to use for any romantic endeavor.
