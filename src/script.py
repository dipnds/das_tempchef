import requests
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor as rf
from sklearn.metrics import mean_squared_error
import pandas as pd

def train_test():

    link = "http://lib.stat.cmu.edu/datasets/boston"
    raw_text = requests.get(link).text # get the raw text
    raw_text = raw_text.split('\n') # split into lines
    headers = raw_text[7:21]
    headers = [h.split()[0] for h in headers]
    raw_text = raw_text[22:-1] # discard description
    
    raw_data = []
    for i in range(0, len(raw_text), 2):
        # each row is split into 2 lines, so join them first
        row = raw_text[i] + raw_text[i+1]
        raw_data.append(row)
    
    # split each row into columns and convert each cell -> string to float
    raw_data = [[float(column) for column in row.split()] for row in raw_data]
    raw_data = np.array(raw_data) # no error => equal length rows, error-free import
    
    # 1/6 parts in test, 5/6 parts in dev for 5-fold cross validation later
    # random seed set for reproducibility
    raw_dev_data, raw_test_data = train_test_split(raw_data, test_size=1/6, random_state=10)
    
    # process train set
    raw_dev_df = pd.DataFrame(raw_dev_data,columns=headers)
    final_dev_df = raw_dev_df.drop('TAX', axis=1)
    
    model = rf(n_estimators=40, max_features='sqrt', max_depth=None, random_state=1)
    
    # process test set
    raw_test_df = pd.DataFrame(raw_test_data,columns=headers)
    final_test_df = raw_test_df.drop('TAX', axis=1)
    
    X_dev = final_dev_df[final_dev_df.columns[:-1]].to_numpy()
    y_dev = final_dev_df[final_dev_df.columns[-1]].to_numpy()
    
    X_test = final_test_df[final_test_df.columns[:-1]].to_numpy()
    y_test = final_test_df[final_test_df.columns[-1]].to_numpy()
            
    model.fit(X_dev,y_dev) # training 
    y_pred = model.predict(X_test) # testing
    
    mse = round(mean_squared_error(y_test, y_pred),3)
    rho = np.corrcoef(y_test, y_pred); rho = round(rho[0,1],3)
    
    # plt.scatter(y_test, y_pred)
    # plt.xlabel('Ground Truth MEDV'); plt.ylabel('Predicted MEDV')
    
    print('Test MSE : ', mse)
    print('Test RHO : ', rho)