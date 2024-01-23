- [1. QT car price prediction model](#1-qt-car-price-prediction-model)
  - [1.1. Authors](#11-authors)
  - [1.2. Project description](#12-project-description)
  - [1.3. Installation](#13-installation)
    - [1.3.1. Install all dependencies and activate venv](#131-install-all-dependencies-and-activate-venv)
    - [1.3.2. Get weights](#132-get-weights)
    - [1.3.3. Run project](#133-run-project)
  - [1.4. Data analysis](#14-data-analysis)
    - [1.4.1. Attributes of dataset](#141-attributes-of-dataset)
    - [1.4.2. Data analysis](#142-data-analysis)
    - [1.4.3. Model training](#143-model-training)
  - [1.5. Basic usage](#15-basic-usage)
  - [1.6. Implementation of the Requests](#16-implementation-of-the-requests)
  - [1.7. Little overview of performance](#17-little-overview-of-performance)
  - [1.8. Work done](#18-work-done)

# 1. QT car price prediction model

Be aware, that due to windows-related dll issues project may have troubles launching under windows machines. If you experience them, I recommend you to try project in VM (opensuse or ubuntu). Be sure to have [python-3.11.6](https://www.python.org/downloads/release/python-3116/)

## 1.1. Authors

Maxim Lapitan 22200839

Maxim Zotov 22200849

[Link to MyGit repo](https://mygit.th-deg.de/mz20849/mm-recommendation)

## 1.2. Project description

Project aims to predict price of the car based on criteria like mileage, volume of the engine, type of gearbox and so on.

Project uses openly distributed dataset from [Kaggle](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge).

The dataset itself was modified and normalized, thus we use [our version](car_price_prediction.csv), which is added directly to repository.

Keep in mind, that project is writte using `*.ui` files in QT Designer. And is divided to 3 separate windows:

<p align="center">
  <figure>
    <img src="doc/form_ui.png" width="600" alt="doc/form_ui.png">
    <figcaption>Main <code>form.ui</code></figcaption>
  </figure><figure>
    <img src="doc/CompareModels_ui.png" width="600" alt="doc/CompareModels_ui.png">
    <figcaption>Model comparison <code> CompareModels.ui</code> </figcaption>
  </figure><figure>
    <img src="doc/influence_ui.png" width="600" alt="doc/influence_ui.png">
    <figcaption>Influence of factor at price <code>influence.ui</code> </figcaption>
  </figure>
</p>

## 1.3. Installation

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

### 1.3.1. Install all dependencies and activate venv

   ```bash
   git clone https://mygit.th-deg.de/mz20849/mm-recommendation.git
   cd mm-recommendation/
   python3.11 -m venv recomendation-venv
   source recomendation-venv/bin/activate
   pip install -r requirements.txt
   ```

### 1.3.2. Get weights

There are 2 options:

1. You can either train them yourself by running provided jupyter notebook `inspect_csv.ipynb`. This will also help you to understand project better
2. Or you can download them by running `download_and_init.py` script, which will download pretrained weights from nextcloud

### 1.3.3. Run project

There are 2 options:

1. Via [QT Creator](https://www.qt.io/download). Open `recomendation.pyproject` as project in QT Creator and press either `Ctrl+R` or build symbol to build and run project. Please be sure to select `recomendation-venv` python binary as executable in Projects-Run in QT creator
2. Using using terminal and `pyside` commands. Activate previously created venv (if not done before) and type

```bash
pyside6-uic form.ui -o ui_form.py
pyside6-uic CompareModels.ui -o ui_CompareModels.py
pyside6-uic influence.ui -o ui_influence.py
```

After that you can run project `python main.py`

Be sure to have a look at [our jupyter notebook](inspect_csv.ipynb) to get familiar with project and its structure.

## 1.4. Data analysis

Data analysis is done exclusively in [jupyter notebook](inspect_csv.ipynb) to prevent interface cluttering with a lot of nonessential information. Please consult [inspect_csv.ipynb](inspect_csv.ipynb) file to get to know our project and our approach better.

### 1.4.1. Attributes of dataset

- Attributes
- ID: integer that numeretes data **(int)**
- Price: price of the care (Target Column) **(int)**
- Levy: tax related term. Tax of importing and exporting the cars **(int)**
- Manufacturer: company that produces cars **(text)**
- Model: model of the produced car by manufacturer **(text)**
- Prod. year: production year of the car **(int)**
- Category: jeep, sedan, cabriolet, hatchback, microbus, goods wagon, universal, coupe, limousine, minivan, pickup **(text)**
- Leather interior: shows if interior of the car is made of leather **(boolean)**
- Fuel type: hybrid, petrol, diesel, CNG (compressed natural gas), plug-in hybrid, LPG (liquefied petroleum gas), hydrogen **(text)**
- Engine volume: from 0.0 to 7.3 (shows how many litres are inside the engine) **(float)**
- Mileage: how much car has been driven in km **(int)**
- Cylinders: amount of cylinders inside the engine **(int)**
- Gear box type: automatic, manual, tiptronic, variator **(text)**
- Drive wheels: 4x4, rear or front, shows if only front wheels are driving wheels either it is rear or all 4 wheels drive the car. **(text)**
- Doors: number of doors in car (trunk does not count) **(text)**
- Wheel: left wheel or right-hand drive, shows if steering wheel is located left side of the car or right **(text)**
- Color: different color of the car body **(text)**
- Airbags: amount of airbags inside the car, from 0 to 16 **(int)**
- Turbo: shows if turbo is installed inside the engine (to power up the car) **(boolean)**

### 1.4.2. Data analysis

Short synopsis of what was done:

- Data source from [Kaggle](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge) was downloaded and edited by hand (to remove anomal values that might break machine learning and pandas). Final file is stored in the root of the project [car_price_prediction.csv](car_price_prediction.csv).
- Edited file was inserted into jupyter notebook, where it was cleaned from outliers (to prevent model from overfitting to these values). Method used is shown on the picture below ![](doc/iqr.png)
- After that data has been split to cathegorical and numerical and plotted accordingly in order to see cars distribution in the dataset.
- After that we tried to plot correlation between each feature with the price of a vehicle.
- Finally, correlation matrix was plotted to check if some cathegories affect other. Here we are mostly interested in correlation with price.
- Next comes training phase.
- Cathegorical features have to be converted into numbers. Thus we used `sklearn.preprocessing.LabelEncoder`. Because we will need to use our model in another project, `transform_dict` mapping was created, so `LabelEncoder` labels are preserved. It looks like this:

  ```json
  {'Manufacturer': {'ACURA': 0,
  'ALFA ROMEO': 1,
  'AUDI': 2,
  'BMW': 3,
  'BUICK': 4,
  'CADILLAC': 5,
  'CHEVROLET': 6,
  'CHRYSLER': 7,
  'CITROEN': 8,
   ........},
   'Leather interior': {False: 0, True: 1},
   'Fuel type': {'CNG': 0,
   'Diesel': 1,
   ........},
   'Gear box type': {'Automatic': 0, 'Manual': 1, 'Tiptronic': 2, 'Variator': 3},
   ........}
  ```

### 1.4.3. Model training

- After that we scaled our data using `sklearn.preprocessing.StandardScaler`, so that neither of weights have more influence just because of value ranges.
- Finally, the training begins. In our case we studied and implemented 5 regression models:
  - [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
  - [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
  - [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
  - [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
  - [XGBRFRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#module-xgboost.sklearn)

## 1.5. Basic usage

Prior to running `main.py` make sure to fullfill prerequisites (see [this](#get-weights)), namely:

- Either run jupyter notebook fully (better to run jupyter) or
- launch `download_and_init.py` to downloaded weights, that are needed for program to run

After folder `weights_variables` is populated with content, you can proceed to `main.py`.

You will be greeted by a starting gui

![](doc/form_ui.png)

Here you can select options like Turbo, Manufacturer via `QComboBox`, set a year with help of `QSlider` and `QSpinBox`, input Mileage using `QLineEdit`.

Additionally you can select from one of 5 [abovementioned models](#data-analysis) and click predict button.

This is an example what could happen.

![](doc/select_parameters_predict.png)

After Predict Price button was clicked, *Compare performance of all models* button appears. On click, opens form, which uses all 5 pre-trained models to predict price.

![](doc/select_parameters_predict_compare.png)

Here we can see how different models predict price differently.

Finally, you can press "See how factors influence price" and play around with graphs and plots. 2d/3d switch switches between price dependancy on one or 2 factors respecitely

![](doc/influence_ui.png)

## 1.6. Implementation of the Requests

- A Desktop App with PyQT6 has to been developed.
- [requirements.txt](requirements.txt) file was used to list the used Python modules.
- A [README.md](README.md) file correstponds to asked in part 01 structure.
- The module venv was used. See [this chapter](#131-install-all-dependencies-and-activate-venv)
- A free data source is used used. It was found on [Kaggle](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge) and modified to suit our needs
- There is a data import in
  - jupyter notebook [inspect_csv.ipynb](inspect_csv.ipynb), `csv`

    ```python
    data = pd.read_csv("car_price_prediction.csv")
    ```

  - gui programm, [influence_widget.py](influence_widget.py), pandas

    ```python
    with open("weights_variables/train_frame.pkl", "rb") as pd_frame:
            self.dataframe = pickle.load(pd_frame)
    ```

- The data is read from a file after app is started. For example in [widget.py](widget.py):

  ```python
  def predict_button(self):
      scaler_file = "weights_variables/scaler.pkl"
      with open(scaler_file, "rb") as s:
          scaler = pickle.load(s)
  ```

- The data is analyzed with Pandas methods, so that a user gets on overview. For example in [inspect_csv.ipynb](inspect_csv.ipynb):

  ```python
  data = pd.read_csv("car_price_prediction.csv")
  data.head()
  data.info()
  data.describe()
  ```

* There are also a bunch of diagrams and data analytics in jupyter notebook. Take a look [inspect_csv.ipynb](inspect_csv.ipynb)

- A program with several different widgets was created. Mainly utilized `QComboBox`, `QPushButton` and `QLineEdit`. All 3 windows can be seen above.

- A Scikit training model algorithms have been applied. You can see which models in section [Model Training](#143-model-training)

- Data was visualized in [inspect_csv.ipynb](inspect_csv.ipynb) and in programm itself. Ui file [influence.ui](influence.ui) is responsible for that. In file [influence_widget.py](influence_widget.py) (which directly uses this `.ui` file) a graphical analysis of data is done.

  ```python
  def plot_figure(self):
      if self.ui.radio_2d.isChecked():
          figure = plot_2d_scatter(self.dataframe, self.ui.combobox_parameter_1.currentText())
      elif self.ui.radio_3d.isChecked():
          figure = plot_3d_scatter(self.dataframe, self.ui.combobox_parameter_1.currentText(), self.ui.combobox_parameter_2.currentText())
  ```

- Statistical analysis of data is performed in [inspect_csv.ipynb](inspect_csv.ipynb)

## 1.7. Little overview of performance

Let us show how our models are working. Here we would predict car prices based on existing used cars that we found in internet.

First car is toyota camry le that cost 8000 dollars.

![](doc/toyota_camry_le_8000.png)

Here is how our model predicted. The result is really close.

![](doc/toyota_camry_le_8000_predicted.png)

Second car is toyota sienna xle that cost 20500 dollars. The model predicted value that is so close to the real price.

![](doc/toyota_sienna_xle_20500_with_prediction.png)

If we go and check average price on this website for this specific car, then it shows that it is really really close to the actual price.

![](doc/toyota_sienna_xle_average_price_on_market.png)

Third car is Dodge Challenger R/T Shaker RWD. The model predicted value that is absolutely close to the actual price.

![](doc/dodge_challenger_rt_rwd_27000.png)

But this was only one offer. Let us check for the average price of this car on website. Now the predited value is only 590 dollars far from the actual average price.

![](doc/dodge_challenger_rt_rwd_average.png)

## 1.8. Work done

In general, the project about a recommendation system has the following parts:

- Graphical User Interface (GUI) with PyQt
- Visualization (with pandas and matplotlib)
- Data analysis with pandas and numpy
- scikit-learn

The project is done by 2 students. We divided our parts by following:

Maxim Zotov:

1) Graphical User Interface with PyQt
2) Visualization

Maxim Lapitan:

3) Pandas with Numpy
4) Scikit-Learn

**Both**: General Python Programming.
