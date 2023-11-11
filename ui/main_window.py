# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_file_open = QAction(MainWindow)
        self.action_file_open.setObjectName(u"action_file_open")
        self.action_file_close = QAction(MainWindow)
        self.action_file_close.setObjectName(u"action_file_close")
        self.action_file_new = QAction(MainWindow)
        self.action_file_new.setObjectName(u"action_file_new")
        self.action_file_save = QAction(MainWindow)
        self.action_file_save.setObjectName(u"action_file_save")
        self.action_file_saveas = QAction(MainWindow)
        self.action_file_saveas.setObjectName(u"action_file_saveas")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_elastic_materials = QAction(MainWindow)
        self.action_elastic_materials.setObjectName(u"action_elastic_materials")
        self.action_strikers = QAction(MainWindow)
        self.action_strikers.setObjectName(u"action_strikers")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(22, 16777215))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(22, 16777215))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(22, 16777215))

        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_file_open)
        self.menu.addAction(self.action_file_close)
        self.menu.addAction(self.action_file_new)
        self.menu.addAction(self.action_file_save)
        self.menu.addAction(self.action_file_saveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_elastic_materials)
        self.menu_2.addAction(self.action_strikers)

        self.retranslateUi(MainWindow)
        self.action_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dynaexp", None))
        self.action_file_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.action_file_close.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.action_file_new.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.action_file_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_file_saveas.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_elastic_materials.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.action_strikers.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u0440\u043d\u0438\u043a\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0415", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
    # retranslateUi

