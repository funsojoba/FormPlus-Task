import os
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from pymongo import MongoClient

application = Flask(__name__)

application.config.from_object(Config)

def get_db():
    client = MongoClient(
        host=os.environ.get("MONGODB_HOSTNAME"),
        port=int(os.environ.get('MONGODB_PORT', '27017')),
        username=os.environ.get('MONGODB_USERNAME'),
        password=os.environ.get('MONGODB_PASSWORD'),
        authSource='admin'
    )
    db = client[os.environ.get("MONGODB_DATABASE")]
    return db


db = get_db()

@application.route('/test-db')
def test_db():
    try:
        test_db = db.get_collection(name=os.environ.get('MONGODB_DATABASE'))
        
        return f"Connected to the database. Collection count"
    except Exception as e:
        return f"Problem {e}"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=5000, 
        use_reloader=True,
        debug=app.config['DEBUG'])