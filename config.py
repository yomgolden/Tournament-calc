# config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# BOT INFORMATION
# ==========================

BOT_NAME = "Tournament Manager"
BOT_VERSION = "2.0.0"

# ==========================
# TELEGRAM
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================
# DATABASE
# ==========================

DATABASE_NAME = "tournament.db"
DATABASE_PATH = f"data/{DATABASE_NAME}"

# ==========================
# APPLICATION SETTINGS
# ==========================

DEBUG = True

DEFAULT_KILL_POINTS = 1

MIN_TEAMS = 2

MAX_TEAMS = 100

MAX_TOURNAMENTS_PER_USER = 100

MAX_TEAM_NAME_LENGTH = 40

MAX_TOURNAMENT_NAME_LENGTH = 50

# ==========================
# TOURNAMENT MODES
# ==========================

TOURNAMENT_MODES = [
    "Battle Royale",
    # Future Modes
    "Multiplayer",
    "Single Elimination",
    "Double Elimination",
    "Swiss",
    "Round Robin",
    "League",
    "FFA",
    "Race"
]

# ==========================
# STATUS
# ==========================

STATUS_ACTIVE = "Active"
STATUS_FINISHED = "Finished"
STATUS_ARCHIVED = "Archived"

# ==========================
# EMOJIS
# ==========================

EMOJI = {
    "success": "✅",
    "error": "❌",
    "warning": "⚠️",
    "trophy": "🏆",
    "team": "👥",
    "results": "📝",
    "leaderboard": "📊",
    "settings": "⚙️",
    "back": "⬅️",
    "next": "➡️",
    "cancel": "❌"
}
