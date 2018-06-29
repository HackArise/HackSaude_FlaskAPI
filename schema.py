from flask_marshmallow import Marshmallow
from models import Employee, Field, LocalType, Local, Demand, Journey
from marshmallow import fields

ma = Marshmallow()

class LocalTypeSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    type = fields.Str()
    tag = fields.Str()

class FieldSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str()
    name = fields.Str()

class EmployeeSchema(ma.Schema):
    cpf = fields.Int(dump_only=True)
    name = fields.Str()
    path_image = fields.Str()
    field_id = fields.Nested(FieldSchema)

class LocalSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    latitude = fields.Str()
    longitude = fields.Str()
    name = fields.Str()
    address = fields.Str()
    phone = fields.Str()
    local_type_id = fields.Nested(LocalTypeSchema)

class DemandSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    field_id = fields.Nested(FieldSchema)
    local_id = fields.Nested(LocalSchema)

class JourneySchema(ma.Schema):
    id = fields.Int(dump_only=True)
    begin = fields.Str()
    end = fields.Str()
    employee_cpf = fields.Nested(EmployeeSchema)
    local_id = fields.Nested(LocalSchema)
