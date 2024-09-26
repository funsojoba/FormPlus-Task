import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
application = create_app(config_name)

if __name__ == '__main__':
    application.run(
        debug=True if config_name == 'dev' else False,
        use_reloader=True
    )
