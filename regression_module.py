# this file contains functions wrapping regression analysis

import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from math import sqrt


def regression_wrapper(data, dep_var, features):
    models = ['DecisionTreeRegressor',
                   'ElasticNet', 'Lasso', 'Ridge', 'LinearRegression', 'KNeighborsRegressor']

    #X_train, X_test, y_train, y_test = train_test_split(data, dep_var, test_size=0.30, random_state=40)

    for model in models:
        print("________________________________________________________________________")
        print("________________________________________________________________________")
        print("________________________________________________________________________")
        for i in range(0, 5):
            print("Fold", i, "------------------------")
            X_train, X_test, y_train, y_test = train_test_split(data, dep_var, test_size=0.30)

            if model == 'DecisionTreeRegressor':
                model_name = eval(model + "(max_depth=8, min_samples_leaf=0.13, random_state=3)")
            else:
                model_name = eval(model + "()")

            model_name.fit(X_train[features], y_train)
            predict= model_name.predict(X_test[features])
            predict_train = model_name.predict(X_train[features])
            print("Model: ", model_name, " mean square error:", np.sqrt(mean_squared_error(y_test, predict)))
            print("Model: ", model_name, " mean square error:", np.sqrt(mean_squared_error(y_train, predict_train)))
            print("Model: ", model_name, " determination coefficients: ", r2_score(y_train, predict_train))

    return X_test, X_train, y_test,  y_train, predict, predict_train
