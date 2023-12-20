# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QLabel, QListWidget
from ui_form import Ui_Widget
import pickle
import joblib

def load_model(file):
    model = joblib.load(type)
    return model

def array_from_dict(dictionary, field):
    return sorted([str(key) for key in dictionary[field]])

class UIHandler:
    def __init__(self, ui_widget):
        self.ui = ui_widget

    def update_label_text(self, text_file):
        with open(text_file, "rb") as pickle_transform_dict:
            transform_dict = pickle.load(pickle_transform_dict)
            print(transform_dict)
            default_index = 0

            # set names in labels
            self.ui.ui.QLabel_turbo.setText("Turbo")
            self.ui.ui.QLabel_gear_box_type.setText("Gear box type")
            self.ui.ui.QLabel_leather_interior.setText("Leather interior")
            self.ui.ui.QLabel_manufacturer.setText("Manufacturer")
            self.ui.ui.QLabel_drive_wheels.setText("Drive wheels")
            self.ui.ui.QLabel_engine_volume.setText("Engine volume")
            self.ui.ui.QLabel_category.setText("Category")
            self.ui.ui.QLabel_fuel_type.setText("Fuel type")
            self.ui.ui.QLabel_wheel.setText("Wheel")
            self.ui.ui.QLabel_cylinders.setText("Cylinders")
            self.ui.ui.QLabel_doors.setText("Doors")
            self.ui.ui.QLabel_model.setText("Model")

            # set values in comboboxes
            self.ui.ui.QComboBox_turbo.addItems(array_from_dict(transform_dict,"Turbo"))
            self.ui.ui.QComboBox_gear_box_type.addItems(array_from_dict(transform_dict,"Gear box type"))
            self.ui.ui.QComboBox_leather_interior.addItems(array_from_dict(transform_dict,"Leather interior"))
            self.ui.ui.QComboBox_manufacturer.addItems(array_from_dict(transform_dict,"Manufacturer"))
            self.ui.ui.QComboBox_drive_wheels.addItems(array_from_dict(transform_dict,"Drive wheels"))
            self.ui.ui.QComboBox_engine_volume.addItems(array_from_dict(transform_dict,"Engine volume"))
            self.ui.ui.QComboBox_category.addItems(array_from_dict(transform_dict,"Category"))
            self.ui.ui.QComboBox_fuel_type.addItems(array_from_dict(transform_dict,"Fuel type"))
            self.ui.ui.QComboBox_wheel.addItems(array_from_dict(transform_dict,"Wheel"))
            self.ui.ui.QComboBox_cylinders.addItems(array_from_dict(transform_dict,"Cylinders"))
            self.ui.ui.QComboBox_doors.addItems(array_from_dict(transform_dict,"Doors"))
            self.ui.ui.QComboBox_model.addItems(["Linear Regression", "Decision Tree","Random Forest","Grid search","XGBRFRegressor"])


            # set default value for each combobox
            self.ui.ui.QComboBox_turbo.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_gear_box_type.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_leather_interior.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_manufacturer.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_drive_wheels.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_engine_volume.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_category.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_fuel_type.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_wheel.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_cylinders.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_doors.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_model.setCurrentIndex(default_index)

