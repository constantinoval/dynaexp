# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_oscchannel.ui'
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
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog_add_oscchannel(object):
    def setupUi(self, Dialog_add_oscchannel):
        if not Dialog_add_oscchannel.objectName():
            Dialog_add_oscchannel.setObjectName(u"Dialog_add_oscchannel")
        Dialog_add_oscchannel.setWindowModality(Qt.ApplicationModal)
        Dialog_add_oscchannel.resize(993, 301)
        self.verticalLayout = QVBoxLayout(Dialog_add_oscchannel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog_add_oscchannel)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_6 = QLabel(Dialog_add_oscchannel)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_4 = QLabel(Dialog_add_oscchannel)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.comment_text = QPlainTextEdit(Dialog_add_oscchannel)
        self.comment_text.setObjectName(u"comment_text")

        self.gridLayout.addWidget(self.comment_text, 3, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Dialog_add_oscchannel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.bars_page = QWidget()
        self.bars_page.setObjectName(u"bars_page")
        self.horizontalLayout = QHBoxLayout(self.bars_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bars_combobox = QComboBox(self.bars_page)
        self.bars_combobox.setObjectName(u"bars_combobox")

        self.horizontalLayout.addWidget(self.bars_combobox)

        self.add_bar_btn = QPushButton(self.bars_page)
        self.add_bar_btn.setObjectName(u"add_bar_btn")
        self.add_bar_btn.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/icons/icons/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_bar_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.add_bar_btn)

        self.label_5 = QLabel(self.bars_page)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.gaugeposition_le = QLineEdit(self.bars_page)
        self.gaugeposition_le.setObjectName(u"gaugeposition_le")

        self.horizontalLayout.addWidget(self.gaugeposition_le)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(3, 1)
        self.stackedWidget.addWidget(self.bars_page)
        self.jacket_page = QWidget()
        self.jacket_page.setObjectName(u"jacket_page")
        self.horizontalLayout_2 = QHBoxLayout(self.jacket_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.jacket_combobox = QComboBox(self.jacket_page)
        self.jacket_combobox.setObjectName(u"jacket_combobox")

        self.horizontalLayout_2.addWidget(self.jacket_combobox)

        self.add_jacket_btn = QPushButton(self.jacket_page)
        self.add_jacket_btn.setObjectName(u"add_jacket_btn")
        self.add_jacket_btn.setMaximumSize(QSize(24, 24))
        self.add_jacket_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.add_jacket_btn)

        self.stackedWidget.addWidget(self.jacket_page)
        self.sample_page_3 = QWidget()
        self.sample_page_3.setObjectName(u"sample_page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.sample_page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.sample_page_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.sample_page_3)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)

        self.channeltype_cb = QComboBox(Dialog_add_oscchannel)
        self.channeltype_cb.addItem("")
        self.channeltype_cb.addItem("")
        self.channeltype_cb.addItem("")
        self.channeltype_cb.setObjectName(u"channeltype_cb")

        self.gridLayout.addWidget(self.channeltype_cb, 0, 1, 1, 1)

        self.label = QLabel(Dialog_add_oscchannel)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.frame = QFrame(Dialog_add_oscchannel)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tarir_le = QLineEdit(self.frame)
        self.tarir_le.setObjectName(u"tarir_le")

        self.horizontalLayout_4.addWidget(self.tarir_le)

        self.calc_tarir_btn = QPushButton(self.frame)
        self.calc_tarir_btn.setObjectName(u"calc_tarir_btn")
        self.calc_tarir_btn.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/calculate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc_tarir_btn.setIcon(icon1)
        self.calc_tarir_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.calc_tarir_btn)


        self.gridLayout.addWidget(self.frame, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog_add_oscchannel)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_add_oscchannel)
        self.buttonBox.accepted.connect(Dialog_add_oscchannel.accept)
        self.buttonBox.rejected.connect(Dialog_add_oscchannel.reject)
        self.channeltype_cb.currentIndexChanged.connect(self.stackedWidget.setCurrentIndex)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_add_oscchannel)
    # setupUi

    def retranslateUi(self, Dialog_add_oscchannel):
        Dialog_add_oscchannel.setWindowTitle(QCoreApplication.translate("Dialog_add_oscchannel", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0437\u043c\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_add_oscchannel", u"\u0418\u0437\u043c\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_add_oscchannel", u"\u0422\u0430\u0440\u0438\u0440\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_add_oscchannel", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.add_bar_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog_add_oscchannel", u"\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u0430\u0442\u0447\u0438\u043a\u0430", None))
        self.add_jacket_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog_add_oscchannel", u"\u041e\u0431\u0440\u0430\u0437\u0435\u0446", None))
        self.channeltype_cb.setItemText(0, QCoreApplication.translate("Dialog_add_oscchannel", u"\u0414\u0430\u0442\u0447\u0438\u043a \u043d\u0430 \u0441\u0442\u0435\u0440\u0436\u043d\u0435", None))
        self.channeltype_cb.setItemText(1, QCoreApplication.translate("Dialog_add_oscchannel", u"\u0414\u0430\u0442\u0447\u0438\u043a \u043d\u0430 \u043e\u0431\u043e\u0439\u043c\u0435", None))
        self.channeltype_cb.setItemText(2, QCoreApplication.translate("Dialog_add_oscchannel", u"\u0414\u0430\u0442\u0447\u0438\u043a \u043d\u0430 \u043e\u0431\u0440\u0430\u0437\u0446\u0435", None))

        self.label.setText(QCoreApplication.translate("Dialog_add_oscchannel", u"\u0422\u0438\u043f \u0438\u0437\u043c\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u0430\u043d\u0430\u043b\u0430", None))
        self.calc_tarir_btn.setText("")
    # retranslateUi

