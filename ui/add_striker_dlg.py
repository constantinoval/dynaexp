# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_striker_dlg.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog_Add_Striker(object):
    def setupUi(self, Dialog_Add_Striker):
        if not Dialog_Add_Striker.objectName():
            Dialog_Add_Striker.setObjectName(u"Dialog_Add_Striker")
        Dialog_Add_Striker.resize(719, 318)
        self.verticalLayout = QVBoxLayout(Dialog_Add_Striker)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Dialog_Add_Striker)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label = QLabel(Dialog_Add_Striker)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_L = QLineEdit(Dialog_Add_Striker)
        self.lineEdit_L.setObjectName(u"lineEdit_L")

        self.gridLayout.addWidget(self.lineEdit_L, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lineEdit_D0 = QLineEdit(Dialog_Add_Striker)
        self.lineEdit_D0.setObjectName(u"lineEdit_D0")

        self.gridLayout.addWidget(self.lineEdit_D0, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label_3 = QLabel(Dialog_Add_Striker)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.pushButton_add_material = QPushButton(Dialog_Add_Striker)
        self.pushButton_add_material.setObjectName(u"pushButton_add_material")
        self.pushButton_add_material.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_material.sizePolicy().hasHeightForWidth())
        self.pushButton_add_material.setSizePolicy(sizePolicy)
        self.pushButton_add_material.setMaximumSize(QSize(22, 16777215))
        self.pushButton_add_material.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_material.setIcon(icon)
        self.pushButton_add_material.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_add_material, 3, 2, 1, 1)

        self.lineEdit_D = QLineEdit(Dialog_Add_Striker)
        self.lineEdit_D.setObjectName(u"lineEdit_D")

        self.gridLayout.addWidget(self.lineEdit_D, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.comboBox_material = QComboBox(Dialog_Add_Striker)
        self.comboBox_material.setObjectName(u"comboBox_material")

        self.gridLayout.addWidget(self.comboBox_material, 3, 1, 1, 1)

        self.label_2 = QLabel(Dialog_Add_Striker)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_5 = QLabel(Dialog_Add_Striker)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.comment_text = QPlainTextEdit(Dialog_Add_Striker)
        self.comment_text.setObjectName(u"comment_text")

        self.gridLayout.addWidget(self.comment_text, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog_Add_Striker)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.lineEdit_D, self.lineEdit_D0)
        QWidget.setTabOrder(self.lineEdit_D0, self.lineEdit_L)
        QWidget.setTabOrder(self.lineEdit_L, self.comboBox_material)
        QWidget.setTabOrder(self.comboBox_material, self.comment_text)
        QWidget.setTabOrder(self.comment_text, self.pushButton_add_material)

        self.retranslateUi(Dialog_Add_Striker)
        self.buttonBox.accepted.connect(Dialog_Add_Striker.accept)
        self.buttonBox.rejected.connect(Dialog_Add_Striker.reject)

        QMetaObject.connectSlotsByName(Dialog_Add_Striker)
    # setupUi

    def retranslateUi(self, Dialog_Add_Striker):
        Dialog_Add_Striker.setWindowTitle(QCoreApplication.translate("Dialog_Add_Striker", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u0434\u0430\u0440\u043d\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_Add_Striker", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440, \u043c\u043c", None))
        self.label.setText(QCoreApplication.translate("Dialog_Add_Striker", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0434\u0438\u0430\u043c\u0435\u0442\u0440, \u043c\u043c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_Add_Striker", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.pushButton_add_material.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog_Add_Striker", u"\u0414\u043b\u0438\u043d\u0430, \u043c\u043c", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_Add_Striker", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
    # retranslateUi

