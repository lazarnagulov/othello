from typing import Protocol


class UserInterface(Protocol):
    def run(self) -> None: ...
    