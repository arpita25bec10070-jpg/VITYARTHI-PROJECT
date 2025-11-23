📝 README: Student Management System (SMS)📚 Project TitleStudent Management System (SMS): A Command-Line Interface (CLI) Application💡 Overview of the ProjectThe Student Management System (SMS) is a basic, modular console application designed to manage student records. It allows administrators to perform fundamental operations such as adding new students, viewing all records, and searching for a specific student by ID.The project adheres to the Model-View-Controller (MVC) architectural patternGetty ImagesExplore, separating data handling, user interface, and application logic into distinct Python modules (student.py, database.py, view.py, and controller.py). The data is stored in-memory using Python objects and lists, simulating a backend database for simplicity and rapid prototyping.✨ FeaturesThe application provides the following core functionalities through an interactive menu:Add New Student (Create): Allows the user to input a unique Student ID, Name, Major, and GPA.View All Students (Read): Displays a list of all current student records in a clear format.Find Student by ID (Read): Searches the records for a specific student using their unique ID and displays the details if found.Input Validation: Ensures the Student ID is an integer and the GPA is a float between $0.0$ and $4.0$.ID Uniqueness Check: Prevents adding a student if the ID already exists in the system.Graceful Exit: Option to terminate the application safely.🛠️ Technologies/Tools UsedCategoryTechnology/ToolPurposeLanguagePython 3.xCore development language.Design PatternModel-View-Controller (MVC)Provides modularity and separation of concerns.StorageIn-Memory Data StoreUtilizes a global Python list (_student_data in database.py) for temporary storage.EnvironmentCommand-line terminal.User interface interaction.🚀 Steps to Install & Run the ProjectSince this project is purely written in standard Python, no external libraries are required.1. File StructureEnsure your project files are organized as follows:sms_project/
├── student.py        # Student Class (Model)
├── database.py       # Data Access Layer (Model)
├── view.py           # User Interface & Input/Output (View)
├── controller.py     # Application Logic (Controller)
└── main.py           # Application Entry Point
2. Running the ApplicationNavigate to the root directory of the project (sms_project/) using your terminal or command prompt.Bashcd /path/to/sms_project
Execute the main file using the Python interpreter:Bashpython main.py
The application will start by loading initial data and displaying the main menu.🧪 Instructions for TestingAfter running python main.py, use the following manual test steps to verify the system's functionality:Test Case 1: View Initial Data (FR2)From the main menu, enter 2 to View All Students.Expected Result: The system should display the three initial students: Alice Smith (101), Bob Johnson (102), and Charlie Brown (103).Test Case 2: Add a New Student (FR1)From the main menu, enter 1 to Add New Student.Input a valid new ID (e.g., 104), Name, Major, and valid GPA (e.g., 3.75).Expected Result: A success message should confirm the addition. Verify by running the View All Students feature again.Test Case 3: Input Validation and Error Handling (FR4)From the main menu, enter 1 to Add New Student.When prompted for GPA, enter an invalid non-numeric value (e.g., five) or an out-of-range value (e.g., 4.5).Expected Result: The system should display an error message (e.g., "Invalid input...") and prompt you to re-enter a valid input.Test Case 4: Find an Existing Student (FR3)From the main menu, enter 3 to Find Student by ID.Enter the ID of an existing student (e.g., 102).Expected Result: The details for "Bob Johnson" should be displayed using the __str__ format.🖼️ Screenshots (Simulated Output)Initial Launch and Viewing DataPlaintext--- Student Management System ---
1. Add New Student
2. View All Students
3. Find Student by ID
4. Exit
Enter your choice (1-4): 2

--- All Students in System ---
ID: 101, Name: Alice Smith, Major: Computer Science, GPA: 3.90
ID: 102, Name: Bob Johnson, Major: Electrical Engineering, GPA: 3.50
ID: 103, Name: Charlie Brown, Major: Business, GPA: 3.20
-------------------------------
Adding a New StudentPlaintextEnter your choice (1-4): 1

--- Enter New Student Data ---
Student ID (e.g., 104): 104
Name: Daisy Miller
Major: Biology
GPA (e.g., 3.75): 3.75

[SYSTEM] Successfully added student: Daisy Miller (ID: 104)
