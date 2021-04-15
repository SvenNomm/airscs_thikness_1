# this code wraps the plotting procedure for 3D scatter plot
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder
from more_itertools import locate


def scatter_wrapper_3D(large_data_sample, large_labels_set, first_three_columns):
    list_of_classes = []
    for label in large_labels_set:
        if label not in list_of_classes:
            list_of_classes.append(label)
    label_encoder = LabelEncoder()
    label_encoder.fit(list_of_classes)
    encoded_labels = label_encoder.transform(list_of_classes)
    large_labels_set_encoded = label_encoder.transform(large_labels_set)

    large_label_set_colored = mpl.cm.Set1(large_labels_set_encoded)
    figure_1 = plt.figure()
    ax = figure_1.add_subplot(111, projection='3d')
    for class_label in list_of_classes:
        indexes = list(locate(large_labels_set, lambda x: x == class_label))
        class_in_data = large_data_sample.loc[indexes, :]
        ax.scatter(large_data_sample.loc[indexes, first_three_columns[0]], large_data_sample.loc[indexes,
                                                                                             first_three_columns[1]],
        large_data_sample.loc[indexes, first_three_columns[2]], marker='o', s=15,
        c=large_label_set_colored[indexes], edgecolors=large_label_set_colored[indexes], label=class_label,
               alpha=0.99)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))
    figure_1.suptitle('Benign traffic: three "best" features')
    ax.set_xlabel(first_three_columns[0])
    ax.set_ylabel(first_three_columns[1])
    ax.set_zlabel(first_three_columns[2])
    plt.show()

    path_to_results = "/Users/sven/data/IoT_Israeli_processed/"
    ffname = path_to_results + list_of_classes[0]+'against_complement.png'
    figure_1.savefig(ffname)
    print("function: scatter_wrapper_3D: That's all folks!!!")