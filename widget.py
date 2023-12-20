# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_Widget
from fill_labels import UIHandler, load_model


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui_handler = UIHandler(self)
        self.ui_handler.update_label_text("weights_variables/export_dict.pkl")
        self.ui.predict_button.clicked.connect(self.predict_button)
        self.init_ui_slots()

    def predict_button(self):
        print("clicked")

    def init_ui_slots(self):
        def update_spin_box_prod_year():
            year = self.ui.QSlider_prod_year.value()
            self.ui.QSpinBox_prod_year.setValue(year)

        self.ui.QSlider_prod_year.valueChanged.connect(update_spin_box_prod_year)

        def update_horizontal_slider_prod_year():
            year = self.ui.QSpinBox_prod_year.value()
            self.ui.QSlider_prod_year.setValue(year)

        self.ui.QSpinBox_prod_year.valueChanged.connect(update_horizontal_slider_prod_year)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
