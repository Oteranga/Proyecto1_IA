import regression as reg
import data as d
import numpy as np
import matplotlib.pyplot as plt
import random

df = d.read_file_columns()

train_df,valid_df,test_df = d.split_groups(df)

x_train_features,y_train_values = d.get_x_y(train_df)
x_valid_features,y_valid_values = d.get_x_y(valid_df)
x_test_features,y_test_values = d.get_x_y(test_df)

    
def algorithm1():
    epochs = 100
    num_tests = 1
    for i in range(num_tests):
        alpha = random.uniform(0,1)
        error_train_list,error_valid_list = reg.regression(x_train_features,y_train_values,x_valid_features,y_valid_values,alpha,epochs)

        plt.figure()
        p1 = plt.scatter(x=list(range(epochs)), y=error_train_list,color="lightskyblue")
        p2 = plt.scatter(x=list(range(epochs)), y=error_valid_list,color="lightgreen")
        
        font1 = {'family':'serif','size':20}
        font2 = {'family':'serif','size':15}
        plt.legend((p1,p2),["Train error","Validation error"])
        
        plt.title("Train and Validation Error vs. Epoch",fontdict=font1)
        plt.xlabel("Epoch",fontdict=font2)
        plt.ylabel("Error",fontdict=font2)
        plt.show()

def algorithm2():
    epochs = 100
    alpha = 0.05
    error_train_list,error_valid_list,error_test_list = reg.regression2(
        x_train_features,y_train_values,x_test_features,y_test_values,x_test_features,y_test_values,alpha,epochs)

    plt.figure()
    #plt.scatter(x=list(range(epochs)), y=error_train_list,color="r")
    plt.scatter(x=list(range(epochs)), y=error_valid_list,color="g")
    plt.scatter(x=list(range(epochs)), y=error_test_list,color="b")
    plt.show()
    
algorithm1()