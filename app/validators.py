def validate_form(data):
    errors = []
    if 'title' not in data or not data['title']:
        errors.append("Form title is required.")
    if 'fields' not in data or not isinstance(data['fields'], list):
        errors.append("Form fields are required and must be a list.")
    return errors

def validate_response(form, data):
    errors = []
    for field in form['fields']:
        if field['required'] and field['name'] not in data['responses']:
            errors.append(f"Field {field['name']} is required.")
    return errors