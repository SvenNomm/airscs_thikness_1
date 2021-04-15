# this file contains differnt functions to perform filter based feature selection

import pandas as pd
import numpy as np
from more_itertools import locate


def fishers_score(data, labels):
    data_length = len(data)
    list_of_classes = []
    for label in labels:
        if label not in list_of_classes:
            list_of_classes.append(label)

    number_of_classes = len(list_of_classes)
    print('Data contains: ', number_of_classes, ' classes.')
    numerator = 0
    denominator = 0
    columns = data.columns
    fishers_score_frame = pd.DataFrame(columns=columns)

    for column in columns:
        column_mean = np.mean(data.loc[:, column])
        numerator = 0
        denominator = 0
        for label in list_of_classes:
            indexes = list(locate(labels, lambda x: x == label))
            class_in_data = data.loc[indexes, column]
            class_mean = np.mean(class_in_data)
            class_std = np.std(class_in_data)
            class_proportion = len(indexes) / data_length
            numerator = numerator + class_proportion * (class_mean - column_mean) ** 2
            denominator = denominator + class_proportion * class_std ** 2

        if denominator != 0:
            fishers_score_frame.loc[0, column] = numerator / denominator
        else:
            fishers_score_frame.loc[0, column] = 0

    print("Fisher's score(s) has/have been computed.")
    return fishers_score_frame