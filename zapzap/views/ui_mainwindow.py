# Form implementation generated from reading ui file './zapzap/ui/ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuChat = QtWidgets.QMenu(parent=self.menubar)
        self.menuChat.setObjectName("menuChat")
        self.menuUsers = QtWidgets.QMenu(parent=self.menubar)
        self.menuUsers.setObjectName("menuUsers")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHide = QtGui.QAction(parent=MainWindow)
        self.actionHide.setObjectName("actionHide")
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionReset_zoom = QtGui.QAction(parent=MainWindow)
        self.actionReset_zoom.setObjectName("actionReset_zoom")
        self.actionZoom_in = QtGui.QAction(parent=MainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtGui.QAction(parent=MainWindow)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionToggle_full_screen = QtGui.QAction(parent=MainWindow)
        self.actionToggle_full_screen.setObjectName("actionToggle_full_screen")
        self.actionReload = QtGui.QAction(parent=MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionNew_chat = QtGui.QAction(parent=MainWindow)
        self.actionNew_chat.setObjectName("actionNew_chat")
        self.actionBy_phone_number = QtGui.QAction(parent=MainWindow)
        self.actionBy_phone_number.setObjectName("actionBy_phone_number")
        self.actionShortcuts = QtGui.QAction(parent=MainWindow)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionSobre_o_ZapZap = QtGui.QAction(parent=MainWindow)
        self.actionSobre_o_ZapZap.setObjectName("actionSobre_o_ZapZap")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHide)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionToggle_full_screen)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionReset_zoom)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuChat.addAction(self.actionReload)
        self.menuChat.addSeparator()
        self.menuChat.addAction(self.actionNew_chat)
        self.menuChat.addAction(self.actionBy_phone_number)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuHelp.addAction(self.actionSobre_o_ZapZap)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuChat.menuAction())
        self.menubar.addAction(self.menuUsers.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuChat.setTitle(_translate("MainWindow", "Chat"))
        self.menuUsers.setTitle(_translate("MainWindow", "Users"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionHide.setText(_translate("MainWindow", "Hide"))
        self.actionHide.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionReset_zoom.setText(_translate("MainWindow", "Reset zoom"))
        self.actionReset_zoom.setShortcut(_translate("MainWindow", "Ctrl+0"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in"))
        self.actionZoom_in.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out"))
        self.actionZoom_out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionToggle_full_screen.setText(_translate("MainWindow", "Toggle full screen"))
        self.actionToggle_full_screen.setShortcut(_translate("MainWindow", "F11"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionReload.setShortcut(_translate("MainWindow", "F5"))
        self.actionNew_chat.setText(_translate("MainWindow", "New chat"))
        self.actionNew_chat.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionBy_phone_number.setText(_translate("MainWindow", "By number phone"))
        self.actionBy_phone_number.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionShortcuts.setText(_translate("MainWindow", "Keyboard shortcuts"))
        self.actionSobre_o_ZapZap.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
