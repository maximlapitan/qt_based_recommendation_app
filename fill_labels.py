# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PyQt6.QtWidgets import QLabel, QApplication, QWidget, QLabel, QListWidget
from ui_form import Ui_Widget
import pickle
import joblib
from copy import deepcopy
from pandas import DataFrame as df
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import matplotlib

default_index = 0
exported_weights = {}

models_to_load = {"Linear Regression": "weights_variables/lin_reg.joblib",
                  "Decision Tree": "weights_variables/tree_reg.joblib",
                  "Random Forest": "weights_variables/forest_reg.joblib",
                  "Grid search": "weights_variables/grid_search.joblib",
                  "XGBRFRegressor": "weights_variables/XGBRFRegressor_model.joblib"}

data = {'Manufacturer': [],
        'Category': [],
        'Leather interior': [],
        'Fuel type': [],
        'Engine volume': [],
        'Gear box type': [],
        'Drive wheels': [],
        'Wheel': [],
        'Turbo': [],
        'Prod. year': [],
        'Mileage': [],
        'Cylinders': [],
        'Doors': []}


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
            # print(transform_dict)

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
            self.ui.ui.QLabel_prod_year.setText("Production Year")

            # set values in comboboxes
            self.ui.ui.QComboBox_turbo.addItems(
                array_from_dict(transform_dict, "Turbo"))
            self.ui.ui.QComboBox_gear_box_type.addItems(
                array_from_dict(transform_dict, "Gear box type"))
            self.ui.ui.QComboBox_leather_interior.addItems(
                array_from_dict(transform_dict, "Leather interior"))
            self.ui.ui.QComboBox_manufacturer.addItems(
                array_from_dict(transform_dict, "Manufacturer"))
            self.ui.ui.QComboBox_drive_wheels.addItems(
                array_from_dict(transform_dict, "Drive wheels"))
            self.ui.ui.QComboBox_engine_volume.addItems(
                array_from_dict(transform_dict, "Engine volume"))
            self.ui.ui.QComboBox_category.addItems(
                array_from_dict(transform_dict, "Category"))
            self.ui.ui.QComboBox_fuel_type.addItems(
                array_from_dict(transform_dict, "Fuel type"))
            self.ui.ui.QComboBox_wheel.addItems(
                array_from_dict(transform_dict, "Wheel"))
            self.ui.ui.QComboBox_cylinders.addItems(
                array_from_dict(transform_dict, "Cylinders"))
            self.ui.ui.QComboBox_doors.addItems(
                array_from_dict(transform_dict, "Doors"))
            self.ui.ui.QComboBox_model.addItems(
                [item for item in models_to_load.keys()])

            # set default value for each combobox
            self.ui.ui.QComboBox_turbo.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_gear_box_type.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_leather_interior.setCurrentIndex(
                default_index)
            self.ui.ui.QComboBox_manufacturer.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_drive_wheels.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_engine_volume.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_category.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_fuel_type.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_wheel.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_cylinders.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_doors.setCurrentIndex(default_index)
            self.ui.ui.QComboBox_model.setCurrentIndex(default_index)

    def fill_data_with_data(self):
        data[self.ui.ui.QLabel_turbo.text()] = [bool(
            self.ui.ui.QComboBox_turbo.currentText())]
        data[self.ui.ui.QLabel_gear_box_type.text()] = [
            self.ui.ui.QComboBox_gear_box_type.currentText()]
        data[self.ui.ui.QLabel_leather_interior.text()] = [bool(
            self.ui.ui.QComboBox_leather_interior.currentText())]
        data[self.ui.ui.QLabel_manufacturer.text()] = [
            self.ui.ui.QComboBox_manufacturer.currentText()]
        data[self.ui.ui.QLabel_drive_wheels.text()] = [
            self.ui.ui.QComboBox_drive_wheels.currentText()]
        data[self.ui.ui.QLabel_engine_volume.text()] = [float(
            self.ui.ui.QComboBox_engine_volume.currentText())]
        data[self.ui.ui.QLabel_category.text()] = [
            self.ui.ui.QComboBox_category.currentText()]
        data[self.ui.ui.QLabel_fuel_type.text()] = [
            self.ui.ui.QComboBox_fuel_type.currentText()]
        data[self.ui.ui.QLabel_wheel.text()] = [
            self.ui.ui.QComboBox_wheel.currentText()]
        data[self.ui.ui.QLabel_cylinders.text()] = [int(
            self.ui.ui.QComboBox_cylinders.currentText())]
        data[self.ui.ui.QLabel_doors.text()] = [int(
            self.ui.ui.QComboBox_doors.currentText())]
        data["Prod. year"] = [self.ui.ui.QSlider_prod_year.value()]
        data["Mileage"] = [int(self.ui.ui.QLineEdit_mileage.text())]
        print(data)
        return encode_data(data)

    def validate_mileage(self):
        pass


def encode_data(data):

    data_encoded = deepcopy(data)

    with open("weights_variables/export_dict.pkl", "rb") as d:
        helper = pickle.load(d)

        for key in data_encoded.keys():
            if helper.get(key) is not None:
                car_to_translate = data_encoded[key][0]
                print(car_to_translate, key)
                # print(key, car_to_translate, helper[key][car_to_translate])
                if key not in ["Mileage", "Prod. year"]:
                    data_encoded[key][0] = helper[key][car_to_translate]
                else:
                    data_encoded[key][0] = car_to_translate

    print(data_encoded)

    return df(data_encoded)


def plot_2d_scatter(df, variable):
    # Check if the variable is present in the DataFrame
    if variable not in df.columns:
        print(f"Variable {variable} not found in DataFrame.")
        return None

    # Create a 2D scatter plot
    fig = Figure()
    ax = fig.add_subplot(111)

    scatter = ax.scatter(df[variable], df['Price'],
                         c=df['Price'], cmap='viridis')
    ax.set_xlabel(variable)
    ax.set_ylabel('Price')
    ax.set_title(f'2D Scatter Plot: {variable} vs Price')
    fig.colorbar(scatter, label='Price')

    return fig


def plot_3d_scatter(df, x_variable, y_variable):
    # Check if the variables are present in the DataFrame
    if x_variable not in df.columns or y_variable not in df.columns:
        print(
            f"One or both of the variables {x_variable}, {y_variable} not found in DataFrame.")
        return

    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(df[x_variable], df[y_variable],
               df['Price'], c=df['Price'], cmap='viridis')
    ax.set_xlabel(x_variable)
    ax.set_ylabel(y_variable)
    ax.set_zlabel('Price')
    ax.set_title(f'3D Scatter Plot: {x_variable}, {y_variable}, Price')

    return fig
