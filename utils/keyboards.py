"""
All Bot Keyboards
"""

from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def home_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📂 My Tournaments",
                    callback_data="my_tournaments"
                )
            ],

            [
                InlineKeyboardButton(
                    text="➕ Create Tournament",
                    callback_data="create_tournament"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⚙️ Settings",
                    callback_data="settings"
                ),

                InlineKeyboardButton(
                    text="❓ Help",
                    callback_data="help"
                )
            ]
        ]
    )


def cancel_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="❌ Cancel",
                    callback_data="cancel"
                )
            ]
        ]
    )


def back_cancel_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⬅ Back",
                    callback_data="back"
                ),

                InlineKeyboardButton(
                    text="❌ Cancel",
                    callback_data="cancel"
                )
            ]
        ]
    )


def summary_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="✅ Create Tournament",
                    callback_data="save_tournament"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⬅ Back",
                    callback_data="back"
                ),

                InlineKeyboardButton(
                    text="❌ Cancel",
                    callback_data="cancel"
                )
            ]
        ]
    )


def tournament_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="👥 Teams",
                    callback_data="teams"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📝 Results",
                    callback_data="results"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🏆 Leaderboard",
                    callback_data="leaderboard"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⚙️ Settings",
                    callback_data="tournament_settings"
                )
            ]
        ]
    )
