from PySide6.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt


class Label(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Freestyle Script", 18))
        self.setStyleSheet("""
            QLabel {
                color: #3E3E3E;
                background-color: transparent;
            }
        """)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(14)
        shadow.setOffset(1, 1)
        shadow.setColor(QColor("#292157"))
        self.setGraphicsEffect(shadow)
