import csv
from os import X_OK
import numpy as np
from pandas import *

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
    data = read_csv(file)
    update_months(data)
    update_days(data)
    return data

def plot_data(data_x,data_y):
    plt.plot(data_x,data_y,'*')
    plt.show()

def normalize_features(x_features):
    return (x_features-x_features.min())/(x_features.max()-x_features.min())

def get_x_y(df):
    x_features = df.iloc[:,:-1]
    y_values = df.iloc[:,-1]
    x_features = normalize_features(x_features)
    return x_features,y_values
