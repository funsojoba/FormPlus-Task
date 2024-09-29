from flask import Flask, redirect, url_for
from flask_pymongo import PyMongo
from config import Config
from flask_swagger_ui import get_swaggerui_blueprint

mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Configure MongoDB
    app.config["MONGO_URI"] = Config.MONGO_URI
    mongo.init_app(app)
    
    
    # Swagger settings
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL, 
        config={  
            'app_name': "Form Management API"
        }
    )
    
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    

    # Register Blueprints
    from app.forms import forms_blueprint
    from app.responses import responses_blueprint

    app.register_blueprint(forms_blueprint)
    app.register_blueprint(responses_blueprint)

    @app.route('/')
    def home():
        return redirect(url_for('swagger_ui.show'))
    
    return app