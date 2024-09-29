# app/forms.py
from flask import Blueprint, jsonify, request
from app.models import create_form, get_form, update_form, delete_form

forms_blueprint = Blueprint('forms', __name__)

@forms_blueprint.route('/forms', methods=['POST'])
def create_new_form():
    data = request.json
    form_id = create_form(data)
    return jsonify({"message": "Form created", "form_id": str(form_id.inserted_id)}), 201

@forms_blueprint.route('/forms/<form_id>', methods=['GET'])
def get_existing_form(form_id):
    form = get_form(form_id)
    if not form:
        return jsonify({"error": "Form not found"}), 404
    return jsonify(form), 200

@forms_blueprint.route('/forms/<form_id>', methods=['PUT'])
def update_existing_form(form_id):
    data = request.json
    updated = update_form(form_id, data)
    return jsonify({"message": "Form updated"}), 200

@forms_blueprint.route('/forms/<form_id>', methods=['DELETE'])
def delete_existing_form(form_id):
    delete_form(form_id)
    return jsonify({"message": "Form deleted"}), 204
