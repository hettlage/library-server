import uuid

import forgery_py
from flask import url_for

from app import db
from app.exceptions import ValidationError


class Keyword(db.Model):
    __tablename__ = 'Keywords'
    uuid = db.Column(db.String(128), unique=True, nullable=False, primary_key=True)
    keyword = db.Column(db.String(256), nullable=False)

    def __init__(self):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())

    def get_url(self):
        return url_for('api.get_keyword', uuid=self.uuid, _external=True)

    def export_data(self):
        return dict(keyword=self.keyword)

    def import_data(self, data):
        try:
            if not self.uuid or 'keyword' in data:
                self.keyword = data['keyword']
        except KeyError as e:
            raise ValidationError('Invalid Keyword: missing {key}'.format(key=e.args[0]))

    @staticmethod
    def generate_fake(count):
        for _ in range(count):
            keyword = Keyword()
            keyword.keyword = forgery_py.lorem_ipsum.words(2)
            db.session.add(keyword)
        db.session.commit()

    def __repr__(self):
        return '<Keyword {keyword}>'.format(keyword=self.keyword)


class Librarian(db.Model):
    __tablename__ = 'Librarians'
    uuid = db.Column(db.String(128), unique=True, nullable=False, primary_key=True)
    given_name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())

    def get_url(self):
        return url_for('api.get_librarian', uuid=self.uuid, _external=True)

    def export_data(self):
        return dict(given_name=self.given_name,
                    surname=self.surname,
                    email=self.email)

    def import_data(self, data):
        try:
            if not self.uuid or 'given_name' in data:
                self.given_name = data['given_name']
            if not self.uuid or 'surname' in data:
                self.surname = data['surname']
            if not self.uuid or 'email' in data:
                self.email = data['email']
        except KeyError as e:
            raise ValidationError('Invalid librarian: missing {key}'.format(key=e.args[0]))

    @staticmethod
    def generate_fake(count):
        for _ in range(count):
            librarian = Librarian()
            librarian.given_name = forgery_py.name.first_name()
            librarian.surname = forgery_py.name.last_name()
            librarian.email = forgery_py.internet.email_address()
            db.session.add(librarian)
        db.session.commit()

    def __repr__(self):
        return "<Librarian {given_name} {surname}>".format(given_name=self.given_name, surname=self.surname)


class Astronomer(db.Model):
    __tablename__ = 'Astronomers'
    uuid = db.Column(db.String(128), unique=True, nullable=False, primary_key=True)
    given_name = db.Column(db.String(128), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self):
        if not self.uuid:
            self.uuid = str(uuid.uuid4())

    def get_url(self):
        return url_for('api.get_astronomer', uuid=self.uuid, _external=True)

    def export_data(self):
        return dict(given_name=self.given_name,
                    surname=self.surname,
                    email=self.email)

    def import_data(self, data):
        try:
            if not self.uuid or 'given_name' in data:
                self.given_name = data['given_name']
            if not self.uuid or 'surname' in data:
                self.surname = data['surname']
            if not self.uuid or 'email' in data:
                self.email = data['email']
        except KeyError as e:
            raise ValidationError('Invalid librarian: missing {key}'.format(key=e.args[0]))

    @staticmethod
    def generate_fake(count):
        for _ in range(count):
            astronomer = Astronomer()
            astronomer.given_name = forgery_py.name.first_name()
            astronomer.surname = forgery_py.name.last_name()
            astronomer.email = forgery_py.internet.email_address()
            db.session.add(astronomer)
        db.session.commit()

    def __repr__(self):
        return "<Astronomer {given_name} {surname}>".format(given_name=self.given_name, surname=self.surname)

