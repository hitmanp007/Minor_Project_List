# 🐍 Python Mini Projects

A structured collection of **20 beginner-to-intermediate Python mini projects** designed to strengthen programming fundamentals through practical implementation.

This repository is not focused on making huge applications. The goal is to **learn by building small, complete, and understandable projects**.

The projects gradually progress from basic Python syntax and logic to GUI applications, file handling, APIs, object-oriented programming, and small real-world applications.

---

## 🎯 Why This Repository?

When learning programming, it is easy to focus on large projects and frameworks while slowly forgetting the fundamentals.

This repository is designed to solve that problem.

Instead of randomly building projects, the projects are arranged in a structured progression:

```text
Python Basics
      ↓
Conditions & Loops
      ↓
Functions
      ↓
Data Structures
      ↓
File Handling
      ↓
OOP
      ↓
GUI
      ↓
APIs & Real-world Applications
```

Each project should be:

* Small enough to understand
* Complete enough to actually work
* Focused on specific programming concepts
* Beginner-friendly
* Easy to modify and experiment with

---

# 📚 Project Roadmap

## 🟢 Level 1 — Python Fundamentals

### 01. Number Guessing Game

**Concepts:**

* Variables
* `input()`
* `if / elif / else`
* Loops
* `random`

**Goal:**
Create a game where the computer generates a random number and the player tries to guess it.

---

### 02. Calculator

**Concepts:**

* Functions
* Variables
* Operators
* Conditional statements
* Tkinter GUI
* Button events
* GUI layouts

**Goal:**
Create a working calculator with a graphical interface.

**Status:** ✅ Completed

---

### 03. Stone Paper Scissor

**Concepts:**

* `random`
* Dictionaries
* Conditions
* Functions
* Loops
* Game logic
* Tkinter GUI

**Goal:**
Create a best-of-three Stone Paper Scissor game against the computer.

**Status:** ✅ Completed

---

### 04. Banking System

**Concepts:**

* Dictionaries
* Functions
* Conditions
* Tkinter
* Frames
* Login system
* Account management

**Goal:**
Create a simple banking application where users can create an account, log in, deposit money, withdraw money, and check their balance.

**Planned structure:**

```text
Home
 │
 ├── Create Account
 │
 └── Login
       │
       ↓
   Dashboard
       │
       ├── Deposit
       ├── Withdraw
       ├── Balance
       └── Transaction History
```

**Status:** 🚧 In Progress

---

### 05. Quiz Game

**Concepts:**

* Lists
* Dictionaries
* Loops
* Conditions
* Functions
* Score calculation

**Goal:**
Build a console-based quiz where users answer multiple questions and receive a final score.

---

## 🟡 Level 2 — Logic & Data Structures

### 06. Password Generator

**Concepts:**

* Strings
* Lists
* Randomization
* Functions

**Goal:**
Generate random passwords based on user-selected length and character types.

---

### 07. To-Do List

**Concepts:**

* Lists
* Functions
* CRUD operations
* Loops
* Tkinter

**Goal:**
Create a simple GUI-based task manager where users can add, delete, and manage tasks.

---

### 08. Contact Book

**Concepts:**

* Dictionaries
* Lists
* Functions
* Searching
* CRUD operations

**Goal:**
Create an application for storing and searching contacts.

---

### 09. Expense Tracker

**Concepts:**

* Lists
* Dictionaries
* Functions
* File handling
* Basic calculations

**Goal:**
Track expenses and calculate total spending.

---

### 10. Countdown Timer

**Concepts:**

* `time`
* Loops
* Functions
* GUI
* Event handling

**Goal:**
Create a countdown timer that displays remaining time and notifies the user when the timer reaches zero.

---

# 🟠 Level 3 — Files, OOP & Applications

### 11. Library Management System

**Concepts:**

* Classes
* Objects
* Lists
* Functions
* File handling
* OOP

**Goal:**
Manage books, borrowers, issue/return operations, and library records.

---

### 12. Employee Management System

**Concepts:**

* Classes
* Objects
* Dictionaries
* OOP
* CRUD operations

**Goal:**
Create a system for managing employee information.

---

### 13. Mini Akinator

**Concepts:**

* Dictionaries
* Conditions
* Functions
* Decision logic
* User input

**Goal:**
Create a simple guessing game that tries to identify a character based on user answers.

---

### 14. File Organizer

**Concepts:**

* `os`
* `shutil`
* File paths
* Loops
* Conditions

**Goal:**
Automatically organize files into folders based on their extensions.

Example:

```text
Downloads/
│
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Others/
```

---

### 15. Student Management System

**Concepts:**

* OOP
* Lists
* Dictionaries
* File handling
* Searching
* Updating records

**Goal:**
Create a system for storing and managing student information.

---

# 🔵 Level 4 — Data & Internet

### 16. CSV Data Analyzer

**Concepts:**

* CSV
* Pandas
* DataFrames
* Data cleaning
* Basic statistics

**Goal:**
Read a CSV file and generate useful information from the dataset.

---

### 17. Weather Application

**Concepts:**

* APIs
* `requests`
* JSON
* Functions
* Error handling

**Goal:**
Fetch real-time weather information using a weather API.

---

### 18. Web Scraper

**Concepts:**

* HTTP requests
* BeautifulSoup
* HTML parsing
* Data extraction
* File handling

**Goal:**
Extract useful information from a website and store the results.

---

### 19. News Application

**Concepts:**

* APIs
* JSON
* `requests`
* Functions
* Error handling

