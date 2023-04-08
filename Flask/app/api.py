from flask import Blueprint, jsonify, request
from .models import *

api_bp = Blueprint('api', __name__)

@api_bp.route('/hello')
def hello_world():
    return 'Hello, World!'

@api_bp.route('/offices', methods=['GET'])
def get_offices():
    offices = Office.query.all()
    return jsonify([office.to_json() for office in offices])

@api_bp.route('/office/<int:idParam>', methods=['GET'])
def get_office(idParam):
    office = Office.query.filter(Office.id == idParam).first()
    return jsonify([office.to_json()])

@api_bp.route('/office', methods=['POST'])
def create_office():
    data = request.get_json()
    office = Office(**data)
    db.session.add(office)
    db.session.commit()
    return jsonify(office.to_json())

@api_bp.route('/office/<int:idParam>', methods=['PUT'])
def update_office(idParam):
    data = request.get_json()
    office = Office.query.get(idParam)
    if office is None:
        return jsonify({'error': 'Office not found'}), 404
    office.name = data['name']
    db.session.commit()
    return jsonify(office.to_json())

@api_bp.route('/office/<int:idParam>', methods=['DELETE'])
def delete_office(idParam):
    office = Office.query.get(idParam)
    if office is None:
        return jsonify({'error': 'Office not found'}), 404
    db.session.delete(office)
    db.session.commit()
    return jsonify({'message': 'Office deleted'})

@api_bp.route('/people', methods=['GET'])
def get_people():
    people = Person.query.all()
    return jsonify([person.to_json() for person in people])

@api_bp.route('/person/<int:idParam>', methods=['GET'])
def get_person(idParam):
    person = Person.query.filter(Person.id == idParam).first()
    return jsonify([person.to_json()])

@api_bp.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    person = Person(**data)
    db.session.add(person)
    db.session.commit()
    print("testee ae")
    return jsonify(person.to_json())

@api_bp.route('/person/<int:idParam>', methods=['PUT'])
def update_person(idParam):
    data = request.get_json()
    person = Person.query.get(idParam)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    person.name = data['name']
    person.age = data['age']
    person.is_retired = data['is_retired']
    person.nationality = data['nationality']
    person.id_office = data['id_office']
    db.session.commit()
    return jsonify(person.to_json())


@api_bp.route('/person/<int:idParam>', methods=['DELETE'])
def delete_person(idParam):
    person = Person.query.get(idParam)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted'})
