# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import sys
from PySide6.QtWidgets import QApplication

from widget import Widget

app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
