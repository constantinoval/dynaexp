import sys
import PySide6.QtGui as pqg
import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.new_main_form import Ui_dynaexp_main_window
from libs.datastorage.db_lib import open_session, create_test_database
from functools import partial
from libs.datastorage.tables import ElasticProperties, Striker
from libs.common_tools import DataModel
from ui.ui_add_elastic_materials_dlg import Add_ElasticMaterial_Dlg
from ui.ui_add_striker_dlg import Add_Striker_Dlg


class AppMainWindow(Ui_dynaexp_main_window, pqw.QMainWindow):
    def __init__(self, *args, **kwargs):
        """
        Инициализации основного окна приложения
        """
        super().__init__(*args, **kwargs)
        # self.setWindowFlags(pqc.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        # TODO: пока работаем с автоматичиски-создаваемой каждый раз таблицей
        #       в дальнейшем поменять на подключение к заданной базе
        # -------------------------------------------------------------------
        # create_test_database()
        self.session = open_session("sqlite:///test.db")
        # -------------------------------------------------------------------
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
        self.stacked_widget.setCurrentIndex(0)
        self.record_delete_btn.pressed.connect(self.delete_record)
        self.record_add_btn.pressed.connect(self.add_table_record)
        self.record_edit_btn.pressed.connect(self.edit_table_record)
        self.table_tview.doubleClicked.connect(self.edit_table_record)
        self.showMaximized()
        # self.show()

    def closeEvent(self, event):
        """
        Выполняется при закрытии приложения
        """
        print("Выход...")
        if self.session:
            self.session.close()
        event.accept()

    @pqc.Slot()
    def set_table_content(self, table_class):
        """
        Отображение таблицы из базы данных в приложении
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
        """
        Обновление заголовка - режим работы приложения при смене вкладок stacke_widget
        """
        text = {
            0: "Режим подключения к базе данных",
            1: "Режим работы с таблицами базы данных",
        }.get(current_index, "")
        self.mode_label.setText(text)

    @pqc.Slot()
    def delete_record(self):
        """
        Удаление выделенной записи из активной таблицы
        """
        if self.session is None:
            return
        if self.data_model is None:
            return
        idx = self.table_tview.selectedIndexes()
        if not idx:
            return
        dlg = pqw.QMessageBox(self)
        dlg.setWindowTitle("Подтвердите удаление записи")
        dlg.setText("Удалить запись?")
        dlg.setStandardButtons(pqw.QMessageBox.Yes | pqw.QMessageBox.No)
        dlg.setIcon(pqw.QMessageBox.Question)
        button = dlg.exec()
        if button == pqw.QMessageBox.No:
            return
        row_num = idx[0].row()
        rec_id = int(self.data_model.records[row_num][0])
        del self.data_model.records[row_num]
        self.data_model.layoutChanged.emit()
        self.session.query(self.data_model.table_class).where(
            self.data_model.table_class.id == rec_id
        ).delete()
        self.session.commit()

    @pqc.Slot()
    def add_table_record(self):
        """
        добавление записи активной таблицы
        """
        if self.session is None:
            return
        if self.data_model is None:
            return
        if self.data_model.table_class == ElasticProperties:
            dlg = Add_ElasticMaterial_Dlg(
                parent=self,
                session=self.session
            )
            dlg.exec()
            if dlg.result():
                self.data_model.records.append(dlg.material.as_data_record)
                self.data_model.layoutChanged.emit()
            return
        if self.data_model.table_class == Striker:
            dlg = Add_Striker_Dlg(
                parent=self,
                session=self.session
            )
            dlg.exec()
            if dlg.result():
                self.data_model.records.append(dlg.striker.as_data_record)
                self.data_model.layoutChanged.emit()
            return

    @pqc.Slot()
    def edit_table_record(self):
        """
        Редактирование активной записи активной таблицы
        """
        if self.session is None:
            return
        if self.data_model is None:
            return
        idx = self.table_tview.selectedIndexes()
        if not idx:
            return
        row_num = idx[0].row()
        rec_id = int(self.data_model.records[row_num][0])
        rec = self.session.query(self.data_model.table_class).where(
            self.data_model.table_class.id == rec_id
        ).one()
        if self.data_model.table_class == ElasticProperties:
            dlg = Add_ElasticMaterial_Dlg(
                parent=self,
                session=self.session,
                material=rec,
            )
            dlg.exec()
            if dlg.result():
                self.data_model.records[row_num] = dlg.material.as_data_record
                self.data_model.layoutChanged.emit()
            return
        if self.data_model.table_class == Striker:
            dlg = Add_Striker_Dlg(
                parent=self,
                session=self.session,
                striker=rec,
            )
            dlg.exec()
            if dlg.result():
                self.data_model.records[row_num] = dlg.striker.as_data_record
                self.data_model.layoutChanged.emit()
            return


if __name__ == '__main__':
    app = pqw.QApplication([])
    window = AppMainWindow()
    app.setStyleSheet(open('stylesheet.qss', 'r').read())
    sys.exit(app.exec())
