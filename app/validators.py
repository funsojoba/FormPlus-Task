def validate_form(data):
    errors = []
    if 'title' not in data or not data['title']:
        errors.append("Form title is required.")
    if 'fields' not in data or not isinstance(data['fields'], list):
        errors.append("Form fields are required and must be a list.")
    return errors

# def validate_response(form, data):
#     errors = []
#     for field in form['fields']:
#         if field['required'] and field['name'] not in data['responses']:
#             errors.append(f"Field {field['name']} is required.")
#     return errors


def validate_response(response_data, form_fields):
    errors = []
    for field in form_fields:
        field_name = field["name"]
        if field["is_required"] and field_name not in response_data:
            errors.append(f"{field_name} is required.")
    return errors if errors else None