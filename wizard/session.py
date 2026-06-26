# wizard/session.py

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WizardSession:

    user_id: int

    screen: str = ""

    message_id: int | None = None

    history: list[str] = field(default_factory=list)

    data: dict[str, Any] = field(default_factory=dict)

    def goto(self, screen: str):

        if self.screen:
            self.history.append(self.screen)

        self.screen = screen

    def back(self):

        if not self.history:
            return None

        self.screen = self.history.pop()

        return self.screen

    def set(self, key, value):

        self.data[key] = value

    def get(self, key, default=None):

        return self.data.get(key, default)

    def reset(self):

        self.screen = ""

        self.history.clear()

        self.data.clear()

        self.message_id = None
