import sys
import PySide6.QtGui as pqg
import PySide6.QtWidgets as pqw
import PySide6.QtCore as pqc
from ui.test_main import Ui_MainWindow
from test_widget import Widget1


class AppMainWindow(Ui_MainWindow, pqw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setWindowFlags(pqc.Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.w1 = Widget1(next_parent=self.stackedWidget2)
        self.w1.setParent(self.stackedWidget1)
        self.w1.hide()
        self.pushButton1.pressed.connect(self.pb1)
        self.pushButton2.pressed.connect(self.pb2)
        self.pushButton3.pressed.connect(self.pb3)
        self.showMaximized()

    @pqc.Slot()
    def pb1(self):
        self.w1.show()
        # effect = pqw.QGraphicsOpacityEffect(self.w1)
        # effect1 = pqw.QGraphicsBlurEffect(self.w1)
        # self.w1.setGraphicsEffect(effect1)
        self.anim = pqc.QPropertyAnimation(self.w1, b'geometry')
        # self.w1.setParent(self.stackedWidget1)
        self.anim.setStartValue(pqc.QRect(
            self.w1.x(), self.w1.y(), 0, self.w1.height()
        ))
        self.anim.setEndValue(pqc.QRect(
            self.w1.x(), self.w1.y(), 200, self.w1.height()
        ))
        self.anim.setEasingCurve(pqc.QEasingCurve.OutBounce)
        self.anim.setDuration(1000)
        # self.w1.show()
        self.anim.start()

    @pqc.Slot()
    def pb2(self):
        self.w1.hide()
        self.w1.setParent(self.stackedWidget2)
        self.w1.show()

    @pqc.Slot()
    def pb3(self):
        del self.w1
        self.redra

if __name__ == '__main__':
    app = pqw.QApplication([])
    window = AppMainWindow()
    # app.setStyleSheet(open('material_dark.qss', 'r').read())
    sys.exit(app.exec())
