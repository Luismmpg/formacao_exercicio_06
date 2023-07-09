from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RespostaForm(FlaskForm):
    resposta = StringField("Resposta:")
    submit = SubmitField("Submeter")
