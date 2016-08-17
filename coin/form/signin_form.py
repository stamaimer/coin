# -*- coding: utf-8 -*-

"""

    coin.form.signin_form
    ~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/17/16

"""

from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, Length, Required
from coin.form import Form

class SignInForm(Form):

    email = StringField("Email", validators=[Email(), Length(1, 64), Required()])

    password = PasswordField("Password", validators=[Required()])

    remember = BooleanField("Remember me")

    submit = SubmitField("Sign In")
