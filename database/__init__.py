"""
Database schema.
"""

USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE NOT NULL,
    username TEXT,
    first_name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

TOURNAMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS tournaments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    mode TEXT NOT NULL,
    status TEXT DEFAULT 'Active',
    max_teams INTEGER NOT NULL,
    kill_points INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

TEAMS_TABLE = """
CREATE TABLE IF NOT EXISTS teams(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tournament_id INTEGER NOT NULL,
    slot INTEGER NOT NULL,
    name TEXT NOT NULL,
    FOREIGN KEY(tournament_id)
        REFERENCES tournaments(id)
        ON DELETE CASCADE
);
"""

RANKINGS_TABLE = """
CREATE TABLE IF NOT EXISTS rankings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tournament_id INTEGER NOT NULL,
    placement INTEGER NOT NULL,
    points INTEGER NOT NULL,
    FOREIGN KEY(tournament_id)
        REFERENCES tournaments(id)
        ON DELETE CASCADE
);
"""

RESULTS_TABLE = """
CREATE TABLE IF NOT EXISTS results(
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
);
"""
