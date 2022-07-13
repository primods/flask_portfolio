from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import numpy as np
from lr import LRModel 
from svm import SVModel
from forms import *

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = "super_secret_key"
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = "slate"


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/linear')
def linear():
    return render_template("linear.html")

@app.route("/lineardemo", methods=["GET", "POST"])
def linear_demo():
    x_val = []
    y_val = []
    if request.form:
        x_val.append(request.form["xdata"])
        y_val.append(request.form["ydata"])
        valid = None
        params = None
        try:
            model_lr = LRModel([float(i) for i in x_val[0].split(",")],[float(j) for j in y_val[0].split(",")])
            model_lr.add_const()
            model_lr.fit_data()
            params = model_lr.fit_data()
            model_lr.plot_data()
            valid = True
        except ValueError:
            valid = False
            params = [0]
        return render_template("simplelr.html",params=params, valid=valid)
    return render_template("lineardemo.html", template_form=LinearDataForm())


@app.route("/svm")
def svm():
    return render_template("svm.html")

@app.route("/svmdemo", methods=["GET", "POST"])
def svmdemo():
    if request.form:
        datasvm = np.array([float(request.form["CHL"]),float(request.form["CHE"]),float(request.form["ALB"]),float(request.form["ALP"]),float(request.form["PRO"]),float(request.form["AST"]),float(request.form["BIL"]),float(request.form["Age"])]).reshape(1,8)
        svm = SVModel(datasvm)
        svm.predict()
        svm.categorize()
        category = svm.category
        svm.plot()
        return render_template("svmdemoresults.html",params=datasvm, category=category)
    return render_template("svmdemo.html",template_form=SVMDataForm())

@app.route("/neuralnet")
def neuralnet():
    return render_template("simpleneuralnet.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/favicon.ico')
def fav():
    return app.send_static_file('favicon.ico')