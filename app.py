import anthropic
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

MARKS_FILE = "marks.txt"

def save_marks(marks, average):
    with open(MARKS_FILE, "w") as file:
        file.write(f"Average: {average:.1f}%\n")
        for subject, mark in marks.items():
            file.write(f"{subject}: {mark}\n")

def load_marks():
    if not os.path.exists(MARKS_FILE):
        return None
    with open(MARKS_FILE, "r") as file:
        return file.read()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    marks = data["marks"]
    average = sum(marks.values()) / len(marks)
    results = {}
    for subject, mark in marks.items():
        results[subject] = {
            "mark": mark,
            "status": "Fail" if mark < 70 else "Pass"
        }
    save_marks(marks, average)
    return jsonify({"average": round(average, 1), "results": results})

@app.route("/load", methods=["GET"])
def load():
    content = load_marks()
    if content:
        return jsonify({"content": content})
    return jsonify({"content": "No marks saved yet!"})

@app.route("/advice", methods=["POST"])
def advice():
    data = request.get_json()
    marks = data["marks"]
    average = data["average"]
    marks_text = "\n".join([f"{subject}: {mark}" for subject, mark in marks.items()])
    client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")
    message = client.messages.create(
        model="claude-opus-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"I am a student with these marks:\n{marks_text}\nAverage: {average}%\nGive me short, specific study advice for my weakest subjects."
            }
        ]
    )
    return jsonify({"advice": message.content[0].text})

if __name__ == "__main__":
    app.run(debug=True)