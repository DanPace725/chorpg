import sqlite3
import os

def create_connection(db_file='chores.db'):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables():
    """Create tables in the SQLite database"""
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ADMIN (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            name TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS PLAYER (
            id INTEGER PRIMARY KEY,
            admin_id INTEGER,
            name TEXT NOT NULL,
            current_level INTEGER,
            total_xp INTEGER,
            virtual_currency INTEGER,
            FOREIGN KEY(admin_id) REFERENCES ADMIN(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TASK (
            id INTEGER PRIMARY KEY,
            admin_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            type TEXT,
            base_xp INTEGER,
            repeating BOOLEAN,
            frequency TEXT,
            FOREIGN KEY(admin_id) REFERENCES ADMIN(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS REWARD (
            id INTEGER PRIMARY KEY,
            admin_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            xp_cost INTEGER,
            currency_cost INTEGER,
            FOREIGN KEY(admin_id) REFERENCES ADMIN(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS SMALL_REWARD (
            id INTEGER PRIMARY KEY,
            admin_id INTEGER,
            name TEXT NOT NULL,
            description TEXT,
            probability_weight INTEGER,
            FOREIGN KEY(admin_id) REFERENCES ADMIN(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ACTIVITYLOG (
            id INTEGER PRIMARY KEY,
            admin_id INTEGER,
            player_id INTEGER,
            task_id INTEGER,
            reward_id INTEGER,
            small_reward_id INTEGER,
            date TEXT,
            xp_earned INTEGER,
            currency_earned INTEGER,
            FOREIGN KEY(admin_id) REFERENCES ADMIN(id),
            FOREIGN KEY(player_id) REFERENCES PLAYER(id),
            FOREIGN KEY(task_id) REFERENCES TASK(id),
            FOREIGN KEY(reward_id) REFERENCES REWARD(id),
            FOREIGN KEY(small_reward_id) REFERENCES SMALL_REWARD(id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS LEVEL (
            level INTEGER PRIMARY KEY,
            admin_id INTEGER,
            xp_required INTEGER,
            reward_id INTEGER,
            FOREIGN KEY(admin_id) REFERENCES ADMIN(id),
            FOREIGN KEY(reward_id) REFERENCES REWARD(id)
        )
        ''')

        conn.commit()
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    create_tables()
