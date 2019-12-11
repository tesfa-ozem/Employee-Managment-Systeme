from flask import Blueprint, request
from blue.models import *
from blue.utilities import *
from flask import jsonify
from datetime import datetime

from blue.utilities.utilities import *

mod = Blueprint('api', __name__)


@mod.route('/employee', methods=['POST'])
def add_employee():
    try:
        if request.json is not None:
            names = request.json['full_names']
            phone = request.json['phone_number']
            email = request.json['email_address']
            # TODO: Configure date
            date_of_birth = request.json['d.o.b']
            id_no = request.json['identification']

            employee = Employee(names=names, email=email, phone=phone, d_o_b=datetime(2012, 3, 3, 10, 10, 10),
                                identification_no=id_no)
            db.session.add(employee)
            db.session.commit()
            db.session.refresh(employee)
            # print(employee.id)
        return jsonify("SUCCESS"), 201
    except Exception as e:
        return str(e)


@mod.route('/employee', methods=['GET'])
def get_employee():
    try:
        employee_id = request.args.get('id')

        employee = Employee.query.filter_by(id=employee_id).first()
        employee_schema = EmployeeSchema()
        print(employee)
        return employee_schema.dump(employee)
    except Exception as e:
        return str(e)


@mod.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        employees = Employee.query.order_by(Employee.id).all()
        employee_schema = EmployeeSchema(many=True)
        print(employees)
        return jsonify(employee_schema.dump(employees))
    except Exception as e:
        print(e)
        return str(e)


@mod.route('/service', methods=['POST'])
def add_service():
    try:
        if request.json is not None:
            name = request.json['service_name']
            price = request.json['service_price']
            service = Service(name=name, price=price)
            db.session.add(service)
            db.session.commit()
        return jsonify('record added'), 201
    except Exception as e:
        return str(e)


@mod.route('/service', methods=['GET'])
def get_service():
    try:
        service_id = request.args.get('id')
        service = Service.query.filter_by(id=service_id).first()
        service_schema = ServiceSchema()

        return service_schema.dump(service)
    except Exception as e:
        return str(e)


@mod.route('/services', methods=['GET'])
def get_all_services():
    try:
        services = Service.query.all()
        service_schema = ServiceSchema()

        return jsonify(service_schema.dump(services))
    except Exception as e:
        return str(e)


@mod.route('/payment', methods=['POST'])
def make_payment():
    u = Utilities()
    return u.make_payment()
