# database/models.py

from database.storage import db


class TournamentModel:

    # -----------------------------
    # CREATE TOURNAMENT
    # -----------------------------

    @staticmethod
    def create(owner_id, name, mode, max_teams, kill_points=1):

        cursor = db.execute(
            """
            INSERT INTO tournaments
            (owner_id, name, mode, max_teams, kill_points)

            VALUES (?, ?, ?, ?, ?)
            """,
            (owner_id, name, mode, max_teams, kill_points)
        )

        return cursor.lastrowid


    # -----------------------------
    # GET TOURNAMENT
    # -----------------------------

    @staticmethod
    def get(tournament_id):

        return db.fetchone(
            """
            SELECT *
            FROM tournaments
            WHERE id = ?
            """,
            (tournament_id,)
        )


    # -----------------------------
    # GET USER TOURNAMENTS
    # -----------------------------

    @staticmethod
    def get_user_tournaments(owner_id):

        return db.fetchall(
            """
            SELECT *
            FROM tournaments

            WHERE owner_id = ?

            ORDER BY id DESC
            """,
            (owner_id,)
        )


    # -----------------------------
    # DELETE TOURNAMENT
    # -----------------------------

    @staticmethod
    def delete(tournament_id):

        db.execute(
            """
            DELETE FROM tournaments

            WHERE id = ?
            """,
            (tournament_id,)
        )


class TeamModel:

    # -----------------------------
    # ADD TEAM
    # -----------------------------

    @staticmethod
    def add_team(tournament_id, slot, name):

        db.execute(
            """
            INSERT INTO teams
            (tournament_id, slot, name)

            VALUES (?, ?, ?)
            """,
            (tournament_id, slot, name)
        )


    # -----------------------------
    # GET ALL TEAMS
    # -----------------------------

    @staticmethod
    def get_teams(tournament_id):

        return db.fetchall(
            """
            SELECT *

            FROM teams

            WHERE tournament_id = ?

            ORDER BY slot
            """,
            (tournament_id,)
        )


    # -----------------------------
    # RENAME TEAM
    # -----------------------------

    @staticmethod
    def rename_team(team_id, new_name):

        db.execute(
            """
            UPDATE teams

            SET name = ?

            WHERE id = ?
            """,
            (new_name, team_id)
        )


    # -----------------------------
    # REMOVE TEAM
    # -----------------------------

    @staticmethod
    def delete_team(team_id):

        db.execute(
            """
            DELETE FROM teams

            WHERE id = ?
            """,
            (team_id,)
        )
