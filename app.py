from flask import Flask, Response, render_template, jsonify, request
from models import Employee, Field, LocalType, Local, Demand, Journey, db
from schema import EmployeeSchema, FieldSchema, LocalTypeSchema, DemandSchema, JourneySchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://arise:arise@localhost'\
                                        '/hacksaude'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

@app.route('/')
def index():
    return

@app.route('/field/register', methods=['POST'])
def FieldRegister():
    field = request.get_json()
    db.session.add(Field(name=field['name'],description=field['description']))
    db.session.commit()
    return Response(status=200, mimetype='application/json')

@app.route('/employee/register', methods=['POST'])
def EmployeeRegister():
    employee = request.get_json()
    db.session.add(Employee(cpf=employee['cpf'], name=employee['name'],
                            path_image=employee['path_image'], field_employees= \
                            Field.query.filter_by(name=employee['field']).first()
                            ))
    db.session.commit()
    return Response(status=200, mimetype='application/json')

@app.route('/localtype/register', methods=['POST'])
def LocaltypeRegister():
    localtype = request.get_json()
    db.session.add(LocalType(type=localtype['type'], tag=localtype['tag']))
    db.session.commit()
    return Response(status=200, mimetype='application/json')

@app.route('/local/register', methods=['POST'])
def LocalRegister():
    local = request.get_json()
    db.session.add(Local(latitude=local['latitude'], longitude=local['longitude'],
                            name=local['name'], address=local['address'], phone=local['phone'],
                            local_type=LocalType.query.filter_by(type=local['tipo']).first()))
    db.session.commit()
    return Response(status=200, mimetype='application/json')


with app.app_context():
	db.create_all()
