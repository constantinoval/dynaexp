# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tableView_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_dlg_tableView(object):
    def setupUi(self, dlg_tableView):
        if not dlg_tableView.objectName():
            dlg_tableView.setObjectName(u"dlg_tableView")
        dlg_tableView.setWindowModality(Qt.ApplicationModal)
        dlg_tableView.resize(839, 315)
        self.horizontalLayout = QHBoxLayout(dlg_tableView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableView = QTableView(dlg_tableView)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.tableView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_add = QPushButton(dlg_tableView)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.verticalLayout.addWidget(self.pushButton_add)

        self.pushButton_edit = QPushButton(dlg_tableView)
        self.pushButton_edit.setObjectName(u"pushButton_edit")

        self.verticalLayout.addWidget(self.pushButton_edit)

        self.pushButton_remove = QPushButton(dlg_tableView)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.verticalLayout.addWidget(self.pushButton_remove)

        self.pushButton_close = QPushButton(dlg_tableView)
        self.pushButton_close.setObjectName(u"pushButton_close")

        self.verticalLayout.addWidget(self.pushButton_close)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(dlg_tableView)
        self.pushButton_close.pressed.connect(dlg_tableView.close)

        QMetaObject.connectSlotsByName(dlg_tableView)
    # setupUi

    def retranslateUi(self, dlg_tableView):
        dlg_tableView.setWindowTitle(QCoreApplication.translate("dlg_tableView", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.pushButton_add.setText(QCoreApplication.translate("dlg_tableView", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_edit.setText(QCoreApplication.translate("dlg_tableView", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_remove.setText(QCoreApplication.translate("dlg_tableView", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_close.setText(QCoreApplication.translate("dlg_tableView", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

