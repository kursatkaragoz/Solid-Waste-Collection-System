# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'katiAtikToplamaDesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MyGUI(object):

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setEnabled(True)
        Window.resize(1240, 700)
        font = QtGui.QFont()
        font.setPointSize(10)

        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")

# label BEGIN
    #Title LABEL
        self.districtLabel = QtWidgets.QLabel(self.centralwidget)
        self.districtLabel.setGeometry(QtCore.QRect(10, 0, 91, 16))
        self.districtLabel.setFont(font)
        self.districtLabel.setObjectName("districtLabel")

        self.truckLabel = QtWidgets.QLabel(self.centralwidget)
        self.truckLabel.setGeometry(QtCore.QRect(310, 0, 91, 16))
        self.truckLabel.setFont(font)
        self.truckLabel.setObjectName("truckLabel")
    #Title Label END

        self.listLabel = QtWidgets.QLabel(self.centralwidget)
        self.listLabel.setGeometry(QtCore.QRect(660, 0, 101, 16))
        self.listLabel.setObjectName("listLabel")

        self.stateLabel = QtWidgets.QLabel(self.centralwidget)
        self.stateLabel.setGeometry(QtCore.QRect(10, 360, 91, 16))
        self.stateLabel.setObjectName("stateLabel")

        self.carCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.carCountLabel.setGeometry(QtCore.QRect(10, 230, 81, 21))
        self.carCountLabel.setFont(font)
        self.carCountLabel.setObjectName("carCountLabel")

        self.personelCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.personelCountLabel.setGeometry(QtCore.QRect(10, 260, 111, 21))
        self.personelCountLabel.setFont(font)
        self.personelCountLabel.setObjectName("personelCountLabel")

        self.districtCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.districtCountLabel.setGeometry(QtCore.QRect(220, 230, 101, 21))
        self.districtCountLabel.setFont(font)
        self.districtCountLabel.setObjectName("districtCountLabel")

        self.streetCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.streetCountLabel.setGeometry(QtCore.QRect(220, 260, 101, 21))
        self.streetCountLabel.setFont(font)
        self.streetCountLabel.setObjectName("streetCountLabel")

        self.containerCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.containerCountLabel.setGeometry(QtCore.QRect(430, 230, 101, 21))
        self.containerCountLabel.setFont(font)
        self.containerCountLabel.setObjectName("stateLabel")

        self.shiftCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.shiftCountLabel.setGeometry(QtCore.QRect(430, 260, 111, 21))
        self.shiftCountLabel.setFont(font)
        self.shiftCountLabel.setObjectName("shiftCountLabel")

        self.weatherLabel = QtWidgets.QLabel(self.centralwidget)
        self.weatherLabel.setGeometry(QtCore.QRect(110, 300, 101, 21))
        self.weatherLabel.setFont(font)
        self.weatherLabel.setObjectName("weatherLabel")

        self.trafficLabel = QtWidgets.QLabel(self.centralwidget)
        self.trafficLabel.setGeometry(QtCore.QRect(320, 300, 111, 21))
        self.trafficLabel.setFont(font)
        self.trafficLabel.setObjectName("trafficLabel")
# Label END

# Entry Begın
        self.truckEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.truckEntry.setGeometry(QtCore.QRect(120, 230, 71, 20))
        self.truckEntry.setObjectName("truckEntry")

        self.personelEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.personelEntry.setGeometry(QtCore.QRect(120, 260, 71, 20))
        self.personelEntry.setObjectName("personelEntry")

        self.districtEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.districtEntry.setGeometry(QtCore.QRect(330, 230, 71, 20))
        self.districtEntry.setObjectName("districtEntry")

        self.streetEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.streetEntry.setGeometry(QtCore.QRect(330, 260, 71, 20))
        self.streetEntry.setObjectName("streetEntry")

        self.containerEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.containerEntry.setGeometry(QtCore.QRect(560, 230, 71, 20))
        self.containerEntry.setObjectName("containerEntry")

        self.shiftEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.shiftEntry.setGeometry(QtCore.QRect(560, 260, 71, 20))
        self.shiftEntry.setObjectName("shiftEntry")

        self.weatherEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.weatherEntry.setGeometry(QtCore.QRect(220, 300, 71, 20))
        self.weatherEntry.setObjectName("weatherEntry")

        self.trafficEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.trafficEntry.setGeometry(QtCore.QRect(440, 300, 71, 20))
        self.trafficEntry.setObjectName("trafficEntry")

