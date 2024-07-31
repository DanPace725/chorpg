import sqlite3
import pandas as pd
import bcrypt
DEFAULT_LEVELS = [
    (1, 100, 100, "Reward: Gift card $5"),
    (2, 200, 300, "Reward: Extra 30 minutes screen time"),
    (3, 300, 600, "Reward: Choice of dinner for one night"),
    (4, 400, 1000, "Reward: Movie night choice"),
    (5, 500, 1500, "Reward: New book or toy"),
    (6, 600, 2100, "Reward: Trip to the local park"),
    (7, 700, 2800, "Reward: $10 cash bonus"),
    (8, 800, 3600, "Reward: Day out at the zoo"),
    (9, 900, 4500, "Reward: Video game"),
    (10, 1000, 5500, "Reward: Weekend family trip")
]


# Utility Functions
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

# Admin Related Functions
def create_tables(conn):
    with conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY,
                admin_id INTEGER,
                name TEXT NOT NULL,
                current_level INTEGER DEFAULT 0,
                total_xp INTEGER DEFAULT 0,
                FOREIGN KEY (admin_id) REFERENCES admin(id)
            );
            CREATE TABLE IF NOT EXISTS Tasks (
                task_id INTEGER PRIMARY KEY,
                admin_id INTEGER,
                task_name TEXT NOT NULL,
                base_xp INTEGER NOT NULL,
                time_multiplier REAL NOT NULL,
                FOREIGN KEY (admin_id) REFERENCES admin(id)
            );
            CREATE TABLE IF NOT EXISTS ActivityLog (
                activity_id INTEGER PRIMARY KEY,
                admin_id INTEGER,
                user_id INTEGER,
                task_id INTEGER,
                date TEXT NOT NULL,
                time_spent INTEGER,
                xp_earned INTEGER,
                bonus_xp INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES Users(user_id),
                FOREIGN KEY (task_id) REFERENCES Tasks(task_id),
                FOREIGN KEY (admin_id) REFERENCES admin(id)
            );
            CREATE TABLE IF NOT EXISTS "Levels" (
                Level INTEGER,
                admin_id INTEGER,
                XPRequired INTEGER,
                CumulativeXP INTEGER,
                Reward TEXT,
                PRIMARY KEY (Level, admin_id),
                FOREIGN KEY (admin_id) REFERENCES admin(id)
);
        """)

def register_admin(conn, username, password):
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO admin (username, password_hash) VALUES (?, ?)", (username, hash_password(password)))
            admin_id = cursor.lastrowid
            initialize_default_levels(conn, admin_id)
        return True
    except sqlite3.IntegrityError as ie:
        print(f"IntegrityError: {ie}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def login_admin(conn, username, password):
    c = conn.cursor()
    c.execute("SELECT id, password_hash FROM admin WHERE username = ?", (username,))
    admin = c.fetchone()
    if admin and check_password(admin[1], password):
        return admin[0], True  # Assuming admin_id is obtained during authentication
    else:
        return None, False

# User Management Functions
def add_user(conn, admin_id, name):
    with conn:
        conn.execute("INSERT INTO Users (admin_id, name) VALUES (?, ?)", (admin_id, name))

def get_users(conn, admin_id):
    c = conn.cursor()
    c.execute("SELECT user_id, name, current_level, total_xp FROM Users WHERE admin_id = ?", (admin_id,))
    return c.fetchall()

def update_user(conn, user_id, name):
    with conn:
        conn.execute("UPDATE Users SET name = ? WHERE user_id = ?", (name, user_id))

def delete_user(conn, user_id):
    with conn:
        conn.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))

# Task Management Functions
def add_task(conn, admin_id, task_name, base_xp, time_multiplier):
    with conn:
        conn.execute("INSERT INTO Tasks (admin_id, task_name, base_xp, time_multiplier) VALUES (?, ?, ?, ?)", (admin_id, task_name, base_xp, time_multiplier))

def get_tasks(conn, admin_id):
    c = conn.cursor()
    c.execute("SELECT task_id, task_name, base_xp, time_multiplier FROM Tasks WHERE admin_id = ?", (admin_id,))
    return c.fetchall()

def update_task(conn, task_id, task_name, base_xp, time_multiplier):
    with conn:
        conn.execute("UPDATE Tasks SET task_name = ?, base_xp = ?, time_multiplier = ? WHERE task_id = ?", (task_name, base_xp, time_multiplier, task_id))

def delete_task(conn, task_id):
    with conn:
        conn.execute("DELETE FROM Tasks WHERE task_id = ?", (task_id,))

# Activity Log Functions
def log_activity(conn, admin_id, user_id, task_id, date, time_spent, bonus_xp=0):
    xp_earned = calculate_xp(conn, task_id, time_spent)
    with conn:
        conn.execute("INSERT INTO ActivityLog (admin_id, user_id, task_id, date, time_spent, xp_earned, bonus_xp) VALUES (?, ?, ?, ?, ?, ?, ?)",
                     (admin_id, user_id, task_id, date, time_spent, xp_earned, bonus_xp))
        update_total_xp(conn, user_id, xp_earned + bonus_xp)  # Update the user's total XP along with logging the activity

def get_user_activities(conn, admin_id, user_id, date):
    c = conn.cursor()
    query = """
    SELECT a.date, t.task_name, a.time_spent, a.xp_earned
    FROM ActivityLog a
    JOIN Tasks t ON a.task_id = t.task_id
    WHERE a.admin_id = ? AND a.user_id = ? AND a.date = ?
    """
    c.execute(query, (admin_id, user_id, date))
    df = pd.DataFrame(c.fetchall(), columns=['Date', 'Task Name', 'Time Spent', 'XP Earned'])
    df.index += 1
    return df

def get_all_user_activities(conn, admin_id, user_id):
    c = conn.cursor()
    query = """
    SELECT a.date, t.task_name, a.time_spent, a.xp_earned
    FROM ActivityLog a
    JOIN Tasks t ON a.task_id = t.task_id
    WHERE a.admin_id = ? AND a.user_id = ?
    ORDER BY a.date DESC
    """
    c.execute(query, (admin_id, user_id))
    df = pd.DataFrame(c.fetchall(), columns=['Date', 'Task Name', 'Time Spent', 'XP Earned'])
    df.index += 1
    return df
# Level Management Functions
def initialize_default_levels(conn, admin_id):
    with conn:
        for level, xp_required, cumulative_xp, reward in DEFAULT_LEVELS:
            conn.execute("""
                INSERT INTO Levels (Level, admin_id, XPRequired, CumulativeXP, Reward)
                VALUES (?, ?, ?, ?, ?)""",
                (level, admin_id, xp_required, cumulative_xp, reward))

def update_level(conn, user_id):
    c = conn.cursor()
    c.execute("SELECT total_xp FROM Users WHERE user_id = ?", (user_id,))
    total_xp = c.fetchone()[0]
    levels = [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]  # Add more as needed
    new_level = len([x for x in levels if x <= total_xp])
    with conn:
        conn.execute("UPDATE Users SET current_level = ? WHERE user_id = ?", (new_level, user_id))

def add_level(conn, admin_id, level, xp_required, cumulative_xp, reward):
    with conn:
        conn.execute("INSERT INTO Levels (Level, admin_id, XPRequired, CumulativeXP, Reward) VALUES (?, ?, ?, ?, ?)",
                     (level, admin_id, xp_required, cumulative_xp, reward))

def update_level_details(conn, admin_id, level, xp_required, cumulative_xp, reward):
    with conn:
        conn.execute("UPDATE Levels SET XPRequired = ?, CumulativeXP = ?, Reward = ? WHERE Level = ? AND admin_id = ?",
                     (xp_required, cumulative_xp, reward, level, admin_id))

def get_levels(conn, admin_id):
    c = conn.cursor()
    c.execute("SELECT Level, XPRequired, CumulativeXP, Reward FROM Levels WHERE admin_id = ?", (admin_id,))
    return c.fetchall()

def update_reward(conn, level, reward, admin_id):
    with conn:
        conn.execute("UPDATE Levels SET Reward = ? WHERE Level = ? AND admin_id = ?", (reward, level, admin_id))

# Helper function to calculate XP
def calculate_xp(conn, task_id, time_spent):
    c = conn.cursor()
    c.execute("SELECT base_xp, time_multiplier FROM Tasks WHERE task_id = ?", (task_id,))
    task = c.fetchone()
    return task[0]
def update_total_xp(conn, user_id, xp_to_add):
    with conn:
        conn.execute("UPDATE Users SET total_xp = total_xp + ? WHERE user_id = ?", (xp_to_add, user_id))
        update_level(conn, user_id)  # Update the user's level after changing XP