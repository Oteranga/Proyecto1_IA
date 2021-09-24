import csv
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
import random
import math
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

def update_months(dataframe):
    dataframe.loc[dataframe["month"] == 'jan', "month"] = 1
    dataframe.loc[dataframe["month"] == 'feb', "month"] = 2
    dataframe.loc[dataframe["month"] == 'mar', "month"] = 3
    dataframe.loc[dataframe["month"] == 'apr', "month"] = 4
    dataframe.loc[dataframe["month"] == 'may', "month"] = 5
    dataframe.loc[dataframe["month"] == 'jun', "month"] = 6
    dataframe.loc[dataframe["month"] == 'jul', "month"] = 7
    dataframe.loc[dataframe["month"] == 'aug', "month"] = 8
    dataframe.loc[dataframe["month"] == 'sep', "month"] = 9
    dataframe.loc[dataframe["month"] == 'oct', "month"] = 10
    dataframe.loc[dataframe["month"] == 'nov', "month"] = 11
    dataframe.loc[dataframe["month"] == 'dec', "month"] = 12

def update_days(dataframe):
    dataframe.loc[dataframe["day"] == 'mon', "day"] = 1
    dataframe.loc[dataframe["day"] == 'tue', "day"] = 2
    dataframe.loc[dataframe["day"] == 'wed', "day"] = 3
    dataframe.loc[dataframe["day"] == 'thu', "day"] = 4
    dataframe.loc[dataframe["day"] == 'fri', "day"] = 5
    dataframe.loc[dataframe["day"] == 'sat', "day"] = 6
    dataframe.loc[dataframe["day"] == 'sun', "day"] = 7

def read_file_columns(file = 'forestfires.csv'):
    data = read_csv(file)
    update_months(data)
    update_days(data)
    return data

def plot_data(data_x,data_y):
    plt.plot(data_x,data_y,'*')
    plt.show()

def split_data(data):
    # x_train, x_rest, y_train, y_rest = train_test_split(x,y,train_size=0.7, shuffle=True)
    # x_valid, x_test, y_valid, y_test = train_test_split(x_rest,y_rest,test_size=0.33)
    train = []
    validation = []
    test = []
    random.shuffle(data)
    for i in range(len(data)):
        if i <= math.ceil(len(data) * 0.7):
            train.append(data[i])
        elif i > math.ceil(len(data) * 0.7) and i <= math.floor(len(data) * 0.9):
            validation.append(data[i])
        else:
            test.append(data[i])
    return train, validation, test

def normalize_features(x_features):
    return (x_features-x_features.min())/(x_features.max()-x_features.min())

data = read_file()
train, val, test = split_data(data)

dataframe = read_file_columns()
x_features = dataframe.iloc[:,:-1]
y_values = dataframe.iloc[:,-1]
x_features = normalize_features(x_features)
print(x_features)



