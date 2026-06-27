"""
Database storage layer.
"""

import aiosqlite

from config import DB_PATH

from database.models import (
    USERS_TABLE,
    TOURNAMENTS_TABLE,
    TEAMS_TABLE,
    RANKINGS_TABLE,
    RESULTS_TABLE,
)


# =====================================================
# DATABASE INITIALIZATION
# =====================================================

async def init_db():

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("PRAGMA foreign_keys = ON;")

        await db.execute(USERS_TABLE)
        await db.execute(TOURNAMENTS_TABLE)
        await db.execute(TEAMS_TABLE)
        await db.execute(RANKINGS_TABLE)
        await db.execute(RESULTS_TABLE)

        await db.commit()


# =====================================================
# USERS
# =====================================================

async def upsert_user(
    telegram_id: int,
    username: str | None = None,
    first_name: str | None = None,
):

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute(
            """
            INSERT INTO users
            (telegram_id, username, first_name)

            VALUES (?, ?, ?)

            ON CONFLICT(telegram_id)

            DO UPDATE SET

                username = excluded.username,

                first_name = excluded.first_name;
            """,
            (
                telegram_id,
                username,
                first_name,
            ),
        )

        await db.commit()


# =====================================================
# TOURNAMENTS
# =====================================================

async def create_tournament(

    owner_id: int,

    name: str,

    mode: str,

    max_teams: int,

    kill_points: int,

):

    async with aiosqlite.connect(DB_PATH) as db:

        cursor = await db.execute(
            """
            INSERT INTO tournaments
            (
                owner_id,
                name,
                mode,
                max_teams,
                kill_points
            )

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                owner_id,
                name,
                mode,
                max_teams,
                kill_points,
            ),
        )

        await db.commit()

        return cursor.lastrowid


async def get_user_tournaments(
    owner_id: int
):

    async with aiosqlite.connect(DB_PATH) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *

            FROM tournaments

            WHERE owner_id = ?

            ORDER BY id DESC
            """,
            (owner_id,),
        )

        return await cursor.fetchall()


async def get_tournament(
    tournament_id: int
):

    async with aiosqlite.connect(DB_PATH) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *

            FROM tournaments

            WHERE id = ?
            """,
            (tournament_id,),
        )

        return await cursor.fetchone()


async def delete_tournament(
    tournament_id: int
):

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute(
            """
            DELETE FROM tournaments

            WHERE id = ?
            """,
            (tournament_id,),
        )

        await db.commit()


# =====================================================
# TEAMS
# =====================================================

async def insert_teams(
    tournament_id: int,
    teams: list[str],
):

    async with aiosqlite.connect(DB_PATH) as db:

        for slot, name in enumerate(teams, start=1):

            await db.execute(
                """
                INSERT INTO teams
                (
                    tournament_id,
                    slot,
                    name
                )

                VALUES (?, ?, ?)
                """,
                (
                    tournament_id,
                    slot,
                    name,
                ),
            )

        await db.commit()


async def get_teams(
    tournament_id: int
):

    async with aiosqlite.connect(DB_PATH) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *

            FROM teams

            WHERE tournament_id = ?

            ORDER BY slot
            """,
            (tournament_id,),
        )

        return await cursor.fetchall()


# =====================================================
# RANKINGS
# =====================================================

async def insert_rankings(
    tournament_id: int,
    rankings: list[tuple[int, int]],
):

    async with aiosqlite.connect(DB_PATH) as db:

        for placement, points in rankings:

            await db.execute(
                """
                INSERT INTO rankings
                (
                    tournament_id,
                    placement,
                    points
                )

                VALUES (?, ?, ?)
                """,
                (
                    tournament_id,
                    placement,
                    points,
                ),
            )

        await db.commit()


async def get_rankings(
    tournament_id: int
):

    async with aiosqlite.connect(DB_PATH) as db:

        db.row_factory = aiosqlite.Row

        cursor = await db.execute(
            """
            SELECT *

            FROM rankings

            WHERE tournament_id = ?

            ORDER BY placement
            """,
            (tournament_id,),
        )

        return await cursor.fetchall()
