# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiplucker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pythonosc.udp_client import SimpleUDPClient
import pprint
ip = "127.0.0.1"
port = 12000

client = SimpleUDPClient(ip, port)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 488)
        self.default_chord = [["On", 0.0]]
        self.default_strum = [["UP", 0.0]]
        self.e_melody = [[41, 1.0, 5, 0.0], [42, 1.0, 5, 1.0], [44, 1.0, 5, 2.0], [46, 1.0, 5, 3.0]]
        self.d_melody = [[51, 1.0, 5, 0.0], [52, 1.0, 5, 1.0], [54, 1.0, 5, 2.0], [56, 1.0, 5, 3.0]]
        self.b_melody = [[59, 1.0, 5, 0.0], [60, 1.0, 5, 1.0], [62, 1.0, 5, 2.0], [64, 1.0, 5, 3.0]]
        self.duration_indefinite = 10
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 240, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 120, 55, 16))
        self.label_5.setObjectName("label_5")
        self.speed_e_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_e_edit.setGeometry(QtCore.QRect(240, 160, 101, 22))
        self.speed_e_edit.setObjectName("speed_e_edit")
        self.speed_d_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_d_edit.setGeometry(QtCore.QRect(240, 200, 101, 22))
        self.speed_d_edit.setObjectName("speed_d_edit")
        self.speed_b_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_b_edit.setGeometry(QtCore.QRect(240, 240, 101, 22))
        self.speed_b_edit.setObjectName("speed_b_edit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 120, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.note_e_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.note_e_edit.setGeometry(QtCore.QRect(130, 160, 101, 22))
        self.note_e_edit.setObjectName("note_e_edit")
        self.note_d_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.note_d_edit.setGeometry(QtCore.QRect(130, 200, 101, 22))
        self.note_d_edit.setObjectName("note_d_edit")
        self.note_b_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.note_b_edit.setGeometry(QtCore.QRect(130, 240, 101, 22))
        self.note_b_edit.setObjectName("note_b_edit")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(350, 280, 93, 28))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(lambda: self.start_string("all"))
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(450, 280, 93, 28))
        self.pause_button.setObjectName("pause_button")
        self.calibrate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calibrate_button.setGeometry(QtCore.QRect(510, 50, 93, 28))
        self.calibrate_button.setObjectName("calibrate_button")
        self.melody_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.melody_all_button.setGeometry(QtCore.QRect(550, 280, 93, 28))
        self.melody_all_button.setObjectName("melody_all_button")
        self.melody_all_button.clicked.connect(lambda: self.get_array("all"))
        self.pause_button_e = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button_e.setGeometry(QtCore.QRect(450, 160, 93, 28))
        self.pause_button_e.setObjectName("pause_button_e")
        self.pause_button_e.clicked.connect(self.pause_sequence)
        self.start_button_e = QtWidgets.QPushButton(self.centralwidget)
        self.start_button_e.setGeometry(QtCore.QRect(350, 160, 93, 28))
        self.start_button_e.setObjectName("start_button_e")
        self.start_button_e.clicked.connect(lambda: self.start_string("e"))
        self.pause_button_d = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button_d.setGeometry(QtCore.QRect(450, 200, 93, 28))
        self.pause_button_d.setObjectName("pause_button_d")
        self.pause_button_d.clicked.connect(self.pause_sequence)
        self.start_button_d = QtWidgets.QPushButton(self.centralwidget)
        self.start_button_d.setGeometry(QtCore.QRect(350, 200, 93, 28))
        self.start_button_d.setObjectName("start_button_d")
        self.start_button_d.clicked.connect(lambda: self.start_string("b"))
        self.pause_button_b = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button_b.setGeometry(QtCore.QRect(450, 240, 93, 28))
        self.pause_button_b.setObjectName("pause_button_b")
        self.pause_button_b.clicked.connect(self.pause_sequence)
        self.start_button_b = QtWidgets.QPushButton(self.centralwidget)
        self.start_button_b.setGeometry(QtCore.QRect(350, 240, 93, 28))
        self.start_button_b.setObjectName("start_button_b")
        self.start_button_b.clicked.connect(lambda: self.start_string("b"))
        self.melody_b = QtWidgets.QPushButton(self.centralwidget)
        self.melody_b.setGeometry(QtCore.QRect(550, 240, 93, 28))
        self.melody_b.setObjectName("melody_b")
        self.melody_b.clicked.connect(lambda: self.get_array("b"))
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 120, 81, 16))
        self.label_9.setObjectName("label_9")
        self.melody_e = QtWidgets.QPushButton(self.centralwidget)
        self.melody_e.setGeometry(QtCore.QRect(550, 160, 93, 28))
        self.melody_e.setObjectName("melody_e")
        self.melody_e.clicked.connect(lambda: self.get_array("e"))
        self.melody_d = QtWidgets.QPushButton(self.centralwidget)
        self.melody_d.setGeometry(QtCore.QRect(550, 200, 93, 28))
        self.melody_d.setObjectName("melody_d")
        self.melody_d.clicked.connect(lambda: self.get_array("d"))
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 120, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 120, 55, 16))
        self.label_10.setObjectName("label_10")
        self.message_text = QtWidgets.QTextEdit(self.centralwidget)
        self.message_text.setGeometry(QtCore.QRect(130, 320, 511, 101))
        self.message_text.setObjectName("message_text")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(60, 350, 61, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(460, 50, 71, 16))
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Multi-plucker UI"))
        self.label_2.setText(_translate("MainWindow", "E:"))
        self.label_3.setText(_translate("MainWindow", "D:"))
        self.label_4.setText(_translate("MainWindow", "B:"))
        self.label_5.setText(_translate("MainWindow", "Strings:"))
        self.label_6.setText(_translate("MainWindow", "Speed"))
        self.label_7.setText(_translate("MainWindow", "Note (MIDI)"))
        self.start_button.setText(_translate("MainWindow", "Start All"))
        self.pause_button.setText(_translate("MainWindow", "Pause All"))
        self.calibrate_button.setText(_translate("MainWindow", "Calibrate"))
        self.melody_all_button.setText(_translate("MainWindow", "Melody All"))
        self.pause_button_e.setText(_translate("MainWindow", "Pause (E)"))
        self.start_button_e.setText(_translate("MainWindow", "Start (E)"))
        self.pause_button_d.setText(_translate("MainWindow", "Pause (D)"))
        self.start_button_d.setText(_translate("MainWindow", "Start (D)"))
        self.pause_button_b.setText(_translate("MainWindow", "Pause (B)"))
        self.start_button_b.setText(_translate("MainWindow", "Start (B)"))
        self.melody_b.setText(_translate("MainWindow", "Melody (B)"))
        self.label_9.setText(_translate("MainWindow", "Melody Start"))
        self.melody_e.setText(_translate("MainWindow", "Melody (E)"))
        self.melody_d.setText(_translate("MainWindow", "Melody (D)"))
        self.label_8.setText(_translate("MainWindow", "Start"))
        self.label_10.setText(_translate("MainWindow", "Pause"))
        self.message_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Message:"))
        self.label_12.setText(_translate("MainWindow", "Reset:"))

    def update_message(self, message):
        self.message_text.append(message)
    
    def start_string(self, string):
        if string == "e":
        #40-49 e
            e_string = [[int(self.note_e_edit.text()), int(self.duration_indefinite), int(self.speed_e_edit.text()), 0.0]]
            self.update_message("Starting E String...")
            self.update_message(str(e_string))
            self.send_to_udp(e_string)
        if string == "d":
        #50-58 d
            d_string = [[int(self.note_d_edit.text()), int(self.duration_indefinite), int(self.speed_d_edit.text()), 0.0]]
            self.update_message("Starting D String...")
            self.update_message(str(d_string))
            self.send_to_udp(d_string)
        if string == "b":
        #59-68 b
            b_string = [[int(self.note_b_edit.text()), int(self.duration_indefinite), int(self.speed_b_edit.text()), 0.0]]
            self.update_message("Starting B String...")
            self.update_message(str(b_string))
            self.send_to_udp(b_string)
        if string == "all":
            self.update_message("Starting All Strings...")
            all_strings = []
            all_strings.append([int(self.note_e_edit.text()), int(self.duration_indefinite), int(self.speed_e_edit.text()), 0.0])
            all_strings.append([int(self.note_d_edit.text()), int(self.duration_indefinite), int(self.speed_d_edit.text()), 0.0])
            all_strings.append([int(self.note_b_edit.text()), int(self.duration_indefinite), int(self.speed_b_edit.text()), 0.0])
            for note in all_strings:
                self.update_message(str(note))
            self.send_to_udp(all_strings)



    def pause_sequence(self, string):
        pass
    
    def get_array(self, string):
        if string == "e":
            self.update_message("Starting E melody...")
            self.update_message(str(pprint.pformat(self.e_melody)))
            self.send_to_udp(self.e_melody)
        if string == "d":
            self.update_message("Starting D melody...")
            self.update_message(str(pprint.pformat(self.d_melody)))
            self.send_to_udp(self.d_melody)
        if string == "b":
            self.update_message("Starting B melody...")
            self.update_message(str(pprint.pformat(self.b_melody)))
            self.send_to_udp(self.b_melody)
        if string == "all":
            self.update_message("Starting All Strings Melody...")
            all_string_melody = []
            for i in range(len(self.e_melody)):
                all_string_melody.append(self.e_melody[i])
                all_string_melody.append(self.d_melody[i])
                all_string_melody.append(self.b_melody[i])
            self.update_message(str(pprint.pformat(all_string_melody)))
            self.send_to_udp(all_string_melody)
                
    
    def send_to_udp(self, arr):
        self.default_chord[0][1] = arr[len(arr)-1][3] + 1
        print(f"Sending message to /Chord: {self.default_chord}")
        print(f"Sending message to /Strum: {self.default_strum}")
        print(f"Sending message to /Pluck: {pprint.pformat(arr)}")
        client.send_message("/Chord", self.default_chord)
        client.send_message("/Strum", self.default_strum)
        client.send_message("/Pluck", arr)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
