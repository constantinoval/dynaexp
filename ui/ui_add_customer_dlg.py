import PySide6.QtWidgets as pqw
from ui.add_customer_dlg import Ui_Dialog_add_customer
from libs.datastorage.tables import Customer

class Add_Customer_Dlg(Ui_Dialog_add_customer, pqw.QDialog):
    def __init__(self, session, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.session = session
        self.instance = instance
        if self.instance:
            self.lineEdit_name.setText(self.instance.name)
            self.comment_text.setPlainText(self.instance.notes)

        # self.exec()

    def accept(self):
        name = self.lineEdit_name.text()
        if self.instance:
            self.instance.name = name
            if comment := str(self.comment_text.toPlainText()):
                self.instance.notes = comment
            self.session.commit()
        else:
            instance = Customer(
                name=name,
            )
            instance.set_creation_time()
            if comment := str(self.comment_text.toPlainText()):
                instance.notes = comment
            self.session.add(instance)
            self.session.commit()
            self.instance = instance
        self.done(1)