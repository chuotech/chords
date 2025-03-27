# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluckingui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
import pprint as pp
import csv
import ast

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 600)
        self.result_array = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 50, 71, 16))
        self.label.setObjectName("label")
        self.array_input = QtWidgets.QLineEdit(self.centralwidget)
        self.array_input.setGeometry(QtCore.QRect(230, 90, 321, 20))
        self.array_input.setText("")
        self.array_input.setObjectName("array_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 61, 16))
        self.label_2.setObjectName("label_2")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(560, 90, 75, 23))
        self.submit_button.setObjectName("submit_button")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(65, 180, 701, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(4)
        self.add_column_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_column_button.setGeometry(QtCore.QRect(400, 380, 100, 23))
        self.add_column_button.setObjectName("add_column_button")
        self.add_column_button.setText("Add Column")
        self.add_column_button.clicked.connect(self.add_column)
        self.remove_column_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_column_button.setGeometry(QtCore.QRect(520, 380, 100, 23))
        self.remove_column_button.setObjectName("remove_column_button")
        self.remove_column_button.setText("Remove Column")
        self.remove_column_button.clicked.connect(self.remove_column)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(140, 380, 75, 23))
        self.stop_button.setObjectName("stop_button")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(60, 380, 75, 23))
        self.start_button.setObjectName("start_button")
        self.save_as_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_as_button.setGeometry(QtCore.QRect(220, 380, 75, 23))
        self.save_as_button.setObjectName("save_as_button")
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.load_button.setObjectName("load_button")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(60, 150, 75, 23))
        self.help_button.setObjectName("help_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_As)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Plucker Input"))
        self.array_input.setPlaceholderText(_translate("MainWindow", "Ex: [[1,1,1,0],[2,2,2,.5],[...]...]"))
        self.label_2.setText(_translate("MainWindow", "Array input:"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.submit_button.clicked.connect(self.array_to_table)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Note"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Duration"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Speed"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Note1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Note2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Note3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Note4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Note5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Note6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Note7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Note8"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.start_button.clicked.connect(self.print_table)
        self.save_as_button.setText(_translate("MainWindow", "Save As"))
        self.save_as_button.clicked.connect(self.save_table_as_csv)
        self.load_button.setText(_translate("MainWindow", "Load"))
        self.load_button.clicked.connect(self.load_from_csv)
        self.help_button.setText(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))

    def add_column(self):
            col_count = self.tableWidget.columnCount()
            self.tableWidget.insertColumn(col_count)
            self.tableWidget.setHorizontalHeaderItem(col_count, QtWidgets.QTableWidgetItem(f"Note{col_count+1}"))

    def remove_column(self):
        col_count = self.tableWidget.columnCount()
        if col_count > 0:
            self.tableWidget.removeColumn(col_count - 1)
    
    def save_table_as_csv(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Table", "", "CSV Files (*.csv);;JSON Files (*.json)", options=options)
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Save headers
            headers = [self.tableWidget.horizontalHeaderItem(col).text() if self.tableWidget.horizontalHeaderItem(col) else f"Column {col+1}" 
                    for col in range(self.tableWidget.columnCount())]
            writer.writerow(headers)
            
            # Save table contents
            for row in range(self.tableWidget.rowCount()):
                row_data = [self.tableWidget.item(row, col).text() if self.tableWidget.item(row, col) else "" 
                            for col in range(self.tableWidget.columnCount())]
                writer.writerow(row_data)

    def load_from_csv(self, file_path):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "Load Table", "", "CSV Files (*.csv);;JSON Files (*.json)", options=options)
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) == 0:
                return

            # Set column count based on file
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setRowCount(len(data) - 1)  # Exclude header row

            # Set headers
            for col, header in enumerate(data[0]):
                self.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(header))

            # Set table data
            for row in range(1, len(data)):
                for col in range(len(data[row])):
                    self.tableWidget.setItem(row - 1, col, QTableWidgetItem(data[row][col]))
        
    def print_table(self):
        """Prints the table as an array with columns as rows and rows as columns."""
        output_array = []
        row_count = self.tableWidget.rowCount()
        col_count = self.tableWidget.columnCount()

        # Extract data from table and store in a 2D list
        table_data = [[self.tableWidget.item(row, col).text() if self.tableWidget.item(row, col) else ""
                    for col in range(col_count)] for row in range(row_count)]

        # Transpose the data (convert columns to rows)
        transposed_data = list(map(list, zip(*table_data)))

        # Print the transposed array
        print("Transposed Table:")
        for row in transposed_data:
            # print(row)
            for i in range(len(row)):
                if i == 1 or i == 3:
                    row[i] = float(row[i])
                else:
                    row[i] = int(row[i])
            output_array.append(row)
        self.result_array = output_array
        pp.pp(output_array)
        

    def array_to_table(self):
        input_text = self.array_input.text().strip()

        if not input_text:
            return  # Do nothing if input is empty

        try:
            # Safely convert the string to a list
            array_data = ast.literal_eval(input_text)

            if not isinstance(array_data, list) or not all(isinstance(row, list) for row in array_data):
                raise ValueError("Invalid format. Must be a 2D list.")

            # Transpose the data (convert rows to columns)
            transposed_data = list(map(list, zip(*array_data)))

            # Get new dimensions after transposing
            row_count = len(transposed_data)
            col_count = max(len(row) for row in transposed_data)  # Get the longest row

            # Resize table
            self.tableWidget.setRowCount(row_count)
            self.tableWidget.setColumnCount(col_count)

            # Fill table with transposed data
            for row_idx, row in enumerate(transposed_data):
                for col_idx, value in enumerate(row):
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except (ValueError, SyntaxError):
            print("Invalid input format! Enter a valid 2D array.")
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
