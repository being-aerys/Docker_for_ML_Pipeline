# Created by Aashish Adhikari at 9:38 AM 7/17/2021

from sklearn import datasets
from sklearn import model_selection
from sklearn import svm
import pickle


iris_data = datasets.load_iris()
X,y = iris_data.data, iris_data.target

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=42, test_size= 0.2)

#assert len(X_train)> len(X_test)

svm_classifier = svm.SVC(gamma="auto")
svm_classifier.fit(X_train, y_train)

accuracy_svm = svm_classifier.score(X_test, y_test)

print("Accuracy of SVM: ", accuracy_svm)

with open("svm_model.pkl", "wb") as svm_model_pickle:
    pickle.dump(svm_classifier, svm_model_pickle)