# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pizzeria.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_confirm = QPushButton(self.centralwidget)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(510, 410, 171, 81))
        font = QFont()
        font.setPointSize(14)
        self.btn_confirm.setFont(font)
        self.textTitulo = QLabel(self.centralwidget)
        self.textTitulo.setObjectName(u"textTitulo")
        self.textTitulo.setGeometry(QRect(20, 10, 401, 71))
        font1 = QFont()
        font1.setPointSize(20)
        self.textTitulo.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 530, 451, 16))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 90, 877, 275))
        self.horizontalAll = QHBoxLayout(self.layoutWidget)
        self.horizontalAll.setObjectName(u"horizontalAll")
        self.horizontalAll.setContentsMargins(0, 0, 0, 0)
        self.verticalInfo = QVBoxLayout()
        self.verticalInfo.setObjectName(u"verticalInfo")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.txt_name = QLineEdit(self.layoutWidget)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.txt_name)


        self.verticalInfo.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalInfo.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.txt_address = QLineEdit(self.layoutWidget)
        self.txt_address.setObjectName(u"txt_address")
        self.txt_address.setFont(font)

        self.horizontalLayout_3.addWidget(self.txt_address)


        self.verticalInfo.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalInfo.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.radBtnCircular = QRadioButton(self.layoutWidget)
        self.radBtnCircular.setObjectName(u"radBtnCircular")
        self.radBtnCircular.setFont(font)
        self.radBtnCircular.setChecked(True)

        self.horizontalLayout.addWidget(self.radBtnCircular)

        self.radBtnRectangular = QRadioButton(self.layoutWidget)
        self.radBtnRectangular.setObjectName(u"radBtnRectangular")
        self.radBtnRectangular.setFont(font)

        self.horizontalLayout.addWidget(self.radBtnRectangular)


        self.verticalInfo.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalInfo.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalInfo.addWidget(self.label_6)


        self.horizontalAll.addLayout(self.verticalInfo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalAll.addItem(self.horizontalSpacer)

        self.formCalendario = QFormLayout()
        self.formCalendario.setObjectName(u"formCalendario")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formCalendario.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.calendarWidget = QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.formCalendario.setWidget(1, QFormLayout.LabelRole, self.calendarWidget)


        self.horizontalAll.addLayout(self.formCalendario)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 370, 346, 141))
        self.gridIngredientes = QGridLayout(self.layoutWidget1)
        self.gridIngredientes.setObjectName(u"gridIngredientes")
        self.gridIngredientes.setContentsMargins(0, 0, 0, 0)
        self.boxPepperoni = QCheckBox(self.layoutWidget1)
        self.boxPepperoni.setObjectName(u"boxPepperoni")
        font2 = QFont()
        font2.setPointSize(12)
        self.boxPepperoni.setFont(font2)

        self.gridIngredientes.addWidget(self.boxPepperoni, 0, 0, 1, 2)

        self.boxPina = QCheckBox(self.layoutWidget1)
        self.boxPina.setObjectName(u"boxPina")
        self.boxPina.setFont(font2)

        self.gridIngredientes.addWidget(self.boxPina, 0, 2, 1, 2)

        self.boxJamon = QCheckBox(self.layoutWidget1)
        self.boxJamon.setObjectName(u"boxJamon")
        self.boxJamon.setFont(font2)

        self.gridIngredientes.addWidget(self.boxJamon, 2, 0, 1, 3)

        self.boxSalchicha = QCheckBox(self.layoutWidget1)
        self.boxSalchicha.setObjectName(u"boxSalchicha")
        self.boxSalchicha.setFont(font2)

        self.gridIngredientes.addWidget(self.boxSalchicha, 2, 3, 1, 3)

        self.boxSalami = QCheckBox(self.layoutWidget1)
        self.boxSalami.setObjectName(u"boxSalami")
        self.boxSalami.setFont(font2)

        self.gridIngredientes.addWidget(self.boxSalami, 1, 0, 1, 2)

        self.boxMushroom = QCheckBox(self.layoutWidget1)
        self.boxMushroom.setObjectName(u"boxMushroom")
        self.boxMushroom.setFont(font2)

        self.gridIngredientes.addWidget(self.boxMushroom, 1, 2, 1, 2)

        self.boxQueso = QCheckBox(self.layoutWidget1)
        self.boxQueso.setObjectName(u"boxQueso")
        self.boxQueso.setFont(font2)

        self.gridIngredientes.addWidget(self.boxQueso, 1, 4, 1, 2)

        self.boxTocino = QCheckBox(self.layoutWidget1)
        self.boxTocino.setObjectName(u"boxTocino")
        self.boxTocino.setFont(font2)

        self.gridIngredientes.addWidget(self.boxTocino, 0, 4, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirmar Pedido", None))
        self.textTitulo.setText(QCoreApplication.translate("MainWindow", u"Pizzeria Los Tilines | Pedido", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Si tiene alg\u00fan problema puede contactarnos en el siguiente n\u00famero: 375 104 3841", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Domicilio: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Forma de la Pizza: ", None))
        self.radBtnCircular.setText(QCoreApplication.translate("MainWindow", u"Circular", None))
        self.radBtnRectangular.setText(QCoreApplication.translate("MainWindow", u"Rectangular", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ingredientes: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D\u00eda a Pedir: ", None))
        self.boxPepperoni.setText(QCoreApplication.translate("MainWindow", u"Pepperoni", None))
        self.boxPina.setText(QCoreApplication.translate("MainWindow", u"Pi\u00f1a", None))
        self.boxJamon.setText(QCoreApplication.translate("MainWindow", u"Jam\u00f3n", None))
        self.boxSalchicha.setText(QCoreApplication.translate("MainWindow", u"Salchicha", None))
        self.boxSalami.setText(QCoreApplication.translate("MainWindow", u"Salami", None))
        self.boxMushroom.setText(QCoreApplication.translate("MainWindow", u"Champi\u00f1on", None))
        self.boxQueso.setText(QCoreApplication.translate("MainWindow", u"Solo Queso", None))
        self.boxTocino.setText(QCoreApplication.translate("MainWindow", u"Tocino", None))
    # retranslateUi

