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

    organization = StringField(u"企业／学术组织名称:", [DataRequired()])

    address1 = StringField(u"地址栏1:", [DataRequired()])

    address2 = StringField(u"地址栏2:")

    city = StringField(u"城市:", [DataRequired()])

    state = SelectField(u"省:", choices=[("test", "test")])

    zip_code = StringField(u"邮政编码:", [DataRequired()])


class PrimaryInterestsForm(Form):

    health_research_topic = SelectMultipleField(u"卫生研究主题",
                                                choices=[(u"临床效果", u"临床效果"), (u"经济学评价", u"经济学评价"),
                                                         (u"卫生政策和卫生系统", u"卫生政策和卫生系统"),
                                                         (u"卫生技术评估", u"卫生技术评估"), (u"人群健康", u"人群健康"),
                                                         (u"其他", u"其他")],
                                                option_widget=widgets.CheckboxInput(),
                                                widget=widgets.ListWidget(prefix_label=0))

    health_research_method = SelectMultipleField(u"卫生研究方法学",
                                                 choices=[(u"比较方法", u"比较方法"), (u"数据库方法", u"数据库方法"),
                                                          (u"模型方法", u"模型方法"), (u"观察法", u"观察法"), (u"统计学方法", u"统计学方法")],
                                                 option_widget=widgets.CheckboxInput(),
                                                 widget=widgets.ListWidget(prefix_label=0))


class RegistrationForm(Form):

    first_name = StringField(u"名:", [DataRequired()])

    last_name = StringField(u"姓:", [DataRequired()])

    degrees = SelectMultipleField(u"学历", choices=[("None", "None"), ("BA", "BA"), ("BEc", "BEc"), ("BS", "BS"),
                                                      ("BSc", "BSc"), ("DPhil", "DPhil"), ("DrPH", "DrPH"),
                                                      ("EdD", "EdD"), ("JD", "JD"), ("MA", "MA"), ("MASc", "MASc"),
                                                      ("MBA", "MBA"), ("MCom", "MCom"), ("MD", "MD"), ("MEd", "MEd"),
                                                      ("MFE", "MFE"), ("MHA", "MHA"), ("MPH", "MPH"), ("Mphil", "Mphil"),
                                                      ("MPP", "MPP"), ("MS", "MS"), ("MSc", "MSc"), ("MSPH", "MSPH"),
                                                      ("PharmD", "PharmD"), ("PhD", "PhD"), ("RN", "RN"), ("RPh", "RPh"),
                                                      ("ScD", "ScD")],
                                  option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=0))

    other_degrees = StringField(u"其他学历:")

    position = StringField(u"职位:")

    mailing_address = FormField(MailingAddressForm)

    work_phone = StringField(u"电话:", [DataRequired()])

    fax = StringField(u"传真:", [DataRequired()])

    email = StringField(u"邮箱:", [DataRequired(), Email()])

    alternate_email = StringField(u"备用邮箱:", [Email()])

    work_environment = SelectField(u"工作环境:", [DataRequired()],
                                   choices=[(u"学术机构", u"学术机构"),
                                            (u"卫生咨询公司", u"卫生咨询公司"),
                                            (u"药物、器械、药品、诊断企业",
                                             u"药物、器械、药品、诊断企业")])

    primary_interests = FormField(PrimaryInterestsForm)

    submit = SubmitField(u"提交")



