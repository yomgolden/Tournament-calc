# wizard/session_manager.py

from wizard.session import WizardSession


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create(self, user_id):

        session = WizardSession(user_id)

        self.sessions[user_id] = session

        return session

    def get(self, user_id):

        if user_id not in self.sessions:

            return self.create(user_id)

        return self.sessions[user_id]

    def remove(self, user_id):

        self.sessions.pop(user_id, None)


session_manager = SessionManager()
