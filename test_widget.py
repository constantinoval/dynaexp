import PySide6.QtGui as pqg
import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.test_widget1 import Ui_Form


class Widget1(Ui_Form, pqw.QWidget):
    def __init__(self, next_parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setWindowFlags(pqc.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.next_parent = next_parent
        self.pushButton.pressed.connect(self.pb)
        # self.show()

    @pqc.Slot()
    def pb(self):
        self.w2 = Widget1()
        self.w2.setParent(self.next_parent)
        self.w2.show()