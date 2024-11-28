from flask import Flask
from .config import Config
from .routes import auth_blueprint
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
jwt = JWTManager(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.route('/')
def hello_world():
    return "Hello world"

