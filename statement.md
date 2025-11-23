## 🛑 Problem Statement

The university currently lacks a centralized, efficient system for managing basic student records. Record-keeping is manual or dispersed across unlinked files, leading to difficulties in retrieving information, performing quick searches, and ensuring data accuracy regarding student enrollment details, academic standing, and contact information. A standardized, accessible, and simple digital solution is required to address these issues.

## 🎯 Scope of the Project

The scope of the **Student Management System (SMS)** project is strictly limited to a **proof-of-concept, console-based application** that demonstrates core data management capabilities.

**In-Scope:**
* Implementation of the **Model-View-Controller (MVC)** architectural pattern.
* The definition and use of a single Student entity (ID, Name, Major, GPA).
* Core functionality: **Add, View All**, and **Find by ID.**
* Basic input validation (data type, range checking for GPA) and ID uniqueness checks.
*Data storage will be **in-memory** (non-persistent list) for the duration of the application run.

**Out-of-Scope (Future Enhancements):**
* Persistent data storage (e.g., database, file I/O).
* Update and Delete functionalities.
* Advanced query/search filters (e.g., searching by Name or Major).
* Graphical User Interface (GUI) or web interface development.

## 👤 Target Users

| User Group | Primary Interaction |
| :--- | :--- |
| **System Administrator** | **Primary Target User.** Responsible for data entry, routine checks, and ensuring the accuracy of student records within the system. |
| **IT/Development Team** | Responsible for maintenance and future enhancement of the underlying code and architecture. |

## ✅ High-Level Features

The system must provide the following core features:
* **Student Record Creation**: Allow a system administrator to enter and save new student data (ID, Name, Major, GPA).
* **Record Retrieval**: Enable the retrieval and display of all student records currently in the system.
* **Unique Search**: Allow fast retrieval of a single student record by their unique Student ID.
* **Data Integrity**: Enforce validation rules for inputs (e.g., GPA must be a float between 0.0 and 4.0) before data is accepted by the system.