**Goal:**
Fetch and display current news using a public API.

---

### 20. Mini E-Commerce System

**Concepts:**

* OOP
* Dictionaries
* Lists
* Functions
* File handling
* Shopping cart logic
* User management

**Goal:**
Build a small e-commerce application with products, cart management, and order processing.

---

# 📊 Learning Progression

| Level                | Projects | Main Focus                           |
| -------------------- | -------- | ------------------------------------ |
| 🟢 Beginner          | 01–05    | Python fundamentals                  |
| 🟡 Basic             | 06–10    | Logic & data structures              |
| 🟠 Intermediate      | 11–15    | OOP & applications                   |
| 🔵 Advanced Beginner | 16–20    | Data, APIs & real-world applications |

---

# 📁 Repository Structure

```text
PYTHON_PROJECTS/
│
├── 01_Number_Guessing_Game/
│   └── main.py
│
├── 02_Calculator/
│   └── main.py
│
├── 03_Stone_Paper_Scissor/
│   └── main.py
│
├── 04_Banking_System/
│   └── main.py
│
├── 05_Quiz_Game/
│   └── main.py
│
├── ...
│
├── 20_Mini_E-Commerce/
│   └── main.py
│
└── README.md
```

Some projects may contain additional files when required:

```text
project/
│
├── main.py
├── data.json
├── background.jpg
└── README.md
```

---

# 🛠️ Technologies Used

The projects primarily use Python and its standard ecosystem.

Depending on the project, technologies may include:

* Python
* Tkinter
* Pandas
* Requests
* BeautifulSoup
* JSON
* CSV
* SQLite

The goal is to introduce libraries **only when they are useful for the concept being practiced**.

---

# 🚀 How to Run a Project

Clone the repository:

```bash
git clone <your-repository-url>
```

Go to the Python projects directory:

```bash
cd PYTHON_PROJECTS
```

Enter any project:

```bash
cd 02_Calculator
```

Run it:

```bash
python main.py
```

For GUI projects, the application window should open automatically.

---

# 🧠 Learning Philosophy

These projects follow one simple rule:

> **Understand → Build → Break → Debug → Improve**

Do not simply copy the code.

For every project:

1. Understand the problem.
2. Plan the solution.
3. Write the code yourself.
4. Run the program.
5. Debug the errors.
6. Improve the project.
7. Document what you learned.
8. Move to the next project.

Getting errors is part of the learning process.

---

# 🎓 For Beginners

If you are a first-year student learning Python, you do **not** need to understand every project immediately.

Start from:

```text
01 → 02 → 03 → 04 → ...
```

Don't jump directly to the advanced projects.

For each project, try to answer:

```text
What problem am I solving?
What Python concepts am I using?
Why does this code work?
What happens if I change it?
Can I add one more feature?
```

If you can answer these questions, you are learning rather than simply completing projects.

---

# 💡 Project Challenge

After completing each project, try adding **one feature of your own**.

For example:

### Calculator

```text
Basic calculator
        ↓
Add percentage
        ↓
Add calculation history
```

### Stone Paper Scissor

```text
Single round
        ↓
Best of 3
        ↓
Scoreboard
        ↓
Play again
```

### Banking System

```text
Create account
        ↓
Login
        ↓
Deposit / Withdraw
        ↓
Transaction history
        ↓
Save data
```

This is where the real learning begins.

---

# 📈 Future Improvements

The projects may later be upgraded using:

* JSON data storage
* SQLite databases
* Better GUI design
* Object-oriented architecture
* APIs
* Web interfaces
* Unit testing
* Error handling
* Authentication
* Deployment

However, the original beginner implementation will remain simple so that students can understand the fundamentals.

---

# 🤝 Contributions

This repository is primarily a learning project, but suggestions and improvements are welcome.

If you find a bug or have an idea for improving a project:

1. Open an issue.
2. Explain the problem or suggestion.
3. If possible, submit a pull request.
4. Keep contributions beginner-friendly and understandable.

---

# 🌱 Project Goal

The ultimate goal of this repository is not to collect 20 projects.

The goal is to build **20 programming experiences**.

By the end, you should be more comfortable with:

```text
Python
  ↓
Problem Solving
  ↓
Programming Logic
  ↓
Data Structures
  ↓
Functions
  ↓
OOP
  ↓
GUI
  ↓
Files & Data
  ↓
APIs
  ↓
Real-world Applications
```

---

## ⭐ Progress

* [x] 01 — Number Guessing Game
* [x] 02 — Calculator
* [x] 03 — Stone Paper Scissor
* [x] 04 — Banking System
* [ ] 05 — Quiz Game
* [ ] 06 — Password Generator
* [x] 07 — To-Do List
* [ ] 08 — Contact Book
* [ ] 09 — Expense Tracker
* [ ] 10 — Countdown Timer
* [ ] 11 — Library Management System
* [ ] 12 — Employee Management System
* [ ] 13 — Mini Akinator
* [ ] 14 — File Organizer
* [ ] 15 — Student Management System
* [ ] 16 — CSV Data Analyzer
* [ ] 17 — Weather Application
* [ ] 18 — Web Scraper
* [ ] 19 — News Application
* [ ] 20 — Mini E-Commerce System

---

## 👨‍💻 Author

**Pranav Sahu**

A structured collection of small Python projects created to strengthen programming fundamentals through practice and experimentation.

---

⭐ If this repository helps you learn Python, consider giving it a star and sharing it with another beginner.

