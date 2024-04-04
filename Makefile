# Set the default value for RM
RM := rm

# Check if running on Windows, then override RM
ifeq ($(OS),Windows_NT)
    RM := del
endif
all:
	pyside6-uic form.ui -o ui_form.py
	pyside6-uic CompareModels.ui -o ui_CompareModels.py
	pyside6-uic influence.ui -o ui_influence.py

clean:
	$(RM) ui_form.py
	$(RM) ui_CompareModels.py
	$(RM) ui_influence.py

run: all
	python main.py