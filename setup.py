from cx_Freeze import setup, Executable
from sys import platform

build_exe_options = {
    "includes": ["PySide6.QtWidgets", "PySide6.QtGui", "sklearn", "pickle", "matplotlib.backends.backend_qtagg",
                 "PySide6.QtCore", "joblib", "copy", "numpy", "pandas", "sklearn.tree", "sklearn.ensemble", "sklearn.linear_model",
                 "sklearn.metrics", "xgboost"]
}

base = "Win32GUI" if platform == "win32" else None

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("main.py", base=base)],
    options={"build_exe": build_exe_options}
)