#!/usr/bin/python3
"""
Blueprint initialization
"""
from flask import Blueprint

# create blueprint to register/mount
api_views = Blueprint('api_views', __name__, url_prefix='/api')

# TDOD: 

# api endpoints
from api.views.index import *
from api.views.blockshain import *
