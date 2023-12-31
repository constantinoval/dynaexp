import PySide6.QtWidgets as pqw
from ui.add_elastic_material_dlg import Ui_Dialog_add_elastic_material
from libs.datastorage.tables import ElasticProperties
from libs.common_tools import to_float

class Add_ElasticMaterial_Dlg(Ui_Dialog_add_elastic_material, pqw.QDialog):
    def __init__(self, session, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.session = session
        self.instance = instance
        if self.instance:
            self.lineEdit_name.setText(self.instance.name)
            self.lineEdit_E.setText(f"{self.instance.E:g}")
            self.lineEdit_c.setText(f"{self.instance.c:g}")
            self.comment_text.setPlainText(self.instance.notes)

        # self.exec()

    def accept(self):
        name = self.lineEdit_name.text()
        E = to_float(self.lineEdit_E.text())
        c = to_float(self.lineEdit_c.text())
        if self.instance:
            self.instance.name = name
            self.instance.E = E
            self.instance.c = c
            if comment := str(self.comment_text.toPlainText()):
                self.instance.notes = comment
            self.session.commit()
        else:
            m = ElasticProperties(
                name=name,
                E=E,
                c=c
            )
            m.set_creation_time()
            if comment := str(self.comment_text.toPlainText()):
                m.notes = comment
            self.session.add(m)
            self.session.commit()
            self.instance = m
        self.done(1)