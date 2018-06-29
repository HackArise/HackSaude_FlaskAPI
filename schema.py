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
    name = fields.Str()
    description = fields.Str()
    # employees = fields.Nested(EmployeeSchema, Many=True)
    # demands = fields.Nested(DemandSchema, Many=True)

class LocalSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    latitude = fields.Str()
    longitude = fields.Str()
    name = fields.Str()
    address = fields.Str()
    phone = fields.Str()
    # local_type_id = fields.Nested(LocalTypeSchema)

class JourneySchema(ma.Schema):
    id = fields.Int(dump_only=True)
    begin = fields.Str()
    end = fields.Str()
    local = fields.Nested(FieldSchema, attribute='local_journeys', only=['name'])

class EmployeeSchema(ma.Schema):
    name = fields.Str()
    cpf = fields.Int()
    path_image = fields.Str()
    field = fields.Nested(FieldSchema, attribute='field_employees', only=['name','description'])
    journeys = fields.Nested(JourneySchema, many=True, only=['begin', 'end', 'local' ])

class DemandSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    field_id = fields.Nested(FieldSchema)
    local_id = fields.Nested(LocalSchema)
