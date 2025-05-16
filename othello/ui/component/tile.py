from typing import Optional

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtGui import QPainter, QColor, QPaintEvent

from othello.models.color import Color


class Tile(QPushButton):
    
    def __init__(self, color: Optional[Color], position: tuple[int, int]) -> None:
        super().__init__()
        self.color: Optional[str] = color.value if color is not None else None
        self.position: tuple[int, int] = position
        self.setFixedSize(50, 50)
    
    def paintEvent(self, _: Optional[QPaintEvent]) -> None:
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.palette().button())
        painter.drawRect(self.rect())
        
        if self.color is None:
            return

        painter.setBrush(QColor(self.color))
        radius= min(self.width(), self.height()) / 2 - 10  
        center = QPoint(self.width() // 2, self.height() // 2)
        painter.drawEllipse(center, radius, radius)

    def sizeHint(self) -> QSize:
        return QSize(100, 100)

    def set_color(self, color: Optional[Color]) -> None:
        self.color = color.value if color is not None else None
        self.update()



