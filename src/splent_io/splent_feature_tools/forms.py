from flask_wtf import FlaskForm
from wtforms import SubmitField


class SplentFeatureToolsForm(FlaskForm):
    submit = SubmitField("Save splent_feature_tools")
