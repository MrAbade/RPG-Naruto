from app import create_app
from environs import Env


env = Env()
application = create_app(env.str('FLASK_ENV'))

if __name__ == '__main__':
    application.run(host='0.0.0.0')
