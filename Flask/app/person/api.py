from flask import Blueprint, jsonify, request
from .models import Person
from app.dao.database import db

api_person_bp = Blueprint('api', __name__)

@api_person_bp.route('/read', methods=['GET'])
def get_people():
    people = Person.query.all()
    return jsonify([person.to_json() for person in people])

@api_person_bp.route('/read/<int:idParam>', methods=['GET'])
def get_person(idParam):
    person = Person.query.filter(Person.id == idParam).first()
    if (person == None):
        return jsonify({'error': 'Person not found'}), 404
    return jsonify([person.to_json()])

@api_person_bp.route('/create', methods=['POST'])
def create_person():
    data = request.get_json()
    person = Person(**data)
    db.session.add(person)
    db.session.commit()
    return jsonify(person.to_json())

@api_person_bp.route('/update/<int:idParam>', methods=['PUT'])
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


@api_person_bp.route('/delete/<int:idParam>', methods=['DELETE'])
def delete_person(idParam):
    person = Person.query.get(idParam)
    if person is None:
        return jsonify({'error': 'Person not found'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted'})