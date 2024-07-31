from fasthtml.common import *
from fasthtml import *
from fasthtml.components import Row, Col, Expander, DataFrame, SubHeader, Header, Input, Button, Container, Progress, Link, Titled, P, HStack, VStack, Text, Html, Main
from fasthtml.fastapp import fast_app, serve, picolink, Style
from db import create_connection, create_tables, login_admin, register_admin
from tracker import show_tracker
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)
app = fast_app(hdrs=(picolink,))


css = Style('''
:root {
    --pico-font-size: 100%;
    --pico-font-family: Arial, sans-serif;
}
body {
    background: linear-gradient(to bottom, #00008b, #000000);
    color: white;
}
.container {
    max-width: 400px;
    margin: 100px auto;
    padding: 20px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.input {
    margin-bottom: 15px;
}
.button {
    background-color: #1e90ff;
    color: white;
}
.link {
    color: #1e90ff;
    text-decoration: none;
}
.header {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}
''')

app = fast_app(hdrs=(picolink, css))

@app.route("/")
def get():
    return Title("Hello World"), Main(H1('Hello, World'), cls="container")
@app.route('/login', methods=["GET", "POST"])
def login():
    return Main(
        Container(
            Row(
                Col(
                    HStack(
                        Text("Login", cls="header"),
                    ),
                    Input(placeholder="Username", cls="input"),
                    Input(type="password", placeholder="Password", cls="input"),
                    Button("Login", cls="button"),
                    Link("Don't have an account? Register here", href="/register", cls="link")
                )
            ), cls="container"
        ), cls="container"
    )

@app.route('/register', methods=["GET", "POST"])
def register():
    return Main(
        Container(
            Row(
                Col(
                    HStack(
                        Text("Register", cls="header"),
                    ),
                    Input(placeholder="Username", cls="input"),
                    Input(placeholder="Email", cls="input"),
                    Input(type="password", placeholder="Password", cls="input"),
                    Input(type="password", placeholder="Confirm Password", cls="input"),
                    Button("Register", cls="button"),
                    Link("Already have an account? Login here", href="/login", cls="link")
                )
            ), cls="container"
        ), cls="container"
    )

serve()
