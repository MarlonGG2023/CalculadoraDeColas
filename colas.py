import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIntValidator
from PyQt6 import uic
from math import factorial

class Calculadora(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("QueueingCalculator.ui", self)

        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_limpiar.clicked.connect(self.limpiar)

        self.llegada = self.lineEdit_llegada
        self.llegada.setValidator(QIntValidator())

        self.servicio = self.lineEdit_servicio
        self.servicio.setValidator(QIntValidator())

        self.numeroServicio = self.lineEdit_numeroServicio
        self.numeroServicio.setValidator(QIntValidator())


        self.label_p = self.findChild(QLabel, "label_P")
        self.label_p0 = self.findChild(QLabel, "label_P0")
        self.label_lq = self.findChild(QLabel, "label_Lq")
        self.label_wq = self.findChild(QLabel, "label_Wq")
        self.label_ls = self.findChild(QLabel, "label_Ls")
        self.label_ws = self.findChild(QLabel, "label_Ws")

    def calcular(self):
        self.update_label()

    def limpiar(self):
        self.llegada.clear()
        self.servicio.clear()
        self.numeroServicio.clear()
        self.label_lq.clear()
        self.label_ls.clear()
        self.label_p.clear()
        self.label_p0.clear()
        self.label_wq.clear()
        self.label_ws.clear()

    def calcularFactorDeUso(self):
        try:
            llegada = float(self.llegada.text())
            servicio = float(self.servicio.text())
            numeroServicio = float(self.numeroServicio.text())
            rho = llegada / (servicio * numeroServicio)
            return rho
        except ValueError:
            return "Error"

    def probabilidadSistemaVacio(self, rho, numeroServicio):
        try:
            numeroServicio = int(numeroServicio)  
            sumatoria = sum((numeroServicio * rho) ** k / factorial(k) for k in range(numeroServicio))
            segundo_termino = (numeroServicio * rho) ** numeroServicio / (factorial(numeroServicio) * (1 - rho))
            p0 = 1 / (sumatoria + segundo_termino)
            return p0
        except ValueError:
            return "Error"

    def calcularLongitudPromedioClientesCola(self, rho, p0):
        try:
            numeroServicio = int(self.numeroServicio.text())
            lq = (rho ** 2 / (1 - rho)) * p0 * (numeroServicio / (factorial(numeroServicio) * ((numeroServicio * (1 - rho)) ** 2)))
            return lq
        except ValueError:
            return "Error"

    def calcularWQ(self, lq):
        try:
            llegada = float(self.llegada.text())
            wq = lq / llegada
            return wq
        except ValueError:
            return "Error"

    def calcularLongitudPromedioClientesSistema(self, lq):
        try:
            llegada = float(self.llegada.text())
            servicio = float(self.servicio.text())
            ls = lq + (llegada / servicio)
            return ls
        except ValueError:
            return "Error"

    def calcularTeimpoPromedioClientesSistema(self, wq):
        try:
            servicio = float(self.servicio.text())
            ws = wq + (1 / servicio)
            return ws
        except ValueError:
            return "Error"

    def update_label(self):
        rho = self.calcularFactorDeUso()
        if rho == "Error":
            self.label_p.setText("Error en el cálculo de Factor de Uso")
            return

        numeroServicio = float(self.numeroServicio.text())
        p0 = self.probabilidadSistemaVacio(rho, numeroServicio)
        if p0 == "Error":
            self.label_p0.setText("Error en el cálculo de P0")
            return

        lq = self.calcularLongitudPromedioClientesCola(rho, p0)
        if lq == "Error":
            self.label_lq.setText("Error en el cálculo de Lq")
            return

        wq = self.calcularWQ(lq)
        if wq == "Error":
            self.label_wq.setText("Error en el cálculo de Wq")
            return

        ls = self.calcularLongitudPromedioClientesSistema(lq)
        if ls == "Error":
            self.label_ls.setText("Error en el cálculo de Ls")
            return

        ws = self.calcularTeimpoPromedioClientesSistema(wq)
        if ws == "Error":
            self.label_ws.setText("Error en el cálculo de Ws")
            return

        self.label_p.setText(f"ρ (Factor de Uso): {rho:.5f}")
        self.label_p0.setText(f"ρο (Probabilidad Sistema Vacío): {p0:.5f}")
        self.label_lq.setText(f"Lq (Longitud Promedio clientes cola): {lq:.5f}")
        self.label_wq.setText(f"Wq (Tiempo promedio clientes cola): {wq:.5f}")
        self.label_ls.setText(f"Ls (Longitud Promedio clientes sistema): {ls:.5f}")
        self.label_ws.setText(f"Ws (Tiempo promedio clientes sistema): {ws:.5f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Calculadora()
    GUI.show()
    sys.exit(app.exec())
