# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

"""
本範例: ML 初學者
相關連結: 
       https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
       https://archive.ics.uci.edu/ml/datasets/Iris
"""

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
data_set = pandas.read_csv(url, names=names)

# shape
print(data_set.shape)
# head
print(data_set.head(20))
# descriptions
print(data_set.describe())
# class distribution
print(data_set.groupby('class').size())

# box and whisker plots
data_set.plot(kind='box', subplots=True, layout=(1, 4), sharex=False, sharey=False)
plt.show()

# histograms
data_set.hist()
plt.show()