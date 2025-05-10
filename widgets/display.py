from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QGraphicsDropShadowEffect
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, QSize, QRectF, QPropertyAnimation, QEasingCurve, QRect, QTimer

from widgets.helper.helper import leave_Event, enter_Event


class ImageWidget(QWidget):
    def __init__(self, image_path, scale_size=(190, 50), parent=None):
        super().__init__(parent)
        self._image_path = image_path
        self._scale_size = QSize(*scale_size)
        self._renderer = None

        self._shadow_offset = 2
        self._hover_shadow_offset = 3
        self._hover_rise = 1
        self._hover_rise_duration = 100
        self.SHADOW_COLOR = "#292157"
        self.base_geometry = QRect(0, 0, 150, 50)

        self._load_image()
        self._setup_ui()
        self._style_line_edit()

    def _load_image(self):
        """Load the SVG image and set widget size."""
        self._renderer = QSvgRenderer(self._image_path)
        if not self._renderer.isValid():
            raise ValueError(f"Failed to load SVG image: {self._image_path}")
        self.setFixedSize(self._scale_size)

    def _setup_ui(self):
        """Set up the layout and QLineEdit."""
        layout = QVBoxLayout(self)
        self.line_edit = QLineEdit(self)
        self.line_edit.setReadOnly(True)
        self.line_edit.setContentsMargins(20, 20, 20, 20)
        self.line_edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.line_edit.mousePressEvent = lambda e, f=self.line_edit.mousePressEvent: (self.shake_window(), f(e))
        layout.addWidget(self.line_edit)
        margin = min(self._scale_size.width(), self._scale_size.height()) // 20
        layout.setContentsMargins(margin, margin, margin, margin)
        self.setLayout(layout)

        # Shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(0)
        self.shadow.setOffset(self._shadow_offset, self._shadow_offset)
        self.shadow.setColor(self.SHADOW_COLOR)
        self.setGraphicsEffect(self.shadow)

        # Animations
        self.scale_anim = QPropertyAnimation(self, b"geometry")
        self.scale_anim.setEasingCurve(QEasingCurve.Type.OutBack)
        self.scale_anim.setDuration(self._hover_rise_duration)

        self.shadow_anim = QPropertyAnimation(self.shadow, b"offset")
        self.shadow_anim.setEasingCurve(QEasingCurve.Type.OutBack)
        self.shadow_anim.setDuration(self._hover_rise_duration)

    def _style_line_edit(self):
        """Style the QLineEdit to be transparent and readable."""
        self.line_edit.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                color: #545656;
                font-family: Comic Sans MS;
                font-size: 22px;
                padding: 5px;
                selection-background-color: none;
            }
        """)
        line_edit_height = self._scale_size.height() // 2
        self.line_edit.setFixedHeight(line_edit_height)

    def paintEvent(self, event):
        """Paint the SVG image as the widget's background."""
        if self._renderer:
            painter = QPainter(self)
            self._renderer.render(painter, QRectF(0, 0, self.width(), self.height()))
            painter.end()

    def text(self):
        """Get the text from the QLineEdit."""
        return self.line_edit.text()

    def setText(self, text):
        """Set the text in the QLineEdit."""
        self.line_edit.setText(text)

    def resizeEvent(self, event):
        # Update base geometry when resized
        self.base_geometry = self.geometry()
        super().resizeEvent(event)

    def enterEvent(self, event):
        enter_Event(self, event)
        super().enterEvent(event)

    def leaveEvent(self, event):
        leave_Event(self, event)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.shake_window()
        super().mousePressEvent(event)

    def shake_window(self):
        """Shaky shaky"""
        actual_pos = self.pos()
        QTimer.singleShot(0, lambda: self.move(actual_pos.x() + 1, actual_pos.y()))
        QTimer.singleShot(50, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(100, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(150, lambda: self.move(actual_pos.x() + -5, actual_pos.y()))
        QTimer.singleShot(200, lambda: self.move(actual_pos.x() + 4, actual_pos.y()))
        QTimer.singleShot(250, lambda: self.move(actual_pos.x() + -2, actual_pos.y()))
        QTimer.singleShot(300, lambda: self.move(actual_pos.x(), actual_pos.y()))