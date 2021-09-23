import csv
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
import random
import math

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def read_file(file = 'forestfires.csv'):
    list = []
    train = []
    validation = []
    test = []

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
                list.append(line)

    # x_train, x_rest, y_train, y_rest = train_test_split(x,y,train_size=0.7, shuffle=True)
    # x_valid, x_test, y_valid, y_test = train_test_split(x_rest,y_rest,test_size=0.33)

    random.shuffle(list)
    for i in range(len(list)):
        if i <= math.ceil(len(list) * 0.7):
            train.append(list[i])
        elif i > math.ceil(len(list) * 0.7) and i <= math.floor(len(list) * 0.9):
            validation.append(list[i])
        else:
            test.append(list[i])
    return train, validation, test

train, val, test = read_file()


