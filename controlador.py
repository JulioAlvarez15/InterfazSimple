from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow, QMessageBox
from pizzeria_ui import Ui_MainWindow
from PySide6.QtCore import QRegularExpression as QRE
from PySide6.QtGui import QRegularExpressionValidator as QREV
import sys

class Ctrl_Interfaz(QtWidgets.QMainWindow):
    
    #! Constructor
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.inicializar()
    
    #! Función para inicializar la interfaz
    def inicializar(self):
        #? Inicializar botones
        self.gui.btn_confirm.setEnabled(False) 
        self.gui.btn_confirm.clicked.connect(self.datosCliente)
        
        #? Conectar señales
        self.gui.txt_name.textChanged.connect(self.activarBoton)
        self.gui.txt_address.textChanged.connect(self.activarBoton)
        self.gui.boxPepperoni.stateChanged.connect(self.activarBoton)
        self.gui.boxPina.stateChanged.connect(self.activarBoton)
        self.gui.boxTocino.stateChanged.connect(self.activarBoton)
        self.gui.boxSalami.stateChanged.connect(self.activarBoton)
        self.gui.boxMushroom.stateChanged.connect(self.activarBoton)
        self.gui.boxQueso.stateChanged.connect(self.activarBoton)
        self.gui.boxJamon.stateChanged.connect(self.activarBoton)
        self.gui.boxSalchicha.stateChanged.connect(self.activarBoton)
        
        #? Validacion nombre
        lim = "[A-z]+ [A-z]+ [A-z]+"
        expresion_regular = QRE(lim)
        validacion_nom = QREV(expresion_regular)
        self.gui.txt_name.setValidator(validacion_nom)
        
        #? Validacion domicilio
        lim = "^[A-Za-z0-9., -#]+$"
        expresion_regular = QRE(lim)
        validacion_address = QREV(expresion_regular)
        self.gui.txt_address.setValidator(validacion_address)

    #! Función para obtener los datos del cliente (Pedido)
    def datosCliente(self):
        nombre = self.gui.txt_name.text()
        domicilio = self.gui.txt_address.text()
        
        if self.gui.radBtnCircular.isChecked():
            tipo = "Circular"
        else:
            tipo = "Rectangular"
        
        #? Guardar ingredientes seleccionados
        ingredientes = []
        if self.gui.boxPepperoni.isChecked():
            ingredientes.append("Pepperoni")
        
        if self.gui.boxPina.isChecked():
            ingredientes.append("Piña")
        
        if self.gui.boxTocino.isChecked():
            ingredientes.append("Tocino")
        
        if self.gui.boxSalami.isChecked():
            ingredientes.append("Salami")
        
        if self.gui.boxMushroom.isChecked():
            ingredientes.append("Champiñones")
        
        if self.gui.boxQueso.isChecked():
            ingredientes.append("Solo Queso")
        
        if self.gui.boxJamon.isChecked():
            ingredientes.append("Jamón")
        
        if self.gui.boxSalchicha.isChecked():
            ingredientes.append("Salchicha")
        
        fecha = self.gui.calendarWidget.selectedDate().toString()
        
        ingredientes_str = ", ".join(ingredientes)
        
        QMessageBox.information(self, "Pedido", f"Nombre: {nombre}\nDomicilio: {domicilio}\nForma: {tipo}\nIngredientes: {ingredientes_str}\nDía de Entrega: {fecha}")

    #! Función para activar el botón del pedido
    def activarBoton(self):
        if (len(self.gui.txt_name.text()) > 2 and len(self.gui.txt_address.text()) > 3) and(self.gui.boxPepperoni.isChecked() or self.gui.boxPina.isChecked() or self.gui.boxTocino.isChecked() or self.gui.boxSalami.isChecked() or self.gui.boxMushroom.isChecked() or self.gui.boxQueso.isChecked() or self.gui.boxJamon.isChecked() or self.gui.boxSalchicha.isChecked()):
            self.gui.btn_confirm.setEnabled(True)
        else:
            self.gui.btn_confirm.setEnabled(False)

#! Main
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ctrl_Interfaz()
    window.show()
    sys.exit(app.exec())
