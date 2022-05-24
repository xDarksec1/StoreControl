from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QRadioButton, QLCDNumber, QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QComboBox
from PyQt5.QtCore import Qt
from interface.tela_addprod import *
from interface.tela_main import *
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QIcon
from datetime import datetime
from dbconnect import *
import requests, os
import subprocess
import sys
from datetime import datetime


class ComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("font-size: 15px")
        self.addItems(["Cabelo", "Maquiagem", "SkinCare", "Unhas"])
        self.property("id")
        self.currentIndexChanged.connect(self.change_category)

    def change_category(self):
        try:
            db = ConnectDb()
            db.update_category(self.id, self.currentText())
        except:
            pass


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class Msg(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("QLabel{ color: white}")
        self.setStyleSheet("background-color: rgb(240, 240, 240;")
        self.type_icon = [
            {"info": QMessageBox.Information},
            {"alert": QMessageBox.Warning},
            {"critical": QMessageBox.Critical},
            {"question": QMessageBox.Question},
        ]

    def send_msg(self, titulo, texto, tipo=None):

        for i in self.type_icon:
            for i in i.items():
                if i[1] == tipo:
                    self.setIcon(i[1])
                    self.setWindowIcon(QIcon(f"icons/{i[0]}.png"))
        self.setText(texto)
        self.setWindowTitle(titulo)
        self.exec_()


class Logs:
    def __init__(self):
        self.date = datetime.now()
        self.caminho = f"Vendas\\{self.date.strftime('%m-%Y')}"
        self.check_dir()
        self.caminho_comp = rf'{self.caminho}\dia-{self.date.strftime("%d")}.txt'
        if not self.arqExiste():
            a = open(self.caminho_comp, "wt+")
            a.close()

    def check_dir(self):
        try:
            os.makedirs(self.caminho)
        except:
            pass

    def write_log(self, nome, qtde, total):
        with open(self.caminho_comp, "a+", encoding="utf-8") as arq:
            dic = f"{nome};{qtde};{total}\n"
            arq.write(dic)

    def arqExiste(self):
        try:
            a = open(self.caminho_comp, "rt")
            a.close()
        except FileNotFoundError:
            return False
        return True


def get_api_hwids():
    link = r"https://hwidlist.rafaelalvarenga.repl.co/"
    req = requests.get(link)
    hwid_list = req.json().split()
    return hwid_list
