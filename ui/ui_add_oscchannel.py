import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.add_oscchannel import Ui_Dialog_add_oscchannel
from libs.datastorage.tables import MeasureBar, Jacket, OscChannel
from libs.common_tools import to_float
from functools import partial
from ui.ui_add_bar_dlg import Add_Bar_Dlg
from ui.ui_add_jacket_dlg import Add_Jacket_Dlg

TABLE_DIALOGS_DICT = {
    MeasureBar: Add_Bar_Dlg,
    Jacket: Add_Jacket_Dlg,
}


class Add_OscChannel_Dlg(Ui_Dialog_add_oscchannel, pqw.QDialog):
    def __init__(self, session, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.session = session
        self.instance = instance
        self.bar_index = 0
        self.jacket_index = 0
        for i, inst in enumerate(self.session.query(MeasureBar).all()):
            self.bars_combobox.addItem(repr(inst), userData=inst)
            if self.instance:
                if inst.id == self.instance.bar_id:
                    self.bar_index = i
        for i, inst in enumerate(self.session.query(Jacket).all()):
            self.jacket_combobox.addItem(repr(inst), userData=inst)
            if self.instance:
                if inst.id == self.instance.jacket_id:
                    self.jacket_index = i
        self.add_bar_btn.pressed.connect(
            partial(
                self.add_table_record,
                MeasureBar,
                self.bars_combobox
            )
        )
        self.add_jacket_btn.pressed.connect(
            partial(
                self.add_table_record,
                Jacket,
                self.jacket_combobox
            )
        )
        if self.instance:
            self.tarir_le.setText(str(self.instance.tarir))
            if self.instance.bar:
                self.channeltype_cb.setCurrentIndex(0)
                self.bars_combobox.setCurrentIndex(self.bar_index)
                self.gaugeposition_le.setText(str(self.instance.gauge_position))
            elif self.instance.jacket:
                self.channeltype_cb.setCurrentIndex(1)
                self.jacket_combobox.setCurrentIndex(self.jacket_index)
            else:
                self.channeltype_cb.setCurrentIndex(2)
            if notes := self.instance.notes:
                self.comment_text.setPlainText(notes)

    @pqc.Slot()
    def add_table_record(self, table_class, combobox):
        if table_class in TABLE_DIALOGS_DICT:
            dlg = TABLE_DIALOGS_DICT[table_class](session=self.session)
            dlg.exec()
            if dlg:
                instance = dlg.instance
                if instance:
                    combobox.addItem(repr(instance), instance)
                    combobox.setCurrentIndex(combobox.count() - 1)

    def accept(self):
        tarir = to_float(self.tarir_le.text())
        match self.channeltype_cb.currentIndex():
            case 0:
                bar = self.bars_combobox.currentData(pqc.Qt.UserRole)
                dat_position = to_float(self.gaugeposition_le.text())
                if self.instance:
                    self.instance.bar = bar
                    self.instance.gauge_position = dat_position
                    self.jacket = None
                else:
                    self.instance = OscChannel(
                        bar=bar,
                        tarir=tarir,
                        gauge_position=dat_position
                    )
                    self.instance.set_creation_time()
                    self.session.add(self.instance)
            case 1:
                jacket = self.jacket_combobox.currentData(pqc.Qt.UserRole)
                if self.instance:
                    self.instance.jacket = jacket
                    self.instance.bar = None
                    self.instance.gauge_position = None
                else:
                    self.instance = OscChannel(
                        jacket=jacket,
                        tarir=tarir,
                    )
                    self.instance.set_creation_time()
                    self.session.add(self.instance)
            case 2:
                if self.instance:
                    self.instance.bar = None
                    self.instance.jacket = None
                    self.instance.gauge_position = None
                else:
                    self.instance = OscChannel(
                        tarir=tarir,
                    )
                    self.instance.set_creation_time()
                    self.session.add(self.instance)
        if comment := str(self.comment_text.toPlainText()):
            self.instance.notes = comment
        self.session.commit()
        self.done(1)
