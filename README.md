# das_tempchef

## Setup

1. The recommended way is using an Anaconda environment. In the Anaconda prompt, run

```
conda create --name das_tempchef python=3.8
conda activate das_tempchef
```
This will create and activate the environment.

2. Clone the repository and enter the created directory by running

```
git clone https://github.com/dipnds/das_tempchef.git
cd das_tempchef
```

3. To install all dependencies in the active environment, run

```
python setup.py install
```


## Execute

1. Activate the Anaconda environment as before

2. In the project's root directory (```../das_tempchef/```) run

```
daschef
```

3. Ground truth and predictions are stored in the file ```das_tempchef/log_predictions.pkl```, for KPI reposts

The loaded variable will be a Python dictionary with the keys 'groundtruth' and 'prediction'


## Experimentation details

The Jupyter notebook ```das_tempchef/explore.ipynb``` contains the details of all data visualisation, data wrangling, related experiments, performance comparison, hyperparameter tuning and testing. The notebook should be self-explanatory. In brief, the workflow consists of

1. Loading and pre-processing the Boston Housing dataset, followed by dev/test split

2. Visualising data statistics and distributions (histograms) to figure out possible feature engineering steps

3. Visualising Correlation Coefficient matrix to plan possible feature reduction steps

4. Designing the baseline experiment using a Random Forest regressor, validated by 5-fold Cross Validation on the dev split

5. Running all the proposed data wrangling processes and comparing their performances

6. Running a hyperparameter tuning job on the best model obtained in the previous step, along with visualisation of results

7. Running the best configuration on the test set, then visualising and logging the final result

8. Writing the final pipeline as .py files for packaging

9. Saving environment variables and GitHub CI/CD actions in .yml files 
