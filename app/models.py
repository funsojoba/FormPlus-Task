from flask_pymongo import PyMongo

mongo = PyMongo()

class Form:
    def __init__(self, title, description, fields, created_by, date_created):
        self.title = title
        self.description = description
        self.fields = fields
        self.created_by = created_by
        self.date_created = date_created
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "fields": self.fields,
            "created_by": self.created_by,
            "date_created": self.date_created
        }

class Response:
    def __init__(self, form_id, user_id, responses, date_submitted):
        self.form_id = form_id
        self.user_id = user_id
        self.responses = responses
        self.date_submitted = date_submitted
    
    def to_dict(self):
        return {
            "form_id": self.form_id,
            "user_id": self.user_id,
            "responses": self.responses,
            "date_submitted": self.date_submitted
        }
