import tempfile
from imports import *


class TelaMain(QMainWindow, Ui_MainWindow, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # telaprincipal
        self.btnDelProd.clicked.connect(self.del_selected_row)
        self.btnEditProd.clicked.connect(self.edit_selected_row)
        self.btnSearch.clicked.connect(lambda: self.show_all(search=True))
        self.inputSearch.returnPressed.connect(lambda: self.show_all(search=True))
        self.btnRefresh.clicked.connect(self.show_all)
        self.setWindowTitle("MissBela Store")
        self.setFixedSize(self.size())

        # tela vendas
        self.btnSearchVendas.clicked.connect(self.show_vendas)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.doubleClicked.connect(self.exec_vendas)
        self.btnExecVendas.clicked.connect(self.exec_vendas)
        self.inputQtde.returnPressed.connect(self.exec_vendas)
        self.inputValor.returnPressed.connect(self.exec_vendas)
        self.btnRefreshVendas.clicked.connect(self.refresh_vendas)

        # returnPresseds
        self.searchVendas.returnPressed.connect(lambda: self.show_vendas())

        # tela addprod
        self.tela_addprod = TelaAddProd()
        self.tela_addprod.btnAddProd.clicked.connect(self.add_prod)
        self.btnInsertProd.clicked.connect(self.tela_addprod.show)

        # lcdPanel
        self.timePanel.setDigitCount(6)
        self.timePanel.setSegmentStyle(QLCDNumber.Flat)
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_clock)
        self.timer.start(1000)

        self.setWindowIcon(QIcon("iconmain.png"))

        self.show_all()
        self.show_vendas()
        self.refresh_vendas()
        self.check_hwid()

    def del_selected_row(self):
        try:
            num = int(self.tableWidget.selectedItems()[0].text())
        except:
            Msg().send_msg("INFORMAÇÃO!", "Selecione um item", QMessageBox.Information)
        else:
            message = QMessageBox()
            message.setWindowIcon(QIcon("iconmain.ico"))
            reply = message.question(
                message,
                f"Confirmação",
                f"Deseja Apagar?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                db = ConnectDb()
                db.del_id(num)
            else:
                return
        finally:
            self.show_all()

    def edit_selected_row(self):
        bd = ConnectDb()
        try:
            lista = []
            lista2 = []
            for i in self.tableWidget.selectedItems():
                lista.append(i.text())

            lista[2] = str(lista[2]).replace(",", ".")
            lista2.append(lista)

            for a, b, c, d in lista2:
                bd.update_prod(int(a), b, float(c), int(d))

        except:
            Msg().send_msg("INFORMAÇÃO!", "Selecione um item", QMessageBox.Information)
            return
        finally:
            self.show_vendas()
            # self.tableWidget.resizeColumnsToContents()

    def show_all(self, search=False):
        bd = ConnectDb()

        try:
            if not search:
                lista = bd.get_all_db()
            else:
                text = self.inputSearch.text().lower()
                if self.radioSearchID.isChecked():
                    lista = bd.search_id(text)
                elif self.radioSearchNome.isChecked():
                    lista = bd.search_nome(text)

            self.tableWidget.setRowCount(len(lista))
        except:
            Msg().send_msg(
                "ATTENTION!", "Escolha um Modo de Busca", QMessageBox.Warning
            )
        else:
            row = 0
            for id, nome, preco, qtde, cat in lista:

                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(id)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(nome))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(preco)))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(qtde)))

                delegate = AlignDelegate(self.tableWidget)
                self.tableWidget.setItemDelegateForColumn(2, delegate)
                self.tableWidget.setItemDelegateForColumn(3, delegate)

                self.combo = ComboBox(self)
                self.combo.id = id
                self.combo.currentIndexChanged.connect(self.show_vendas)

                for i in range(self.combo.count()):
                    if self.combo.itemText(i) == cat:
                        self.combo.setCurrentIndex(i)

                self.tableWidget.setCellWidget(row, 4, self.combo)

                row += 1
            self.tableWidget.resizeColumnToContents(0)
            self.tableWidget.resizeColumnToContents(1)

    def add_prod(self):
        bd = ConnectDb()
        self.tela_addprod.show()
        category = ""
        if self.tela_addprod.radioBtnCabelo.isChecked():
            category = "Cabelo"
        elif self.tela_addprod.radioBtnMake.isChecked():
            category = "Maquiagem"
        elif self.tela_addprod.radioBtnPele.isChecked():
            category = "SkinCare"
        elif self.tela_addprod.radioBtnUnhas.isChecked():
            category = "Unhas"
        elif category == "":
            Msg().send_msg(
                "ATTENTION!", "Selecione uma categoria!", QMessageBox.Warning
            )
            return

        try:
            id = int(self.tela_addprod.inputId.text())
            qtde = int(self.tela_addprod.inputQtde.text())
            nome = self.tela_addprod.inputNome.text().lower()
            valor = float(self.tela_addprod.inputValor.text().replace(",", "."))
        except:
            Msg().send_msg("ERROR!", "Algo errado nos valores", QMessageBox.Critical)
            return
        else:
            try:
                bd.add_prod(id, nome, valor, qtde, category)
            except sqlite3.Error:
                Msg().send_msg("ATTENTTION!", f"ID JÁ EXISTENTE", QMessageBox.Warning)
            except:
                Msg().send_msg("DBERROR", "ERRO NA DB", QMessageBox.Critical)
            else:
                Msg().send_msg("SUCESS", "PRODUTO ADICIONADO!", QMessageBox.Information)
                self.tela_addprod.close()
            finally:
                self.show_all()
                self.show_vendas()

    def closeEvent(self, event):

        self.tela_addprod.close()
        self.close()

    def lcd_clock(self):
        time = datetime.now().strftime("%H:%M")
        self.timePanel.display(time)

    def check_hwid(self):
        try:
            list_hwid = get_api_hwids()
        except:
            Msg().send_msg("APIERROR", "Dados da API inacessíveis", QMessageBox.Warning)
            sys.exit()
        else:
            hwid = (
                str(subprocess.check_output("wmic csproduct get uuid"), "utf-8")
                .split("\n")[1]
                .strip()
            )
            if hwid not in list_hwid:
                Msg().send_msg(
                    "ENCERRANDO",
                    "Entre em contato com desenvolvedor, seu produto não está registrado",
                    QMessageBox.Critical,
                )
                self.close()
                sys.exit()

    def show_vendas(self):
        bd = ConnectDb()
        lista = bd.search_all(self.searchVendas.text())
        self.tableView.setRowCount(len(lista))

        row = 0
        for id, nome, preco, qtde, cat in lista:
            self.tableView.setItem(row, 0, QTableWidgetItem(str(id)))
            self.tableView.setItem(row, 1, QTableWidgetItem(nome))
            self.tableView.setItem(row, 2, QTableWidgetItem(str(preco)))
            self.tableView.setItem(row, 3, QTableWidgetItem(str(qtde)))
            self.tableView.setItem(row, 4, QTableWidgetItem(str(cat)))

            delegate = AlignDelegate(self.tableWidget)
            self.tableView.setItemDelegateForColumn(2, delegate)
            self.tableView.setItemDelegateForColumn(3, delegate)

            row += 1

        self.tableView.resizeColumnToContents(1)
        self.tableView.resizeColumnToContents(0)

    def exec_vendas(self):

        try:
            qtde_vendida = self.inputQtde.text()
            qtde_vendida = int(qtde_vendida)
        except:
            Msg().send_msg("ATTENTTION!", "Apenas números", QMessageBox.Information)
            return
        else:
            try:
                lst = self.tableView.selectedItems()
                qtde_estoque = int(lst[3].text())
                valor = float(lst[2].text())
                nome = lst[1].text()
                id = float(lst[0].text())
                if qtde_estoque >= qtde_vendida:
                    qtde_final = qtde_estoque - qtde_vendida
                else:
                    Msg().send_msg(
                        "ESTOQUE!",
                        "Quantidade no estoque insuficiente",
                        QMessageBox.Information,
                    )
                    return
            except:
                Msg().send_msg(
                    "ATTENTION!", "SELECIONE UM PRODUTO", QMessageBox.Information
                )
            else:
                total = round(qtde_vendida * float(valor), 2)
                exchange = 0
                if self.inputValor.text():
                    try:
                        exchange = round(
                            float(self.inputValor.text().replace(",", ".")) - total, 2
                        )
                    except:
                        Msg().send_msg(
                            "ERRO", "Valor informado errado", QMessageBox.Warning
                        )
                        return
                message = QMessageBox()
                message.setWindowIcon(QIcon("iconmain.ico"))
                reply = message.question(
                    message,
                    f"Confirmação",
                    f"Produto: {nome}\n\tQuantidade: {qtde_vendida}\n\tTotal: R${total}\n\tTroco: R${exchange}",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes,
                )

                if reply == QMessageBox.Yes:
                    bd = ConnectDb()
                    bd.update_prod(int(id), nome, float(valor), int(qtde_final))
                    Msg().send_msg(
                        "VENDA REALIZADA",
                        f"Produto: {nome}\nQuantidade: {qtde_vendida}\nTotal:R$ {total}",
                        QMessageBox.Information,
                    )
                    log = Logs()
                    log.write_log(nome, qtde_vendida, total)
            finally:
                self.refresh_vendas()
                self.show_vendas()
                self.show_all()

    def refresh_vendas(self):
        self.listWidget.clear()
        logstr = Logs()
        lista = []
        with open(logstr.caminho_comp, "r", encoding="utf-8") as arq:
            for i in arq:
                lst = i.replace("\n", "").split(";")
                lista.append(lst)
        soma = 0
        for nome, qtde, total in lista:
            i = f"{nome}, Qtde: {qtde}, Total:R$ {total}"
            soma += float(total)
            self.listWidget.addItem(i)

        self.lcdTotalVendas.setDigitCount(6)
        self.lcdTotalVendas.setSegmentStyle(QLCDNumber.Flat)
        self.lcdTotalVendas.display(soma)


class TelaAddProd(QMainWindow, Ui_TelaAddProd):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon("iconmain.png"))
        self.setFixedSize(350, 165)

    def closeEvent(self, event):
        self.close()


def main():
    qt = QApplication(sys.argv)
    app = TelaMain()
    app.show()
    sys.exit(qt.exec_())


if __name__ == "__main__":
    tempdir = tempfile.gettempdir()
    lockfile = os.sep.join([tempdir, "myapp.lock"])
    try:
        if os.path.isfile(lockfile):
            os.unlink(lockfile)
    except WindowsError as e:  # Should give you smth like 'WindowsError: [Error 32] The process cannot access the file because it is being used by another process..'
        # there's instance already running
        sys.exit(0)

    with open(lockfile, "wb") as lockfileobj:
        # run your app's main here
        main()
    os.unlink(lockfile)
