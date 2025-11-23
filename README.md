# 📚 Project Title

**Student Management System (SMS)**: A Command-Line Interface (CLI) Application

## 💡 Overview of the Project

The Student Management System (SMS) is a basic, modular console application designed to manage student records (ID, Name, Major, GPA). It allows administrators to perform fundamental operations such as adding new students, viewing all records, and searching for a specific student by ID.

The project is structured using the Model-View-Controller (MVC) architectural pattern, which separates concerns for better maintenance and organization:

*Model (student.py, database.py): Handles the data structure and access logic.

*View (view.py): Manages all user interaction (menus, prompts, displays).

*Controller (controller.py): Contains the application logic and mediates between the Model and View.

The data is stored in-memory using standard Python lists and objects, simulating a backend database.

## ✨ Features

The application provides the following core functionalities through an interactive menu:

* **Add New Student (Create)**: Allows the user to input data for a new student record.

* **View All Students (Read)**: Displays a comprehensive list of all student records currently in the system.

* **Find Student by ID (Read)**: Searches for a specific student using their unique ID.

* **Robust Input Validation**: Ensures the Student ID is an integer and the GPA is a float strictly between $0.0$ and $4.0$.

* **ID Uniqueness Check**: Prevents adding a student if the ID already exists, maintaining data integrity.

## 🛠️ Technologies/Tools Used

| Category | Technology/Tool | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core development language. |
| **Design Pattern** | Model-View-Controller (MVC) | Provides modularity and separation of concerns. |
| **Storage** | In-Memory Data Store | Utilizes a global Python list (`_student_data` in `database.py`) for temporary object storage. |

## 🚀 Steps to Install & Run the Project

The project uses only standard Python features, so no external library installation is necessary.

## 1. File Structure
Ensure your files are placed in a single directory:

sms_project/

├── student.py # Student Class definition

├── database.py # Data Access Layer

├── view.py # User Interface logic

├── controller.py # Application logic

└── main.py # Entry Point


## 2. Running the Application

1. Navigate to the root project directory (sms_project/) in your terminal:
   
```Bash
cd /path/to/sms_project
```

 2. Execute the main file using the Python interpreter:
   
```Bash
python main.py
```

The application will launch, initialize three sample records, and display the main menu.

## 🧪 Instructions for Testing

Run the application and follow these steps to verify functionality:

| Test Case | Steps | Expected Result |
| :--- | :--- | :--- |
| **View Initial Data** | Select option **`2`** (View All Students). | Displays three pre-loaded students (IDs 101, 102, 103). |
| **Add New Student** | Select **`1`**, enter new data (e.g., ID: 104, Name: 'Daisy', GPA: 3.75). | Success message appears. Student appears when viewing all records. |
| **Validation Check** | Select **`1`**. When prompted for GPA, enter `5.0`. | Error message appears ("GPA must be between 0.0 and 4.0."), and reprompts for valid input. |
| **Find Student** | Select **`3`**, enter existing ID (e.g., **`102`**). | Details for "Bob Johnson" are displayed. |
| **Duplicate ID Check**| Select **`1`**, enter existing ID (e.g., **`101`**). | Error message: "Student with ID 101 already exists." |
