import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.add_experimentsgroup_dlg import Ui_Dialog_ExperimentsGroup
from ui.ui_add_customer_dlg import Add_Customer_Dlg
from ui.ui_add_executor_dlg import Add_Executor_Dlg
from libs.datastorage.tables import ExperimentsGroup, Executor, Customer
from functools import partial

TABLE_DIALOGS_DICT = {
    Customer: Add_Customer_Dlg,
    Executor: Add_Executor_Dlg,
}


class Add_ExperimentsGroup_Dlg(Ui_Dialog_ExperimentsGroup, pqw.QDialog):
    def __init__(self, session, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.session = session
        self.instance = instance
        customer_index = 0
        executor_index = 0
        for i, m in enumerate(self.session.query(Customer).all()):
            self.comboBox_customer.addItem(repr(m), userData=m)
            if self.instance:
                if m.id == self.instance.customer_id:
                    customer_index = i
        for i, m in enumerate(self.session.query(Executor).all()):
            self.comboBox_executor.addItem(repr(m), userData=m)
            if self.instance:
                if m.id == self.instance.executor_id:
                    executor_index = i
        self.pushButton_add_customer.pressed.connect(
            partial(
                self.add_table_record,
                Customer,
                self.comboBox_customer
            )
        )
        self.pushButton_add_executor.pressed.connect(
            partial(
                self.add_table_record,
                Executor,
                self.comboBox_executor
            )
        )
        if self.instance:
            self.lineEdit_shortname.setText(str(self.instance.short_name))
            self.lineEdit_contract.setText(str(self.instance.contract))
            self.comment_text.setPlainText(self.instance.notes)
        self.comboBox_customer.setCurrentIndex(customer_index)
        self.comboBox_executor.setCurrentIndex(executor_index)

    @pqc.Slot()
    def add_table_record(self, table_class, combobox):
        if table_class in TABLE_DIALOGS_DICT:
            dlg = TABLE_DIALOGS_DICT[table_class](session=self.session)
            dlg.exec()
            if dlg:
                instance = dlg.instance
                if instance:
                    combobox.addItem(repr(instance), instance)
                    combobox.setCurrentIndex(combobox.count()-1)

    def accept(self):
        short_name =self.lineEdit_shortname.text()
        contract =self.lineEdit_contract.text()
        customer = self.comboBox_customer.currentData(pqc.Qt.UserRole)
        executor = self.comboBox_executor.currentData(pqc.Qt.UserRole)
        if self.instance:
            self.instance.short_name = short_name
            self.instance.contract = contract
            self.instance.customer = customer
            self.instance.executor = executor
            if comment := str(self.comment_text.toPlainText()):
                self.instance.notes = comment
            self.session.commit()
        else:
            instance = ExperimentsGroup(
                short_name=short_name,
                contract=contract,
                customer=customer,
                executor=executor
            )
            instance.set_creation_time()
            if comment := str(self.comment_text.toPlainText()):
                instance.notes = comment
            self.session.add(instance)
            self.session.commit()
            self.instance = instance
        self.done(1)