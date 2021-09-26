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

def regression(x_1,y_1,x_2,y_2,alpha,epochs, k = 12):
    error_1_list = []
    error_2_list = []
    w_values = np.random.uniform(0,1,k)
    b = np.random.rand()
    for i in range(epochs):
        dw_values, db = derivate(x_1,y_1,w_values,b,k)
        w, b = update(w_values,b,dw_values,db,alpha,k)
        error_1_value = error(x_1,y_1,w_values,b)
        error_2_value = error(x_2,y_2,w_values,b)
        error_1_list.append(error_1_value)
        error_2_list.append(error_2_value)
        if i > 20000:
            break
    return error_1_list,error_2_list

def regression2(x_1,y_1,x_2,y_2,x_3,y_3,alpha,epochs, k = 12):
    error_1_list = []
    error_2_list = []
    error_3_list = []
    w_values = np.random.uniform(0,1,k)
    b = np.random.rand()
    
    for i in range(epochs):
        dw_values, db = derivate(x_1,y_1,w_values,b,k)
        w, b = update(w_values,b,dw_values,db,alpha,k)
        error_1_value = error(x_1,y_1,w_values,b)
        error_2_value = error(x_2,y_2,w_values,b)
        error_3_value = error(x_3,y_3,w_values,b)
        
        error_1_list.append(error_1_value)
        error_2_list.append(error_2_value)
        error_3_list.append(error_3_value)
        if i > 20000:
            break
    return error_1_list,error_2_list,error_3_list
