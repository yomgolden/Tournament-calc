# database/storage.py

import sqlite3
from pathlib import Path

from config import DATABASE_PATH


class Database:
    def __init__(self):
        Path("data").mkdir(exist_ok=True)

        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        # Users
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            username TEXT,
            first_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Tournaments
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tournaments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            mode TEXT NOT NULL,
            status TEXT DEFAULT 'Active',
            max_teams INTEGER NOT NULL,
            kill_points INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Teams
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            slot INTEGER NOT NULL,
            name TEXT NOT NULL,

            FOREIGN KEY(tournament_id)
                REFERENCES tournaments(id)
                ON DELETE CASCADE
        )
        """)

        # Placement Points
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rankings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            placement INTEGER NOT NULL,
            points INTEGER NOT NULL,

            FOREIGN KEY(tournament_id)
                REFERENCES tournaments(id)
                ON DELETE CASCADE
        )
        """)

        # Match Results
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            match_number INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            placement INTEGER NOT NULL,
            kills INTEGER NOT NULL,
            placement_points INTEGER NOT NULL,
            total_points INTEGER NOT NULL,

            FOREIGN KEY(tournament_id)
                REFERENCES tournaments(id)
                ON DELETE CASCADE,

            FOREIGN KEY(team_id)
                REFERENCES teams(id)
                ON DELETE CASCADE
        )
        """)

        self.connection.commit()

    def execute(self, query, values=()):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        return cursor

    def fetchone(self, query, values=()):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()

    def fetchall(self, query, values=()):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchall()


db = Database()
