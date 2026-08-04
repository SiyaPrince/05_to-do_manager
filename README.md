# ✅ To-Do List Manager

A modular command-line To-Do List Manager built with Python that enables users to create, organize, update, complete, search, and delete tasks through an intuitive menu-driven interface.

The project demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations, task lifecycle management, modular software architecture, reusable validation components, and clean software engineering practices.

---

# 📌 Project Overview

The To-Do List Manager is designed to help users organize and manage tasks during a single application session.

Each task is represented as a structured data object containing descriptive information, priority, due date, and completion status. The application manages these tasks using an in-memory collection while providing a complete set of CRUD operations.

Unlike simpler task trackers, this project introduces the concept of an entity lifecycle, allowing tasks to transition between different states as work progresses.

---

# ✨ Features

* Create new tasks
* View all tasks
* Search tasks by keyword
* Update existing tasks
* Mark tasks as completed
* Delete tasks
* Display detailed task information
* Numbered task selection
* Input validation
* Menu-driven command-line interface
* Modular project structure
* Reusable validation functions

---

# 🛠 Technologies Used

* Python 3
* Python Standard Library

No external libraries are required.

---

# 📂 Project Structure

```text
To-Do-List-Manager/
│
├── main.py
│
├── core_operations/
│   ├── add_task.py
│   ├── complete_task.py
│   ├── delete_task.py
│   ├── search_task.py
│   ├── update_task.py
│   └── view_tasks.py
│
├── support_operations/
│   ├── display_task_details.py
│   ├── validate_title.py
│   ├── validate_description.py
│   ├── validate_due_date.py
│   ├── validate_priority.py
│   ├── display_menu.py
│   └── display_welcome.py
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📋 Task Model

Each task is represented as a dictionary.

```python
task = {
    "title": "Write README",
    "description": "Document the To-Do List project",
    "due_date": "2026-08-05",
    "priority": "High",
    "status": "Pending"
}
```

All tasks are stored inside a collection.

```python
tasks = [
    {
        "title": "Write README",
        "description": "Document the project",
        "due_date": "2026-08-05",
        "priority": "High",
        "status": "Pending"
    }
]
```

This data model allows the application to efficiently perform searching, updating, deletion, and status management operations.

---

# ⚙️ Application Workflow

```text
Start Application
        │
        ▼
Display Welcome Screen
        │
        ▼
Display Menu
        │
        ▼
Select Operation
        │
        ├── Add Task
        ├── View Tasks
        ├── Search Tasks
        ├── Update Task
        ├── Mark Task Complete
        ├── Delete Task
        └── Exit
```

Each menu option delegates work to its own dedicated function, improving maintainability and readability.

---

# 🧩 CRUD Operations

## Create

Users can create tasks by providing:

* Title
* Description
* Due Date
* Priority

Each new task is automatically assigned an initial status of **Pending**.

---

## Read

The application supports:

* Viewing all tasks
* Searching by keyword

Task information is displayed using a reusable formatting function to ensure consistent presentation throughout the application.

---

## Update

Users can modify existing tasks.

Fields can be updated individually while leaving unchanged values intact.

---

## Complete

Tasks can be marked as completed without modifying any other task information.

This demonstrates state transitions within the task lifecycle.

---

## Delete

Tasks can be permanently removed after selecting the desired task from the numbered task list.

---

# 🔄 Task Lifecycle

Unlike previous projects, tasks change state over time.

```text
Pending
    │
    ▼
