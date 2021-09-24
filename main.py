import regression as reg
import data as d
import numpy as np
import math
import matplotlib.pyplot as plt

data = d.read_file()

df = d.read_file_columns()
train_df, valid_df, test_df = np.split(df.sample(frac=1, random_state=42),[int(math.ceil(.7*len(df))), int(math.floor(.9*len(df)))])

x_train_features,y_train_values = d.get_x_y(train_df)
x_valid_features,y_valid_values = d.get_x_y(valid_df)
x_test_features,y_test_values = d.get_x_y(test_df)

error_train_list,error_valid_list = reg.regression(x_train_features,y_train_values,x_valid_features,y_valid_values,0.05,10)

plt.plot(error_train_list,error_valid_list,'*')
plt.show()