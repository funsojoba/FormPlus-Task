from app import app, mongo
from config import Config

# Configure Flask app
app.config.from_object(Config)

# Initialize the MongoDB connection
mongo.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app.config['DEBUG'])