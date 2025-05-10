from PySide6.QtCore import QRect, QPointF


def enter_Event(parent, event):
    # Stop any ongoing animations
    parent.scale_anim.stop()
    parent.shadow_anim.stop()

    # Calculate scaled geometry relative to base
    scaled_geometry = QRect(
        parent.base_geometry.x() - 5, parent.base_geometry.y() - parent._hover_rise,
        parent.base_geometry.width() + 10, parent.base_geometry.height() + 10
    )

    parent.scale_anim.setStartValue(parent.geometry())
    parent.scale_anim.setEndValue(scaled_geometry)

    parent.shadow_anim.setStartValue(parent.shadow.offset())
    parent.shadow_anim.setEndValue(QPointF(parent._hover_shadow_offset, parent._hover_shadow_offset))

    parent.scale_anim.start()
    parent.shadow_anim.start()


def leave_Event(parent, event):
    # Stop any ongoing animations
    parent.scale_anim.stop()
    parent.shadow_anim.stop()

    # Revert to base geometry
    parent.scale_anim.setStartValue(parent.geometry())
    parent.scale_anim.setEndValue(parent.base_geometry)

    parent.shadow_anim.setStartValue(parent.shadow.offset())
    parent.shadow_anim.setEndValue(QPointF(parent._shadow_offset, parent._shadow_offset))

    parent.scale_anim.start()
    parent.shadow_anim.start()
