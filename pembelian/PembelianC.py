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

class Pembelian(object):
	def Pembelian__init(self):
		#inisialisasisiasi INDEX Halaman Pembelian
		self.INDEX_ST_PEMBELIAN_MENU = 0
		self.INDEX_ST_PEMBELIAN_PERMINTAANBARANG = 1
		self.INDEX_ST_PEMBELIAN_ORDERPEMBELIAN = 2
		self.INDEX_ST_PEMBELIAN_PENERIMAAN = 3
		self.INDEX_ST_PEMBELIAN_HUTANG = 4
		self.INDEX_ST_PEMBELIAN_PEMBAYARANHUTANG = 5
		self.INDEX_ST_PEMBELIAN_RETURPEMBELIAN = 6
		
		#Tombol Pada Halaman Menu
		self.tb_Pembelian_PermintaanBarang.clicked.connect(self.Pembelian_GoTo_PermintaanBarang)
		self.tb_Pembelian_OrderPembelian.clicked.connect(self.Pembelian_GoTo_OrderPembelian)
		self.tb_Pembelian_Penerimaan.clicked.connect(self.Pembelian_GoTo_PenerimaanBarang)
		self.tb_Pembelian_HutangUsaha.clicked.connect(self.Pembelian_GoTo_HutangUsaha)
		self.tb_Pembelian_PembayaranHutang.clicked.connect(self.Pembelian_GoTo_PembayaranHutang)
		self.tb_Pembelian_ReturPembelian.clicked.connect(self.Pembelian_GoTo_ReturPembelian)
		
		#Tombol pada Permintaan Barang
		self.tb_Pembelian_PermintaanBarang_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		
		#Tombol pada Order Pembelian
		self.tb_Pembelian_OrderPembelian_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		
		#Tombol pada Penerimaan Barang
		
		#Tombol pada Hutang Usaha
		self.tb_Pembelian_HutangUsaha_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		
		#Tombol pada Pembayaran Hutang
		
		#Tombol pada Retur Pembelian
	
	def Pembelian_GoTo_Menu(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_MENU)
		return	
		
	def Pembelian_GoTo_PermintaanBarang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PERMINTAANBARANG)
		return
	
	def Pembelian_GoTo_OrderPembelian(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP)
		self.cb_Pembelian_OrderPembelian_Nama.clear()
		self.cb_Pembelian_OrderPembelian_Gudang.clear()
		jumlahRow = self.tbl_Pembelian_OrderPembelian.rowCount()
		#print jumlahRow
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Pembelian_OrderPembelian.removeRow(a)
		kodePembelian = str(self.le_Pembelian_OrderPembelian_NoPO.text())
		query = "SELECT * FROM gd_nama_alamat WHERE `tipe` LIKE 'vendor'"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Pembelian_OrderPembelian_Nama.addItem(self.DatabaseRunQuery(query)[a][2])
		query = "SELECT * FROM gd_data_gudang"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Pembelian_OrderPembelian_Gudang.addItem(self.DatabaseRunQuery(query)[a][2])
		query = "SELECT * FROM `gd_order_pembelian` WHERE `kodeTransaksi` LIKE '"+kodePembelian+"'"
		result = self.DatabaseRunQuery(query) 
		if len(result) != 0:
			for a in range(0,len(result)):
				print "tambah row"
				self.tbl_Pembelian_OrderPembelian.insertRow(a)
				self.tbl_Pembelian_OrderPembelian.setItem(a,0,QtGui.QTableWidgetItem(result[a][3])) #kode
				sql = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` = '"+result[a][3]+"'"
				self.tbl_Pembelian_OrderPembelian.setItem(a,1,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][5]))) #nama produk
				self.tbl_Pembelian_OrderPembelian.setItem(a,3,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][3]))) #jumlah
				self.tbl_Pembelian_OrderPembelian.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][4]))) #satuan
				self.tbl_Pembelian_OrderPembelian.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][5]))) #harga
				self.tbl_Pembelian_OrderPembelian.setItem(a,5,QtGui.QTableWidgetItem(result[a][6])) #diskon
				total = result[a][4]*result[a][5]
				self.tbl_Pembelian_OrderPembelian.setItem(a,6,QtGui.QTableWidgetItem(str(total))) #total harga
				self.tbl_Pembelian_OrderPembelian	.setItem(a,7,QtGui.QTableWidgetItem(result[a][7]))
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_ORDERPEMBELIAN)
	
	def Pembelian_GoTo_OrderPembelian_TambahProduk(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP_TAMBAHPRODUK)
		self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Satuan.clear()
		self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Nama.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Jumlah.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Harga.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Diskon.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Pajak.clear()
		
		#Autocomplete diilangi karena produk belum tentu ada di database
		""" query = "SELECT * FROM gd_data_produk"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.addItem(self.DatabaseRunQuery(query)[a][5])
		query = "SELECT * FROM gd_satuan_pengukuran"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Satuan.addItem(self.DatabaseRunQuery(query)[a][1])
		nama = str(self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.currentText())
		query = "SELECT * FROM `gd_data_produk` WHERE `namaBarang` LIKE '"+nama+"'"
		kodeBarang = self.DatabaseRunQuery(query)[0][1]
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.setText(kodeBarang)"""
		return
	
	def Pembelian_OrderPembelian_TambahProduk(self):
		
		pass
	
	def Pembelian_GoTo_PenerimaanBarang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PENERIMAAN)
		return
	
	def Pembelian_GoTo_HutangUsaha(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_HUTANG)
		return
	
	def Pembelian_GoTo_PembayaranHutang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PEMBAYARANHUTANG)
		return
	
	def Pembelian_GoTo_ReturPembelian(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_RETURPEMBELIAN)
		return
