# wizard/screen.py

from abc import ABC, abstractmethod


class Screen(ABC):

    id = ""
    title = ""

    @abstractmethod
    async def render(self, user_id):
        """
        Returns:
            text,
            keyboard
        """
        pass

    @abstractmethod
    async def validate(self, message):
        """
        Validate user input.
        """
        pass

    @abstractmethod
    async def save(self, session, message):
        """
        Save user input.
        """
        pass

    @abstractmethod
    def next(self):
        """
        Next screen ID.
        """
        pass

    @abstractmethod
    def previous(self):
        """
        Previous screen ID.
        """
        pass
