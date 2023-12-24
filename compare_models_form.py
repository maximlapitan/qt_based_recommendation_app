# This Python file uses the following encoding: utf-8

# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
from ui_CompareModels import Ui_CompareModels
import joblib

from fill_labels import models_to_load


class CompareModels(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CompareModels()
        self.ui.setupUi(self)
        self.ui.button_close_compare_form.clicked.connect(self.close)
        self.setWindowIcon(QIcon('doc/icon.png'))

    def receive_data(self,*args):
        self.data = args[0]

    def open_predict_close(self, model_name, data_encoded):
        model_file = models_to_load[model_name]
        prediction = ""
        with open(model_file, "rb") as m:
            model = joblib.load(m)
            prediction = round(abs(model.predict(data_encoded)[0]), 2)
        return prediction

    def showEvent(self, event):
        for i, (model_name, model_path) in enumerate(models_to_load.items()):
            prediction = str(self.open_predict_close(model_name, self.data))
            self.ui.QTable_comparison_models.setItem(i, 0, QTableWidgetItem(model_name))
            self.ui.QTable_comparison_models.setItem(i, 1, QTableWidgetItem(prediction))
            self.ui.QTable_comparison_models.resizeColumnsToContents()
            self.ui.QTable_comparison_models.resizeRowsToContents()

    def setTableWidth(self):
            width = self.ui.QTable_comparison_models.verticalHeader().width()
            width += self.ui.QTable_comparison_models.horizontalHeader().length()
            if self.ui.QTable_comparison_models.verticalScrollBar().isVisible():
                width += self.ui.QTable_comparison_models.verticalScrollBar().width()
            width += self.ui.QTable_comparison_models.frameWidth() * 2
            self.ui.QTable_comparison_models.setFixedWidth(width)

    def resizeEvent(self, event):
            self.setTableWidth()
            super(CompareModels, self).resizeEvent(event)
