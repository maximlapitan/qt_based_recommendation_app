# QT car price prediction model

## Authors

Maxim Lapitan 22200839

Maxim Zotov 22200849

[Link to MyGit repo](https://mygit.th-deg.de/mz20849/mm-recommendation)

## Project description

Project aims to predict price of the car based on criteria like mileage, volume of the engine, type of gearbox and so on.

Project uses openly distributed dataset from [Kaggle](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge).

The dataset itself was modified and normalized, thus we use [our version](car_price_prediction.csv), which is added directly to repository.

Keep in mind, that project is writte using `*.ui` files in QT Designer.

## Installation

There are several steps of installation, which have to be read carefully.

Software version used:

| Name         | Version |
| ------------ | ------- |
| python       | 3.11.6  |
| matplotlib   | 3.8.2   |
| PyQt6        | 6.4.2   |
| PySide6      | 6.6.0   |
| scikit-learn | 1.3.2   |
| seaborn      | 0.13.0  |
| xgboost      | 2.0.2   |


1. Install all dependencies and activate venv
   ```bash
   git clone https://mygit.th-deg.de/mz20849/mm-recommendation.git
   cd mm-recommendation/
   python3.11 -m venv recomendation-venv
   source recomendation-venv/bin/activate
   pip install -r requirements.txt
   ```

1. Get weights. There are 2 options:
   1. You can either train them yourself by running provided jupyter notebook `inspect_csv.ipynb`. This will also help you to understand project better
   2. Or you can download them by running `download_and_init.py` script, which will download pretrained weights from nextcloud
2. Run project. There are 2 options:
   1. Via [QT Creator](https://www.qt.io/download). Open `recomendation.pyproject` as project in QT Creator and press either `Ctrl+R` or build symbol to build and run project. Please be sure to select `recomendation-venv` python binary as executable in Projects-Run in QT creator
   2. Using using terminal and `pyside` commands. Activate previously created venv (if not done before) and type 
   ```bash
   pyside6-uic form.ui -o ui_form.py
   pyside6-uic CompareModels.ui -o ui_CompareModels.py
   pyside6-uic influence.ui -o ui_influence.py
   ```
   After that you can run project `python main.py`

Be sure to have a look at [our jupyter notebook](inspect_csv.ipynb) to get familiar with project and its structure.

## Data analysis

## Basic usage

## Implementation of the Requests

## Work done