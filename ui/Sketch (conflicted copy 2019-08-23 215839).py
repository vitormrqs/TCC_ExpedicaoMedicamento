# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import csv
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtGui import *   
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from .Ui_Sketch import Ui_MainWindow

def mensagem(texto):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("H3V informa:")
    msg.setInformativeText(str(texto))
    msg.setWindowTitle("H3V")
    #msg.setDetailedText("Detalhes.")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()

def att_Table(self):
    connection=sqlite3.connect("estoque.db")
    result = connection.execute("SELECT * FROM ESTOQUE WHERE FLAG = '1'")
    self.tableWidget.setRowCount(0)
    for row_number,  row_data in enumerate(result):
        self.tableWidget.insertRow(row_number)
        for column_number,  data in enumerate(row_data):
            self.tableWidget.setItem(row_number, column_number,  QtWidgets.QTableWidgetItem(str(data)))
    connection.close()

def exportar_Excel(linhas):
    with open("Estoque.csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Pedido:','Data:','Medico:','Paciente:','Neosoro:','Salonpas:','Puran T4:','Alegra:', 'Flag:'])
        spamwriter.writerow(['','','','','','','','',''])
        for x in linhas:
            spamwriter.writerow(x)
    
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        ##Variaveis globais:
        global medico
        global data
        global neosoro
        global alegra
        global puran
        global salonpas
        data = ""
        #Conexão com o banco de dados;
        connection=sqlite3.connect("estoque.db")
        #Escrevendo em cada label a quantidade disponivel no estoque
            #1
        est1 = connection.execute("SELECT SUM(rem1) FROM ESTOQUE where pedido >= 0")
        est1 = est1.fetchone()[0]
        self.label_2.setText(str(est1))
        self.label_17.setText(str(est1))
            #2
        est2 = connection.execute("SELECT SUM(rem2) FROM ESTOQUE where pedido >= 0")
        est2 = est2.fetchone()[0]
        self.label_14.setText(str(est2))
        self.label_21.setText(str(est2))
            #3
        est3 = connection.execute("SELECT SUM(rem3) FROM ESTOQUE where pedido >= 0")
        est3 = est3.fetchone()[0]
        self.label_3.setText(str(est3))
        self.label_15.setText(str(est3))
            #4
        est4 = connection.execute("SELECT SUM(rem4) FROM ESTOQUE where pedido >= 0")
        est4 =est4.fetchone()[0]
        self.label_12.setText(str(est4))
        self.label_20.setText(str(est4))
        connection.close()
        self.tableWidget.setHorizontalHeaderLabels(["Pedido", "Data", "Médico", "Paciente", "Neosoro", "Salonpas", "Puran T4", "Alegra", "Ativo"]) 
        att_Table(self)
        
    @pyqtSlot(QDate) #Identifica o dia
    def on_calendarWidget_clicked(self, date): 
        """
        Captura do dia selecionado.
        
        @param date DESCRIPTION
        @type QDate
        """
        global data
        data = self.calendarWidget.selectedDate()
        data=data.toString()
        ##Alteracao de ''qui 10 out 2019'' para ''2019-10-10''
        ddia=data[8:10]
        ##Arrumando os dias que não possuem 2 dígitos
        if (ddia[1]==" "):
            dmes=data[4:7]
            dano=data[10:14]
            ddia="0"+data[8:9]
        else:
            dmes=data[4:7]
            dano=data[11:15]
        if (dmes=="jan"):
            dmes="01"
        elif (dmes=="fev"):
            dmes="02"
        elif (dmes=="mar"):
            dmes="03"
        elif (dmes=="abr"):
            dmes="04"
        elif (dmes=="mai"):
            dmes="05"
        elif (dmes=="jun"):
            dmes="06"
        elif (dmes=="jul"):
            dmes="07"
        elif (dmes=="ago"):
            dmes="08"
        elif (dmes=="set"):
            dmes="09"
        elif (dmes=="out"):
            dmes="10"
        elif (dmes=="nov"):
            dmes="11"
        else:
            dmes="12"
        data=dano+"-"+dmes+"-"+ddia
        
    @pyqtSlot() #Limpa campos e adiciona receita na db
    def on_pushButton_3_clicked(self):
        """
        Limpa os radioButtons, editText e checkBox e também insere os campos no banco de dados.
        """
        global data
        medico=''
        paciente=''
        #RADIOBUTTONS;
            ##Verifica qual é o ativado:
        if self.radioButton.isChecked():
            medico='Dra. Alice'
        if self.radioButton_2.isChecked():
            medico='Dr. Humberto'
        if self.radioButton_3.isChecked():
            medico='Dra. Andreia'
        if self.radioButton_4.isChecked():
            medico='Dr. Hans Chucrutes'
            ##Desligar os radioButtons;
        self.radioButton.setCheckable(False)
        self.radioButton_2.setCheckable(False)
        self.radioButton_3.setCheckable(False)
        self.radioButton_4.setCheckable(False)
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_4.setChecked(False)
        self.radioButton.setCheckable(True)
        self.radioButton_2.setCheckable(True)
        self.radioButton_3.setCheckable(True)
        self.radioButton_4.setCheckable(True)
        
        #CHECKBOX:
        if self.checkBox_9.isChecked():
            rem1=-int(self.lineEdit_2.text()) #Neosoro
        else:
            rem1=0
        if self.checkBox_13.isChecked():
            rem2=-int(self.lineEdit_5.text()) #Salonpas
        else:
            rem2=0
        if self.checkBox_16.isChecked():
            rem3=-int(self.lineEdit_4.text()) #Puran T4
        else:
            rem3=0
        if self.checkBox_12.isChecked():
            rem4=-int(self.lineEdit_3.text()) #Alegra
        else:
            rem4=0
            #Desliga os checkBox:
        self.checkBox_9.setCheckState(False)
        self.checkBox_13.setCheckState(False)
        self.checkBox_16.setCheckState(False)
        self.checkBox_12.setCheckState(False)
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        
        #EDITTEXT:
            ##Atribuir o valor do paciente a variável e limpar:
        paciente=self.lineEdit.text()
        self.lineEdit.setText("")
        
        #Conexão com o banco de dados;
        connection=sqlite3.connect("estoque.db")
        
        #Aproveita a conexão e adquire o NºPedido:
        pedido=connection.execute("SELECT MAX(pedido) FROM ESTOQUE where pedido >= 0")
        pedido=pedido.fetchone()[0]+1
        flag='1'
        #Insere no db se as condicoes forem preenchidas corretamente:
        if medico!="" and data!="" and paciente!="":
            connection.execute("INSERT INTO ESTOQUE VALUES(?,?,?,?,?,?,?,?,?)",  (pedido, data,  medico,  paciente,  rem1,  rem2,  rem3,  rem4,  flag))
            connection.commit()
            mensagem("Pedido do paciente " +'%s' %(paciente) + " efetuado com sucesso! Favor retirar na enfermaria o pedido N°"  +'%i' %(pedido) + ".")
        else:
            mensagem("Existe algo errado com a prescrição..")
            
        #Criação de um cursor para contagem das linhas da db para futura exportação:
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM ESTOQUE")
        linhas = cursor.fetchall()

        #Escrevendo em cada label a quantidade disponivel no estoque
            #1
        est1 = connection.execute("SELECT SUM(rem1) FROM ESTOQUE where pedido >= 0")
        est1 = est1.fetchone()[0]
        self.label_2.setText(str(est1))
        self.label_17.setText(str(est1))
            #2
        est2 = connection.execute("SELECT SUM(rem2) FROM ESTOQUE where pedido >= 0")
        est2 = est2.fetchone()[0]
        self.label_14.setText(str(est2))
        self.label_21.setText(str(est2))
            #3
        est3 = connection.execute("SELECT SUM(rem3) FROM ESTOQUE where pedido >= 0")
        est3 = est3.fetchone()[0]
        self.label_3.setText(str(est3))
        self.label_15.setText(str(est3))
            #4
        est4 = connection.execute("SELECT SUM(rem4) FROM ESTOQUE where pedido >= 0")
        est4 =est4.fetchone()[0]
        self.label_12.setText(str(est4))
        self.label_20.setText(str(est4))
        connection.close()

        if medico=="" and data=="" and paciente=="":
            ##Exportando para um csv;
            exportar_Excel(linhas)
                    
        att_Table(self)
    
    @pyqtSlot() #'Deleta' o pedido do estoque
    def on_pushButton_2_clicked(self):
        """
        'Deleta' pedido do estoque
        """
        #Detecta o pedido:
        pedido=str(self.lineEdit_7.text()).strip()
        #Deleta o pedido:
        connection=sqlite3.connect("estoque.db")
        verificacao = connection.execute("SELECT count(pedido) FROM ESTOQUE WHERE PEDIDO = ? AND FLAG=1",  (pedido, ))
        verificacao = verificacao.fetchone()[0]
        if verificacao!=0:
            connection.execute("UPDATE ESTOQUE SET FLAG='0' WHERE PEDIDO = ?",  (pedido, ))
            connection.commit()
            mensagem("Pedido N°"  +'%s' %(pedido) + " removido com sucesso.")
        else:
            mensagem("Pedido N°"  +'%s' %(pedido) + " inexistente.")
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM ESTOQUE")
        linhas = cursor.fetchall()
        connection.close()
        #Limpa o campo:
        self.lineEdit_7.setText("")
        #Exportando para um csv;
        exportar_Excel(linhas)
        #Atualizando a tabela;     
        att_Table(self)

    @pyqtSlot() #Reposicao de Neosoro
    def on_pushButton_4_clicked(self):
        """
        Deleta pedido do estoque
        """
        inp = QtWidgets.QInputDialog(self)
        rem1, ok = QInputDialog.getInt(inp, "H3V pergunta","Quantidade a ser adicionada:", 25, 0, 100, 1)
        if ok:
            connection=sqlite3.connect("estoque.db")
            pedido=connection.execute("SELECT MAX(pedido) FROM ESTOQUE where pedido >= 0")
            pedido=pedido.fetchone()[0]+1
            connection.execute("INSERT INTO ESTOQUE VALUES(?,?,?,?,?,?,?,?,?)",  (pedido, '0',  '0',  '0',  rem1,  0,  0,  0,  '0'))
            connection.commit()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM ESTOQUE")
            linhas = cursor.fetchall()
                ##Exportando para um csv;
            exportar_Excel(linhas)
            #Conexão com o banco de dados;
            #Escrevendo em cada label a quantidade disponivel no estoque
            est1 = connection.execute("SELECT SUM(rem1) FROM ESTOQUE where pedido >= 0")
            est1 = est1.fetchone()[0]
            self.label_2.setText(str(est1))
            self.label_17.setText(str(est1))
            connection.close()
            mensagem("Adicionado "  +'%i' %(rem1) + " Neosoro ao estoque com sucesso.")
        else:
            mensagem("Reposição cancelada.")
            
    @pyqtSlot() #Reposicao de Salonpas
    def on_pushButton_11_clicked(self):
        """
        Deleta pedido do estoque
        """
        inp = QtWidgets.QInputDialog(self)
        rem2, ok = QInputDialog.getInt(inp, "H3V pergunta","Quantidade a ser adicionada:", 25, 0, 100, 1)
        if ok:
            connection=sqlite3.connect("estoque.db")
            pedido=connection.execute("SELECT MAX(pedido) FROM ESTOQUE where pedido >= 0")
            pedido=pedido.fetchone()[0]+1
            connection.execute("INSERT INTO ESTOQUE VALUES(?,?,?,?,?,?,?,?,?)",  (pedido, '0',  '0',  '0',  0,  rem2,  0,  0,  '0'))
            connection.commit()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM ESTOQUE")
            linhas = cursor.fetchall()
                ##Exportando para um csv;
            exportar_Excel(linhas)
            #Escrevendo em cada label a quantidade disponivel no estoque
            est2 = connection.execute("SELECT SUM(rem2) FROM ESTOQUE where pedido >= 0")
            est2 = est2.fetchone()[0]
            self.label_14.setText(str(est2))
            self.label_21.setText(str(est2))
            connection.close()
            mensagem("Adicionado "  +'%i' %(rem2) + " Salonpas ao estoque com sucesso.")
        else:
            mensagem("Reposição cancelada.")
    
    @pyqtSlot() #Reposicao de Puran T4
    def on_pushButton_7_clicked(self):
        """
        Deleta pedido do estoque
        """
        inp = QtWidgets.QInputDialog(self)
        rem3, ok = QInputDialog.getInt(inp, "H3V pergunta","Quantidade a ser adicionada:", 25, 0, 100, 1)
        if ok:
            connection=sqlite3.connect("estoque.db")
            pedido=connection.execute("SELECT MAX(pedido) FROM ESTOQUE where pedido >= 0")
            pedido=pedido.fetchone()[0]+1
            connection.execute("INSERT INTO ESTOQUE VALUES(?,?,?,?,?,?,?,?,?)",  (pedido, '0',  '0',  '0',  0,  0,  rem3,  0,  '0'))
            connection.commit()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM ESTOQUE")
            linhas = cursor.fetchall()
                ##Exportando para um csv;
            exportar_Excel(linhas)
            #Escrevendo em cada label a quantidade disponivel no estoque
            est3 = connection.execute("SELECT SUM(rem3) FROM ESTOQUE where pedido >= 0")
            est3 = est3.fetchone()[0]
            self.label_3.setText(str(est3))
            self.label_15.setText(str(est3))
            connection.close()
            mensagem("Adicionado "  +'%i' %(rem3) + " Puran T4 ao estoque com sucesso.")
        else:
            mensagem("Reposição cancelada.", "H3V informa")
                
    @pyqtSlot() #Reposicao de Alegra
    def on_pushButton_8_clicked(self):
        """
        Deleta pedido do estoque
        """
        inp = QtWidgets.QInputDialog(self)
        rem4, ok = QInputDialog.getInt(inp, "H3V pergunta","Quantidade a ser adicionada:", 25, 0, 100, 1)
        if ok:
            connection=sqlite3.connect("estoque.db")
            pedido=connection.execute("SELECT MAX(pedido) FROM ESTOQUE where pedido >= 0")
            pedido=pedido.fetchone()[0]+1
            connection.execute("INSERT INTO ESTOQUE VALUES(?,?,?,?,?,?,?,?,?)",  (pedido, '0',  '0',  '0',  0,  0,  0,  rem4,  '0'))
            connection.commit()
            cursor=connection.cursor()
            cursor.execute("SELECT * FROM ESTOQUE")
            linhas = cursor.fetchall()
                ##Exportando para um csv;
            exportar_Excel(linhas)
            #Escrevendo em cada label a quantidade disponivel no estoque
            est4 = connection.execute("SELECT SUM(rem4) FROM ESTOQUE where pedido >= 0")
            est4 = est4.fetchone()[0]
            self.label_12.setText(str(est4))
            self.label_20.setText(str(est4))
            connection.close()
            mensagem("Adicionado "  +'%i' %(rem4) + " Alegra ao estoque com sucesso.")
        else:
            mensagem("Reposição cancelada.")
    
    @pyqtSlot() #Atualização da fila de pedidos
    def on_pushButton_5_clicked(self):
        """
        Atualização da fila de pedidos
        """
        att_Table(self)

