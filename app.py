import sys
from PyQt6 import QtWidgets , uic , QtGui , QtCore
from PyQt6.QtCore import QSize, Qt, QDate
from PyQt6.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QComboBox, 
                             QLineEdit, 
                             QPushButton, 
                             QCheckBox,
                             QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self ).__init__()
        uic.loadUi('LibraryManagementSystem.ui', self )
        self.setWindowTitle("Library Management System")
        self.categories = {
            'Database Systems': ['ERD', 'SQL', 'OLAP', 'Data Mining'],
            'OOP': ['C++', 'Java'],
            'Artificial Intelligence': ['Machine Learning', 'Robotics', 'Computer Vision']
        }
        self.categoryComboBox.activated.connect(self.update_subcategories)
        self.update_subcategories
        self.pushButton1.clicked.connect(self.update_authorNames)
        self.checkBox.stateChanged.connect(self.toggle_Issuance)
        self.pushButton_2.clicked.connect(self.verify)
        self.pushButton3.clicked.connect(self.close_window)
        self.show ()

    def update_subcategories(self):
        selected_category = self.categoryComboBox.currentText()
        self.subcategoryComboBox.clear()
        if selected_category in self.categories:
            subcategories = self.categories[selected_category]
            self.subcategoryComboBox.addItems(subcategories)
    
    def update_authorNames(self):
        authorName = self.lineEdit.text()
        if authorName:
            self.textEdit.append(authorName)
            self.lineEdit.clear()
    
    def toggle_Issuance(self, state):
        status = self.checkBox.isChecked()
        self.lineEdit_2.setEnabled(status)
        self.dateEdit_2.setEnabled(status)
    
    def verify(self):
        message = ""
        state = True
        content = self.lineEdit1.text()
        if len(content) == 0:
            state = False
            if len(message) != 0:
                message = message + " or "
            message = message + "Name is Missing"
        isbn = self.lineEdit2.text()
        if len(isbn) > 12:
            state = False
            if len(message) != 0:
                message = message + " or "
            message = message + "The Length of ISBN is greater than 12"
        elif len(isbn) == 0:
            state = False
            if len(message) != 0:
                message = message + " or "
            message = message + "ISBN is Missing"
        if self.dateEdit.date() >= QDate.currentDate():
            state = False
            if len(message) != 0:
                message = message + " or "
            message = message + "Purchased On Date is greater than today"
        if self.radioButton_3.isChecked():
            content = self.textEdit.toPlainText()
            if len(content) != 0:
                state = False
                if len(message) != 0:
                    message = message + " or "
                message = message + "Has an Author"
        else:
            content = self.textEdit.toPlainText()
            if len(content) == 0:
                state = False
                if len(message) != 0:
                    message = message + " or "
                message = message + "Author is Missing"
        if self.checkBox.isChecked():
            content = self.lineEdit_2.text()
            if len(content) == 0:
                state = False
                if len(message) != 0:
                    message = message + " or "
                message = message + "Issued to is Empty"
            if not (self.dateEdit.date() < self.dateEdit_2.date() < QDate.currentDate()):
                state = False
                if len(message) != 0:
                    message = message + " or "
                message = message + "Issue Date must be After Purchased On Date And Before Today"

        if state == True:
            message = "Book added successfully!"
        
        self.show_Message(message)
        
    def show_Message(self, message):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Message Box")
        dlg.setText(message)
        dlg.exec()
    
    def close_window(self):
        self.close()
    
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec()