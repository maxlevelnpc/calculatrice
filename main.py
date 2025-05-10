import sys

from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
from windows.main_window import Calculatrice, CalculatriceUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._number_keys = {getattr(Qt.Key, f"Key_{i}"): str(i) for i in range(10)}

        self.ui = CalculatriceUI(self)
        self.ui.setupUi()

        self.logic = Calculatrice(self.ui)
        self.logic.setupLogic()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.ui.renderer.render(painter, QRectF(0, 0, self.width(), self.height()))
        painter.end()

    def mousePressEvent(self, event):
        """Store the drag start position when the left mouse button is pressed."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.ui.drag_pos = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """Move the window while dragging with the left mouse button."""
        if event.buttons() & Qt.MouseButton.LeftButton and self.ui.drag_pos is not None:
            self.move(event.globalPosition().toPoint() - self.ui.drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Clear the drag position when the mouse button is released."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.ui.drag_pos = None
            event.accept()

    def keyPressEvent(self, event):
        key = event.key()
        if key in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.logic.calculate()
        elif key == Qt.Key.Key_Backspace:
            self.logic.on_button_delete()
        elif key in self._number_keys:
            current = self.ui.display.text()
            value = self._number_keys[key]
            self.ui.display.setText(current + value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
