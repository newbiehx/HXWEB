__author__ = 'Mrsong'
from flask import Blueprint
auth = Blueprint('auth', __name__)

#avoid circle import
from . import views
