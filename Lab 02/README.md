# Lab 02 - Library Management System using PyQt6

This project was developed for **Lab 02** of the **CS355/CE373 Database Systems** course at **Habib University**.

The lab focuses on building a **desktop application with multiple forms in PyQt6**. The application allows users to search for books, view book details in a separate form, and delete books from the displayed list.

---

## Objective

The main objective of this lab is to learn how to work with **multiple GUI forms** in PyQt6 and pass data between them.

In this project, a **Library Management System** was built with the following features:

- Display all books stored in a hardcoded Python list
- Search books using multiple criteria
- View full details of a selected book in a separate read-only form
- Delete a selected book after confirmation
- Close the application

---

## Features

### 1. Book Search Form
The main form displays all available books in a table when the application starts.

Each book record includes:

- ISBN
- Title
- Category
- Type
- Issued status

### 2. Search Functionality
Users can search for books using the following filters:

- **Category**
- **Title**
- **Type**
- **Issued status**

Only the rows matching the selected criteria remain visible in the table.

### 3. View Book Form
When the user selects a row and clicks **View**, a second form opens on top of the main form.

This form shows the selected book’s details in **view-only mode**, so the user cannot edit them.

### 4. Delete Functionality
When the user selects a book and clicks **Delete**, a confirmation message box appears.

- Clicking **Yes** removes the selected row from the table
- Clicking **No** cancels the operation

### 5. Close Button
The **Close** button exits the application.

---

## Technologies Used

- **Python**
- **PyQt6**
- **Qt Designer**

---

## Project Files

```bash
.
├── app.py
├── LibraryManagementSystem_Lab02.ui
├── ViewBook.ui
└── README.md
