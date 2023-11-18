# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_main_form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)
import resources_rc

class Ui_dynaexp_main_window(object):
    def setupUi(self, dynaexp_main_window):
        if not dynaexp_main_window.objectName():
            dynaexp_main_window.setObjectName(u"dynaexp_main_window")
        dynaexp_main_window.resize(1049, 600)
        self.centralwidget = QWidget(dynaexp_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar_frame = QFrame(self.centralwidget)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 50))
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.menu_btn = QPushButton(self.top_bar_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setMinimumSize(QSize(30, 30))
        self.menu_btn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(20, 20))
        self.menu_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.menu_btn)

        self.mode_label = QLabel(self.top_bar_frame)
        self.mode_label.setObjectName(u"mode_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.mode_label.setFont(font)
        self.mode_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.mode_label)


        self.gridLayout.addWidget(self.top_bar_frame, 0, 0, 1, 2)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QStackedWidget(self.frame_5)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.connection_page = QWidget()
        self.connection_page.setObjectName(u"connection_page")
        self.horizontalLayout_3 = QHBoxLayout(self.connection_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.connection_page)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.stacked_widget.addWidget(self.connection_page)
        self.tables_page = QWidget()
        self.tables_page.setObjectName(u"tables_page")
        self.verticalLayout_4 = QVBoxLayout(self.tables_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tables_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.elastic_properties_btn = QPushButton(self.frame_2)
        self.elastic_properties_btn.setObjectName(u"elastic_properties_btn")
        sizePolicy.setHeightForWidth(self.elastic_properties_btn.sizePolicy().hasHeightForWidth())
        self.elastic_properties_btn.setSizePolicy(sizePolicy)
        self.elastic_properties_btn.setMinimumSize(QSize(0, 0))
        self.elastic_properties_btn.setCheckable(True)
        self.elastic_properties_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.elastic_properties_btn)

        self.strikers_btn = QPushButton(self.frame_2)
        self.strikers_btn.setObjectName(u"strikers_btn")
        self.strikers_btn.setCheckable(True)
        self.strikers_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.strikers_btn)

        self.bars_btn = QPushButton(self.frame_2)
        self.bars_btn.setObjectName(u"bars_btn")
        self.bars_btn.setCheckable(True)
        self.bars_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.bars_btn)

        self.jacket_btn = QPushButton(self.frame_2)
        self.jacket_btn.setObjectName(u"jacket_btn")
        self.jacket_btn.setCheckable(True)
        self.jacket_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.jacket_btn)

        self.customer_btn = QPushButton(self.frame_2)
        self.customer_btn.setObjectName(u"customer_btn")
        self.customer_btn.setCheckable(True)
        self.customer_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.customer_btn)

        self.executor_btn = QPushButton(self.frame_2)
        self.executor_btn.setObjectName(u"executor_btn")
        self.executor_btn.setCheckable(True)
        self.executor_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.executor_btn)

        self.experimentsgroup_btn = QPushButton(self.frame_2)
        self.experimentsgroup_btn.setObjectName(u"experimentsgroup_btn")
        self.experimentsgroup_btn.setCheckable(True)
        self.experimentsgroup_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.experimentsgroup_btn)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.verticalSpacer_3 = QSpacerItem(20, 203, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.table_tview = QTableView(self.frame_6)
        self.table_tview.setObjectName(u"table_tview")
        self.table_tview.setFrameShape(QFrame.NoFrame)
        self.table_tview.setFrameShadow(QFrame.Plain)
        self.table_tview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_tview.setSortingEnabled(False)
        self.table_tview.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_6.addWidget(self.table_tview)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(31, 0))
        self.frame_4.setMaximumSize(QSize(31, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.record_add_btn = QPushButton(self.frame_4)
        self.record_add_btn.setObjectName(u"record_add_btn")
        self.record_add_btn.setMinimumSize(QSize(30, 30))
        self.record_add_btn.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.record_add_btn.setIcon(icon1)
        self.record_add_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.record_add_btn)

        self.record_edit_btn = QPushButton(self.frame_4)
        self.record_edit_btn.setObjectName(u"record_edit_btn")
        self.record_edit_btn.setMinimumSize(QSize(30, 30))
        self.record_edit_btn.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/editing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.record_edit_btn.setIcon(icon2)
        self.record_edit_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.record_edit_btn)

        self.record_delete_btn = QPushButton(self.frame_4)
        self.record_delete_btn.setObjectName(u"record_delete_btn")
        self.record_delete_btn.setMinimumSize(QSize(30, 30))
        self.record_delete_btn.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.record_delete_btn.setIcon(icon3)
        self.record_delete_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.record_delete_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 429, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame)

        self.stacked_widget.addWidget(self.tables_page)

        self.verticalLayout.addWidget(self.stacked_widget)


        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.small_menu_frame = QFrame(self.centralwidget)
        self.small_menu_frame.setObjectName(u"small_menu_frame")
        self.small_menu_frame.setMinimumSize(QSize(42, 0))
        self.small_menu_frame.setMaximumSize(QSize(42, 100000))
        self.small_menu_frame.setStyleSheet(u"")
        self.small_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.small_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.small_menu_frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 6)
        self.connect_btn_small = QPushButton(self.small_menu_frame)
        self.connect_btn_small.setObjectName(u"connect_btn_small")
        self.connect_btn_small.setMinimumSize(QSize(40, 40))
        self.connect_btn_small.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/database (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_btn_small.setIcon(icon4)
        self.connect_btn_small.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.connect_btn_small)

        self.tables_btn_small = QPushButton(self.small_menu_frame)
        self.tables_btn_small.setObjectName(u"tables_btn_small")
        self.tables_btn_small.setMinimumSize(QSize(40, 40))
        self.tables_btn_small.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/database_table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tables_btn_small.setIcon(icon5)
        self.tables_btn_small.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.tables_btn_small)

        self.verticalSpacer = QSpacerItem(27, 455, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.exit_btn_small = QPushButton(self.small_menu_frame)
        self.exit_btn_small.setObjectName(u"exit_btn_small")
        self.exit_btn_small.setMinimumSize(QSize(40, 40))
        self.exit_btn_small.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_small.setIcon(icon6)
        self.exit_btn_small.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.exit_btn_small)


        self.horizontalLayout.addWidget(self.small_menu_frame)

        self.full_menu_frame = QFrame(self.centralwidget)
        self.full_menu_frame.setObjectName(u"full_menu_frame")
        self.full_menu_frame.setMinimumSize(QSize(170, 0))
        self.full_menu_frame.setMaximumSize(QSize(170, 16777215))
        self.full_menu_frame.setStyleSheet(u"")
        self.full_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.full_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.full_menu_frame)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connect_btn_full = QPushButton(self.full_menu_frame)
        self.connect_btn_full.setObjectName(u"connect_btn_full")
        self.connect_btn_full.setMinimumSize(QSize(0, 30))
        self.connect_btn_full.setMaximumSize(QSize(16777215, 30))
        self.connect_btn_full.setIcon(icon4)
        self.connect_btn_full.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.connect_btn_full)

        self.tables_btn_full = QPushButton(self.full_menu_frame)
        self.tables_btn_full.setObjectName(u"tables_btn_full")
        self.tables_btn_full.setMinimumSize(QSize(0, 30))
        self.tables_btn_full.setMaximumSize(QSize(16777215, 30))
        self.tables_btn_full.setIcon(icon5)
        self.tables_btn_full.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.tables_btn_full)

        self.verticalSpacer_2 = QSpacerItem(20, 451, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.exit_btn_full = QPushButton(self.full_menu_frame)
        self.exit_btn_full.setObjectName(u"exit_btn_full")
        self.exit_btn_full.setMinimumSize(QSize(0, 30))
        self.exit_btn_full.setMaximumSize(QSize(16777215, 30))
        self.exit_btn_full.setIcon(icon6)
        self.exit_btn_full.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.exit_btn_full)


        self.horizontalLayout.addWidget(self.full_menu_frame)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        dynaexp_main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(dynaexp_main_window)
        self.menu_btn.toggled.connect(self.full_menu_frame.setVisible)
        self.menu_btn.toggled.connect(self.small_menu_frame.setHidden)
        self.exit_btn_full.pressed.connect(dynaexp_main_window.close)
        self.exit_btn_small.pressed.connect(dynaexp_main_window.close)

        self.stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(dynaexp_main_window)
    # setupUi

    def retranslateUi(self, dynaexp_main_window):
        dynaexp_main_window.setWindowTitle(QCoreApplication.translate("dynaexp_main_window", u"MainWindow", None))
        self.menu_btn.setText("")
        self.mode_label.setText("")
        self.label_2.setText(QCoreApplication.translate("dynaexp_main_window", u"Connection Page", None))
        self.label.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.elastic_properties_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.strikers_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0423\u0434\u0430\u0440\u043d\u0438\u043a", None))
        self.bars_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u041c\u0435\u0440\u043d\u044b\u0439 \u0441\u0442\u0435\u0440\u0436\u0435\u043d\u044c", None))
        self.jacket_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u041e\u0431\u043e\u0439\u043c\u0430", None))
        self.customer_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.executor_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u041e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439", None))
        self.experimentsgroup_btn.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0413\u0440\u0443\u043f\u043f\u0430 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.pushButton_3.setText(QCoreApplication.translate("dynaexp_main_window", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.pushButton_4.setText(QCoreApplication.translate("dynaexp_main_window", u"\u041e\u0431\u0440\u0430\u0437\u0435\u0446", None))
        self.pushButton_5.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0418\u0437\u043c\u0435\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u0430\u043d\u0430\u043b", None))
#if QT_CONFIG(tooltip)
        self.record_add_btn.setToolTip(QCoreApplication.translate("dynaexp_main_window", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.record_add_btn.setText("")
#if QT_CONFIG(tooltip)
        self.record_edit_btn.setToolTip(QCoreApplication.translate("dynaexp_main_window", u"\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.record_edit_btn.setText("")
#if QT_CONFIG(tooltip)
        self.record_delete_btn.setToolTip(QCoreApplication.translate("dynaexp_main_window", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.record_delete_btn.setText("")
        self.connect_btn_small.setText("")
        self.tables_btn_small.setText("")
        self.exit_btn_small.setText("")
        self.connect_btn_full.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0421\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435 \u0441 \u0411\u0414", None))
        self.tables_btn_full.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.exit_btn_full.setText(QCoreApplication.translate("dynaexp_main_window", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

