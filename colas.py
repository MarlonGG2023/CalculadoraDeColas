import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QRadioButton
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QLinearGradient, QGradient, QColor, QIntValidator
from math import factorial
from PyQt6 import uic



class Calculadora(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("QueueingCalculator.ui", self)
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_limpiar.clicked.connect(self.limpiar)
        self.llegada = self.ui.lineEdit_llegada
        self.llegada.setValidator(QIntValidator)
        self.llegada.textChanged.connect(self)
        self.servicio = self.ui.lineEdit_servicio
        self.servicio.setValidator(QIntValidator)
        self.numeroServicio = self.ui.lineEdit_numeroServicio
        self.numeroServicio.setValidator(QIntValidator)
        self.cliente = self.ui.lineEdit_cliente
        self.cliente.setValidator(QIntValidator)
        self.label_p = self.findChild(QLabel,"label_P")
        self.label_p0 = self.findChild(QLabel,"label_P0")
        self.label_lq = self.findChild(QLabel,"label_Lq")
        self.label_wq = self.findChild(QLabel,"label_Wq")
        self.label_ls = self.findChild(QLabel,"label_Ls")
        self.label_ws = self.findChild(QLabel,"lavWs")

    def calcular(self):
        self.update_label(self)
        return
    
    
    
    def limpiar(self):
     self.llegada.clear()
     self.servicio.clear()
     self.numeroServicio.clear()
     self.cliente.clear()
   


    def calcularFactorDeUso(self):
        rho = self.llegada.text / self.servicio.text * self.numeroServicio.text
        return rho
        
    def ProbabilidadNingunaPersonaSistema(self,rho):
        return

    def update_label(self):
        FactorDeUso = self.calcularFactorDeUso(self)
        self.label_p.setText(FactorDeUso)
        #self.label_numero.setText(balota)
       

 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec())