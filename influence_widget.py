# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from ui_influence import Ui_InfluenceForm
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QTableWidgetItem, QGraphicsScene, QGraphicsProxyWidget
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsView, QWidget
from PySide6.QtGui import QImageReader, QImage, QPixmap
import pickle
from fill_labels import plot_2d_scatter, plot_3d_scatter, default_index
import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class InfluenceWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InfluenceForm()
        self.ui.setupUi(self)

        with open("weights_variables/train_frame.pkl", "rb") as pd_frame:
            self.dataframe = pickle.load(pd_frame)

    def showEvent(self, event):
        with open("weights_variables/feature_by_importance.pkl", "rb") as features_file:
                features = pickle.load(features_file)
                self.ui.combobox_parameter_1.addItems([feature for _, feature in features])
                self.ui.combobox_parameter_2.addItems([feature for _, feature in features])
                self.ui.combobox_parameter_1.setCurrentIndex(default_index)
                self.ui.combobox_parameter_2.setCurrentIndex(default_index)

        figure = plot_2d_scatter(self.dataframe, self.ui.combobox_parameter_1.currentText())

        canvas = FigureCanvas(figure)

        canvas.draw()
        buffer = canvas.buffer_rgba()
        qimage = QImage(buffer, canvas.get_width_height()[0], canvas.get_width_height()[1], QImage.Format_ARGB32)

        pixmap = QPixmap.fromImage(qimage)

        pixmap_item = QGraphicsPixmapItem(pixmap)

        scene = QGraphicsScene()

        scene.addItem(pixmap_item)

        self.ui.graphicsView_matplotlib.setScene(scene)

