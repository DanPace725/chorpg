from fasthtml.common import *
from database import create_connection, create_tables
from routes import app
from fastapi import Request

def get_session(request: Request):
    return request.session

conn = create_connection()
create_tables()


serve()