# Entry END

        self.selectShiftCombo = QtWidgets.QComboBox(self.centralwidget)
        self.selectShiftCombo.setGeometry(90, 358, 541, 22)
        self.selectShiftCombo.setObjectName("selectShiftCombo")


# Table Begin
        self.districtTable = QtWidgets.QTableWidget(self.centralwidget)
        self.districtTable.setGeometry(QtCore.QRect(10, 20, 261, 192))
        self.districtTable.setObjectName("districtTable")
        self.districtTable.setColumnCount(0)
        self.districtTable.setRowCount(0)

        self.truckTable = QtWidgets.QTableWidget(self.centralwidget)
        self.truckTable.setGeometry(QtCore.QRect(310, 20, 321, 192))
        self.truckTable.setObjectName("truckTable")
        self.truckTable.setColumnCount(0)
        self.truckTable.setRowCount(0)

        self.stateTable = QtWidgets.QTableWidget(self.centralwidget)
        self.stateTable.setGeometry(QtCore.QRect(10, 385, 1210, 272))
        self.stateTable.setObjectName("stateTable")
        self.stateTable.setRowCount(1)
        self.stateTable.setColumnCount(12)
        columns = ['Baslangic Zamani','Trafik Gecikme','Araç','Mahalle','Sokak','Kont. S','Toplanan Cöp(Kg)','Toplam Cöp(Kg)','Kalan Personel','Servis Süresi','Toplam Servis','Bitis Zamani']
        self.stateTable.setHorizontalHeaderLabels(columns)

        self.outputList = QtWidgets.QListWidget(self.centralwidget)
        self.outputList.setGeometry(QtCore.QRect(660, 20, 560, 352))
        self.outputList.setObjectName("outputList")

# Button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 330, 621, 23))
        self.startButton.setObjectName("startButton")

# Other
        Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 21))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")

        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setObjectName("menuClear")
        Window.setMenuBar(self.menubar)

        self.dataImportButton = QtWidgets.QAction(Window)
        self.dataImportButton.setObjectName("dataImportButton")
        self.actionNEW = QtWidgets.QAction(Window)
        self.actionNEW.setObjectName("action...")
        self.resetButton = QtWidgets.QAction(Window)
        self.resetButton.setObjectName("resetButton")

        self.menuMen.addAction(self.dataImportButton)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.actionNEW)
        self.menuClear.addAction(self.resetButton)
        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "GOP Katı Atık Toplama Modellemesi"))
        self.carCountLabel.setText(_translate("Window", "Araç Sayısı"))
        self.personelCountLabel.setText(_translate("Window", "Personel Sayısı"))
        self.districtCountLabel.setText(_translate("Window", "Mahalle Sayısı"))
        self.streetCountLabel.setText(_translate("Window", "Sokak Sayısı"))
        self.containerCountLabel.setText(_translate("Window", "Konteyner Sayısı"))
        self.shiftCountLabel.setText(_translate("Window", "Vardiya Sayısı"))
        self.weatherLabel.setText(_translate("Window", "Hava Durumu"))
        self.trafficLabel.setText(_translate("Window", "Trafik Durumu"))
        self.startButton.setText(_translate("Window", "Modeli Başlat"))
        self.stateLabel.setText(_translate("Window", "Model Durumı"))
        self.districtLabel.setText(_translate("Window", "Mahaleler"))
        self.truckLabel.setText(_translate("Window", "Araçlar"))
        self.listLabel.setText(_translate("Window", "Adım Adım İşlemler"))

        self.menuMen.setTitle(_translate("Window", "Menü"))
        self.dataImportButton.setText(_translate("Window", "Veri Yükle (.xlsx)"))
        self.actionNEW.setText(_translate("Window", "action..."))
        self.menuClear.setTitle(_translate("Window", "Temizle"))
        self.resetButton.setText(_translate("Window", "Sıfırla"))

