# -*- coding: utf-8 -*-

"""

    coin.app.form.signin_form
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/17/16

"""

from flask_wtf import Form
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, Length, DataRequired


class SignInForm(Form):

    email = StringField("Email", validators=[Email(), Length(1, 64), DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])

    remember = BooleanField("Remember me")

    submit = SubmitField("Sign In")
