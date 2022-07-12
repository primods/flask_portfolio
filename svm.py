from sklearn.svm import SVC
import numpy as np
import pickle
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt

svm_model = pickle.load(open("svm_hepatitis.sav","rb"))
pca_param = pickle.load(open("pca_param.sav","rb"))
normalizer = pickle.load(open("normalizer.sav","rb"))
xpoints, ypoints = pickle.load(open("xpoints.sav","rb"))

class SVModel():
    def __init__(self,xdata):
        self.x = normalizer().transform(xdata)
        self.pca = ""
        self.y = ""
        self.category = ""
    def predict(self):
        self.pca = pca_param.transform(self.x)
        self.y = svm_model.predict(self.pca)
    def categorize(self):
      if self.y == 2:
        self.category = "Hepatitis"
      else:
        self.category = "Not Hepatitis"
    def plot(self):
        plt.figure()
        ax = plot_decision_regions(xpoints, ypoints, clf=svm_model, legend=1,colors="red,cyan")
        handles, labels = ax.get_legend_handles_labels()
        ay = plt.scatter(self.pca[0][0],self.pca[0][1], c="blue", marker="x", s=50, label="your point")
        ax.legend(handles, ['Disease', 'Healthy'], 
        framealpha=0.3, scatterpoints=1)
        plt.xlim(-0.75, 1)
        plt.ylim(-1, 1.5)
        plt.savefig("static\datasvm.png")