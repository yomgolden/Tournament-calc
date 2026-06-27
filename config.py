"""
Global Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(
        "BOT_TOKEN is missing inside .env"
    )

# ---------------------------------
# Tournament
# ---------------------------------

MIN_TEAMS = 2
MAX_TEAMS = 100

DEFAULT_KILL_POINTS = 1

TEAM_DISPLAY_LIMIT = 5

# ---------------------------------
# Database
# ---------------------------------

DB_PATH = "tournament.db"

# ---------------------------------
# Bot
# ---------------------------------

BOT_NAME = "Tournament Manager"

VERSION = "1.0.0"
