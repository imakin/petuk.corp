# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_kasbank.ui'
#
# Created: Wed Jan 21 09:22:37 2015
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

class Ui_st_KasBank(object):
    def setupUi(self, st_KasBank):
        st_KasBank.setObjectName(_fromUtf8("st_KasBank"))
        st_KasBank.resize(777, 584)
        st_KasBank.setStyleSheet(_fromUtf8("QFrame{border:0px;}"))
        self.st_Menu = QtGui.QWidget()
        self.st_Menu.setObjectName(_fromUtf8("st_Menu"))
        self.igr_KasBank_Menu = QtGui.QGridLayout(self.st_Menu)
        self.igr_KasBank_Menu.setObjectName(_fromUtf8("igr_KasBank_Menu"))
        self.fr_Menu_Content = QtGui.QFrame(self.st_Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Menu_Content.sizePolicy().hasHeightForWidth())
        self.fr_Menu_Content.setSizePolicy(sizePolicy)
        self.fr_Menu_Content.setMinimumSize(QtCore.QSize(640, 480))
        self.fr_Menu_Content.setMaximumSize(QtCore.QSize(640, 480))
        self.fr_Menu_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Menu_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Menu_Content.setObjectName(_fromUtf8("fr_Menu_Content"))
        self.tb_Menu_KasMasuk = QtGui.QPushButton(self.fr_Menu_Content)
        self.tb_Menu_KasMasuk.setGeometry(QtCore.QRect(150, 160, 151, 161))
        self.tb_Menu_KasMasuk.setObjectName(_fromUtf8("tb_Menu_KasMasuk"))
        self.tb_Menu_KasKeluar = QtGui.QPushButton(self.fr_Menu_Content)
        self.tb_Menu_KasKeluar.setGeometry(QtCore.QRect(330, 160, 151, 161))
        self.tb_Menu_KasKeluar.setObjectName(_fromUtf8("tb_Menu_KasKeluar"))
        self.igr_KasBank_Menu.addWidget(self.fr_Menu_Content, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_KasBank_Menu.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_KasBank_Menu.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_KasBank_Menu.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_KasBank_Menu.addItem(spacerItem3, 1, 2, 1, 1)
        st_KasBank.addWidget(self.st_Menu)
        self.st_KasMasuk = QtGui.QWidget()
        self.st_KasMasuk.setObjectName(_fromUtf8("st_KasMasuk"))
        self.verticalLayout = QtGui.QVBoxLayout(self.st_KasMasuk)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fr_KasMasuk_t = QtGui.QFrame(self.st_KasMasuk)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_t.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_t.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_t.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasMasuk_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasMasuk_t.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_t.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_t.setObjectName(_fromUtf8("fr_KasMasuk_t"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fr_KasMasuk_t)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lb_KasMasuk_Judul = QtGui.QLabel(self.fr_KasMasuk_t)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lb_KasMasuk_Judul.sizePolicy().hasHeightForWidth())
        self.lb_KasMasuk_Judul.setSizePolicy(sizePolicy)
        self.lb_KasMasuk_Judul.setMinimumSize(QtCore.QSize(300, 0))
        self.lb_KasMasuk_Judul.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_KasMasuk_Judul.setFont(font)
        self.lb_KasMasuk_Judul.setObjectName(_fromUtf8("lb_KasMasuk_Judul"))
        self.horizontalLayout.addWidget(self.lb_KasMasuk_Judul)
        spacerItem4 = QtGui.QSpacerItem(226, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.le_KasMasuk_Search = QtGui.QLineEdit(self.fr_KasMasuk_t)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.le_KasMasuk_Search.sizePolicy().hasHeightForWidth())
        self.le_KasMasuk_Search.setSizePolicy(sizePolicy)
        self.le_KasMasuk_Search.setMinimumSize(QtCore.QSize(200, 0))
        self.le_KasMasuk_Search.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_KasMasuk_Search.setObjectName(_fromUtf8("le_KasMasuk_Search"))
        self.horizontalLayout.addWidget(self.le_KasMasuk_Search)
        self.verticalLayout.addWidget(self.fr_KasMasuk_t)
        self.fr_KasMasuk_Content = QtGui.QFrame(self.st_KasMasuk)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_Content.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_Content.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_Content.setObjectName(_fromUtf8("fr_KasMasuk_Content"))
        self.verticalLayout.addWidget(self.fr_KasMasuk_Content)
        self.fr_KasMasuk_b = QtGui.QFrame(self.st_KasMasuk)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_b.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_b.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_b.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasMasuk_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasMasuk_b.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_b.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_b.setObjectName(_fromUtf8("fr_KasMasuk_b"))
        self.verticalLayout.addWidget(self.fr_KasMasuk_b)
        st_KasBank.addWidget(self.st_KasMasuk)

        self.retranslateUi(st_KasBank)
        st_KasBank.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(st_KasBank)

    def retranslateUi(self, st_KasBank):
        st_KasBank.setWindowTitle(_translate("st_KasBank", "StackedWidget", None))
        self.tb_Menu_KasMasuk.setText(_translate("st_KasBank", "Kas Masuk", None))
        self.tb_Menu_KasKeluar.setText(_translate("st_KasBank", "Kas Keluar", None))
        self.lb_KasMasuk_Judul.setText(_translate("st_KasBank", "Kas Masuk", None))
        self.le_KasMasuk_Search.setPlaceholderText(_translate("st_KasBank", "Type to search...", None))

