# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from ui_influence import Ui_InfluenceForm
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QTableWidgetItem, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsView, QWidget
from PySide6.QtGui import QImageReader, QImage, QPixmap, QIcon
import pickle
from fill_labels import plot_2d_scatter, plot_3d_scatter, default_index
import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import Qt

class InfluenceWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfluenceForm()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('doc/icon.png'))

        with open("weights_variables/train_frame.pkl", "rb") as pd_frame:
            self.dataframe = pickle.load(pd_frame)

        self.ui.combobox_parameter_1.currentTextChanged.connect(self.plot_figure)
        self.ui.combobox_parameter_2.currentTextChanged.connect(self.plot_figure)
        self.ui.radio_2d.toggled.connect(self.plot_figure)
        self.ui.radio_3d.toggled.connect(self.plot_figure)
        self.canvas = None

    def showEvent(self, event):
        with open("weights_variables/feature_by_importance.pkl", "rb") as features_file:
                features = pickle.load(features_file)
        self.ui.combobox_parameter_1.addItems([feature for _, feature in features])
        self.ui.combobox_parameter_2.addItems([feature for _, feature in features])
        self.ui.combobox_parameter_1.setCurrentIndex(default_index)
        self.ui.combobox_parameter_2.setCurrentIndex(default_index)

        self.plot_figure()

    def resizeEvent(self, event):
        if self.canvas == None:
            pass
        else:
            self.display_bitmap(self.canvas)
        # self.plot_figure()
        self.ui.graphicsView_matplotlib.fitInView(self.ui.graphicsView_matplotlib.sceneRect(), aspectRadioMode=Qt.KeepAspectRatio)

    def display_bitmap(self, canvas):
        buffer = canvas.buffer_rgba()
        qimage = QImage(buffer, canvas.get_width_height()[0], canvas.get_width_height()[1], QImage.Format_ARGB32)

        pixmap = QPixmap.fromImage(qimage)

        pixmap_item = QGraphicsPixmapItem(pixmap)

        scene = QGraphicsScene()

        scene.addItem(pixmap_item)

        self.ui.graphicsView_matplotlib.setScene(scene)

    def plot_figure(self):
        if self.ui.radio_2d.isChecked():
            figure = plot_2d_scatter(self.dataframe, self.ui.combobox_parameter_1.currentText())
        elif self.ui.radio_3d.isChecked():
            figure = plot_3d_scatter(self.dataframe, self.ui.combobox_parameter_1.currentText(), self.ui.combobox_parameter_2.currentText())

        self.canvas = FigureCanvas(figure)
        print(figure)
        self.canvas.draw()

        self.display_bitmap(self.canvas)

