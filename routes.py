from fasthtml.common import *
from components import *
from database import create_connection

app = FastHTML()

@app.get('/')
def home(): 
    return IndexPage()



@app.get('/tracker')
def tracker(): 
    conn = create_connection()
    tasks_list = conn.execute("SELECT * FROM task").fetchall()
    return TrackerPage(tasks_list)
