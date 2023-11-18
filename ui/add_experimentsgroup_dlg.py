# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_experimentsgroup_dlg.ui'
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

class Ui_Dialog_ExperimentsGroup(object):
    def setupUi(self, Dialog_ExperimentsGroup):
        if not Dialog_ExperimentsGroup.objectName():
            Dialog_ExperimentsGroup.setObjectName(u"Dialog_ExperimentsGroup")
        Dialog_ExperimentsGroup.resize(719, 318)
        self.verticalLayout = QVBoxLayout(Dialog_ExperimentsGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(Dialog_ExperimentsGroup)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.comment_text = QPlainTextEdit(Dialog_ExperimentsGroup)
        self.comment_text.setObjectName(u"comment_text")

        self.gridLayout.addWidget(self.comment_text, 4, 1, 1, 1)

        self.comboBox_customer = QComboBox(Dialog_ExperimentsGroup)
        self.comboBox_customer.setObjectName(u"comboBox_customer")

        self.gridLayout.addWidget(self.comboBox_customer, 2, 1, 1, 1)

        self.pushButton_add_customer = QPushButton(Dialog_ExperimentsGroup)
        self.pushButton_add_customer.setObjectName(u"pushButton_add_customer")
        self.pushButton_add_customer.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_customer.sizePolicy().hasHeightForWidth())
        self.pushButton_add_customer.setSizePolicy(sizePolicy)
        self.pushButton_add_customer.setMaximumSize(QSize(22, 16777215))
        self.pushButton_add_customer.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_customer.setIcon(icon)
        self.pushButton_add_customer.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_add_customer, 2, 2, 1, 1)

        self.label_3 = QLabel(Dialog_ExperimentsGroup)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton_add_executor = QPushButton(Dialog_ExperimentsGroup)
        self.pushButton_add_executor.setObjectName(u"pushButton_add_executor")
        self.pushButton_add_executor.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_add_executor.sizePolicy().hasHeightForWidth())
        self.pushButton_add_executor.setSizePolicy(sizePolicy)
        self.pushButton_add_executor.setMaximumSize(QSize(22, 16777215))
        self.pushButton_add_executor.setFocusPolicy(Qt.NoFocus)
        self.pushButton_add_executor.setIcon(icon)
        self.pushButton_add_executor.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_add_executor, 3, 2, 1, 1)

        self.label = QLabel(Dialog_ExperimentsGroup)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(Dialog_ExperimentsGroup)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.comboBox_executor = QComboBox(Dialog_ExperimentsGroup)
        self.comboBox_executor.setObjectName(u"comboBox_executor")

        self.gridLayout.addWidget(self.comboBox_executor, 3, 1, 1, 1)

        self.lineEdit_shortname = QLineEdit(Dialog_ExperimentsGroup)
        self.lineEdit_shortname.setObjectName(u"lineEdit_shortname")

        self.gridLayout.addWidget(self.lineEdit_shortname, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog_ExperimentsGroup)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_contract = QLineEdit(Dialog_ExperimentsGroup)
        self.lineEdit_contract.setObjectName(u"lineEdit_contract")

        self.gridLayout.addWidget(self.lineEdit_contract, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog_ExperimentsGroup)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.lineEdit_shortname, self.lineEdit_contract)
        QWidget.setTabOrder(self.lineEdit_contract, self.comboBox_customer)
        QWidget.setTabOrder(self.comboBox_customer, self.comboBox_executor)
        QWidget.setTabOrder(self.comboBox_executor, self.comment_text)

        self.retranslateUi(Dialog_ExperimentsGroup)
        self.buttonBox.accepted.connect(Dialog_ExperimentsGroup.accept)
        self.buttonBox.rejected.connect(Dialog_ExperimentsGroup.reject)

        QMetaObject.connectSlotsByName(Dialog_ExperimentsGroup)
    # setupUi

    def retranslateUi(self, Dialog_ExperimentsGroup):
        Dialog_ExperimentsGroup.setWindowTitle(QCoreApplication.translate("Dialog_ExperimentsGroup", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_ExperimentsGroup", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.pushButton_add_customer.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog_ExperimentsGroup", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.pushButton_add_executor.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_ExperimentsGroup", u"\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_ExperimentsGroup", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0438\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_ExperimentsGroup", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440", None))
    # retranslateUi

