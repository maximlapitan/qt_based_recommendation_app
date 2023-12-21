# This Python file uses the following encoding: utf-8

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel

from ui_CompareModels import Ui_Form
from fill_labels import UIHandler, load_model, models_to_load
import joblib
import pickle

class CompareModels(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

