all:
	pyside6-uic form.ui -o ui_form.py
	pyside6-uic CompareModels.ui -o ui_CompareModels.py
	pyside6-uic influence.ui -o ui_influence.py