Completed
```

Managing this lifecycle introduces concepts commonly found in project management software and workflow systems.

---

# ✅ Input Validation

The application validates user input before modifying task data.

Validation includes:

* Required task titles
* Optional descriptions
* Due date formatting
* Priority validation
* Invalid menu selections
* Invalid task selections
* Empty collections
* Empty search terms

These validation steps help preserve data integrity throughout the application.

---

# 🏗 Software Design

The application follows a modular architecture where each function performs a single responsibility.

### Core Operations

Responsible for business logic.

* Add Task
* View Tasks
* Search Tasks
* Update Task
* Complete Task
* Delete Task

### Support Operations

Responsible for reusable functionality.

* Display formatting
* Welcome screen
* Menu display
* Input validation

### Application Controller

Coordinates the overall workflow by presenting the menu, processing user selections, and delegating execution to the appropriate modules.

This separation of concerns keeps the application maintainable and easy to extend.

---

# 💡 Python Concepts Demonstrated

* Functions
* Parameters
* Return Values
* Lists
* Dictionaries
* Strings
* Loops
* Conditional Statements
* Input Validation
* Exception Handling
* Modular Programming
* Collections
* CRUD Operations
* Dictionary Manipulation
* Data Traversal

---

# 📈 Software Engineering Concepts Practiced

This project demonstrates practical implementation of:

* Entity Lifecycle Management
* CRUD Architecture
* Data Modelling
* State Management
* Separation of Concerns
* Single Responsibility Principle
* Defensive Programming
* Reusable Components
* Modular Software Design
* Program Flow
* Data Integrity
* Clean Code Practices
* User Experience Design

---

# 🚀 Future Improvements

The current implementation provides a strong foundation that can be expanded into a full-featured task management platform.

Potential enhancements include:

## Persistent Storage

Store tasks using:

* JSON
* CSV
* SQLite
* PostgreSQL
* MongoDB

This would allow tasks to persist between application sessions.

---

## Categories

Allow tasks to belong to categories such as:

* Personal
* Work
* Study
* Finance
* Health

---

## Tags

Support multiple tags per task.

Example:

```text
#python
#portfolio
#assignment
```

---

## Priority Sorting

Automatically sort tasks by:

* High
* Medium
* Low

---

## Due Date Sorting

Display tasks in chronological order based on deadlines.

---

## Filtering

Allow users to filter tasks by:

* Status
* Priority
* Due Date
* Category
* Tags

---

## Progress Dashboard

Display statistics such as:

* Total Tasks
* Pending Tasks
* Completed Tasks
* Overdue Tasks
* Completion Percentage

---

## Task Dependencies

Support prerequisite tasks.

Example:

```text
Write Documentation

↓

Create Release

↓

Deploy Application
```

---

## Recurring Tasks

Support daily, weekly, monthly, and yearly recurring tasks.

---

## Reminders

Notify users when tasks approach their due dates.

---

## Calendar Integration

Synchronize tasks with Google Calendar or Outlook Calendar.

---

## Search Enhancements

Support searching by:

* Due Date
* Priority
* Category
* Status
* Multiple keywords

---

## Undo Operations

Allow recently deleted or modified tasks to be restored.

---

## Task History

Track every modification made to each task.

---

## User Authentication

Support multiple users with separate task collections.

---

## Team Collaboration

Expand the application into a collaborative task management platform supporting:

* Shared projects
* Assigned tasks
* Comments
* Activity history
* Team permissions

---

## Notifications

Support:

* Email notifications
* Desktop notifications
* SMS reminders
* Push notifications

---

## Graphical User Interface

Develop a desktop version using:

* Tkinter
* PyQt

---

## Web Application

Build a browser-based version using:

* Flask
* FastAPI
* Django

---

## Mobile Application

Develop Android and iOS applications using Flutter.

---

## REST API

Expose all task operations through a REST API for integration with external systems.

---

## AI Integration

Enhance the application with intelligent features such as:

* Automatic priority suggestions
* Smart due date recommendations
* Task summarization
* Productivity analytics
* Natural language task creation
* Intelligent scheduling
* Workload balancing
* AI-powered daily planning

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/to-do-list-manager.git
```

Navigate to the project directory:

```bash
cd to-do-list-manager
```

Run the application:

```bash
python main.py
```

---

# 📊 Skills Demonstrated

* Python Programming
* CRUD Application Development
* Task Lifecycle Management
* Data Modelling
* Software Architecture
* Input Validation
* Modular Programming
* State Management
* Defensive Programming
* Clean Code Practices
* Command-Line Application Development
* Problem Solving

---

# 📄 License

This project is licensed under my personal projects.

---

# ⭐ Acknowledgements

This project was developed as part of a structured software engineering portfolio focused on progressively building more sophisticated Python applications. It demonstrates practical software engineering principles including modular architecture, reusable validation, entity lifecycle management, data modelling, and clean, maintainable code while implementing a complete command-line task management system.
