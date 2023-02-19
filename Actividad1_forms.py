from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField,PasswordField
from wtforms import validators


class UserForm(Form):

    matricula = StringField('Numero',[
        validators.DataRequired(message="El numero es requerido")]
                            )
    numero=StringField('Numero')
