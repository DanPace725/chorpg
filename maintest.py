from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Html(
        Head(
            Title("Modern Web App"),
            Script(src="https://unpkg.com/htmx.org@1.5.0/dist/htmx.min.js"),
            Style("""
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
                }
                .container {
                    text-align: center;
                    background: white;
                    padding: 2em;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                button {
                    padding: 1em 2em;
                    border: none;
                    border-radius: 5px;
                    background-color: #4CAF50;
                    color: white;
                    font-size: 1em;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }
                button:hover {
                    background-color: #45a049;
                }
            """)
        ),
        Body(
            Div(
                Div(
                    P("Welcome to the Modern Web App!", id="message"),
                    Button("Click Me", id="myButton", hx_post="/clicked", hx_swap="outerHTML"),
                    id="content",
                    Class="container"
                )
            )
        )
    )

@rt('/clicked', methods=['POST'])
def clicked():
    return P("Button clicked! This is an interactive app.", id="message")

serve()
