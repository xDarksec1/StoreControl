# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_addprod.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaAddProd(object):
    def setupUi(self, TelaAddProd):
        TelaAddProd.setObjectName("TelaAddProd")
        TelaAddProd.resize(349, 165)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("iconmain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        TelaAddProd.setWindowIcon(icon)
        TelaAddProd.setStyleSheet("background-color: rgb(0, 52, 76);")
        self.centralwidget = QtWidgets.QWidget(TelaAddProd)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAddProd = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnAddProd.setFont(font)
        self.btnAddProd.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.btnAddProd.setObjectName("btnAddProd")
        self.gridLayout.addWidget(self.btnAddProd, 13, 1, 1, 1)
        self.inputValor = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValor.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.inputValor.setObjectName("inputValor")
        self.gridLayout.addWidget(self.inputValor, 10, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.inputId = QtWidgets.QLineEdit(self.centralwidget)
        self.inputId.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.inputId.setObjectName("inputId")
        self.gridLayout.addWidget(self.inputId, 2, 1, 1, 1)
        self.inputNome = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNome.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.inputNome.setObjectName("inputNome")
        self.gridLayout.addWidget(self.inputNome, 7, 1, 1, 1)
        self.radioBtnUnhas = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.radioBtnUnhas.setFont(font)
        self.radioBtnUnhas.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioBtnUnhas.setObjectName("radioBtnUnhas")
        self.gridLayout.addWidget(self.radioBtnUnhas, 10, 2, 1, 1)
        self.inputQtde = QtWidgets.QLineEdit(self.centralwidget)
        self.inputQtde.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.inputQtde.setObjectName("inputQtde")
        self.gridLayout.addWidget(self.inputQtde, 9, 1, 1, 1)
        self.radioBtnCabelo = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.radioBtnCabelo.setFont(font)
        self.radioBtnCabelo.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioBtnCabelo.setObjectName("radioBtnCabelo")
        self.gridLayout.addWidget(self.radioBtnCabelo, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 2, 1)
        self.radioBtnPele = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.radioBtnPele.setFont(font)
        self.radioBtnPele.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioBtnPele.setObjectName("radioBtnPele")
        self.gridLayout.addWidget(self.radioBtnPele, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)
        self.radioBtnMake = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.radioBtnMake.setFont(font)
        self.radioBtnMake.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioBtnMake.setObjectName("radioBtnMake")
        self.gridLayout.addWidget(self.radioBtnMake, 7, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        TelaAddProd.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaAddProd)
        QtCore.QMetaObject.connectSlotsByName(TelaAddProd)

    def retranslateUi(self, TelaAddProd):
        _translate = QtCore.QCoreApplication.translate
        TelaAddProd.setWindowTitle(_translate("TelaAddProd", "Adicionar Prod"))
        self.btnAddProd.setText(_translate("TelaAddProd", "Adicionar Produto"))
        self.label_5.setText(_translate("TelaAddProd", "Qtde:"))
        self.radioBtnUnhas.setText(_translate("TelaAddProd", "Unhas"))
        self.radioBtnCabelo.setText(_translate("TelaAddProd", "Cabelo"))
        self.label_4.setText(_translate("TelaAddProd", "Categoria"))
        self.radioBtnPele.setText(_translate("TelaAddProd", "SkinCare"))
        self.label_2.setText(_translate("TelaAddProd", "Nome:"))
        self.label_3.setText(_translate("TelaAddProd", "Valor: R$"))
        self.radioBtnMake.setText(_translate("TelaAddProd", "Maquiagem"))
        self.label.setText(_translate("TelaAddProd", "Id:"))
