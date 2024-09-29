from flask import Blueprint, jsonify, request
from app.models import get_form, create_response

responses_blueprint = Blueprint('responses', __name__)

@responses_blueprint.route('/forms/<form_id>/responses', methods=['POST'])
def submit_response(form_id):
    form = get_form(form_id)
    if not form:
        return jsonify({"error": "Form not found"}), 404

    data = request.json
    validation_errors = validate_response(data, form["fields"])
    if validation_errors:
        return jsonify({"error": validation_errors}), 400

    response_id = create_response(form_id, data)
    return jsonify({"message": "Response submitted", "response_id": str(response_id.inserted_id)}), 201
