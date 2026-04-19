# Library Management System - PyQt6 Lab

A simple desktop application built with **PyQt6** and **Qt Designer** for a database systems lab. This project implements a **Library Management System** form where a user can enter book details, manage authors, select categories and subcategories, choose the book type, handle issuance information, and validate the entered data before saving. The lab manual defines this as a desktop GUI exercise for learning PyQt6 widgets, event handling, and form validation, and the repository includes both the Python logic file and the `.ui` design file. 

## Lab Objective

The goal of this lab is to practice building desktop-based applications using **PyQt6** and **Qt Designer**, with a focus on GUI controls and event-driven programming.

## Features

This application supports the following functionality:

- Enter book information such as:
  - **Name**
  - **ISBN**
  - **Purchased On** date
- Select a **Category** from:
  - Database Systems
  - OOP
  - Artificial Intelligence
- Automatically load related **Subcategories** based on the selected category.
- Add one or more **authors** to the author list.
- Select the **book type** using radio buttons:
  - Reference Book
  - Text Book
  - Journal
- Mark whether the book is **issued** using a checkbox.
- Enable or disable **Issued By** and **Issued On** fields depending on issuance status.
- Validate the form when the **Okay** button is pressed.
- Show a **message box** for successful submission or validation errors.
- Close the application using the **Close** button.

## Validation Rules

The form is designed around the lab requirements and checks these rules:

1. **ISBN** must not be longer than 12 characters.
2. **Purchased On** date must be earlier than today's date.
3. If the selected type is **Journal**, it should not have any authors.
4. If the selected type is **Reference Book** or **Text Book**, it must have at least one author.
5. If the book is marked as **issued**:
   - **Issued By** must not be empty.
   - **Issued On** must be later than **Purchased On**.
   - **Issued On** must also be earlier than today's date.

## Project Structure

```bash
.
├── app.py                     # Main PyQt6 application logic
├── LibraryManagementSystem.ui # UI designed in Qt Designer
└── README.md                  # Project documentation
```

## Technologies Used

- **Python 3**
- **PyQt6**
- **Qt Designer**

## How to Run

1. Clone this repository:

```bash
git clone <your-repository-link>
cd <your-repository-folder>
```

2. Install PyQt6:

```bash
pip install PyQt6
```

3. Run the application:

```bash
python app.py
```

## How the Application Works

- The UI is loaded from `LibraryManagementSystem.ui` using `uic.loadUi()`.
- Categories and their subcategories are stored in a Python dictionary inside `app.py`.
- When the category changes, the subcategory combo box is updated.
- Authors can be added from the input field into the text area by clicking **Add**.
- When the **Issued** checkbox is toggled, the issuance fields are enabled or disabled.
- When the **Okay** button is clicked, the application verifies the entered data and displays a message box.

## Repository Files

### `app.py`
Contains the main application code, including:
- UI loading
- signal-slot connections
- category/subcategory handling
- author list updates
- issuance toggling
- input validation
- message box display

### `LibraryManagementSystem.ui`
Contains the GUI layout created in **Qt Designer**, including:
- labels
- line edits
- combo boxes
- group boxes
- radio buttons
- check box
- date edits
- action buttons

## Learning Outcomes

Through this lab, the project demonstrates:

- designing a GUI with Qt Designer
- connecting widgets to Python logic
- using signal-slot mechanisms in PyQt6
- working with combo boxes, radio buttons, text inputs, check boxes, and date edits
- validating user input in a desktop application
- showing feedback using message boxes

## Notes

This project was created as part of **Lab 1** for the **CS355/CE373 Database Systems** course at **Habib University**.

## License

This project is for academic and learning purposes.
