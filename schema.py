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

class DemandSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    fields = fields.Nested(FieldSchema, attribute='field_demands', only=['name'])
    # local_id = fields.Nested(LocalSchema)

class LocalSchema(ma.Schema):
    name = fields.Str()
    address = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()
    phone = fields.Str()
    local_type = fields.Nested(LocalTypeSchema, attribute='local_type', only=['type','tag'])
    demands = fields.Nested(DemandSchema, many=True, only=['fields'])

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
