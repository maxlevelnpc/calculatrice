from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF, QSize, QPropertyAnimation, QEasingCurve, QRect

from widgets.helper.helper import leave_Event, enter_Event


class ImageButton(QPushButton):
    def __init__(self, svg_path, value=None, size=(54, 40), parent=None):
        super().__init__(parent)
        self._shadow_offset = 2
        self._hover_shadow_offset = 3
        self._hover_rise = 1
        self._hover_rise_duration = 100
        self.SHADOW_COLOR = "#292157"
        self.base_geometry = QRect(0, 0, 150, 50)

        self._svg_path = svg_path
        self._value = value
        self._size = QSize(*size)
        self._renderer = None
        self.setProperty("value", value)
        self._load_svg()
        self.setStyleSheet("border: none;")
        self.setFixedSize(self._size)

        # Shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(0)  # Set to 0 for a solid shadow
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

    def _load_svg(self):
        """Load the SVG image."""
        self._renderer = QSvgRenderer(self._svg_path)
        if not self._renderer.isValid():
            raise ValueError(f"Failed to load SVG: {self._svg_path}")

    def paintEvent(self, event):
        """Paint the SVG image."""
        if self._renderer:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            self._renderer.render(painter, QRectF(0, 0, self.width(), self.height()))
            painter.end()
        super().paintEvent(event)

    def sizeHint(self):
        """Return the preferred size of the button."""
        return self._size

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
