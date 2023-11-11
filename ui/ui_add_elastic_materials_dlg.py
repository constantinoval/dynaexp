import PySide6.QtWidgets as pqw
from ui.add_elastic_material_dlg import Ui_Dialog_add_elastic_material
from libs.datastorage.tables import ElasticProperties
from libs.common_tools import to_float

class Add_ElasticMaterial_Dlg(Ui_Dialog_add_elastic_material, pqw.QDialog):
    def __init__(self, session, material=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.session = session
        self.material = material
        if self.material:
            self.lineEdit_name.setText(self.material.name)
            self.lineEdit_E.setText(f"{self.material.E:g}")
            self.lineEdit_c.setText(f"{self.material.c:g}")

        # self.exec()

    def accept(self):
        name = self.lineEdit_name.text()
        E = to_float(self.lineEdit_E.text())
        c = to_float(self.lineEdit_c.text())
        if self.material:
            self.material.name = name
            self.material.E = E
            self.material.c = c
            self.session.commit()
        else:
            m = ElasticProperties(
                name=name,
                E=E,
                c=c
            )
            self.session.add(m)
            self.session.commit()
            self.material = m
        self.done(1)