from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie

class OverlayWidget(QWidget):
    def __init__(self, parent=None, display_text = ''):
        super().__init__(parent)
        self.setStyleSheet("background-color: rgba(100, 100, 100, 128);")
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground, False)
        self.setWindowOpacity(0.7)
        self.setFocusPolicy(Qt.NoFocus)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignCenter)

        self.textLabel = QLabel(display_text)
        self.textLabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.textLabel.setStyleSheet("color: white; font: bold 14px; background-color: transparent;")
        self.textLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addWidget(self.textLabel)

        self.label = QLabel()
        self.label.setMaximumHeight(100)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.movie = QMovie(u":/assets/loading.gif")
        self.movie.jumpToFrame(0)
        frame_size = self.movie.currentImage().size()
        self.label.setFixedSize(frame_size)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.setLayout(layout)

        if parent is not None:
            self.resize(parent.size())
            parent.installEventFilter(self)


