# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login/login_ui.ui'
#
# Created: Fri Jan 30 16:29:52 2015
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fr_Main(object):
    def setupUi(self, fr_Main):
        fr_Main.setObjectName(_fromUtf8("fr_Main"))
        fr_Main.resize(743, 575)
        fr_Main.setStyleSheet(_fromUtf8("background:white;"))
        fr_Main.setFrameShape(QtGui.QFrame.StyledPanel)
        fr_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.igr_Main = QtGui.QGridLayout(fr_Main)
        self.igr_Main.setObjectName(_fromUtf8("igr_Main"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Main.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Main.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Main.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Main.addItem(spacerItem3, 2, 1, 1, 1)
        self.st_Main = QtGui.QStackedWidget(fr_Main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.st_Main.sizePolicy().hasHeightForWidth())
        self.st_Main.setSizePolicy(sizePolicy)
        self.st_Main.setMinimumSize(QtCore.QSize(480, 320))
        self.st_Main.setMaximumSize(QtCore.QSize(480, 320))
        self.st_Main.setStyleSheet(_fromUtf8("QPushButton{border-style:outset;border-width:1px;border-radius:4px;border-color:rgb(156, 156, 156);background-color:#ffffff;min-height:25px;}"))
        self.st_Main.setObjectName(_fromUtf8("st_Main"))
        self.st_Connect = QtGui.QWidget()
        self.st_Connect.setObjectName(_fromUtf8("st_Connect"))
        self.fr_Connect = QtGui.QFrame(self.st_Connect)
        self.fr_Connect.setGeometry(QtCore.QRect(90, 70, 301, 111))
        self.fr_Connect.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Connect.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Connect.setObjectName(_fromUtf8("fr_Connect"))
        self.formLayout = QtGui.QFormLayout(self.fr_Connect)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lb_Connect_Judul = QtGui.QLabel(self.fr_Connect)
        self.lb_Connect_Judul.setObjectName(_fromUtf8("lb_Connect_Judul"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_Connect_Judul)
        self.lb_Connect_Alamat = QtGui.QLabel(self.fr_Connect)
        self.lb_Connect_Alamat.setObjectName(_fromUtf8("lb_Connect_Alamat"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lb_Connect_Alamat)
        self.le_Connect_Alamat = QtGui.QLineEdit(self.fr_Connect)
        self.le_Connect_Alamat.setObjectName(_fromUtf8("le_Connect_Alamat"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.le_Connect_Alamat)
        self.chk_Connect_Lokal = QtGui.QCheckBox(self.fr_Connect)
        self.chk_Connect_Lokal.setObjectName(_fromUtf8("chk_Connect_Lokal"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.chk_Connect_Lokal)
        self.tb_Connect_Ok = QtGui.QPushButton(self.st_Connect)
        self.tb_Connect_Ok.setGeometry(QtCore.QRect(140, 190, 187, 27))
        self.tb_Connect_Ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Connect_Ok.setObjectName(_fromUtf8("tb_Connect_Ok"))
        self.st_Main.addWidget(self.st_Connect)
        self.st_Login = QtGui.QWidget()
        self.st_Login.setObjectName(_fromUtf8("st_Login"))
        self.fr_Login = QtGui.QFrame(self.st_Login)
        self.fr_Login.setGeometry(QtCore.QRect(80, 80, 321, 181))
        self.fr_Login.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Login.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Login.setObjectName(_fromUtf8("fr_Login"))
        self.ifl_Login = QtGui.QFormLayout(self.fr_Login)
        self.ifl_Login.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.ifl_Login.setObjectName(_fromUtf8("ifl_Login"))
        self.lb_Login_Judul = QtGui.QLabel(self.fr_Login)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_Login_Judul.setFont(font)
        self.lb_Login_Judul.setObjectName(_fromUtf8("lb_Login_Judul"))
        self.ifl_Login.setWidget(0, QtGui.QFormLayout.FieldRole, self.lb_Login_Judul)
        self.lb_Login_User = QtGui.QLabel(self.fr_Login)
        self.lb_Login_User.setObjectName(_fromUtf8("lb_Login_User"))
        self.ifl_Login.setWidget(3, QtGui.QFormLayout.LabelRole, self.lb_Login_User)
        self.le_Login_User = QtGui.QLineEdit(self.fr_Login)
        self.le_Login_User.setObjectName(_fromUtf8("le_Login_User"))
        self.ifl_Login.setWidget(3, QtGui.QFormLayout.FieldRole, self.le_Login_User)
        self.lb_Login_Password = QtGui.QLabel(self.fr_Login)
        self.lb_Login_Password.setObjectName(_fromUtf8("lb_Login_Password"))
        self.ifl_Login.setWidget(4, QtGui.QFormLayout.LabelRole, self.lb_Login_Password)
        self.le_Login_Password = QtGui.QLineEdit(self.fr_Login)
        self.le_Login_Password.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.le_Login_Password.setObjectName(_fromUtf8("le_Login_Password"))
        self.ifl_Login.setWidget(4, QtGui.QFormLayout.FieldRole, self.le_Login_Password)
        self.le_Login_Password_Confirm = QtGui.QLineEdit(self.fr_Login)
        self.le_Login_Password_Confirm.setObjectName(_fromUtf8("le_Login_Password_Confirm"))
        self.ifl_Login.setWidget(5, QtGui.QFormLayout.FieldRole, self.le_Login_Password_Confirm)
        self.lb_Login_Password_Confirm = QtGui.QLabel(self.fr_Login)
        self.lb_Login_Password_Confirm.setObjectName(_fromUtf8("lb_Login_Password_Confirm"))
        self.ifl_Login.setWidget(5, QtGui.QFormLayout.LabelRole, self.lb_Login_Password_Confirm)
        self.tb_Login_Ok = QtGui.QPushButton(self.st_Login)
        self.tb_Login_Ok.setGeometry(QtCore.QRect(200, 220, 85, 27))
        self.tb_Login_Ok.setObjectName(_fromUtf8("tb_Login_Ok"))
        self.st_Main.addWidget(self.st_Login)
        self.st_Database = QtGui.QWidget()
        self.st_Database.setObjectName(_fromUtf8("st_Database"))
        self.fr_Database = QtGui.QFrame(self.st_Database)
        self.fr_Database.setGeometry(QtCore.QRect(110, 10, 271, 301))
        self.fr_Database.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Database.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Database.setObjectName(_fromUtf8("fr_Database"))
        self.igr_Database = QtGui.QGridLayout(self.fr_Database)
        self.igr_Database.setObjectName(_fromUtf8("igr_Database"))
        self.sc_Database_List = QtGui.QScrollArea(self.fr_Database)
        self.sc_Database_List.setWidgetResizable(True)
        self.sc_Database_List.setObjectName(_fromUtf8("sc_Database_List"))
        self.scontent_Database_List = QtGui.QWidget()
        self.scontent_Database_List.setGeometry(QtCore.QRect(0, 0, 249, 199))
        self.scontent_Database_List.setObjectName(_fromUtf8("scontent_Database_List"))
        self.ivl_Database_ListContent = QtGui.QVBoxLayout(self.scontent_Database_List)
        self.ivl_Database_ListContent.setObjectName(_fromUtf8("ivl_Database_ListContent"))
        self.sc_Database_List.setWidget(self.scontent_Database_List)
        self.igr_Database.addWidget(self.sc_Database_List, 2, 0, 1, 1)
        self.le_Database_Search = QtGui.QLineEdit(self.fr_Database)
        self.le_Database_Search.setObjectName(_fromUtf8("le_Database_Search"))
        self.igr_Database.addWidget(self.le_Database_Search, 1, 0, 1, 1)
        self.lb_Database_Judul = QtGui.QLabel(self.fr_Database)
        self.lb_Database_Judul.setObjectName(_fromUtf8("lb_Database_Judul"))
        self.igr_Database.addWidget(self.lb_Database_Judul, 0, 0, 1, 1)
        self.tb_Database_Create = QtGui.QPushButton(self.fr_Database)
        self.tb_Database_Create.setObjectName(_fromUtf8("tb_Database_Create"))
        self.igr_Database.addWidget(self.tb_Database_Create, 3, 0, 1, 1)
        self.st_Main.addWidget(self.st_Database)
        self.igr_Main.addWidget(self.st_Main, 1, 1, 1, 1)

        self.retranslateUi(fr_Main)
        self.st_Main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fr_Main)

    def retranslateUi(self, fr_Main):
        fr_Main.setWindowTitle(_translate("fr_Main", "Frame", None))
        self.lb_Connect_Judul.setText(_translate("fr_Main", "Pilih Server", None))
        self.lb_Connect_Alamat.setText(_translate("fr_Main", "Alamat Server :", None))
        self.le_Connect_Alamat.setText(_translate("fr_Main", "localhost", None))
        self.chk_Connect_Lokal.setText(_translate("fr_Main", "Lokal komputer ini", None))
        self.tb_Connect_Ok.setText(_translate("fr_Main", "OK", None))
        self.lb_Login_Judul.setText(_translate("fr_Main", "Login ", None))
        self.lb_Login_User.setText(_translate("fr_Main", "User", None))
        self.le_Login_User.setText(_translate("fr_Main", "admin", None))
        self.lb_Login_Password.setText(_translate("fr_Main", "Password", None))
        self.lb_Login_Password_Confirm.setText(_translate("fr_Main", "Confirm :", None))
        self.tb_Login_Ok.setText(_translate("fr_Main", "OK", None))
        self.lb_Database_Judul.setText(_translate("fr_Main", "Pilih Database Perusahaan", None))
        self.tb_Database_Create.setText(_translate("fr_Main", "Buat Database Baru", None))

