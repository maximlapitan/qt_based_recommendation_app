# This Python file uses the following encoding: utf-8

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QTableWidgetItem

from ui_CompareModels import Ui_CompareModels
import joblib
import pickle

from fill_labels import models_to_load, encode_data


class CompareModels(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CompareModels()
        self.ui.setupUi(self)

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

