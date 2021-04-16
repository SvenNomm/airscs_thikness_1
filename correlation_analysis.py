# this  file contains the functions necessary to compute correlations between the variables and if necessary plot the results

import pandas as pd
import numpy as np


def correlation_analysis(data, dependent_var):

    column_names = data.columns.values
    correlations_frame = pd.DataFrame(columns=column_names, dtype="float64")

    number_of_variables = len(column_names)
    #colinearity_matrix = np.zeros((number_of_variables, number_of_variables))
    collinearity_frame = pd.DataFrame(index=pd.Index(column_names), columns=pd.Index(column_names), dtype="float64")

    for column_name in column_names:
        r = np.corrcoef(data[column_name], dependent_var)
        correlations_frame.loc[0, column_name] = r[0, 1]
        for column in column_names:
            a = data[column_name]
            b = data[column]
            r = np.corrcoef(data[column_name],data[column])
            collinearity_frame.loc[column_name, column] = r[0, 1]

    return collinearity_frame, correlations_frame


