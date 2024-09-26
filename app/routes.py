from flask import Flask, jsonify, request
from app.models import mongo, Form, Response
from app.validators import validate_form, validate_response
from app.analytics import get_form_responses_count
from datetime import datetime

app = Flask(__name__)

# Endpoint to create a form
@app.route('/forms', methods=['POST'])
def create_form():
    data = request.json
    errors = validate_form(data)
    if errors:
        return jsonify({"error": errors}), 400

    form = Form(
        title=data['title'],
        description=data['description'],
        fields=data['fields'],
        created_by=data['created_by'],
        date_created=datetime.utcnow()
    )
    mongo.db.forms.insert_one(form.to_dict())
    return jsonify({"message": "Form created successfully!"}), 201

# Retrieve form by ID
@app.route('/forms/<form_id>', methods=['GET'])
def get_form(form_id):
    form = mongo.db.forms.find_one({"_id": form_id})
    if form:
        return jsonify(form), 200
    return jsonify({"error": "Form not found!"}), 404

# Submit a response to a form
@app.route('/forms/<form_id>/responses', methods=['POST'])
def submit_response(form_id):
    form = mongo.db.forms.find_one({"_id": form_id})
    if not form:
        return jsonify({"error": "Form not found!"}), 404

    data = request.json
    errors = validate_response(form, data)
    if errors:
        return jsonify({"error": errors}), 400

    response = Response(
        form_id=form_id,
        user_id=data['user_id'],
        responses=data['responses'],
        date_submitted=datetime.utcnow()
    )
    mongo.db.responses.insert_one(response.to_dict())
    return jsonify({"message": "Response submitted successfully!"}), 201

# Delete a form
@app.route('/forms/<form_id>', methods=['DELETE'])
def delete_form(form_id):
    result = mongo.db.forms.delete_one({"_id": form_id})
    if result.deleted_count == 1:
        return jsonify({"message": "Form deleted successfully!"}), 200
    return jsonify({"error": "Form not found!"}), 404

# Update a form
@app.route('/forms/<form_id>', methods=['PUT'])
def update_form(form_id):
    form = mongo.db.forms.find_one({"_id": form_id})
    if not form:
        return jsonify({"error": "Form not found!"}), 404

    data = request.json
    mongo.db.forms.update_one({"_id": form_id}, {"$set": data})
    return jsonify({"message": "Form updated successfully!"}), 200

# Analytics endpoint (optional)
@app.route('/forms/<form_id>/analytics', methods=['GET'])
def form_analytics(form_id):
    count = get_form_responses_count(form_id)
    return jsonify({"response_count": count}), 200
