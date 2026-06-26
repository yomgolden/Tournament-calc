# services/state_service.py

class StateManager:

    def __init__(self):
        self.users = {}

    def create(self, user_id):
        self.users[user_id] = {
            "step": None,
            "history": [],
            "data": {}
        }

    def exists(self, user_id):
        return user_id in self.users

    def get(self, user_id):
        if not self.exists(user_id):
            self.create(user_id)

        return self.users[user_id]

    def set_step(self, user_id, step):

        state = self.get(user_id)

        if state["step"]:
            state["history"].append(state["step"])

        state["step"] = step

    def get_step(self, user_id):

        return self.get(user_id)["step"]

    def back(self, user_id):

        state = self.get(user_id)

        if not state["history"]:
            return None

        state["step"] = state["history"].pop()

        return state["step"]

    def set_data(self, user_id, key, value):

        self.get(user_id)["data"][key] = value

    def get_data(self, user_id, key, default=None):

        return self.get(user_id)["data"].get(key, default)

    def clear(self, user_id):

        if self.exists(user_id):
            del self.users[user_id]


state = StateManager()
