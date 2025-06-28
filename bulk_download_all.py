import os
import subprocess

classes = list(range(1, 13))
mediums = ["English", "Hindi"]
subjects = [
    "Mathematics", "Science", "English", "Hindi", "Sanskrit", "Social Science",
    "Physics", "Chemistry", "Biology", "Economics", "History", "Geography",
    "Political Science", "Accountancy", "Business Studies", "Psychology",
    "Sociology", "Computer Science", "Environmental Studies"
]

os.makedirs("books", exist_ok=True)

for cls in classes:
    for medium in mediums:
        for subject in subjects:
            folder = f"books/Class_{cls}"
            os.makedirs(folder, exist_ok=True)
            cmd = f"python ncertdownloader.py --class {cls} --subject \"{subject}\" --medium {medium}"
            print(f"Running: {cmd}")
            try:
                subprocess.run(cmd, shell=True, check=True)
            except subprocess.CalledProcessError:
                print(f"❌ Skipped: Class {cls} - {subject} ({medium})")

