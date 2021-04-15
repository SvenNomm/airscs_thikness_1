# this scrept loads the ice thikness data files and performs attemts to perform classification workflow.

import pandas as pd
import os
from boruta import BorutaPy

from filter_models import fishers_score
from graphical_output import scatter_wrapper_3D
from classification_module import classifier_wrapper_1

from sklearn.ensemble import RandomForestRegressor
import numpy as np


features_nr = 5
#path = "C:/Users/Sven/Puu/Data_files/AIRSCS/thikness_1/"
path = "/Users/sven/kohalikTree/Data/AIRSCS/thikness_1/"
#file_name = "thickness_dataset_EW_v3.csv"
file_name = "thickness_dataset_IW_v3_clear.csv"
full_filename = path + file_name
data = pd.read_csv(full_filename, sep=';')
print("All data has been loaded.")

column_names = data.columns.values
cols = len(column_names)
rows = len(data)
print("it contains ", rows, " rows  and", cols, " columns")

# feature selection non cross validated
# create list of labels
labels = data['thick_class'].to_list()

# We have to discuss the meaning of this columns with Sander
del data['thick_class']
del data['segVal']
del data['time']
del data['mode']
del data['meas_thick']
data = data.apply(pd.to_numeric, errors='coerce')
fishers_score_frame = fishers_score(data, labels)
fishers_score_sorted = fishers_score_frame.sort_values(by=[0], axis=1, ascending=False)
sorted_columns = fishers_score_sorted.columns
first_columns = sorted_columns[0:features_nr]

print("Dealing with ", features_nr, "featues: ", first_columns)
print("Corresponding Fisher's scores are:", fishers_score_sorted.loc[0, first_columns])
classifier_wrapper_1(data[first_columns], labels)

#scatter_wrapper_3D(data, labels, first_columns)


###initialize Boruta
forest = RandomForestRegressor(
   n_jobs = -1,
   max_depth = 5
)
boruta = BorutaPy(
   estimator = forest,
   n_estimators = 'auto',
   max_iter = 100 # number of trials to perform
)
### fit Boruta (it accepts np.array, not pd.DataFrame)
boruta.fit(np.array(data[first_columns]), np.array(labels))
### print results
green_area = data[first_columns].columns[boruta.support_].to_list()
blue_area = data[first_columns].columns[boruta.support_weak_].to_list()
print('features in the green area:', green_area)
print('features in the blue area:', blue_area)


print("That's all folks!!!")
#next try regression methods
