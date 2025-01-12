# Form implementation generated from reading ui file './zapzap/ui/ui_browser.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Browser(object):
    def setupUi(self, Browser):
        Browser.setObjectName("Browser")
        Browser.resize(1137, 606)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Browser)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browser_sidebar = QtWidgets.QFrame(parent=Browser)
        self.browser_sidebar.setMinimumSize(QtCore.QSize(50, 0))
        self.browser_sidebar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.browser_sidebar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.browser_sidebar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.browser_sidebar.setObjectName("browser_sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.browser_sidebar)
        self.verticalLayout.setContentsMargins(5, 6, 5, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.page_buttons_layout = QtWidgets.QVBoxLayout()
        self.page_buttons_layout.setSpacing(0)
        self.page_buttons_layout.setObjectName("page_buttons_layout")
        self.verticalLayout.addLayout(self.page_buttons_layout)
        self.line = QtWidgets.QFrame(parent=self.browser_sidebar)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.settings_buttons_layout = QtWidgets.QFrame(parent=self.browser_sidebar)
        self.settings_buttons_layout.setObjectName("settings_buttons_layout")
        self.layout_2 = QtWidgets.QVBoxLayout(self.settings_buttons_layout)
        self.layout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_2.setSpacing(6)
        self.layout_2.setObjectName("layout_2")
        self.btn_new_account = QtWidgets.QPushButton(parent=self.settings_buttons_layout)
        self.btn_new_account.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_new_account.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_new_account.setText("")
        self.btn_new_account.setIconSize(QtCore.QSize(20, 20))
        self.btn_new_account.setFlat(False)
        self.btn_new_account.setObjectName("btn_new_account")
        self.layout_2.addWidget(self.btn_new_account)
        spacerItem = QtWidgets.QSpacerItem(20, 473, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.layout_2.addItem(spacerItem)
        self.btn_new_chat_number = QtWidgets.QPushButton(parent=self.settings_buttons_layout)
        self.btn_new_chat_number.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_new_chat_number.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_new_chat_number.setText("")
        self.btn_new_chat_number.setIconSize(QtCore.QSize(20, 20))
        self.btn_new_chat_number.setObjectName("btn_new_chat_number")
        self.layout_2.addWidget(self.btn_new_chat_number)
        self.btn_new_chat = QtWidgets.QPushButton(parent=self.settings_buttons_layout)
        self.btn_new_chat.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_new_chat.setText("")
        self.btn_new_chat.setIconSize(QtCore.QSize(20, 20))
        self.btn_new_chat.setObjectName("btn_new_chat")
        self.layout_2.addWidget(self.btn_new_chat)
        self.line_2 = QtWidgets.QFrame(parent=self.settings_buttons_layout)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.layout_2.addWidget(self.line_2)
        self.btn_open_settings = QtWidgets.QPushButton(parent=self.settings_buttons_layout)
        self.btn_open_settings.setMinimumSize(QtCore.QSize(35, 35))
        self.btn_open_settings.setText("")
        self.btn_open_settings.setIconSize(QtCore.QSize(20, 20))
        self.btn_open_settings.setObjectName("btn_open_settings")
        self.layout_2.addWidget(self.btn_open_settings)
        self.verticalLayout.addWidget(self.settings_buttons_layout)
        self.horizontalLayout.addWidget(self.browser_sidebar)
        self.pages = QtWidgets.QStackedWidget(parent=Browser)
        self.pages.setObjectName("pages")
        self.horizontalLayout.addWidget(self.pages)

        self.retranslateUi(Browser)
        QtCore.QMetaObject.connectSlotsByName(Browser)

    def retranslateUi(self, Browser):
        _translate = QtCore.QCoreApplication.translate
        Browser.setWindowTitle(_translate("Browser", "Form"))
        self.btn_new_account.setToolTip(_translate("Browser", "Novo usuário"))
        self.btn_new_chat_number.setToolTip(_translate("Browser", "New conversation by the phone number"))
        self.btn_new_chat.setToolTip(_translate("Browser", "New conversation"))
        self.btn_open_settings.setToolTip(_translate("Browser", "ZapZap Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Browser = QtWidgets.QWidget()
    ui = Ui_Browser()
    ui.setupUi(Browser)
    Browser.show()
    sys.exit(app.exec())
