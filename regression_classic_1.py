# this script commands regression analysis on the data.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from correlation_analysis import correlation_analysis
from regression_module import regression_wrapper
from conversion_module import format_time_diff
from conversion_module import get_date

features_nr = 80

path = "C:/Users/Sven/Puu/Data_files/AIRSCS/thikness_1/"
#path = "/Users/sven/kohalikTree/Data/AIRSCS/thikness_1/"
file_name = "thickness_dataset_EW_v3.csv"
#file_name = "thickness_dataset_IW_v3_clear.csv"
full_filename = path + file_name
data = pd.read_csv(full_filename, sep=';')
print("All data has been loaded.")

column_names = data.columns.values
cols = len(column_names)
rows = len(data)
print("it contains ", rows, " rows  and", cols, " columns")

# feature selection non cross validated
# create list of labels
dependent_variable = data['meas_thick']
#dependent_variable = data['thick_class']

# convert time difference
data['time_diff'] = data['time_diff'].map(lambda a: format_time_diff(a))
print('Time difference conversion has been performed.')

# get month
data['meas_time'] = data['meas_time'].map(lambda a: get_date(a))
print('Date has been extracted.')

# We have to discuss the meaning of this columns with Sander
del data['thick_class']
del data['segVal']
del data['time']
del data['mode']
#del data['meas_time']
#del data['time_diff']
del data['meas_thick']
#del data['meas_lon']
#del data['meas_lat']
del data['prec_low_co']
#columns_list = data.columns.values
#data[columns_list] = data[columns_list]/data[columns_list].max()
collinearity_frame, correlations_frame = correlation_analysis(data, dependent_variable)

col_names = correlations_frame.columns.values

#plt.imshow(collinearity_frame, cmap='hot', interpolation='nearest')
#plt.show()
#ax = sns.heatmap(collinearity_frame)
#plt.show()

correlations_frame_sorted = correlations_frame.sort_values(by=[0], axis=1, ascending=False)
sorted_columns = correlations_frame_sorted.columns
first_columns = sorted_columns[0:features_nr]

print("Dealing with ", features_nr, "featues: ", first_columns)
print("Corresponding correlation coefficients  scores are:", correlations_frame_sorted.loc[0, first_columns])
#data_to_process = pd.concat([data[first_columns], data['time_diff'], data['meas_time'], data['meas_lat']], axis=1)
X_test, X_train, y_test,  y_train, predict, predict_train = regression_wrapper(data, dependent_variable, first_columns)


# find max and mn values
x_max = data[first_columns[0]].max()
x_min = data[first_columns[0]].min()
y_max = data[first_columns[1]].max()
y_min = data[first_columns[1]].min()
#linear_regression_model.predict([x_min, y_min])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(data[first_columns[0]], data[first_columns[1]], dependent_variable, marker=10)
plt.show()


print("That's all folks!!!")

fig_1 = plt.figure()
ax = fig_1.add_subplot(projection='3d')
ax.scatter(X_train['time_diff'], X_train['meas_time'], predict_train-y_train, marker=10)
ax.set_xlabel('Time difference')
ax.set_ylabel('Month')
ax.set_zlabel('Residuals')
plt.show()

fig_2 = plt.figure()
ax = fig_2.add_subplot(projection='3d')
ax.scatter(X_train['meas_lon'], X_train['meas_lat'], predict_train-y_train, marker=10)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Residuals')
plt.title('Train set residuals')
plt.show()

fig_3 = plt.figure()
ax = fig_3.add_subplot(projection='3d')
ax.scatter(X_test['meas_lon'], X_test['meas_lat'], predict - y_test, marker=10)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Residuals')
plt.title('Test set residuals')
plt.show()

# encorporrate time into modeling.
# investigate if position of the images and time play the role in modeing precision. 
