# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login/admin_ui.ui'
#
# Created: Tue Feb 10 17:24:49 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_fr_Admin(object):
    def setupUi(self, fr_Admin):
        fr_Admin.setObjectName(_fromUtf8("fr_Admin"))
        fr_Admin.resize(679, 571)
        fr_Admin.setStyleSheet(_fromUtf8("QFrame{\n"
"    border:0px;\n"
"}"))
        fr_Admin.setFrameShape(QtGui.QFrame.StyledPanel)
        fr_Admin.setFrameShadow(QtGui.QFrame.Raised)
        self.igr_Admin = QtGui.QGridLayout(fr_Admin)
        self.igr_Admin.setObjectName(_fromUtf8("igr_Admin"))
        self.st_Admin = QtGui.QStackedWidget(fr_Admin)
        self.st_Admin.setObjectName(_fromUtf8("st_Admin"))
        self.st_Menu = QtGui.QWidget()
        self.st_Menu.setObjectName(_fromUtf8("st_Menu"))
        self.igr_Menu = QtGui.QGridLayout(self.st_Menu)
        self.igr_Menu.setObjectName(_fromUtf8("igr_Menu"))
        self.tb_TutupAdmin = QtGui.QPushButton(self.st_Menu)
        self.tb_TutupAdmin.setMinimumSize(QtCore.QSize(40, 40))
        self.tb_TutupAdmin.setMaximumSize(QtCore.QSize(100, 40))
        self.tb_TutupAdmin.setObjectName(_fromUtf8("tb_TutupAdmin"))
        self.igr_Menu.addWidget(self.tb_TutupAdmin, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Menu.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Menu.addItem(spacerItem1, 1, 0, 1, 1)
        self.fr_Main = QtGui.QFrame(self.st_Menu)
        self.fr_Main.setMinimumSize(QtCore.QSize(320, 240))
        self.fr_Main.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Main.setObjectName(_fromUtf8("fr_Main"))
        self.tb_EditAdmin = QtGui.QPushButton(self.fr_Main)
        self.tb_EditAdmin.setGeometry(QtCore.QRect(70, 130, 191, 61))
        self.tb_EditAdmin.setObjectName(_fromUtf8("tb_EditAdmin"))
        self.tb_ListUser = QtGui.QPushButton(self.fr_Main)
        self.tb_ListUser.setGeometry(QtCore.QRect(70, 60, 191, 61))
        self.tb_ListUser.setObjectName(_fromUtf8("tb_ListUser"))
        self.igr_Menu.addWidget(self.fr_Main, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Menu.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Menu.addItem(spacerItem3, 0, 1, 1, 1)
        self.st_Admin.addWidget(self.st_Menu)
        self.st_Users = QtGui.QWidget()
        self.st_Users.setObjectName(_fromUtf8("st_Users"))
        self.ivl_Users_Luar = QtGui.QVBoxLayout(self.st_Users)
        self.ivl_Users_Luar.setObjectName(_fromUtf8("ivl_Users_Luar"))
        self.lb_Users_Judul = QtGui.QLabel(self.st_Users)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lb_Users_Judul.sizePolicy().hasHeightForWidth())
        self.lb_Users_Judul.setSizePolicy(sizePolicy)
        self.lb_Users_Judul.setMinimumSize(QtCore.QSize(0, 25))
        self.lb_Users_Judul.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lb_Users_Judul.setObjectName(_fromUtf8("lb_Users_Judul"))
        self.ivl_Users_Luar.addWidget(self.lb_Users_Judul)
        self.tbl_ListUser_List = QtGui.QTableWidget(self.st_Users)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tbl_ListUser_List.sizePolicy().hasHeightForWidth())
        self.tbl_ListUser_List.setSizePolicy(sizePolicy)
        self.tbl_ListUser_List.setStyleSheet(_fromUtf8("QTableWidget{border-width:1px;border-color:rgb(150, 137, 188);border-style:outset;border-radius:0px;}"))
        self.tbl_ListUser_List.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tbl_ListUser_List.setObjectName(_fromUtf8("tbl_ListUser_List"))
        self.tbl_ListUser_List.setColumnCount(3)
        self.tbl_ListUser_List.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_ListUser_List.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_ListUser_List.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_ListUser_List.setHorizontalHeaderItem(2, item)
        self.ivl_Users_Luar.addWidget(self.tbl_ListUser_List)
        self.fr_Users = QtGui.QFrame(self.st_Users)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Users.sizePolicy().hasHeightForWidth())
        self.fr_Users.setSizePolicy(sizePolicy)
        self.fr_Users.setMinimumSize(QtCore.QSize(0, 30))
        self.fr_Users.setMaximumSize(QtCore.QSize(16777215, 40))
        self.fr_Users.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Users.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Users.setObjectName(_fromUtf8("fr_Users"))
        self.ihl_Users_Dalam = QtGui.QHBoxLayout(self.fr_Users)
        self.ihl_Users_Dalam.setObjectName(_fromUtf8("ihl_Users_Dalam"))
        self.tb_Users_Tambah = QtGui.QPushButton(self.fr_Users)
        self.tb_Users_Tambah.setObjectName(_fromUtf8("tb_Users_Tambah"))
        self.ihl_Users_Dalam.addWidget(self.tb_Users_Tambah)
        self.tb_Users_Ubah = QtGui.QPushButton(self.fr_Users)
        self.tb_Users_Ubah.setObjectName(_fromUtf8("tb_Users_Ubah"))
        self.ihl_Users_Dalam.addWidget(self.tb_Users_Ubah)
        self.tb_Users_Hapus = QtGui.QPushButton(self.fr_Users)
        self.tb_Users_Hapus.setObjectName(_fromUtf8("tb_Users_Hapus"))
        self.ihl_Users_Dalam.addWidget(self.tb_Users_Hapus)
        spacerItem4 = QtGui.QSpacerItem(258, 19, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ihl_Users_Dalam.addItem(spacerItem4)
        self.tb_Users_Tutup = QtGui.QPushButton(self.fr_Users)
        self.tb_Users_Tutup.setObjectName(_fromUtf8("tb_Users_Tutup"))
        self.ihl_Users_Dalam.addWidget(self.tb_Users_Tutup)
        self.ivl_Users_Luar.addWidget(self.fr_Users)
        self.st_Admin.addWidget(self.st_Users)
        self.st_Users_Tambah = QtGui.QWidget()
        self.st_Users_Tambah.setObjectName(_fromUtf8("st_Users_Tambah"))
        self.ivl_Users_Tambah_Luar = QtGui.QVBoxLayout(self.st_Users_Tambah)
        self.ivl_Users_Tambah_Luar.setObjectName(_fromUtf8("ivl_Users_Tambah_Luar"))
        self.fr_Users_Tambah_t = QtGui.QFrame(self.st_Users_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Users_Tambah_t.sizePolicy().hasHeightForWidth())
        self.fr_Users_Tambah_t.setSizePolicy(sizePolicy)
        self.fr_Users_Tambah_t.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_Users_Tambah_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_Users_Tambah_t.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Users_Tambah_t.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Users_Tambah_t.setObjectName(_fromUtf8("fr_Users_Tambah_t"))
        self.ihl_Users_Tambah_t = QtGui.QHBoxLayout(self.fr_Users_Tambah_t)
        self.ihl_Users_Tambah_t.setObjectName(_fromUtf8("ihl_Users_Tambah_t"))
        self.lb_Users_Tambah_Judul = QtGui.QLabel(self.fr_Users_Tambah_t)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Users_Tambah_Judul.setFont(font)
        self.lb_Users_Tambah_Judul.setObjectName(_fromUtf8("lb_Users_Tambah_Judul"))
        self.ihl_Users_Tambah_t.addWidget(self.lb_Users_Tambah_Judul)
        self.ivl_Users_Tambah_Luar.addWidget(self.fr_Users_Tambah_t)
        self.fr_Users_Tambah_Content = QtGui.QFrame(self.st_Users_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.fr_Users_Tambah_Content.sizePolicy().hasHeightForWidth())
        self.fr_Users_Tambah_Content.setSizePolicy(sizePolicy)
        self.fr_Users_Tambah_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Users_Tambah_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Users_Tambah_Content.setObjectName(_fromUtf8("fr_Users_Tambah_Content"))
        self.ifl_Users_Tambah_Content = QtGui.QFormLayout(self.fr_Users_Tambah_Content)
        self.ifl_Users_Tambah_Content.setObjectName(_fromUtf8("ifl_Users_Tambah_Content"))
        self.lb_Users_Tambah_Username = QtGui.QLabel(self.fr_Users_Tambah_Content)
        self.lb_Users_Tambah_Username.setObjectName(_fromUtf8("lb_Users_Tambah_Username"))
        self.ifl_Users_Tambah_Content.setWidget(0, QtGui.QFormLayout.LabelRole, self.lb_Users_Tambah_Username)
        self.lb_Users_Tambah_Password = QtGui.QLabel(self.fr_Users_Tambah_Content)
        self.lb_Users_Tambah_Password.setObjectName(_fromUtf8("lb_Users_Tambah_Password"))
        self.ifl_Users_Tambah_Content.setWidget(1, QtGui.QFormLayout.LabelRole, self.lb_Users_Tambah_Password)
        self.lb_Users_Tambah_Priviledge = QtGui.QLabel(self.fr_Users_Tambah_Content)
        self.lb_Users_Tambah_Priviledge.setObjectName(_fromUtf8("lb_Users_Tambah_Priviledge"))
        self.ifl_Users_Tambah_Content.setWidget(3, QtGui.QFormLayout.LabelRole, self.lb_Users_Tambah_Priviledge)
        self.le_Users_Tambah_Username = QtGui.QLineEdit(self.fr_Users_Tambah_Content)
        self.le_Users_Tambah_Username.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_Users_Tambah_Username.setObjectName(_fromUtf8("le_Users_Tambah_Username"))
        self.ifl_Users_Tambah_Content.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_Users_Tambah_Username)
        self.le_Users_Tambah_Password = QtGui.QLineEdit(self.fr_Users_Tambah_Content)
        self.le_Users_Tambah_Password.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_Users_Tambah_Password.setObjectName(_fromUtf8("le_Users_Tambah_Password"))
        self.ifl_Users_Tambah_Content.setWidget(1, QtGui.QFormLayout.FieldRole, self.le_Users_Tambah_Password)
        self.cb_Users_Tambah_Priviledge = QtGui.QComboBox(self.fr_Users_Tambah_Content)
        self.cb_Users_Tambah_Priviledge.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cb_Users_Tambah_Priviledge.setObjectName(_fromUtf8("cb_Users_Tambah_Priviledge"))
        self.cb_Users_Tambah_Priviledge.addItem(_fromUtf8(""))
        self.cb_Users_Tambah_Priviledge.addItem(_fromUtf8(""))
        self.cb_Users_Tambah_Priviledge.addItem(_fromUtf8(""))
        self.cb_Users_Tambah_Priviledge.addItem(_fromUtf8(""))
        self.cb_Users_Tambah_Priviledge.addItem(_fromUtf8(""))
        self.ifl_Users_Tambah_Content.setWidget(3, QtGui.QFormLayout.FieldRole, self.cb_Users_Tambah_Priviledge)
        self.lb_Users_Tambah_Password_Confirm = QtGui.QLabel(self.fr_Users_Tambah_Content)
        self.lb_Users_Tambah_Password_Confirm.setObjectName(_fromUtf8("lb_Users_Tambah_Password_Confirm"))
        self.ifl_Users_Tambah_Content.setWidget(2, QtGui.QFormLayout.LabelRole, self.lb_Users_Tambah_Password_Confirm)
        self.le_Users_Tambah_Password_Confirm = QtGui.QLineEdit(self.fr_Users_Tambah_Content)
        self.le_Users_Tambah_Password_Confirm.setMinimumSize(QtCore.QSize(200, 0))
        self.le_Users_Tambah_Password_Confirm.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_Users_Tambah_Password_Confirm.setObjectName(_fromUtf8("le_Users_Tambah_Password_Confirm"))
        self.ifl_Users_Tambah_Content.setWidget(2, QtGui.QFormLayout.FieldRole, self.le_Users_Tambah_Password_Confirm)
        self.ivl_Users_Tambah_Luar.addWidget(self.fr_Users_Tambah_Content)
        self.fr_Users_Tambah_b = QtGui.QFrame(self.st_Users_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Users_Tambah_b.sizePolicy().hasHeightForWidth())
        self.fr_Users_Tambah_b.setSizePolicy(sizePolicy)
        self.fr_Users_Tambah_b.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_Users_Tambah_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_Users_Tambah_b.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Users_Tambah_b.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Users_Tambah_b.setObjectName(_fromUtf8("fr_Users_Tambah_b"))
        self.ihl_Users_Tambah_b = QtGui.QHBoxLayout(self.fr_Users_Tambah_b)
        self.ihl_Users_Tambah_b.setObjectName(_fromUtf8("ihl_Users_Tambah_b"))
        self.tb_Users_Tambah_Simpan = QtGui.QPushButton(self.fr_Users_Tambah_b)
        self.tb_Users_Tambah_Simpan.setObjectName(_fromUtf8("tb_Users_Tambah_Simpan"))
        self.ihl_Users_Tambah_b.addWidget(self.tb_Users_Tambah_Simpan)
        spacerItem5 = QtGui.QSpacerItem(440, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ihl_Users_Tambah_b.addItem(spacerItem5)
        self.tb_Users_Tambah_Tutup = QtGui.QPushButton(self.fr_Users_Tambah_b)
        self.tb_Users_Tambah_Tutup.setObjectName(_fromUtf8("tb_Users_Tambah_Tutup"))
        self.ihl_Users_Tambah_b.addWidget(self.tb_Users_Tambah_Tutup)
        self.ivl_Users_Tambah_Luar.addWidget(self.fr_Users_Tambah_b)
        self.st_Admin.addWidget(self.st_Users_Tambah)
        self.igr_Admin.addWidget(self.st_Admin, 1, 0, 1, 1)

        self.retranslateUi(fr_Admin)
        self.st_Admin.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fr_Admin)

    def retranslateUi(self, fr_Admin):
        fr_Admin.setWindowTitle(_translate("fr_Admin", "Frame", None))
        self.tb_TutupAdmin.setText(_translate("fr_Admin", "Tutup Admin", None))
        self.tb_EditAdmin.setText(_translate("fr_Admin", "Edit Admin", None))
        self.tb_ListUser.setText(_translate("fr_Admin", "List User", None))
        self.lb_Users_Judul.setText(_translate("fr_Admin", "Users", None))
        item = self.tbl_ListUser_List.horizontalHeaderItem(0)
        item.setText(_translate("fr_Admin", "Username", None))
        item = self.tbl_ListUser_List.horizontalHeaderItem(1)
        item.setText(_translate("fr_Admin", "Password", None))
        item = self.tbl_ListUser_List.horizontalHeaderItem(2)
        item.setText(_translate("fr_Admin", "Kewenangan", None))
        self.tb_Users_Tambah.setText(_translate("fr_Admin", "Tambah", None))
        self.tb_Users_Ubah.setText(_translate("fr_Admin", "Ubah", None))
        self.tb_Users_Hapus.setText(_translate("fr_Admin", "Hapus", None))
        self.tb_Users_Tutup.setText(_translate("fr_Admin", "Tutup", None))
        self.lb_Users_Tambah_Judul.setText(_translate("fr_Admin", "Tambah User", None))
        self.lb_Users_Tambah_Username.setText(_translate("fr_Admin", "Username :", None))
        self.lb_Users_Tambah_Password.setText(_translate("fr_Admin", "Password :", None))
        self.lb_Users_Tambah_Priviledge.setText(_translate("fr_Admin", "Priviledge :", None))
        self.cb_Users_Tambah_Priviledge.setItemText(0, _translate("fr_Admin", "Administrator", None))
        self.cb_Users_Tambah_Priviledge.setItemText(1, _translate("fr_Admin", "Accountant", None))
        self.cb_Users_Tambah_Priviledge.setItemText(2, _translate("fr_Admin", "Finance", None))
        self.cb_Users_Tambah_Priviledge.setItemText(3, _translate("fr_Admin", "Sales", None))
        self.cb_Users_Tambah_Priviledge.setItemText(4, _translate("fr_Admin", "Custom", None))
        self.lb_Users_Tambah_Password_Confirm.setText(_translate("fr_Admin", "Confirm Password: ", None))
        self.tb_Users_Tambah_Simpan.setText(_translate("fr_Admin", "Simpan", None))
        self.tb_Users_Tambah_Tutup.setText(_translate("fr_Admin", "Tutup", None))

