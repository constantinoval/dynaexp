# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")

        self.verticalLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")

        self.verticalLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton(self.centralwidget)
        self.pushButton3.setObjectName(u"pushButton3")

        self.verticalLayout.addWidget(self.pushButton3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.stackedWidget1 = QStackedWidget(self.centralwidget)
        self.stackedWidget1.setObjectName(u"stackedWidget1")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget1.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget1.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget1)

        self.stackedWidget2 = QStackedWidget(self.centralwidget)
        self.stackedWidget2.setObjectName(u"stackedWidget2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget2.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

