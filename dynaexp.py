import sys
import PySide6.QtGui as pqg
import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.new_main_form import Ui_dynaexp_main_window
from libs.datastorage.db_lib import open_session, create_test_database
# from ui.ui_elastic_materials_dlg import ElasticMaterials_Dlg
# from ui.ui_strikers_dlg import Strikers_Dlg
from functools import partial
from libs.datastorage.tables import ElasticProperties, Striker
from libs.common_tools import DataModel

class AppMainWindow(Ui_dynaexp_main_window, pqw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setWindowFlags(pqc.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        create_test_database()
        self.session = open_session("sqlite:///test.db")
        self.menu_btn.setChecked(True)
        self.menu_btn.setChecked(False)
        self.data_model = None
        self.connect_btn_small.pressed.connect(partial(self.stacked_widget.setCurrentIndex, 0))
        self.connect_btn_full.pressed.connect(partial(self.stacked_widget.setCurrentIndex, 0))
        self.tables_btn_small.pressed.connect(partial(self.stacked_widget.setCurrentIndex, 1))
        self.tables_btn_full.pressed.connect(partial(self.stacked_widget.setCurrentIndex, 1))
        self.elastic_properties_btn.pressed.connect(partial(self.set_table_content, ElasticProperties))
        self.strikers_btn.pressed.connect(partial(self.set_table_content, Striker))
        self.stacked_widget.currentChanged.connect(self.on_mode_changed)
        self.showMaximized()
        # self.show()

    def closeEvent(self, event):
        print("Выход...")
        if self.session:
            self.session.close()
        event.accept()

    @pqc.Slot()
    def set_table_content(self, table_class):
        """
        Отображение таблицы из базы данных для отображения в форме
        """
        if self.session is None:
            return
        if self.data_model:
            del self.data_model
        self.data_model = DataModel(session=self.session, table_class=table_class)
        self.table_tview.setModel(self.data_model)
        horizontalHeader = self.table_tview.horizontalHeader()
        for i in range(table_class.data_record_columns()):
            horizontalHeader.setSectionResizeMode(
                i, pqw.QHeaderView.ResizeMode.ResizeToContents
            )
        self.table_tview.verticalHeader().hide()

    @pqc.Slot()
    def on_mode_changed(self, current_index: int):
        text = {
            0: "Режим подключения к базе дынных",
            1: "Режим работы с таблицами базы данных",
        }.get(current_index, "")
        self.mode_label.setText(text)


if __name__ == '__main__':
    app = pqw.QApplication([])
    window = AppMainWindow()
    app.setStyleSheet(open('stylesheet.qss', 'r').read())
    sys.exit(app.exec())
