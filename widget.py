# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_Widget
from fill_labels import UIHandler, models_to_load
import joblib
import pickle
from compare_models_form import CompareModels
from time import sleep
from copy import deepcopy
from influence_widget import InfluenceWidget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui_handler = UIHandler(self)
        self.ui_handler.update_label_text("weights_variables/export_dict.pkl")
        self.ui.predict_button.clicked.connect(self.predict_button)
        self.init_ui_slots()
        self.ui.compare_performance_button.hide()
        self.ui.compare_performance_button.clicked.connect(
            self.open_second_form)
        self.comparison_form = CompareModels()
        self.influence_widget = InfluenceWidget()
        self.ui.button_influence_of_factors.clicked.connect(self.open_drawing_form)
        self.setWindowIcon(QIcon('doc/icon.png'))

    def predict_button(self):
        scaler_file = "weights_variables/scaler.pkl"
        with open(scaler_file, "rb") as s:
            scaler = pickle.load(s)
            model_file = models_to_load[self.ui.QComboBox_model.currentText()]
            with open(model_file, "rb") as m:
                model = joblib.load(m)
                pandas_frame_to_scale = self.ui_handler.fill_data_with_data()
                scaled_pandas_frame = scaler.transform(pandas_frame_to_scale)
                prediction = round(
                    abs(model.predict(scaled_pandas_frame)[0]), 2)
                self.ui.QLabel_car_cost.setText(str(prediction))
                exported_weights = deepcopy(scaled_pandas_frame)
                self.comparison_form.receive_data(exported_weights)
        self.ui.compare_performance_button.show()

    def init_ui_slots(self):
        def update_spin_box_prod_year():
            year = self.ui.QSlider_prod_year.value()
            self.ui.QSpinBox_prod_year.setValue(year)

        self.ui.QSlider_prod_year.valueChanged.connect(
            update_spin_box_prod_year)

        def update_horizontal_slider_prod_year():
            year = self.ui.QSpinBox_prod_year.value()
            self.ui.QSlider_prod_year.setValue(year)

        self.ui.QSpinBox_prod_year.valueChanged.connect(
            update_horizontal_slider_prod_year)

    def open_second_form(self):
        self.comparison_form.show()

    def open_drawing_form(self):
        self.influence_widget.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
