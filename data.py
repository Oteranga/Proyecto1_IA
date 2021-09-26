import csv
from os import X_OK
import numpy as np
from numpy.core.numeric import True_
import pandas as pd
import math

def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def read_file(file = 'forestfires.csv'):
    data_list = []
    with open(file) as csvfile:
        data = csv.reader(csvfile, delimiter = ',')
        for line in data:
            if line[0] != 'X':
                line[0] = normalize_data(int(line[0]))
                line[1] = normalize_data(int(line[1]))
                for i in range(4, 13):
                    if line[i] == '0':
                        line[i] = 0
                    else:
                        line[i] = float(line[i])
                data_list.append(line)
    return data_list

def update_months(df):
    df.loc[df["month"] == 'jan', "month"] = 1
    df.loc[df["month"] == 'feb', "month"] = 2
    df.loc[df["month"] == 'mar', "month"] = 3
    df.loc[df["month"] == 'apr', "month"] = 4
    df.loc[df["month"] == 'may', "month"] = 5
    df.loc[df["month"] == 'jun', "month"] = 6
    df.loc[df["month"] == 'jul', "month"] = 7
    df.loc[df["month"] == 'aug', "month"] = 8
    df.loc[df["month"] == 'sep', "month"] = 9
    df.loc[df["month"] == 'oct', "month"] = 10
    df.loc[df["month"] == 'nov', "month"] = 11
    df.loc[df["month"] == 'dec', "month"] = 12

def update_days(df):
    df.loc[df["day"] == 'mon', "day"] = 1
    df.loc[df["day"] == 'tue', "day"] = 2
    df.loc[df["day"] == 'wed', "day"] = 3
    df.loc[df["day"] == 'thu', "day"] = 4
    df.loc[df["day"] == 'fri', "day"] = 5
    df.loc[df["day"] == 'sat', "day"] = 6
    df.loc[df["day"] == 'sun', "day"] = 7

def read_file_columns(file = 'forestfires.csv'):
    data = pd.read_csv(file)
    update_months(data)
    update_days(data)
    return data

def plot_data(data_x,data_y):
    pd.plt.plot(data_x,data_y,'*')
    pd.plt.show()

def normalize_features(x_features):
    for column in x_features.columns[1:]:
        low_value = x_features[column].max()-x_features[column].min() if x_features[column].max()-x_features[column].min() != 0 else 0
        if low_value == 0:
            return 0
        else:
            return (x_features[column]-x_features[column].min())/low_value

def get_x_y(df):
    x_features = df.iloc[:,:-1]
    y_values = df.iloc[:,-1]
    #x_features = normalize_features(x_features)
    return x_features,y_values

def split_groups(df):
    train_df = pd.DataFrame(columns=df.columns)
    valid_df = pd.DataFrame(columns=df.columns)
    test_df = pd.DataFrame(columns=df.columns)
    
    a,b,c = 0,0,0
    for index, row in df.iterrows():
        if index <= math.ceil(df.shape[0] * 0.7):
            train_df.loc[a] = row.values
            a += 1
        elif index > math.ceil(df.shape[0] * 0.7) and index <= math.floor(df.shape[0] * 0.9):
            valid_df.loc[b,:] = row.values
            b += 1
        else:
            test_df.loc[c,:] = row.values
            c += 1
            
    return train_df,valid_df,test_df
