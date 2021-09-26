import numpy as np

x_train = []
x_valid = []
y_train = []
y_valid = []

def h(x_features,w_values,b):
    return np.dot(w_values,x_features) + b

def derivate(x_features,y_values,w_values,b,k):
    sum1 = 0
    sum2 = 0
    dw_temp_list = []
    for i in range(len(y_values)):
        x_temp = np.array(x_features.loc[i])
        sum1 += (y_values[i] - h(x_temp,w_values,b)) * (-1)

    for j in range(k):
        for i in range(len(y_values)):
            x_temp = np.array(x_features.loc[i])
            x_ji = x_features.iloc[i,j]
            sum2 += (y_values[i] - h(x_temp,w_values,b)) *(-x_ji)
            dw_temp_list.append(sum2)

    db = sum1 / len(y_values)
    dw_values = [i/len(y_values) for i in dw_temp_list]
    return dw_values, db

def update(w_values,b,dw_values,db,alpha,k):
    w_new = [w_values[j] - alpha*dw_values[j] for j in range(k)]
    b_new = b - alpha*db
    return w_new, b_new

def error(x_features,y_values,w_values,b):
    sum1 = 0
    for i in range(len(y_values)):
        x_temp = np.array(x_features.loc[i])
        sum1 += pow(y_values[i] - h(x_temp,w_values,b), 2)

    sum1 /= 2*len(y_values)
    return sum1

def regression(x_train,y_train,x_valid,y_valid,alpha,epochs, k = 12):
    error_train_list = []
    error_valid_list = []
    w_values = np.random.uniform(0,1,k)
    b = np.random.rand()
    for i in range(epochs):
        dw_values, db = derivate(x_train,y_train,w_values,b,k)
        w, b = update(w_values,b,dw_values,db,alpha,k)
        error_train_value = error(x_train,y_train,w_values,b)
        error_valid_value = error(x_valid,y_valid,w_values,b)
        error_train_list.append(error_train_value)
        error_valid_list.append(error_valid_value)
        if i > 20000:
            break
    return error_train_list,error_valid_list

def regression2(x_train,y_train,x_valid,y_valid,x_test,y_test,alpha,epochs, k = 12):
    error_train_list = []
    error_valid_list = []
    error_test_list = []
    w_values = np.random.uniform(0,1,k)
    b = np.random.rand()
    for i in range(epochs):
        dw_values, db = derivate(x_train,y_train,w_values,b,k)
        w, b = update(w_values,b,dw_values,db,alpha,k)
        error_train_value = error(x_train,y_train,w_values,b)
        error_valid_value = error(x_valid,y_valid,w_values,b)
        error_test_value = error(x_test,y_test,w_values,b)
        
        error_train_list.append(error_train_value)
        error_valid_list.append(error_valid_value)
        error_test_list.append(error_test_value)
        if i > 20000:
            break
    return error_train_list,error_valid_list,error_test_list