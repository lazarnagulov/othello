from typing import Optional
from othello.ui.console_interface import ConsoleInterface
from othello.ui.user_interface import UserInterface
from othello.ui.gui import GUI
import sys

def main() -> None:
    ui: Optional[UserInterface] = None
    argv: list[str] = sys.argv
    if len(argv) != 1:
        match argv[1]:
            case "--console" | "-c": ui = ConsoleInterface(argv)
            case "--ui" | "-u": ui = GUI(argv)
            case _: ui = GUI(argv)
    else:
        ui = GUI(argv)

    ui.run()
    
if __name__ == "__main__":
    main()