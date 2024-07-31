from fasthtml.common import *

def IndexPage():
    return Html(
        Head(
            Title("Chores XP Tracker"),
            Style("""
                body {
                    background: linear-gradient(to bottom, #000428, #004e92);
                    color: white;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }
                a {
                    color: #61dafb;
                    text-decoration: none;
                    font-size: 1.2em;
                    margin: 0 1em;
                }
                a:hover {
                    text-decoration: underline;
                }
                h1 {
                    font-size: 3em;
                    margin-bottom: 0.5em;
                }
                p {
                    font-size: 1.5em;
                    margin-bottom: 2em;
                }
            """)
        ),
        Body(
            Div(
                H1("Chores XP Tracker"),
                P("Welcome to the Chores XP Tracker"),
                Div(
                    A("Manage Chores", href="/chores"),
                    A("Track Progress", href="/tracker")
                )
            )
        )
    )



def TrackerPage(tasks_list):
    return Div(
        H1("Track Progress"),
        Ul(*[Li(f"Task {task['id']}: {task['date']} - {task['time_spent']} mins") for task in tasks_list]),
        P("View your progress and achievements here."),
        A("Home", href="/")
    )
