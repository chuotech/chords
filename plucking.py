# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluckingui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QDialog, QWidget, QVBoxLayout, QPushButton
import pretty_midi
import pprint as pp
import csv
import ast
class ClickableProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None, ui_main_window=None, input_array=None, current_time=0):
        super().__init__(parent)
        self.ui_main_window = ui_main_window
        self.input_array = input_array if input_array else []
        self.current_time = current_time
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            click_position = event.x()  # Get the clicked position on the progress bar
            total_width = self.width()  # Get the total width of the progress bar
            new_value = float((click_position / total_width) * self.maximum())  # Calculate the new value based on the click
            self.setValue(int(new_value))

            # After setting the progress bar value, call the function to update note info
            self.update_note_info()

    def update_note_info(self):
        for note_info in self.input_array:
            if note_info['start'] <= self.current_time <= (note_info['start'] + note_info['duration']):
                # Use stored reference to update the line edits
                self.ui_main_window.note_line.setText(str(note_info['note_number']))
                self.ui_main_window.duration_line.setText(str(note_info['duration']))
                self.ui_main_window.speed_line.setText(str(note_info['speed']))
                self.ui_main_window.start_line.setText(str(note_info['start']))
                break

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 348)
        self.input_array = []
        self.total_duration = 0
        self.advanced_window = None
        self.current_value = 0
        self.current_note = 0
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = ClickableProgressBar(self.centralwidget, ui_main_window=self, input_array=self.input_array, current_time=self.current_value)
        self.progressBar.setGeometry(QtCore.QRect(110, 220, 601, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.current_time_label = QtWidgets.QLabel("0.0s", self.centralwidget)
        self.current_time_label.setGeometry(QtCore.QRect(720, 220, 50, 23))
        self.current_time_label.setObjectName("current_time_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(280, 180, 75, 23))
        self.start_button.setObjectName("start_button")
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(340, 260, 75, 23))
        self.pause_button.setObjectName("pause_button")
        self.plus5_button = QtWidgets.QPushButton(self.centralwidget)
        self.plus5_button.setGeometry(QtCore.QRect(580, 260, 75, 23))
        self.plus5_button.setObjectName("plus5_button")
        self.minus5_button = QtWidgets.QPushButton(self.centralwidget)
        self.minus5_button.setGeometry(QtCore.QRect(180, 260, 75, 23))
        self.minus5_button.setObjectName("minus5_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(360, 180, 75, 23))
        self.clear_button.setObjectName("clear_button")
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setGeometry(QtCore.QRect(260, 260, 75, 23))
        self.prev_button.setObjectName("prev_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(500, 260, 75, 23))
        self.next_button.setObjectName("next_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.note_line = QtWidgets.QLineEdit(self.centralwidget)
        self.note_line.setGeometry(QtCore.QRect(190, 90, 41, 20))
        self.note_line.setText("")
        self.note_line.setObjectName("note_line")
        self.duration_line = QtWidgets.QLineEdit(self.centralwidget)
        self.duration_line.setGeometry(QtCore.QRect(190, 120, 41, 20))
        self.duration_line.setText("")
        self.duration_line.setObjectName("duration_line")
        self.speed_line = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_line.setGeometry(QtCore.QRect(190, 150, 41, 20))
        self.speed_line.setText("")
        self.speed_line.setObjectName("speed_line")
        self.start_line = QtWidgets.QLineEdit(self.centralwidget)
        self.start_line.setGeometry(QtCore.QRect(190, 180, 41, 20))
        self.start_line.setText("")
        self.start_line.setObjectName("start_line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 60, 121, 16))
        self.label_5.setObjectName("label_5")
        self.save_as_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_as_button.setGeometry(QtCore.QRect(440, 180, 75, 23))
        self.save_as_button.setObjectName("save_as_button")
        self.save_as_button.clicked.connect(self.save_midi)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(440, 150, 75, 23))
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_edited)
        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(520, 180, 75, 23))
        self.load_button.setObjectName("load_button")
        self.load_button.clicked.connect(self.load_midi)
        self.advance_button = QtWidgets.QPushButton(self.centralwidget)
        self.advance_button.setGeometry(QtCore.QRect(600, 180, 75, 23))
        self.advance_button.setObjectName("advance_button")
        self.resume_button = QtWidgets.QPushButton(self.centralwidget)
        self.resume_button.setGeometry(QtCore.QRect(420, 260, 75, 23))
        self.resume_button.setObjectName("resume_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 30, 61, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.progressBar.valueChanged.connect(self.update_current_time_label)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.pause_button.setText(_translate("MainWindow", "Pause"))
        self.plus5_button.setText(_translate("MainWindow", "+5sec"))
        self.minus5_button.setText(_translate("MainWindow", "-5sec"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.prev_button.setText(_translate("MainWindow", "Prev. Note"))
        self.next_button.setText(_translate("MainWindow", "Next Note"))
        self.label.setText(_translate("MainWindow", "Note"))
        self.label_2.setText(_translate("MainWindow", "Duration"))
        self.label_3.setText(_translate("MainWindow", "Speed"))
        self.label_4.setText(_translate("MainWindow", "Start"))
        self.label_5.setText(_translate("MainWindow", "Current Note Info.:"))
        self.save_as_button.setText(_translate("MainWindow", "Save As"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.load_button.setText(_translate("MainWindow", "Load"))
        self.advance_button.setText(_translate("MainWindow", "Advanced"))
        self.resume_button.setText(_translate("MainWindow", "Resume"))
        self.label_6.setText(_translate("MainWindow", "Plucker UI"))

        self.advance_button.clicked.connect(self.help_clicked)

    def save_midi(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Save MIDI", "", "MIDI Files (*.mid)", options=options)
        if file_path:
            midi = pretty_midi.PrettyMIDI()
            instrument = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano

            # Iterate through the columns (notes) of the table
            for curr_note in self.input_array:
                note = pretty_midi.Note(velocity=50, pitch= curr_note["note_number"], start= curr_note["start"], end= curr_note["start"] + curr_note["duration"])
                instrument.notes.append(note)
            midi.instruments.append(instrument)

            # Write the MIDI data to the specified file
            midi.write(file_path)
            print(f"MIDI file saved at: {file_path}")    
    def load_midi(self):
        # Open file dialog to select a MIDI file
        file_dialog = QtWidgets.QFileDialog()
        midi_file, _ = file_dialog.getOpenFileName(None, "Open MIDI File", "", "MIDI Files (*.mid *.midi)")
        
        if midi_file:
            self.load_midi_data(midi_file)

    def load_midi_data(self, midi_file):
        try:
            midi_data = pretty_midi.PrettyMIDI(midi_file)
            
            # Clear any existing notes in the array
            self.input_array.clear()

            # A list to store the last note's end time for calculating speed
            last_end_time = 0
            total_duration = 0  # Variable to store the total duration of the MIDI file

            # Extract note information from each instrument
            for instrument in midi_data.instruments:
                for note in instrument.notes:
                    # Calculate the note's duration
                    duration = note.end - note.start
                    
                    # Calculate the speed (difference in start time between consecutive notes)
                    speed = note.start - last_end_time if last_end_time else 0
                    
                    # Store the note information as a dictionary
                    note_info = {
                        'note_number': note.pitch,
                        'duration': duration,
                        'speed': int(speed),
                        'start': note.start,
                    }
                    self.input_array.append(note_info)
                    
                    # Update last end time
                    last_end_time = note.end

                    # Update the total duration based on the last note's end time
                    self.total_duration = note.end

            # Set the progress bar's maximum value to the total duration of the MIDI file
            # self.progressBar.setMaximum(int(total_duration))

            # Print out the array for debugging
            print("Loaded MIDI with", len(self.input_array), "notes.")
            for note_info in self.input_array:
                print(note_info)
        
        except Exception as e:
            print(f"Error loading MIDI file: {e}")

    def update_current_time_label(self):
        # Get the current value of the progress bar
        self.current_value = self.progressBar.value()
        self.current_value = self.total_duration*(self.current_value/100)
        self.show_info()
        # Set the current time label as a string
        self.current_time_label.setText(f"{self.current_value:.2f}s")

    def show_info(self):
        for i in range(len(self.input_array)):
            if self.input_array[i]['start'] <= self.current_value < (self.input_array[i]['start'] + self.input_array[i]['duration']):
                self.note_line.setText(str(self.input_array[i]['note_number']))
                self.duration_line.setText(str(self.input_array[i]['duration']))
                self.speed_line.setText(str(self.input_array[i]['speed']))
                self.start_line.setText(str(self.input_array[i]['start']))
                self.current_note = i
                print(i)
                break  # Stop after finding the first matching note
    def save_edited(self):
        self.input_array[self.current_note]['note_number'] = int(self.note_line.text())
        self.input_array[self.current_note]['duration'] = float(self.duration_line.text())
        self.input_array[self.current_note]['speed'] = int(self.speed_line.text())
        self.input_array[self.current_note]['start'] = float(self.start_line.text())
        pp.pp(self.input_array)
    def start_sequence(self):
        # single_tick = self.progressBar.maximum() / self.total_duration
        # curent_tick = self.progressBar.value()
        # while()
        pass
    def pause_sequence(self):
        pass
    def update_note(self):
        pass
    # def mousePressEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton:
    #         click_position = event.x()
    #         total_width = self.progressBar.width()
            
    #         # Convert click position to a time value
    #         clicked_time = (click_position / total_width) * self.total_duration
            
    #         # Update progress bar
    #         self.progressBar.setValue(int((clicked_time / self.total_duration) * 100))
            
    #         # Find the corresponding note
    #         for note_info in self.input_array:
    #             if note_info['start'] <= clicked_time <= (note_info['start'] + note_info['duration']):
    #                 self.note_line.setText(str(note_info['note_number']))
    #                 self.duration_line.setText(str(note_info['duration']))
    #                 self.speed_line.setText(str(note_info['speed']))
    #                 self.start_line.setText(str(note_info['start']))
    #                 break  # Stop after finding the first matching note

    def help_clicked(self):
        if self.advanced_window is None or not self.advanced_window.isVisible():
            self.advanced_window = AdvancedWindow()
            self.advanced_window.show()

class AdvancedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Window")
        self.resize(833, 600)
        self.result_array = []

        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.submit_button.clicked.connect(self.array_to_table)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(65, 180, 701, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setVerticalHeaderLabels(["Note", "Duration", "Speed", "Start"])
        self.tableWidget.setHorizontalHeaderLabels(["Note 1", "Note 2", "Note 3", "Note 4", "Note 5", "Note 6", "Note 7", "Note 8"])
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

        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(140, 380, 75, 23))
        self.stop_button.setObjectName("stop_button")

        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(60, 380, 75, 23))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.print_table)

        self.save_as_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_as_button.setGeometry(QtCore.QRect(220, 380, 75, 23))
        self.save_as_button.setObjectName("save_as_button")
        self.save_as_button.clicked.connect(self.save_table_as_midi)

        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.load_button.setObjectName("load_button")
        self.load_button.clicked.connect(self.load_from_midi)

        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(60, 150, 75, 23))
        self.help_button.setObjectName("help_button")
        self.help_button.clicked.connect(self.help_clicked)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("AdvancedWindow", "Plucker Input"))
        self.array_input.setPlaceholderText(_translate("AdvancedWindow", "Ex: [[1,1,1,0],[2,2,2,.5],[...]...]"))
        self.label_2.setText(_translate("AdvancedWindow", "Array input:"))
        self.submit_button.setText(_translate("AdvancedWindow", "Submit"))
        self.stop_button.setText(_translate("AdvancedWindow", "Stop"))
        self.start_button.setText(_translate("AdvancedWindow", "Start"))
        self.save_as_button.setText(_translate("AdvancedWindow", "Save As"))
        self.load_button.setText(_translate("AdvancedWindow", "Load"))
        self.help_button.setText(_translate("AdvancedWindow", "Help"))

    def add_column(self):
        col_count = self.tableWidget.columnCount()
        self.tableWidget.insertColumn(col_count)
        self.tableWidget.setHorizontalHeaderItem(col_count, QTableWidgetItem(f"Note{col_count+1}"))

    def remove_column(self):
        col_count = self.tableWidget.columnCount()
        if col_count > 0:
            self.tableWidget.removeColumn(col_count - 1)

    def save_table_as_midi(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save MIDI", "", "MIDI Files (*.mid)", options=options)
        if file_path:
            midi = pretty_midi.PrettyMIDI()
            instrument = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano

            # Iterate through the columns (notes) of the table
            for col in range(self.tableWidget.columnCount()):
                try:
                    # Extract attributes from the rows for each column (note)
                    note_number = int(self.tableWidget.item(0, col).text()) if self.tableWidget.item(0, col) else 0  # Default to 0 if empty
                    duration = float(self.tableWidget.item(1, col).text()) if self.tableWidget.item(1, col) else 1.0  # Default to 1.0 if empty
                    velocity = int(self.tableWidget.item(2, col).text()) if self.tableWidget.item(2, col) else 64  # Default to 64 if empty
                    start_time = float(self.tableWidget.item(3, col).text()) if self.tableWidget.item(3, col) else 0.0  # Default to 0.0 if empty

                    # Create a new note with the extracted data
                    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start_time, end=start_time + duration)
                    instrument.notes.append(note)

                except (ValueError, AttributeError) as e:
                    print(f"Skipping invalid data in column {col}: {e}")
                    continue  # Skip columns with invalid data

            # Append the instrument (with its notes) to the MIDI object
            midi.instruments.append(instrument)

            # Write the MIDI data to the specified file
            midi.write(file_path)
            print(f"MIDI file saved at: {file_path}")


    def load_from_midi(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Load MIDI", "", "MIDI Files (*.mid)", options=options)
        if file_path:
            midi = pretty_midi.PrettyMIDI(file_path)

            notes = []
            for instrument in midi.instruments:
                for note in instrument.notes:
                    notes.append([note.pitch, note.end - note.start, note.velocity, note.start])

            if not notes:
                return

            # Transpose the data: This swaps rows and columns
            transposed_data = list(zip(*notes))  # Transpose rows and columns

            # Set the number of rows and columns based on transposed data
            self.tableWidget.setRowCount(len(transposed_data))  # Set number of rows to the number of columns from original data
            self.tableWidget.setColumnCount(len(transposed_data[0]))  # Set number of columns to the number of rows from original data

            # Set proper headers for flipped table layout
            self.tableWidget.setHorizontalHeaderLabels([f"Note {i+1}" for i in range(len(transposed_data[0]))])
            self.tableWidget.setVerticalHeaderLabels(["Note", "Duration", "Speed", "Start"])

            # Fill the table with transposed data
            for row in range(len(transposed_data)):
                for col in range(len(transposed_data[row])):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(transposed_data[row][col])))

    def array_to_table(self):
        try:
            array_data = eval(self.array_input.text())
            if isinstance(array_data, list) and all(isinstance(row, list) for row in array_data):
                self.tableWidget.setRowCount(len(array_data))
                self.tableWidget.setColumnCount(len(array_data[0]))
                for col_idx, row in enumerate(array_data):
                    for row_idx, value in enumerate(row):
                        self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except Exception as e:
            print(f"Invalid input: {e}")

    def print_table(self):
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        for row in range(rows):
            for col in range(cols):
                item = self.tableWidget.item(row, col)
                if item:
                    print(item.text(), end=" ")
                else:
                    print("None", end=" ")
            print()

    def help_clicked(self):
        QtWidgets.QMessageBox.information(self, "Help", "This is the Advanced Window Help section.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
