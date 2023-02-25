from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField, TextAreaField,PasswordField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')


class UserForm(Form):

    matricula = StringField('Matricula',[
        validators.DataRequired(message="La matricula es requerida")]
                            )
    nombre = StringField('Nombre',[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=5,max=15,message="Ingresa un valor maximo")]
                            )
    
    apaterno=StringField('Apaterno',[mi_validacion])
    amaterno=StringField('Amaterno')
    email=EmailField('Email')

class LoginForm(Form):
    
    username = StringField('usuario',[
        validators.DataRequired(message="La usuario es requerido")]
                            )
    password = PasswordField('contraseña',[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=5,max=15,message="Ingresa un valor maximo")]
                            )