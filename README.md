# Student Marks Tracker

A full stack web app to track student marks, calculate averages, and get AI-powered study advice.

## Features
- Add any subject and mark dynamically
- Calculates average percentage
- Pass/fail indicator per subject (pass = 70 and above)
- Saves marks to a file
- AI study advice powered by Claude

## Tech Stack
- Python + Flask (backend)
- HTML, CSS, JavaScript (frontend)
- Anthropic Claude API (AI advice)

## How to Run

1. Install dependencies:
2. 2. Add your Anthropic API key in `app.py`
3. Run the app: py app.py
4. Open your browser and go to:
http://127.0.0.1:5000
## Project Structure
student-marks-tracker/
├── app.py           # Flask backend
├── marks.txt        # Saved marks
├── peak.py          # Original terminal version
└── Templates/
└── index.html   # Frontend
## About
Built from scratch as a learning project to get into NTU.
