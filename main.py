from fasthtml.common import *
from database import create_connection, create_tables
from routes import app

conn = create_connection()
create_tables()


serve()
