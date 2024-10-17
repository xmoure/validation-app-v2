import os
import chess
from PySide6.QtCore import Qt, Signal, QSize, QUrl
from PySide6.QtWidgets import QWidget, QMessageBox, QLabel, QSizePolicy, QApplication
from PySide6.QtGui import QPixmap, QMovie, QIcon, QDesktopServices, QTransform
from views.validation_window_ui import ValidationWindow
from chess_game.chessboard import Chessboard
from database.mongo_db import mongo_db_instance
from controllers.data_fetcher import DataFetcher
from controllers.overlay_widget import OverlayWidget
import tempfile
import traceback
from config import get_ssh_details

class ValidationWindowForm(QWidget, ValidationWindow):
    data_ready = Signal(dict)
    def __init__(self, parent = None, match_id= '') -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('FEN Validation')
        self.starting_fen = ''
        self.generated_fen_text_edit.setEnabled(False)
        self.current_image_index = 0
        self.main_window = parent
        self.match_id = match_id
        self.match = {}
        self.current_image_data = ''
        self.current_fen = ''
        self.setWindowFlag(Qt.Window)
        self.main_window.hide()
        self.show_loading()
        self.overlay = OverlayWidget(self, "Validating...")
        self.overlay.setGeometry(self.rect())
        self.overlay.hide()
        self.cancel_validation_btn.clicked.connect(self.close)
        self.save_validation_btn.clicked.connect(self.on_validate)
        self.chess_img_label.clicked.connect(self.open_image_with_os_application)
        self.start_data_fetching(match_id)
        self.current_image_orientation = ''
        self.rotation_angle = 0
        self.rotate_image_btn.clicked.connect(self.rotate_image)

    def closeEvent(self, event):
        self.main_window.show()
        self.main_window.load_matches()
        event.accept()

    def rotate_image(self):
        # Increment the rotation angle by 90 degrees
        self.rotation_angle = (self.rotation_angle + 90) % 360
        # Update the image with the new rotation
        self.apply_image_rotation()

    def apply_image_rotation(self):
        if not self.current_image_data:
            return

        pixmap = QPixmap()
        pixmap.loadFromData(self.current_image_data)

        # Apply rotation
        transform = QTransform()
        transform.rotate(self.rotation_angle)
        pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)

        # Set the rotated and scaled image
        pixmap = pixmap.scaled(550, 600, Qt.KeepAspectRatio)
        self.chess_img_label.setPixmap(pixmap)

    def set_chess_game(self, fen):
        self.board = chess.Board(fen)
        self.scene = Chessboard(self.board)
        self.chess_graphic_view.setScene(self.scene)
        self.scene.fenUpdated.connect(self.update_fen_label)
        self.scene.render()

    def update_fen_label(self, fen):
        fen = self.get_fen_base(fen)
        self.generated_fen_text_edit.setText(fen)
        self.current_fen = fen


    def get_image_name(self):
        file = self.current_move['file']
        file_name = file.split("/")[-1]
        return file_name

    def update_image_count_label(self):
        current_position = self.current_image_index + 1
        total_images = len(self.match['moves'])
        self.count_images_label.setText(f"Image {current_position} out of {total_images}")
        self.image_text_label.setText(f" Image {self.get_image_name()}")

    def extract_fen_details(self,fen):
        parts = fen.split(' ')
        if len(parts) > 1:
            details = ' '.join(parts[1:])
            return details
        else:
            return ""

    def get_fen_base(self,fen_string):
        return fen_string.split(' ')[0]

    def open_image_with_os_application(self):
        try:
            if self.current_image_data.isEmpty():
                return

            # Write image data to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            temp_file.write(self.current_image_data.data())
            temp_file.close()
            if os.path.getsize(temp_file.name) > 0:
                if not QDesktopServices.openUrl(QUrl.fromLocalFile(temp_file.name)):
                    print("Failed to open the image with the default application.")
            else:
                print("The temporary image file is empty.")

        except Exception as e:
            print("An exception occurred while attempting to open the image:", e)
            traceback.print_exc()

    def show_next_image(self):
        if self.current_image_index < len(self.match['moves']):
            self.current_move = self.match['moves'][self.current_image_index]
            # Request the DataFetcher to fetch the next image
            self.data_fetcher.fetch_next_image(self.current_move)
            fen = self.get_fen_base(self.current_move['fen'])
            self.current_fen = fen
            self.starting_fen = fen
            self.update_fen_label(self.current_fen)
            self.set_chess_game(self.current_fen)
            self.update_image_count_label()
        else:
            self.finish_validation()

    def on_image_fetched(self, image_data):
        self.current_image_data = image_data
        self.rotation_angle = 0
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        pixmap = pixmap.scaled(550, 600, Qt.KeepAspectRatio)
        self.chess_img_label.setPixmap(pixmap)
        self.setButtonLoadingState(False)
        self.overlay.hide()

    def on_validate(self):
        self.setButtonLoadingState(True)
        self.show_overlay()
        QApplication.processEvents()
        success = self.save_validation()
        if success:
            self.current_image_index += 1
            self.show_next_image()
        else:
            self.setButtonLoadingState(False)
            self.overlay.hide()


    def on_data_fetched(self, match_data, image_data):
        self.hide_loading()
        self.match = match_data
        self.current_move = self.match['moves'][self.current_image_index]
        fen = fen = self.get_fen_base(self.current_move['fen'])
        self.current_image_orientation = self.match['orientation']
        self.starting_fen = fen
        self.set_chess_game(fen)
        self.on_image_fetched(image_data)
        self.update_image_count_label()
        self.update_fen_label(fen)

    def on_fetch_error(self, error_message):
        self.hide_loading()
        self.overlay.hide()
        QMessageBox.critical(self, "Error", "Failed to fetch data: " + error_message)

    def finish_validation(self):
        self.overlay.hide()
        QMessageBox.information(self, "Validation finished", "You have finished validating all the images for the selected chess game.")
        self.close()
        self.main_window.show()

    def start_data_fetching(self, match_id):
        if not mongo_db_instance.is_connected():
            mongo_db_instance.connect()
        ssh_details = get_ssh_details()
        self.data_fetcher = DataFetcher(mongo_db_instance, match_id, ssh_details, parent=self)
        self.data_fetcher.data_fetched.connect(self.on_data_fetched)
        self.data_fetcher.error_occurred.connect(self.on_fetch_error)
        self.data_fetcher.image_fetched.connect(self.on_image_fetched)
        self.data_fetcher.start()

    def show_loading(self):
        self.loader_label = QLabel(self.central_widget_frame)
        self.loader_label.setAlignment(Qt.AlignCenter)
        self.loader_movie = QMovie(u":/assets/loading.gif")
        self.loader_label.setMovie(self.loader_movie)
        self.loader_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Hide all elements that should not be visible during loading
        self.content_frame.hide()
        self.img_count_frame.hide()
        self.image_board_frame.hide()
        self.generated_fen_frame.hide()
        self.btns_frame.hide()


        self.verticalLayout.setAlignment(Qt.AlignCenter)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.addWidget(self.loader_label)
        self.loader_label.setStyleSheet("border: none;")

        # Start the loader animation and show the loader label
        self.loader_movie.start()
        self.loader_label.show()
        self.loader_label.raise_()

    def hide_loading(self):
        self.loader_movie.stop()
        self.loader_label.hide()

        # Show other UI elements
        self.content_frame.show()
        self.img_count_frame.show()
        self.image_board_frame.show()
        self.generated_fen_frame.show()
        self.btns_frame.show()

    def save_validation(self):
        try:
            if not mongo_db_instance.is_connected():
                mongo_db_instance.connect()

            matched_count, modified_count = mongo_db_instance.update_match_move_verified_and_fen(
                self.match_id,
                self.current_move['_id'],
                self.current_fen,
                self.starting_fen,
            )
            if matched_count == 0:
                raise ValueError("No matching document found with the provided match_id and move_id.")
            if modified_count == 0:
                raise ValueError("The move was not updated, possibly because it was already verified or had the same FEN.")
            #QMessageBox.information(self, "Update Successful", "The move has been verified and updated successfully.")
            return True

        except Exception as e:
            QMessageBox.critical(self, "Update Failed", f"An error occurred while updating the move: {e}")
            return False


    def setButtonLoadingState(self, isLoading=True):
        icon1 = QIcon()
        if isLoading:
            self.save_validation_btn.setText("Validating...")
            self.save_validation_btn.setEnabled(False)
            icon1.addFile(u":/assets/icons/loader.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.save_validation_btn.setIcon(icon1)
            self.save_validation_btn.setIconSize(QSize(22, 22))
        else:
            self.save_validation_btn.setText("Validate and Save")
            self.save_validation_btn.setEnabled(True)
            icon1.addFile(u":/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
            self.save_validation_btn.setIcon(icon1)
            self.save_validation_btn.setIconSize(QSize(22, 22))
        QApplication.processEvents()

    def show_overlay(self):
        self.overlay.show()
        self.overlay.raise_()
        self.overlay.setGeometry(self.frameGeometry())




