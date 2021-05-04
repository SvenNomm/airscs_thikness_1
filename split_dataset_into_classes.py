# this script goes through the initial folder and copies files to the corresponding subfolder


import os
import pandas as pd
import numpy as np
import shutil


path = "C:/Users/Sven/Puu/Data_files/AIRSCS/thikness_1/"
#path = "/Users/sven/kohalikTree/Data/AIRSCS/thikness_1/"
file_name = "thickness_dataset_EW_v3.csv"
#file_name = "thickness_dataset_IW_v3_clear.csv"
full_filename = path + file_name
data = pd.read_csv(full_filename, sep=';')
print("Unique ID and ice class data have been loaded.")



# calculate class proportions
rows = len(data)
print("Data set contains", rows, " observation points.")

list_of_classes = []
class_elements = np.zeros((1, 4))
class_indexes = {}

for i in range (0, rows):
    if data.loc[i, 'thick_class'] in list_of_classes:
        idx = list_of_classes.index(data.loc[i, 'thick_class'])
        class_elements[0, idx] = class_elements[0, idx] + 1
    else:
        list_of_classes.append(data.loc[i, 'thick_class'])
        idx = len(list_of_classes)
        class_elements[0, idx-1] = class_elements[0, idx-1] + 1
print("Corresponding quantities in each class:", class_elements)

class_number = len(list_of_classes)
list_of_class_indexes = []

# read dir list
path_images = path + 'ew/'
target_dir = path + 'ew_classes/thick_class_'
folder_listing = os.listdir(path_images)
print(folder_listing)

for file_name in folder_listing:
    fname = file_name.split(".")
    fname = fname[0].split("_")
    print(int(fname[2]))
    idx = data[data['segVal'] == int(fname[2])].index.values.astype(int)
    if len(idx) != 0:
        class_id = data.loc[idx[0], 'thick_class']
        td = target_dir + str(class_id) + '/' + file_name
        shutil.copy(path_images + file_name, td)









