# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flashcards.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 270)
        MainWindow.setMinimumSize(QtCore.QSize(580, 270))
        MainWindow.setMaximumSize(QtCore.QSize(1160, 540))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 591, 281))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 10, 281, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(390, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(30, 40, 521, 151))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 16, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 4, 0, 4)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.settingsButton = QtWidgets.QPushButton(self.tab)
        self.settingsButton.setGeometry(QtCore.QRect(480, 210, 75, 23))
        self.settingsButton.setObjectName("settingsButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 551, 181))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 199, 451, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.practiceCancelBtn = QtWidgets.QPushButton(self.tab_2)
        self.practiceCancelBtn.setGeometry(QtCore.QRect(470, 200, 91, 31))
        self.practiceCancelBtn.setObjectName("practiceCancelBtn")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.removeButton = QtWidgets.QPushButton(self.tab_3)
        self.removeButton.setGeometry(QtCore.QRect(480, 130, 75, 23))
        self.removeButton.setObjectName("removeButton")
        self.addButton = QtWidgets.QPushButton(self.tab_3)
        self.addButton.setGeometry(QtCore.QRect(480, 90, 75, 23))
        self.addButton.setObjectName("addButton")
        self.createButton = QtWidgets.QPushButton(self.tab_3)
        self.createButton.setGeometry(QtCore.QRect(480, 210, 75, 23))
        self.createButton.setObjectName("createButton")
        self.editButton = QtWidgets.QPushButton(self.tab_3)
        self.editButton.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.editButton.setObjectName("editButton")
        self.importButton = QtWidgets.QPushButton(self.tab_3)
        self.importButton.setGeometry(QtCore.QRect(480, 10, 75, 23))
        self.importButton.setObjectName("importButton")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(240, 210, 31, 20))
        self.label_2.setObjectName("label_2")
        self.inputName = QtWidgets.QLineEdit(self.tab_3)
        self.inputName.setGeometry(QtCore.QRect(280, 210, 181, 20))
        self.inputName.setObjectName("inputName")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 451, 189))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 449, 187))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableView = QtWidgets.QTableView(self.scrollAreaWidgetContents_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 451, 191))
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setDefaultSectionSize(21)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flashcard Whiz"))
        self.label.setText(_translate("MainWindow", "Select the decks you want to practice:"))
        self.pushButton.setText(_translate("MainWindow", "Practice"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Selection"))
        self.practiceCancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Practice"))
        self.removeButton.setText(_translate("MainWindow", "Delete card"))
        self.addButton.setText(_translate("MainWindow", "Add card"))
        self.createButton.setText(_translate("MainWindow", "Create"))
        self.editButton.setText(_translate("MainWindow", "Edit deck"))
        self.importButton.setText(_translate("MainWindow", "Import deck"))
        self.label_2.setText(_translate("MainWindow", "NAME:"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Create"))
