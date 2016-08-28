# -*- coding: utf-8 -*-

"""

    coin.app.form.registration_form
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/28/16
    
"""

from flask_wtf import Form
from wtforms import widgets, FormField, SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class MailingAddressForm(Form):

    organization = StringField("Organization:", [DataRequired()])

    address1 = StringField("Address1:", [DataRequired()])

    address2 = StringField("Address2:")

    city = StringField("City:", [DataRequired()])

    state = SelectField("State:", choices=[("test", "test")])

    zip_code = StringField("Zip/Postal Code:", [DataRequired()])

    country = SelectField("Country:", choices=[("test", "test")])


class PrimaryInterestsForm(Form):

    health_research_topic = SelectMultipleField("Health Research Topic",
                                                choices=[("Clinical outcomes", "Clinical outcomes"),
                                                         ("Economic evaluation", "Economic evaluation"),
                                                         ("Health policy & systems", "Health policy & systems"),
                                                         ("Health technology assessment", "Health technology assessment"),
                                                         ("Patient-centered Outcomes(PRO/QOL)", "Patient-centered Outcomes(PRO/QOL)"),
                                                         ("Personalized medicine", "Personalized medicine"),
                                                         ("Population health", "Population health"),
                                                         ("Other", "Other")],
                                                option_widget=widgets.CheckboxInput(),
                                                widget=widgets.ListWidget(prefix_label=0))

    health_research_method = SelectMultipleField("Health Research Method",
                                                 choices=[("Comparative methods", "Comparative methods"),
                                                          ("Database methods", "Database methods"),
                                                          ("Modeling methods", "Modeling methods"),
                                                          ("Observational methods", "Observational methods"),
                                                          ("Preference-based methods(including medication adherence)", "Preference-based methods(including medication adherence)"),
                                                          ("Statistical methods", "Statistical methods")],
                                                 option_widget=widgets.CheckboxInput(),
                                                 widget=widgets.ListWidget(prefix_label=0))


class RegistrationForm(Form):

    first_name = StringField("First Name:", [DataRequired()])

    last_name = StringField("Last Name:", [DataRequired()])

    degrees = SelectMultipleField("Degrees", choices=[("None", "None"), ("BA", "BA"), ("BEc", "BEc"), ("BS", "BS"),
                                                      ("BSc", "BSc"), ("DPhil", "DPhil"), ("DrPH", "DrPH"),
                                                      ("EdD", "EdD"), ("JD", "JD"), ("MA", "MA"), ("MASc", "MASc"),
                                                      ("MBA", "MBA"), ("MCom", "MCom"), ("MD", "MD"), ("MEd", "MEd"),
                                                      ("MFE", "MFE"), ("MHA", "MHA"), ("MPH", "MPH"), ("Mphil", "Mphil"),
                                                      ("MPP", "MPP"), ("MS", "MS"), ("MSc", "MSc"), ("MSPH", "MSPH"),
                                                      ("PharmD", "PharmD"), ("PhD", "PhD"), ("RN", "RN"), ("RPh", "RPh"),
                                                      ("ScD", "ScD")],
                                  option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=0))

    other_degrees = StringField("Other Degrees:")

    position = StringField("Position:")

    mailing_address = FormField(MailingAddressForm)

    work_phone = StringField("Work Phone:", [DataRequired()])

    fax = StringField("Fax:", [DataRequired()])

    email = StringField("Email:", [DataRequired(), Email()])

    alternate_email = StringField("Alternate Email:", [Email()])

    work_environment = SelectField("Work Environment:", [DataRequired()],
                                   choices=[("Academia", "Academia"),
                                            ("Health Research/Consulting", "Health Research/Consulting"),
                                            ("Industry/Pharmacentical/Medical Device/Diagnostic",
                                             "Industry/Pharmacentical/Medical Device/Diagnostic")])

    primary_interests = FormField(PrimaryInterestsForm)

    submit = SubmitField("Submit")



