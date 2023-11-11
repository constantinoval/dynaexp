import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.add_striker_dlg import Ui_Dialog_Add_Striker
from ui.ui_add_elastic_materials_dlg import Add_ElasticMaterial_Dlg
from libs.datastorage.tables import ElasticProperties, Striker
from libs.common_tools import to_float


class Add_Striker_Dlg(Ui_Dialog_Add_Striker, pqw.QDialog):
    def __init__(self, session, striker=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.session = session
        self.striker = striker
        mat_index = 0
        for i, m in enumerate(self.session.query(ElasticProperties).all()):
            self.comboBox_material.addItem(repr(m), userData=m)
            if self.striker:
                if m.id == self.striker.material.id:
                    mat_index = i
        self.pushButton_add_material.pressed.connect(self.add_material)
        if self.striker:
            self.lineEdit_D.setText(str(self.striker.D))
            self.lineEdit_D0.setText(str(self.striker.D0))
            self.lineEdit_L.setText(str(self.striker.L))
        self.comboBox_material.setCurrentIndex(mat_index)

    @pqc.Slot()
    def add_material(self):
        dlg = Add_ElasticMaterial_Dlg(session=self.session)
        dlg.exec()
        if dlg:
            m = dlg.material
            self.comboBox_material.addItem(repr(m), m)
            self.comboBox_material.setCurrentIndex(self.comboBox_material.count()-1)

    def accept(self):
        D = to_float(self.lineEdit_D.text())
        D0 = to_float(self.lineEdit_D0.text())
        L = to_float(self.lineEdit_L.text())
        m = self.comboBox_material.currentData(pqc.Qt.UserRole)
        if self.striker:
            self.striker.D = D
            self.striker.D0 = D0
            self.striker.L = L
            self.striker.material = m
            self.session.commit()
        else:
            s = Striker(D=D, D0=D0, L=L, material=m)
            self.session.add(s)
            self.session.commit()
            self.striker = s
        self.done(1)