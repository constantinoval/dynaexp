import PySide6.QtGui as pqg
import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from libs.datastorage.tables import ElasticProperties
from ui.tableView_dlg import Ui_dlg_tableView
from ui.ui_add_elastic_materials_dlg import AddElasticMaterial_Dlg


class DataModel(pqc.QAbstractTableModel):
    def __init__(self, *args, session, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = session
        self.records = []
        m: ElasticProperties
        for m in session.query(ElasticProperties).all():
            self.records.append(m.as_data_record)

    def data(self, index, role) -> str:
        if role == pqc.Qt.ItemDataRole.DisplayRole:
            return self.records[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        headers = ElasticProperties.data_record_header()
        if role == pqc.Qt.ItemDataRole.DisplayRole and orientation == pqc.Qt.Orientation.Horizontal:
            return headers[section]
        else:
            return super().headerData(section, orientation, role)

    def rowCount(self, parent):
        return len(self.records)

    def columnCount(self, parent):
        return ElasticProperties.data_record_columns()


class ElasticMaterials_Dlg(Ui_dlg_tableView, pqw.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Свойства установки")
        self.model = DataModel(session=self.parent().session)
        self.tableView.setModel(self.model)
        horizontalHeader = self.tableView.horizontalHeader()
        for i in range(ElasticProperties.data_record_columns()):
            horizontalHeader.setSectionResizeMode(
                i, pqw.QHeaderView.ResizeMode.ResizeToContents
            )
        self.tableView.verticalHeader().hide()
        self.pushButton_remove.pressed.connect(self.delete_record)
        self.pushButton_add.pressed.connect(self.add_record)
        self.pushButton_edit.pressed.connect(self.edit_record)
        self.tableView.doubleClicked.connect(self.edit_record)
        self.exec()

    @pqc.Slot()
    def delete_record(self):
        idx = self.tableView.selectedIndexes()
        if not idx:
            return
        row_num = idx[0].row()
        rec_id = int(self.model.records[row_num][0])
        del self.model.records[row_num]
        self.model.layoutChanged.emit()
        self.parent().session.query(ElasticProperties).where(ElasticProperties.id == rec_id).delete()
        self.parent().session.commit()

    @pqc.Slot()
    def add_record(self):
        dlg = AddElasticMaterial_Dlg(parent=self, session=self.parent().session)
        dlg.exec()
        if dlg.result():
            self.model.records.append(dlg.material.as_data_record)
            self.model.layoutChanged.emit()

    @pqc.Slot()
    def edit_record(self):
        idx = self.tableView.selectedIndexes()
        if not idx:
            return
        row_num = idx[0].row()
        rec_id = int(self.model.records[row_num][0])
        rec = self.parent().session.query(ElasticProperties).where(ElasticProperties.id == rec_id).one()
        if rec is None:
            return
        dlg = AddElasticMaterial_Dlg(parent=self, session=self.parent().session, material=rec)
        dlg.exec()
        if dlg.result():
            self.model.records[row_num] = dlg.material.as_data_record
            self.model.layoutChanged.emit()

