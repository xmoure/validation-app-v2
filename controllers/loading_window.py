from PySide6.QtWidgets import  QLabel, QDialog, QVBoxLayout
from PySide6.QtGui import QMovie

class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModal(True)
        self.setWindowTitle('Loading...')

        self.spinner_label = QLabel("Loading, please wait...", self)
        spinner_movie = QMovie(u":/assets/loading.gif")
        self.spinner_label.setMovie(spinner_movie)

        layout = QVBoxLayout(self)
        layout.addWidget(self.spinner_label)

        spinner_movie.start()
