# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from ui_influence import Ui_InfluenceForm
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QTableWidgetItem

class InfluenceWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfluenceForm()
        self.ui.setupUi(self)
