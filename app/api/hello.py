from flask import Blueprint

hello_bp = Blueprint('main', __name__)

@hello_bp.route('/')
def home():
    return "Hello, Flask!"
