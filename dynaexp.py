import sys
import PySide6.QtGui as pqg
import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.main_window import Ui_MainWindow
from libs.datastorage.db_lib import open_session, create_test_database
from ui.ui_elastic_materials_dlg import ElasticMaterials_Dlg
from ui.ui_strikers_dlg import Strikers_Dlg

class AppMainWindow(Ui_MainWindow, pqw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setWindowFlags(pqc.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        create_test_database()
        self.session = open_session("sqlite:///test.db")
        self.action_file_new.triggered.connect(self.file_new)
        self.action_elastic_materials.triggered.connect(self.show_elastic_properties_dialog)
        self.action_strikers.triggered.connect(self.show_strikers_table_dialog)
        self.showMaximized()

    @pqc.Slot()
    def file_new(self):
        pass
        # print("Создание базы в памяти...")
        # self.session = open_session("sqlite://")

    @pqc.Slot()
    def show_elastic_properties_dialog(self):
        if self.session is None:
            return
        dlg = ElasticMaterials_Dlg(parent=self)

    @pqc.Slot()
    def show_strikers_table_dialog(self):
        if self.session is None:
            return
        dlg = Strikers_Dlg(parent=self)

    def closeEvent(self, event):
        print("Выход...")
        if self.session:
            self.session.close()
        event.accept()


if __name__ == '__main__':
    app = pqw.QApplication([])
    window = AppMainWindow()
    app.setStyleSheet(open('material_dark.qss', 'r').read())
    sys.exit(app.exec())
