# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\OwnCloud\Maua\6 ano\ECA703 - Trabalho de Conclusao de Curso\4-Programa\ui\Sketch.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(967, 525)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/vmarq/Desktop/Capture.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 420, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 169, 128))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 171, 41))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_8.addWidget(self.groupBox_3)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(220, 230, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 370, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 263, 210, 93))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_4.addWidget(self.checkBox_9)
        self.checkBox_16 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_4.addWidget(self.checkBox_16)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(280, 263, 210, 93))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_5.addWidget(self.checkBox_12, 0, QtCore.Qt.AlignLeft)
        self.checkBox_13 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_5.addWidget(self.checkBox_13)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab)
        self.layoutWidget4.setGeometry(QtCore.QRect(510, 60, 400, 270))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_14.addWidget(self.label_4)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget4)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_14.addWidget(self.calendarWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(120, 20, 680, 231))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget5)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 8, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.tableWidget)
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(720, 300, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(640, 300, 44, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.layoutWidget6 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget6.setGeometry(QtCore.QRect(610, 330, 251, 74))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_9.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_9.addWidget(self.pushButton_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_10.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget6)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_10.addWidget(self.lineEdit_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 260, 80, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.layoutWidget7 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget7.setGeometry(QtCore.QRect(50, 310, 501, 101))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_17.addWidget(self.label_10)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget7)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.verticalLayout_16.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.verticalLayout_16.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_18.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_15.addWidget(self.label_20)
        self.verticalLayout_15.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_17.addWidget(self.label_21)
        self.verticalLayout_15.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18.addLayout(self.verticalLayout_15)
        self.verticalLayout_17.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_25.addLayout(self.verticalLayout_17)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget7)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_12.addWidget(self.pushButton_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget7)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_12.addWidget(self.pushButton_7)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget7)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_11.addWidget(self.pushButton_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget7)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_11.addWidget(self.pushButton_11)
        self.horizontalLayout_9.addLayout(self.verticalLayout_11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_25.addLayout(self.verticalLayout_13)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.layoutWidget8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget8.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "H3V Solucoes"))
        self.groupBox.setTitle(_translate("MainWindow", "Doutores"))
        self.radioButton.setText(_translate("MainWindow", "Dra. Alice"))
        self.radioButton_2.setText(_translate("MainWindow", "Dr. Humberto"))
        self.radioButton_3.setText(_translate("MainWindow", "Dra. Andreia"))
        self.radioButton_4.setText(_translate("MainWindow", "Dr. Hans Chucrutes"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Paciente"))
        self.label_6.setText(_translate("MainWindow", "Prescrição"))
        self.pushButton_3.setText(_translate("MainWindow", "Prescrever"))
        self.checkBox_9.setText(_translate("MainWindow", "Neosoro"))
        self.checkBox_16.setText(_translate("MainWindow", "Puran T4"))
        self.label_2.setText(_translate("MainWindow", "XXX"))
        self.label_3.setText(_translate("MainWindow", "XXX"))
        self.checkBox_12.setText(_translate("MainWindow", "Alegra"))
        self.checkBox_13.setText(_translate("MainWindow", "Salonpas"))
        self.label_12.setText(_translate("MainWindow", "XXX"))
        self.label_14.setText(_translate("MainWindow", "XXX"))
        self.label_4.setText(_translate("MainWindow", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Prescrição Médica"))
        self.label_7.setText(_translate("MainWindow", "Fila dos pedidos"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_18.setText(_translate("MainWindow", "Nº Pedido"))
        self.label_8.setText(_translate("MainWindow", "Ações"))
        self.pushButton.setText(_translate("MainWindow", "Resgatar pedido"))
        self.pushButton_2.setText(_translate("MainWindow", "Deletar pedido"))
        self.pushButton_5.setText(_translate("MainWindow", "Atualizar fila"))
        self.label_10.setText(_translate("MainWindow", "Estoque atual"))
        self.label.setText(_translate("MainWindow", "Neosoro"))
        self.label_17.setText(_translate("MainWindow", "N"))
        self.label_5.setText(_translate("MainWindow", "Puran T4"))
        self.label_15.setText(_translate("MainWindow", "N"))
        self.label_11.setText(_translate("MainWindow", "Alegra"))
        self.label_20.setText(_translate("MainWindow", "N"))
        self.label_13.setText(_translate("MainWindow", "Salonpas"))
        self.label_21.setText(_translate("MainWindow", "N"))
        self.label_9.setText(_translate("MainWindow", "Repor estoques"))
        self.pushButton_4.setText(_translate("MainWindow", "Neosoro"))
        self.pushButton_7.setText(_translate("MainWindow", "Puran T4"))
        self.pushButton_8.setText(_translate("MainWindow", "Alegra"))
        self.pushButton_11.setText(_translate("MainWindow", "Salonpas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Resgate Farmacêutico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())