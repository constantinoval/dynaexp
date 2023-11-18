# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_customer_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_add_customer(object):
    def setupUi(self, Dialog_add_customer):
        if not Dialog_add_customer.objectName():
            Dialog_add_customer.setObjectName(u"Dialog_add_customer")
        Dialog_add_customer.setWindowModality(Qt.ApplicationModal)
        Dialog_add_customer.resize(720, 301)
        self.verticalLayout = QVBoxLayout(Dialog_add_customer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Dialog_add_customer)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label = QLabel(Dialog_add_customer)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comment_text = QPlainTextEdit(Dialog_add_customer)
        self.comment_text.setObjectName(u"comment_text")

        self.gridLayout.addWidget(self.comment_text, 1, 1, 1, 1)

        self.lineEdit_name = QLineEdit(Dialog_add_customer)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog_add_customer)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.lineEdit_name, self.comment_text)

        self.retranslateUi(Dialog_add_customer)
        self.buttonBox.accepted.connect(Dialog_add_customer.accept)
        self.buttonBox.rejected.connect(Dialog_add_customer.reject)

        QMetaObject.connectSlotsByName(Dialog_add_customer)
    # setupUi

    def retranslateUi(self, Dialog_add_customer):
        Dialog_add_customer.setWindowTitle(QCoreApplication.translate("Dialog_add_customer", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_add_customer", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.label.setText(QCoreApplication.translate("Dialog_add_customer", u"\u0418\u043c\u044f \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
    # retranslateUi

