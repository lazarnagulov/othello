import sys
from pathlib import Path

from othello.ui.component.game_window import GameWindow
from othello.ui.user_interface import UserInterface

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon


class GUI(UserInterface):    

    def __init__(self, argv: list[str]) -> None:        
        self.app: QApplication = QApplication(argv)  
        sorce_dir: Path = Path(__file__).resolve().parent.parent.parent
        icon_dir: str = str(sorce_dir / "img" / "logo.png")
        self.app.setWindowIcon(QIcon(icon_dir))   
        self.window = GameWindow(argv)
        
    
    def run(self) -> None:
        self.window.show()
        sys.exit(self.app.exec_())
