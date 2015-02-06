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
def _fromUtf8(s):
	return s
	
class DataRekening(object):
	def __init__(self,parent=None):
		pass
		
	def DataMaster_DataRekening(self):
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAREKENING)
		
		RekeningField = ["id", "noAkun", "namaAkun", "namaAliasAkun", "saldoAwal", "saldoSekarang", "isKas"]
		def REK(flname):
			return RekeningField.index(flname)
		
		#---got to clear table first
		for r in range(0,self.tbl_DataMaster_DataRekening_Fcontent_LRekening.rowCount()+1):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.removeRow(r)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(0)
		
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		for row in range(0,len(result)):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.insertRow(row)
			for xx in range(0,6):
				if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,xx)==None):
					item = QtGui.QTableWidgetItem()
					self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, xx, item)
			
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)
			item.setText(str(result[row][REK("noAkun")]))
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)
			item.setText(str(result[row][REK("namaAkun")]))
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)
			item.setText(str(result[row][REK("namaAliasAkun")]))
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,3)
			item.setText(str(result[row][REK("saldoAwal")]))
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,4)
			item.setText(str(result[row][REK("saldoSekarang")]))
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,5)
			if (result[row][REK("isKas")]>0):item.setText(str("v"))
			else:item.setText(str(" "))
			
	
		def _SetActiveIndex(a,b):
			kode = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(a,0).text())
			sql = "SELECT * FROM `gd_rekening_jurnal` WHERE `noAkun` LIKE '"+kode+"' ;"
			res = self.DatabaseRunQuery(sql)
			self.DataMaster_DataRekening_Edit_idEDIT = res[0][0]
			return
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked)
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked.connect(_SetActiveIndex)
		#---Sinyal tombol tambah
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Tambah.clicked)
		self.tb_DataMaster_DataRekening_Tambah.clicked.connect(self.DataMaster_DataRekening_Tambah)
		#---Sinyal tombol hapus
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Delete.clicked)
		self.tb_DataMaster_DataRekening_Delete.clicked.connect(self.DataMaster_DataRekening_Delete)
		#---tombol edit
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Edit.clicked)
		#--- confirmasi edit
		self.tb_DataMaster_DataRekening_Edit.clicked.connect(functools.partial(self.DataMaster_Popup,"Edit nomor rekening jurnal ini? Hanya lanjutkan bila anda faham apa yang anda lakukan!",self.DataMaster_DataRekening_Edit))
	
	def DataMaster_DataRekening_Tambah(self):
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAREKENING_TAMBAH)
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Tambah_Batal.clicked)
		self.tb_DataMaster_DataRekening_Tambah_Batal.clicked.connect(self.DataMaster_DataRekening)
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Tambah_Simpan.clicked)
		self.tb_DataMaster_DataRekening_Tambah_Simpan.clicked.connect(self.DataMaster_DataRekening_Tambah_Act_Simpan)
		pass
		
	def DataMaster_DataRekening_Tambah_Act_Simpan(self):
		nomor = str(self.le_DataMaster_DataRekening_NomorAkun.text())
		nama = str(self.le_DataMaster_DataRekening_NamaAkun.text())
		namaalias = str(self.le_DataMaster_DataRekening_NamaAliasAkun.text())
		jadi = False
		if (self.DataMaster_DataRekening_Edit_idEDIT<0):
			jadi = self.DatabaseInsertAvoidreplace(self.dbDatabase,"gd_rekening_jurnal","noAkun",nomor,
											["noAkun","namaAkun","namaAliasAkun"],
											[nomor,nama,namaalias],
											"Penyimpanan tidak dapat dilakukan karena telah terdapat nomor akun yang sama!",
											self.DataMaster_DataRekening_Tambah)
		else:
			jadi = self.DatabaseInsertReplace(self.dbDatabase,"gd_rekening_jurnal","id",self.DataMaster_DataRekening_Edit_idEDIT,
											["noAkun","namaAkun","namaAliasAkun"],
											[nomor,nama,namaalias])
		if (jadi):
			#---sukses Kembali ke room DataRekening
			self.DataMaster_DataRekening()
			self.DataMaster_DataRekening_Edit_idEDIT = -1
		#----bila tidak sukses, bertahan di room tambah
		pass
	
	def DataMaster_DataRekening_Edit(self):
		if (self.DataMaster_DataRekening_Edit_idEDIT<0):
			return
		data = self.DatabaseRunQuery("SELECT * FROM `gd_rekening_jurnal` WHERE `id` = "+str(self.DataMaster_DataRekening_Edit_idEDIT)+" ;")
		if len(data)<0:
			return
		
		self.le_DataMaster_DataRekening_NomorAkun.setText(str(data[0][self.DataMaster_DataRekening_Field.index("noAkun")]))
		self.le_DataMaster_DataRekening_NamaAkun.setText(str(data[0][self.DataMaster_DataRekening_Field.index("namaAkun")]))
		self.le_DataMaster_DataRekening_NamaAliasAkun.setText(str(data[0][self.DataMaster_DataRekening_Field.index("namaAliasAkun")]))
		self.DataMaster_DataRekening_Tambah()
	
	def DataMaster_DataRekening_Delete(self):
		if (self.DataMaster_DataRekening_Edit_idEDIT<0):
			return
		def _CommitDelete():
			self.DatabaseRunQuery("DELETE FROM `gd_rekening_jurnal` WHERE `id` = "+str(self.DataMaster_DataRekening_Edit_idEDIT)+" ;")
			self.DataMaster_DataRekening_RefreshInfo()
		data = self.DatabaseRunQuery("SELECT * FROM `gd_rekening_jurnal` WHERE `id` = "+str(self.DataMaster_DataRekening_Edit_idEDIT)+" ;")
		if len(data)<0:
			return
		self.DataMaster_Popup("Anda yakin akan menghapus rekening "+str(data[0][self.DataMaster_DataRekening_Field.index("noAkun")])+"?\n\n"+\
								"Lanjutkan hapus hanya bila anda mengerti apa yang anda lakukan!",
								_CommitDelete)
		
	def DataMaster_DataRekening_Popup_Pilih(self,data=None,fcb_ok=False,fcb_cancel=False):
		"Tunjukkan Popup untuk memilih data rekening, hasil disimpen ke variabel data[0] (nomor rekening) dan data[1] (nama rekening)"
		if (data==None):
			data = ["",""]
		if len(data)<2:
			data = ["",""]
		if fcb_ok==False:
			fcb_ok = self.DataMaster_None
		if fcb_cancel==False:
			fcb_cancel = self.DataMaster_None
		
		CNOMOR_REKENING = 0
		CNAMA_REKENING = 1
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(len(result))
		for row in range(0,len(result)):
			
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)==None):
				item = QtGui.QTableWidgetItem()
				#~ item.setColumnWidth(300)
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 0, item)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)==None):
				itema = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 1, itema)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)==None):
				itemb = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 2, itemb)
			
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)
			item.setText(result[row][1])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)
			item.setText(result[row][2])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)
			item.setText(result[row][3])
	
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		
		
		def kembalikan():
			#----Kembalikan, dan disconnect sinyal dilakukan di BukuBesar_DaftarTransaksiJurnal_PilihRekening.ubahcell instead
			self.fr_DataMaster_DataRekening.setParent(self.st_DataMaster_DataRekening)
			self.ivl_DataMaster_DataRekening_Luar.addWidget(self.fr_DataMaster_DataRekening)
			self.fr_DataMaster_DataRekening_Fb.show()
			
		#---------------------------------------------------------------Panggil Popup disini
		self.DataMaster_Popup("",fcb_ok,650,WinH-200,kembalikan,fcb_cancel,True)
		
		FrameWindow = self.findChild(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		
		self.fr_DataMaster_DataRekening.setParent(FrameWindow)
		self.fr_DataMaster_DataRekening.show()
		self.fr_DataMaster_DataRekening.setGeometry(QtCore.QRect(5,5,640,WinH-250))
		self.fr_DataMaster_DataRekening_Fb.hide()
		
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked)
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked)
		
		def setDatarekeningTerpilih(row,column):
			data[0] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNOMOR_REKENING).text())
			data[1] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNAMA_REKENING).text())
			#----Kembalikan, jangan disconnect sinyal krna ini sinyal itu sendiri, dilakukan di BukuBesar_DaftarTransaksiJurnal_PilihRekening.ubahcell instead
			self.fr_DataMaster_DataRekening.setParent(self.st_DataMaster_DataRekening)
			self.ivl_DataMaster_DataRekening_Luar.addWidget(self.fr_DataMaster_DataRekening)
			self.fr_DataMaster_DataRekening_Fb.show()
			self.DataMaster_Popup_Tutup()
			
		def setDatarekeningTerpilihNC(row,column):
			data[0] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNOMOR_REKENING).text())
			data[1] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNAMA_REKENING).text())
		
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked.connect(setDatarekeningTerpilih)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked.connect(fcb_ok)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked.connect(setDatarekeningTerpilihNC)
		
	
	
	def DataMaster_DataRekening_RefreshInfo(self):
		#---got to clear table first
		for r in range(0,self.tbl_DataMaster_DataRekening_Fcontent_LRekening.rowCount()+1):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.removeRow(r)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(0)
		
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		for row in range(0,len(result)):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.insertRow(row)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)==None):
				item = QtGui.QTableWidgetItem()
				#~ item.setColumnWidth(300)
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 0, item)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)==None):
				itema = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 1, itema)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)==None):
				itemb = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 2, itemb)
			
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)
			item.setText(result[row][1])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)
			item.setText(result[row][2])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)
			item.setText(result[row][3])
	
