
def h(w_list,x_list,b):
    h_value = 0
    return h_value

def derivate(x_list,x_matrix,y_list,w_list,b,k):
    sum1 = 0
    sum2 = 0
    dw_temp_list = []
    for i in range(len(y_list)):
        sum1 += (y_list[i] - h(x_list[i],w_list,b)) * (-1)

    for j in range(k):
        for i in range(len(y_list)):
            sum2 += (y_list[i] - h(x_list[i],w_list,b)) *(-x_matrix[j][i])
            dw_temp_list.append(sum2)

    db = sum1 / len(y_list)
    dw_list = [i/len(y_list) for i in dw_temp_list]
    return dw_list, db

def update(w_list,b,dw_list,db,alpha,k):
    w_new = [w_list[j] - alpha*dw_list[j] for j in range(k)]
    b_new = b - alpha*db
    return w_new, b_new

def error(x_list,y_list,w_list,b):
    sum1 = 0
    for i in range(len(y_list)):
        sum1 += pow(y_list[i] - h(x_list[i],w_list,b), 2)

    sum1 /= 2*len(y_list)
    return sum1
