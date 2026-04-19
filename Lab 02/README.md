# Lab 02 — Library Management System with Multiple Forms (PyQt6)

A desktop-based **Library Management System** built with **PyQt6** and **Qt Designer** as part of **CS355/CE373 Database Systems (Fall 2024)** at **Habib University**. This lab focuses on building a GUI application that works with **multiple forms**, lets users **search** for books using filters, **view** book details in a separate read-only window, and **delete** books with confirmation.

## Overview

This project implements a simple library management interface using a hardcoded Python list as the data source. The main window displays all books in a table and provides search controls for filtering by:

- category
- title
- type
- issuance status

The application also includes a secondary **View Book** form that opens on top of the main window and shows the selected book's details in **view-only mode**.

## Lab Objective

According to the lab manual, the goal of this lab is to help students work with **multiple GUI forms** in PyQt6 and **exchange data across them** while building a library management system. fileciteturn1file1L13-L20

## Features

- Displays all books from a hardcoded Python list in a table on startup
- Search books using:
  - **Category** (`Database`, `OOP`, `AI`)
  - **Title**
  - **Type** (`Reference Book`, `Text Book`, `Journal`)
  - **Issued** status
- Opens a separate **View Book** window for the selected record
- Shows book details in **read-only form**
- Deletes the selected book after user confirmation
- Closes the application from the main window

These are the main requirements described in the lab manual. fileciteturn1file1L21-L33 fileciteturn1file1L34-L46 fileciteturn1file1L47-L66

## Project Structure

```text
.
├── app.py
├── LibraryManagementSystem_Lab02.ui
├── ViewBook.ui
└── Lab 02.pdf
```

## Technologies Used

- **Python**
- **PyQt6**
- **Qt Designer**

## How It Works

### 1. Main Window
The main window loads the UI from `LibraryManagementSystem_Lab02.ui`, sets the title to **Library Management System**, and fills the table widget with book records from the hardcoded `books` list. Each row contains:

- ISBN
- Title
- Category
- Type
- Issued

This matches the lab requirement for the search form and table widget. fileciteturn1file0L13-L36 fileciteturn1file1L21-L33

### 2. Search Functionality
The `search()` method reads input from the title field, category combo box, issued checkbox, and type radio buttons. It then filters the visible rows in the table by hiding rows that do not match the selected criteria. Before each search, all rows are shown again using `showtable()`. fileciteturn1file0L43-L80

### 3. View Book Form
The `view()` method checks whether a row is selected. If a row is selected, it extracts the book details from the current row and opens a `ViewBook` window. The second form receives the selected data and displays it in disabled input fields so the user cannot edit the details. fileciteturn1file0L85-L99 fileciteturn1file0L128-L159

### 4. Delete Functionality
The `delete()` method also checks whether a row is selected. If so, it opens a confirmation message box. The row is removed only if the user presses **Yes**. fileciteturn1file0L101-L111 fileciteturn1file0L118-L126

### 5. Close Button
The main form closes when the user clicks the close button. fileciteturn1file0L113-L116

## Hardcoded Book Data

The application uses a Python list named `books` as its data source. Each record stores:

1. ISBN
2. Title
3. Category
4. Type
5. Issued status

This was required in the lab because database connectivity had not yet been covered. fileciteturn1file0L13-L20 fileciteturn1file1L47-L66

## Running the Project

### Requirements

Install PyQt6 first:

```bash
pip install PyQt6
```

### Run

Make sure these files are in the same folder:

- `app.py`
- `LibraryManagementSystem_Lab02.ui`
- `ViewBook.ui`

Then run:

```bash
python app.py
```

## Example Workflow

1. Launch the app
2. View all books in the table
3. Enter one or more search filters
4. Click **Search** to narrow the results
5. Select a row and click **View** to open the read-only details form
6. Select a row and click **Delete** to remove it after confirmation
7. Click **Close** to exit the application

## Notes

- The current implementation removes the selected row from the **table widget**, but the original `books` list itself is not updated after deletion. The lab manual expects deletion from the Python list and then redisplaying the table. fileciteturn1file0L101-L111 fileciteturn1file1L67-L78
- The lab manual also notes that the skeleton file expects the UI file name `Lab02.ui` and the table widget object name `booksTableWidget`. This project uses `LibraryManagementSystem_Lab02.ui`, so make sure the filename in `uic.loadUi(...)` matches your actual file. fileciteturn1file1L79-L85

## Learning Outcomes

By completing this lab, students practice:

- building desktop applications in PyQt6
- working with multiple windows/forms
- passing data between forms
- populating and reading table widgets
- implementing search/filter logic
- using confirmation dialogs and read-only fields in GUI applications

## Course Information

- **Course:** CS355 / CE373 — Database Systems
- **Lab:** Lab 02 — Building Desktop Applications with Multiple Forms in PyQt6
- **Institution:** Habib University
- **Semester:** Fall 2024 fileciteturn1file1L1-L12

## Author

Add your name, student ID, and GitHub profile here.

```text
Name: Your Name
Student ID: Your ID
GitHub: your-github-link
```
