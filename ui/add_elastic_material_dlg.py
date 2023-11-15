# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_elastic_material_dlg.ui'
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

class Ui_Dialog_add_elastic_material(object):
    def setupUi(self, Dialog_add_elastic_material):
        if not Dialog_add_elastic_material.objectName():
            Dialog_add_elastic_material.setObjectName(u"Dialog_add_elastic_material")
        Dialog_add_elastic_material.setWindowModality(Qt.ApplicationModal)
        Dialog_add_elastic_material.resize(720, 301)
        self.verticalLayout = QVBoxLayout(Dialog_add_elastic_material)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Dialog_add_elastic_material)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(Dialog_add_elastic_material)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_E = QLineEdit(Dialog_add_elastic_material)
        self.lineEdit_E.setObjectName(u"lineEdit_E")

        self.gridLayout.addWidget(self.lineEdit_E, 1, 1, 1, 1)

        self.lineEdit_name = QLineEdit(Dialog_add_elastic_material)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog_add_elastic_material)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_c = QLineEdit(Dialog_add_elastic_material)
        self.lineEdit_c.setObjectName(u"lineEdit_c")

        self.gridLayout.addWidget(self.lineEdit_c, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog_add_elastic_material)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.comment_text = QPlainTextEdit(Dialog_add_elastic_material)
        self.comment_text.setObjectName(u"comment_text")

        self.gridLayout.addWidget(self.comment_text, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog_add_elastic_material)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.lineEdit_name, self.lineEdit_E)
        QWidget.setTabOrder(self.lineEdit_E, self.lineEdit_c)
        QWidget.setTabOrder(self.lineEdit_c, self.comment_text)

        self.retranslateUi(Dialog_add_elastic_material)
        self.buttonBox.accepted.connect(Dialog_add_elastic_material.accept)
        self.buttonBox.rejected.connect(Dialog_add_elastic_material.reject)

        QMetaObject.connectSlotsByName(Dialog_add_elastic_material)
    # setupUi

    def retranslateUi(self, Dialog_add_elastic_material):
        Dialog_add_elastic_material.setWindowTitle(QCoreApplication.translate("Dialog_add_elastic_material", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_add_elastic_material", u"\u041c\u043e\u0434\u0443\u043b\u044c \u042e\u043d\u0433\u0430, \u041c\u041f\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog_add_elastic_material", u"\u0418\u043c\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_add_elastic_material", u"\u0421\u043a\u043e\u0440\u043e\u0442\u044c \u0437\u0432\u0443\u043a\u0430, \u043c/c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_add_elastic_material", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
    # retranslateUi

