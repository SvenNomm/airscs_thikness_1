# this file contains wrappers for differnt classifiers.


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier

def classifier_wrapper_1(data_set, labels):
    classifiers = ['KNeighborsClassifier', 'DecisionTreeClassifier',
                   'RandomForestClassifier','LogisticRegression','LinearSVC', 'AdaBoostClassifier']   # 'LogisticRegression', ,  'LinearSVC' 'AdaBoostClassifier'
    train_set, test_set, train_labels, test_labels = train_test_split(data_set, labels, test_size=0.3)
    for classifier_name in classifiers:
        cl_name = classifier_name + "()"
        classifier = eval(classifier_name + "()")
        #classifier.fit(train_set, train_labels)
        accuracy = cross_val_score(classifier, train_set, train_labels,  cv=5, scoring='accuracy')
        recall = cross_val_score(classifier, train_set, train_labels,  cv=5, scoring='recall_micro')
        precision = cross_val_score(classifier, train_set, train_labels,  cv=5, scoring='precision_macro')
        f1_score = cross_val_score(classifier, train_set, train_labels,  cv=5, scoring='f1_macro')
        print(classifier_name, " : accuracy: ", accuracy, " ; recall: ", recall, " ; precision: ", precision, " ; f1_score:", f1_score)

    # semarately for the MLPClassifier
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes = (5, 5), random_state = 1)
    #clf.fit(train_set, train_labels)
    accuracy = cross_val_score(clf, train_set, train_labels, cv=5, scoring='accuracy')
    recall = cross_val_score(clf, train_set, train_labels, cv=5, scoring='recall_micro')
    precision = cross_val_score(clf, train_set, train_labels, cv=5, scoring='precision_macro')
    f1_score = cross_val_score(clf, train_set, train_labels, cv=5, scoring='f1_macro')
    print("MLPCassifier", " : accuracy: ", accuracy, " ; recall: ", recall, " ; precision: ", precision,
          " ; f1_score:", f1_score)

