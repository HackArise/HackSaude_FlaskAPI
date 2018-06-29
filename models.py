from sqlalchemy import DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__='Employee'
    #FIELDS#
    cpf = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80))
    path_image = db.Column(db.String(80))
    field_id = db.Column(db.Integer, db.ForeignKey('Field.id'))
    #RELATIONS#
    journeys = db.relationship('Journey', backref='employees', lazy=True)

class Field(db.Model):
    __tablename__='Field'
    #FIELDS#
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(140))
    #RELATIONS#
    employees = db.relationship('Employee', backref='field_employees', lazy=True)
    demands = db.relationship('Demand', backref='field_demands', lazy=True)

class Demand(db.Model):
    __tablename__='Demand'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    field_id = db.Column(db.Integer, db.ForeignKey('Field.id'))
    local_id = db.Column(db.Integer, db.ForeignKey('Local.id'))

class Local(db.Model):
    __tablename__='Local'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    latitude = db.Column(db.String(80))
    longitude = db.Column(db.String(80))
    name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    phone = db.Column(db.String(80))
    local_type_id = db.Column(db.Integer, db.ForeignKey('LocalType.id'))
    #RELATIONS#
    journeys = db.relationship('Journey', backref='local_journeys', lazy=True)
    demands = db.relationship('Demand', backref='local_demands', lazy=True)

class LocalType(db.Model):
    __tablename__='LocalType'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    type = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    #RELATIONS#
    locals = db.relationship('Local', backref='local_type', lazy=True)

class Journey(db.Model):
    __tablename__='Journey'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    begin = db.Column(db.String(80))
    end = db.Column(db.String(80))
    employee_cpf = db.Column(db.BigInteger, db.ForeignKey('Employee.cpf'))
    local_id = db.Column(db.Integer, db.ForeignKey('Local.id'))
