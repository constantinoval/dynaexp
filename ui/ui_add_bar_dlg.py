import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.add_striker_dlg import Ui_Dialog_Add_Striker
from ui.ui_add_elastic_materials_dlg import Add_ElasticMaterial_Dlg
from libs.datastorage.tables import ElasticProperties, MeasureBar
from libs.common_tools import to_float


class Add_Bar_Dlg(Ui_Dialog_Add_Striker, pqw.QDialog):
    def __init__(self, session, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("Добавление мерного стержня")
        self.session = session
        self.instance = instance
        mat_index = 0
        for i, m in enumerate(self.session.query(ElasticProperties).all()):
            self.comboBox_material.addItem(repr(m), userData=m)
            if self.instance:
                if m.id == self.instance.material.id:
                    mat_index = i
        self.pushButton_add_material.pressed.connect(self.add_material)
        if self.instance:
            self.lineEdit_D.setText(str(self.instance.D))
            self.lineEdit_D0.setText(str(self.instance.D0))
            self.lineEdit_L.setText(str(self.instance.L))
            self.comment_text.setPlainText(self.instance.notes)
        self.comboBox_material.setCurrentIndex(mat_index)

    @pqc.Slot()
    def add_material(self):
        dlg = Add_ElasticMaterial_Dlg(session=self.session)
        dlg.exec()
        if dlg:
            m = dlg.material
            if m:
                self.comboBox_material.addItem(repr(m), m)
                self.comboBox_material.setCurrentIndex(self.comboBox_material.count()-1)

    def accept(self):
        D = to_float(self.lineEdit_D.text())
        D0 = to_float(self.lineEdit_D0.text())
        L = to_float(self.lineEdit_L.text())
        m = self.comboBox_material.currentData(pqc.Qt.UserRole)
        if self.instance:
            self.instance.D = D
            self.instance.D0 = D0
            self.instance.L = L
            self.instance.material = m
            if comment := str(self.comment_text.toPlainText()):
                self.instance.notes = comment
            self.session.commit()
        else:
            s = MeasureBar(D=D, D0=D0, L=L, material=m)
            s.set_creation_time()
            if comment := str(self.comment_text.toPlainText()):
                s.notes = comment
            self.session.add(s)
            self.session.commit()
            self.instance = s
        self.done(1)