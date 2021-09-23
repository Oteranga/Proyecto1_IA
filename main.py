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
                line[0] = int(line[0])
                line[1] = int(line[1])
                for i in range(4, 13):
                    if line[i] == '0':
                        line[i] = 0
                    else:
                        line[i] = float(line[i])
                data_list.append(line)
    return data_list

def read_file_columns(file = 'forestfires.csv'):
    data_list = []
    data = read_csv(file)
    x = data['X'].tolist()
    y = data['Y'].tolist()
    month = data['month'].tolist()
    day = data['day'].tolist()
    ffmc = data['FFMC'].tolist()
    dmc = data['DMC'].tolist()
    dc = data['DC'].tolist()
    isi = data['ISI'].tolist()
    temp = data['temp'].tolist()
    rh = data['RH'].tolist()
    wind = data['wind'].tolist()
    rain = data['rain'].tolist()
    area = data['area'].tolist()       
    data_list = {'X':x,'Y':y,'month':month,'day':day,'FFMC':ffmc,'DMC':dmc,'DC':dc,'ISI':isi,'temp':temp,'RH':rh,'wind':wind,'rain':rain,'area':area}
    return data_list

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

def update_months(months):
    months_new = []
    for i in range(len(months)):
        month = months[i]
        if month=='jan': months_new.append(1)
        if month=='feb': months_new.append(2)
        if month=='mar': months_new.append(3)
        if month=='apr': months_new.append(4)
        if month=='may': months_new.append(5)
        if month=='jun': months_new.append(6)
        if month=='jul': months_new.append(7)
        if month=='aug': months_new.append(8)
        if month=='sep': months_new.append(9)
        if month=='oct': months_new.append(10)
        if month=='nov': months_new.append(11)
        if month=='dec': months_new.append(12)
    return months_new

def update_days(days):
    months_new = []
    for i in range(len(days)):
        day = days[i]
        if day=='mon': months_new.append(1)
        if day=='tue': months_new.append(2)
        if day=='wed': months_new.append(3)
        if day=='thu': months_new.append(4)
        if day=='fri': months_new.append(5)
        if day=='sat': months_new.append(6)
        if day=='sun': months_new.append(7)
    return months_new
        
data = read_file()
columns_data = read_file_columns()
columns_data['month'] = update_months(columns_data['month'])
columns_data['day'] = update_days(columns_data['day'])
plot_data(columns_data['X'],columns_data['Y'])
train, val, test = split_data(data)


