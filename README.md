[README.md](https://github.com/user-attachments/files/29211815/README.md)
 🐍 Python CLI & Web Projects

> A collection of 9 Python projects — from beginner CLI tools to a full-stack Flask web application.

**Author:** Sai Srivatsva | **Language:** Python 3.x | **License:** MIT

---

## 📁 Repository Structure

```
python-projects/
├── task1_Simple_Calculator__CLI_.py
├── task2_guessing_game.py
├── task3_todo_list.py
├── task4_password_generator.py
├── task5_file_organizer.py
├── task6_weather_app.py
├── task7_student_management.py
├── task8-webscraper-Sai_srivatsva.py
└── 9_project.py                   # Full-stack Flask web app
```

---

## 📋 Table of Contents

1. [Simple Calculator (CLI)](#task-1-simple-calculator-cli)
2. [Number Guessing Game](#task-2-number-guessing-game)
3. [To-Do List (CLI)](#task-3-to-do-list-cli)
4. [Password Generator](#task-4-password-generator)
5. [Automated File Organizer](#task-5-automated-file-organizer)
6. [Real-Time Weather App](#task-6-real-time-weather-app)
7. [Student Management System](#task-7-student-management-system)
8. [Web Scraper](#task-8-web-scraper)
9. [Full-Stack Task Manager (Flask)](#task-9-full-stack-task-manager-flask)

---

## Task 1: Simple Calculator (CLI)

**Objective:** A command-line calculator for basic arithmetic operations.

**Tech Stack:** Python 3.x · Built-ins only

**Features:**
- Supports addition, subtraction, multiplication, and division
- Division-by-zero guard
- Input validation — rejects non-numeric entries

**How to Run:**
```bash
python task1_Simple_Calculator__CLI_.py
```

---

## Task 2: Number Guessing Game

**Objective:** An interactive CLI game where the user guesses a secret number between 1 and 100.

**Tech Stack:** Python 3.x · `random`

**Features:**
- Random number generation each round
- Higher / lower hints after every guess
- Attempt counter and replay option

**How to Run:**
```bash
python task2_guessing_game.py
```

---

## Task 3: To-Do List (CLI)

**Objective:** A menu-driven command-line to-do manager.

**Tech Stack:** Python 3.x · Built-ins only

**Features:**
- View, add, and delete tasks via a numbered menu
- Input validation on all operations
- Clean formatted list output

**How to Run:**
```bash
python task3_todo_list.py
```

---

## Task 4: Password Generator

**Objective:** Generates cryptographically random passwords with guaranteed character-class diversity.

**Tech Stack:** Python 3.x · `random` · `string`

**Features:**
- Guaranteed inclusion of uppercase, lowercase, digits, and symbols
- Configurable length (minimum 4 characters)
- O(N) time complexity using native C-bound `random.choices()`

**How to Run:**
```bash
python task4_password_generator.py
```

---

## Task 5: Automated File Organizer

**Objective:** Scans a directory and sorts files into categorized subfolders by extension.

**Tech Stack:** Python 3.x · `os` · `shutil`

**Features:**
- Supports 17+ file extensions across Images, Docs, and Videos categories
- Uses `os.scandir()` for O(1) auxiliary memory usage
- Creates destination folders only when needed
- Skips subdirectories — processes files only

**How to Run:**
```bash
python task5_file_organizer.py
# Enter directory path, or press Enter for current directory
```

---

## Task 6: Real-Time Weather App

**Objective:** Fetches live weather data for any city using the wttr.in API.

**Tech Stack:** Python 3.x · `requests`

**Features:**
- Real-time temperature (°C), humidity (%), and condition description
- Uses the free wttr.in JSON endpoint — no API key required
- Handles network errors, invalid city names, and timeouts gracefully

**Install & Run:**
```bash
pip install requests
python task6_weather_app.py
```

---

## Task 7: Student Management System

**Objective:** A persistent CRUD system for managing student records via CLI.

**Tech Stack:** Python 3.x · `json` · `os` · Storage: `students.json`

**Features:**
- Add, update, view, and delete student records
- Persistent storage via a local JSON file
- O(1) dictionary lookups for all record operations
- Duplicate student ID prevention

> ⚠️ **Known Bug:** In the update option (choice `2`), `add_student()` is called instead of `update_student()`. Fix: replace `add_student(s_id, name, grade)` with `update_student(s_id, name, grade)` on that line.

**How to Run:**
```bash
python task7_student_management.py
```

---

## Task 8: Web Scraper

**Objective:** Scrapes product titles and prices from books.toscrape.com into a CSV file.

**Tech Stack:** Python 3.x · `requests` · `BeautifulSoup4` · `csv`

**Features:**
- Targets `article.product_pod` elements for accurate data extraction
- Streams rows directly to CSV — O(1) memory regardless of dataset size
- Uses `requests.Session()` to reuse TCP connections for speed
- Handles missing or changed HTML elements gracefully

**Install & Run:**
```bash
pip install requests beautifulsoup4
python task8-webscraper-Sai_srivatsva.py
# Output: scraped_data.csv (auto-generated)
```

---

## Task 9: Full-Stack Task Manager (Flask)

**Objective:** A fully functional, responsive web application for personal task management with user authentication.

**Tech Stack:** Python 3.x · Flask · SQLite3 · Werkzeug · HTML/CSS

**Features:**
- Secure user registration and login with hashed passwords (`werkzeug.security`)
- Per-user task isolation — SQL queries are bound to the active session's user ID
- Create tasks, toggle completion status, and delete tasks
- Single-file architecture — routing, database init, and UI all in `9_project.py`
- Responsive embedded HTML/CSS template (no external frameworks)

**Install & Run:**
```bash
pip install flask werkzeug
python 9_project.py
# Open your browser: http://127.0.0.1:5000
```

---

## ⚡ Quick Setup (All Dependencies)

```bash
git clone https://github.com/your-username/python-projects.git
cd python-projects
pip install flask werkzeug requests beautifulsoup4
```

Tasks 1–5 use only the Python standard library — no installation needed.

---


*Built with Python 3 · Tasks 1–8 are standalone CLI scripts · Task 9 is a Flask web application*

