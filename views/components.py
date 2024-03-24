from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, Signal

class Button(QPushButton):
    def __init__(self, icon, color):
        super().__init__()
        self.setMinimumSize(30, 30)
        self.set_cursor()
        self.setIcon(QIcon(f"assets/icons/{icon}.png"))
        self.setStyleSheet(f"border-radius: 15px; background-color: {color};")

    def set_cursor(self):
        pointer = QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)

class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
