import MySQLdb
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSvg
from PyQt4.QtCore import * #nganggo QDateTime, ra apal e package ngarepe opo QtCore.QDateTime rung nyobo
from PyQt4.QtGui import *
import sip #lali nggo ngopo
import sys,os
import functools #partial
import itertools #ubah tuple ke array
import re #regular expression
from datetime import datetime #tanggal, a= datetime.now(); cobo dicheck dir(a); a.year,

from ui_kasbank import Ui_st_KasBank
from KasMasuk import KasMasuk

class KasBank(KasMasuk):
	def KasBank_init(self,parent=None):
		super(KasBank,self).__init__(parent)
		self.st_kasbank = QtGui.QStackedWidget(self.tab_KasBank)
		self.ui_kasbank = Ui_st_KasBank()
		self.ui_kasbank.setupUi(self.st_kasbank)
		self.tab_KasBank.findChild(QtGui.QVBoxLayout).addWidget(self.st_kasbank)
		
		#--- menu signal
		self.ui_kasbank.tb_Menu_KasMasuk.clicked.connect(self.KasBank_KasMasuk)
	
