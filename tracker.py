from fasthtml.common import *
from fasthtml.fastapp import fast_app, serve
from db import create_connection, create_tables, get_users, get_tasks, log_activity, get_user_activities, login_admin, get_levels, get_all_user_activities
import pandas as pd
from datetime import datetime
from fasthtml.components import Row, Col, Expander, DataFrame, SubHeader, Header, Input, Button, Container, Progress, Link, Form, SelectBox, Success, DateInput, NumberInput 

app, rt = fast_app()
database = "chores.db"
conn = create_connection(database)
create_tables(conn)

@rt('/')
def main():
    cookies = app.cookies(prefix="myapp_", password="password")

    if 'admin_id' not in cookies:
        return login_page(cookies)

    admin_id = cookies['admin_id']
    return show_tracker(conn, admin_id)

def login_page(cookies):
    def handle_login(data):
        username = data['username']
        password = data['password']
        admin_id = login_admin(conn, username, password)
        if admin_id:
            cookies['auth_token'] = str(admin_id)
            app.redirect('/')
        else:
            return Html.Div("Invalid username or password", className="error")

    return Container(
        Header("Login", level=2),
        Row(
            Col(Input(label="Username", name="username")),
            Col(Input(label="Password", name="password", input_type="password")),
            Col(Button("Login", type="submit"))
        ),
        on_submit=handle_login
    )

def show_tracker(conn, admin_id):
    user_list = get_users(conn, admin_id)
    user_names = {user[0]: user[1] for user in user_list}

    def handle_selection(data):
        selected_user_id = data['selected_user_id']
        current_date = datetime.now().date()
        return display_user_progress(conn, selected_user_id, admin_id, current_date)

    return Container(
        Header("Chore Tracker", level=2),
        SelectBox(
            label='Select Child',
            options=list(user_names.keys()),
            format_func=lambda x: user_names[x],
            name='selected_user_id'
        ),
        on_submit=handle_selection
    )

def display_user_progress(conn, user_id, admin_id, current_date):
    user_details = get_users(conn, admin_id)
    user_details = [user for user in user_details if user[0] == user_id][0]
    user_name, current_level, total_xp = user_details[1], user_details[2], user_details[3]

    levels = get_levels(conn, admin_id)
    current_level_info = next((level for level in levels if level[0] == current_level), None)
    next_level_info = next((level for level in levels if level[0] == current_level + 1), None)

    xp_for_next_level = next_level_info[2] if next_level_info else 100
    progress_percent = min(max(total_xp / xp_for_next_level, 0), 1)

    today_tasks = get_user_activities(conn, admin_id, user_id, str(current_date))
    all_tasks = get_all_user_activities(conn, admin_id, user_id)

    return Container(
        Header(f"{user_name}'s Chore Progress", level=1),
        Row(
            Col(
                SubHeader(f"Level {current_level}"),
                Progress(value=progress_percent, label=f"{total_xp} / {xp_for_next_level} XP to Next Level")
            ),
            Col(SubHeader(f"{total_xp} XP"))
        ),
        Header("Today's Tasks", level=2),
        DataFrame(data=today_tasks) if not today_tasks.empty else Html.Div("No tasks for today."),
        Expander(
            title="View All Tasks",
            content=DataFrame(data=all_tasks) if not all_tasks.empty else Html.Div("No tasks found.")
        ),
        manage_tasks(conn, user_id, admin_id)
    )

def manage_tasks(conn, user_id, admin_id):
    task_list = get_tasks(conn, admin_id)
    task_options = {task[0]: task[1] for task in task_list}

    def handle_log_task(data):
        task_id = data['task_id']
        date = data['date']
        time_spent = data['time_spent']
        bonus_xp = data['bonus_xp']
        log_activity(conn, admin_id, user_id, task_id, str(date), time_spent)
        return Success("Task logged successfully!")

    return Container(
        SelectBox(
            label='Select Task',
            options=list(task_options.keys()),
            format_func=lambda x: task_options[x],
            name='task_id'
        ),
        DateInput(label="Date", name='date'),
        NumberInput(label="Time Spent (minutes)", name='time_spent', min_value=0, value=0),
        NumberInput(label="Bonus XP", name='bonus_xp', min_value=0, value=0),
        Button('Log Task', type='submit', on_click=handle_log_task)
    )

if __name__ == "__main__":
    serve()