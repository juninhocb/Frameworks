from flask import Blueprint, jsonify, request
from .models import Office
from app.dao.database import db 

api_office_bp = Blueprint('api', __name__)

@api_office_bp.route('/hello')
def hello_world():
    return 'Hello, World!'

@api_office_bp.route('/read', methods=['GET'])
def get_offices():
    offices = Office.query.all()
    return jsonify([office.to_json() for office in offices])

@api_office_bp.route('/read/<int:idParam>', methods=['GET'])
def get_office(idParam):
    office = Office.query.filter(Office.id == idParam).first()
    if (office == None):
        return jsonify({'error': 'Office not found'}), 404 
    return jsonify([office.to_json()])

@api_office_bp.route('/create', methods=['POST'])
def create_office():
    data = request.get_json()
    office = Office(**data)
    db.session.add(office)
    db.session.commit()
    return jsonify(office.to_json())

@api_office_bp.route('/update/<int:idParam>', methods=['PUT'])
def update_office(idParam):
    data = request.get_json()
    office = Office.query.get(idParam)
    if office is None:
        return jsonify({'error': 'Office not found'}), 404
    office.name = data['name']
    db.session.commit()
    return jsonify(office.to_json())

@api_office_bp.route('/delete/<int:idParam>', methods=['DELETE'])
def delete_office(idParam):
    office = Office.query.get(idParam)
    if office is None:
        return jsonify({'error': 'Office not found'}), 404
    db.session.delete(office)
    db.session.commit()
    return jsonify({'message': 'Office deleted'})


