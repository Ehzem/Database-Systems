from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtCore import Qt, QSize, QModelIndex
import sys
from PyQt6.QtWidgets import (QApplication, 
                             QMainWindow, 
                             QComboBox, 
                             QLineEdit, 
                             QPushButton, 
                             QCheckBox,
                             QVBoxLayout,
                             QTableWidget,
                             QMessageBox)


books = [
["0201144719 9780201144710","An introduction to database systems","Database","Reference Book","True"],
["0805301453 9780805301458","Fundamentals of database systems","Database","Reference Book","False"],
["1571690867 9781571690869","Object oriented programming in Java","OOP","Text Book","False"],
["1842652478 9781842652473","Object oriented programming using C++","OOP","Text Book","False"],
["0070522618 9780070522619","Artificial intelligence","AI","Journal","False"],
["0865760047 9780865760042","The Handbook of artificial intelligence","AI","Journal","False"],
]

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(UI, self).__init__() 
        # Load the .ui file
        uic.loadUi('LibraryManagementSystem_Lab02.ui', self) 
        self.setWindowTitle("Library Management System")
        self.booksTableWidget.setRowCount(len(books))
        for i in range(len(books)):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem(books[i][j])
                # Make the items non-editable
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable) 
                self.booksTableWidget.setItem(i,j,item)
        # Connect the search function with the search button.
        self.pushButton_1.clicked.connect(self.search)
        # Connect the view function with the view button.
        self.pushButton_3.clicked.connect(self.view)
        # Connect the delete function with the delete button.
        self.pushButton_2.clicked.connect(self.delete)
        # Connect the close function with the close button.
        self.pushButton_4.clicked.connect(self.close_window)
        
    def search(self):
        #Function to show rows of all tables incase any previous search hides any rows
        self.showtable()
        
        #Storing search parameters and appropriate variables
        title = self.lineEdit.text()
        category = self.comboBox_1.currentText()
        status = self.checkBox.isChecked()
        Type = ""
        if self.radioButton_1.isChecked():
            Type = "Reference Book"
        elif self.radioButton_2.isChecked():
            Type = "Text Book"
        elif self.radioButton_3.isChecked():
            Type = "Journal"
        
        #Translating status bool to string
        if status == False:
            status = "False"
        elif status == True:
            status = "True"
        
        #Iterating over the nested list to see if search data is not present
        #If searched data is not present that row is hidden
        for row in range(self.booksTableWidget.rowCount()):
            if category not in self.booksTableWidget.item(row, 2).text():
                self.booksTableWidget.hideRow(row)
            if status not in self.booksTableWidget.item(row, 4).text():
                self.booksTableWidget.hideRow(row)
            if len(Type) != 0:
                if Type not in self.booksTableWidget.item(row, 3).text():
                    self.booksTableWidget.hideRow(row)
            if len(title) != 0:
                if title not in self.booksTableWidget.item(row, 1).text():
                    self.booksTableWidget.hideRow(row)
        pass
        
    def showtable(self):
        for row in range(self.booksTableWidget.rowCount()):
            self.booksTableWidget.showRow(row)
        
    def view(self):
        #Check if a row is selected
        selected_row = self.booksTableWidget.selectionModel().selectedRows()
        if len(selected_row) != 0:
            #Identify which row is selected
            row = self.booksTableWidget.currentRow() 
            isbn = self.booksTableWidget.item(row, 0).text()
            title = self.booksTableWidget.item(row, 1).text()
            category = self.booksTableWidget.item(row, 2).text()
            Type = self.booksTableWidget.item(row, 3).text()
            issued = self.booksTableWidget.item(row, 4).text()
            self.view_book = ViewBook(isbn, title, category, Type, issued)
            self.view_book.show()
        pass
        
    def delete(self):
        #Check if a row is selected
        selected_row = self.booksTableWidget.selectionModel().selectedRows()
        if len(selected_row) != 0:
            #Identify which row is selected
            row = self.booksTableWidget.currentRow() 
            #Show last confirmation before deletion
            flag = self.show_Message()
            #Row is deleted based on final confirmation
            if flag == True:
                self.booksTableWidget.removeRow(row)
            else:
                pass
        pass

    def close_window(self):
        self.close()
        pass

    def show_Message(self):
        #Creating message box to ask for final confirmation before deletion of entry
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirmation Box")
        dlg.setIcon(QMessageBox.Icon.Warning)
        dlg.setText("Are you sure you want to delete this book ?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        response = dlg.exec()
        #Checks which button is pressed as last confirmation
        if response == QMessageBox.StandardButton.Yes:
            return True
        elif response == QMessageBox.StandardButton.No:
            return False
            

class ViewBook(QtWidgets.QMainWindow):  
    def __init__(self, isbn, title, category, Type, issued):
        # Call the inherited classes __init__ method
        super(ViewBook, self).__init__() 
        # Load the .ui file
        uic.loadUi('ViewBook.ui', self) 
        self.setWindowTitle("View Book")
        
        #Diplaying appropriate data and then disabling the widget
        self.lineEdit_1.setText(isbn)
        self.lineEdit_1.setDisabled(True)
        self.lineEdit_2.setText(title)
        self.lineEdit_2.setDisabled(True)
        self.lineEdit_3.setText(category)
        self.lineEdit_3.setDisabled(True)
        self.radioButton_1.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        if Type == "Reference Book":
            self.radioButton_1.setChecked(True)
        elif Type == "Text Book":
            self.radioButton_2.setChecked(True)
        elif Type == "Journal":
            self.radioButton_3.setChecked(True)
        self.groupBox.setDisabled(True)
        if issued == "True":
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        self.checkBox.setDisabled(True)
    pass
        
        
        



app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = UI() # Create an instance of our 
window.show()
app.exec() # Start the application

