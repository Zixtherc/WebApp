from .settings import project
from .urls import *

project.register_blueprint(blueprint = home)
project.register_blueprint(blueprint = register)