from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, validators

class LinearDataForm(FlaskForm):
    xdata = StringField("X values",[validators.DataRequired(), validators.Length(min=3,message="More than one value required")])
    ydata = StringField("Y values",[validators.DataRequired(), validators.Length(min=3,message="More than one value required")])
    submit = SubmitField("Make the model!")

class SVMDataForm(FlaskForm):
    CHL = FloatField("Cholesterol",[validators.DataRequired(), validators.Length(min=1)])
    CHE = FloatField("Serum Cholinesterase",[validators.DataRequired(), validators.Length(min=1)])
    ALB = FloatField("Serum Albumin",[validators.DataRequired(), validators.Length(min=1)])
    ALP = FloatField("Alkaline Phosphatase",[validators.DataRequired(), validators.Length(min=1)])
    PRO = FloatField("Total Protein",[validators.DataRequired(), validators.Length(min=1)])
    AST = FloatField("Aspartate aminotransferase/AST",[validators.DataRequired(), validators.Length(min=1)])
    BIL = FloatField("Bilirubin",[validators.DataRequired(), validators.Length(min=1)])
    Age = IntegerField("Age",[validators.DataRequired(), validators.Length(min=1)])
    submit = SubmitField("Predict!") 