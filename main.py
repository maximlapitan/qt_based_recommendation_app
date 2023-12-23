# This Python file uses the following encoding: utf-8

"""IMPORTANT: run these 3 commands before you continue
pyside6-uic form.ui -o ui_form.py
pyside6-uic CompareModels.ui -o ui_CompareModels.py
pyside6-uic influence.ui -o ui_influence.py
"""


import sys
from PySide6.QtWidgets import QApplication

from widget import Widget

app = QApplication(sys.argv)
widget = Widget()
widget.show()
sys.exit(app.exec())
