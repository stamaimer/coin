# -*- coding: utf-8 -*-

"""

    coin.app.model.registration
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/29/16

"""


from app.model import db


class Registration(db.Model):

    __tablename__ = "registration"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(255))

    last_name = db.Column(db.String(255))

    degrees = db.Column(db.String(255))

    other_degrees = db.Column(db.String(255))

    position = db.Column(db.String(255))

    organization = db.Column(db.String(255))

    address1 = db.Column(db.String(255))

    address2 = db.Column(db.String(255))

    city = db.Column(db.String(255))

    state = db.Column(db.String(255))

    zip_code = db.Column(db.String(255))

    work_phone = db.Column(db.String(255))

    fax = db.Column(db.String(255))

    email = db.Column(db.String(255))

    alternate_email = db.Column(db.String(255))

    work_environment = db.Column(db.String(255))

    health_research_topic = db.Column(db.String(255))

    health_research_method = db.Column(db.String(255))

    def __init__(self, first_name, last_name, degrees, other_degrees, position, organization, address1, address2, city,
                 state, zip_code, country, work_phone, fax, email, alternate_email, work_environment,
                 health_research_topic, health_research_method):

        self.first_name = first_name
        self.last_name = last_name
        self.degrees = degrees
        self.other_degrees = other_degrees
        self.position = position
        self.organization = organization
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.alternate_email = alternate_email
        self.work_environment = work_environment
        self.health_research_topic=health_research_topic
        self.health_research_method=health_research_method
