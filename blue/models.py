from datetime import datetime
from blue import db
from blue import ma


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(64))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(10))
    d_o_b = db.Column(db.DateTime, default=datetime.utcnow())
    identification_no = db.Column(db.String(15))
    appointments_id = db.Column(db.Integer, db.ForeignKey("appointments.id"))
    appointment = db.relationship("Appointments")
    sale_id = db.Column(db.Integer, db.ForeignKey("sale.id"))
    sale = db.relationship("Sale")


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.String())
    appointments_id = db.Column(db.Integer, db.ForeignKey("appointments.id"))
    appointment = db.relationship("Appointments")
    sale_id = db.Column(db.Integer, db.ForeignKey("sale.id"))


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(64))
    email = db.Column(db.String())
    phone = db.Column(db.String())
    appointments_id = db.Column(db.Integer, db.ForeignKey("appointments.id"))
    appointment = db.relationship("Appointments")
    sale_id = db.Column(db.Integer, db.ForeignKey("sale.id"))
    sale = db.relationship("Sale")


class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.String())
    client = db.relationship("Client", uselist=False)
    service = db.relationship("Service", uselist=False)
    employee = db.relationship("Employee", uselist=False)


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    amount_paid = db.Column(db.String())
    balance = db.Column(db.String)
    employee_com = db.Column(db.String())
    payment_mode = db.Column(db.String())
    service = db.relationship("Service")
    employee = db.relationship("Employee", uselist=False)
    client = db.relationship("Client", uselist=False)


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee


class ServiceSchema(ma.ModelSchema):
    class Meta:
        model = Service


class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client


class AppointmentsSchema(ma.ModelSchema):
    class Meta:
        model = Appointments


class SaleSchema(ma.ModelSchema):
    class Meta:
        model = Sale
