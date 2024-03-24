import os
import subprocess
import shutil
import resource_rc
import csv
import chess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QDialog
from PySide6.QtGui import QPixmap
from views.validation_window_ui import ValidationWindow
from chess_game.chessboard import Chessboard

class ValidationWindowForm(QWidget, ValidationWindow):
    def __init__(self, parent = None, folder_path = None, destination_folder_path = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('FEN Validation')
        self.generated_fen_text_edit.setEnabled(False)
        self.initial_fen_details = ''
        self.new_fen = ''
        self.csv_file_path= ''
        self.image_paths = []
        self.fen_strings = []
        self.current_index = 0
        self.main_window = parent
        self.folder_path =  folder_path
        self.destination_folder_path = destination_folder_path
        self.setWindowFlag(Qt.Window)
        self.main_window.hide()
        self.cancel_validation_btn.clicked.connect(self.close)
        self.read_csv_and_display_first_element()
        self.save_validation_btn.clicked.connect(self.validate_and_show_next)
        self.chess_img_label.clicked.connect(self.show_image_dialog)

    def read_csv_and_display_first_element(self):
        try:
            self.csv_file_path = self.find_csv_filename(self.folder_path)
            with open(self.csv_file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    self.image_paths.append(row['file'])
                    self.fen_strings.append(row['fen'])
                # After loading, display the first image and FEN if available
                if self.image_paths and self.fen_strings:
                    self.initial_fen_details = self.extract_fen_details(self.fen_strings[0])
                    self.set_image(self.image_paths[0])
                    self.set_chess_game(self.fen_strings[0])
                    self.update_image_count_label()
                    self.update_fen_label(self.fen_strings[0])
        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Error", e)

    def find_csv_filename(self,directory):
        csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
        if len(csv_files) == 1:
            return os.path.join(directory, csv_files[0])
        elif len(csv_files) > 1:
            raise Exception("More than one CSV file found in the directory.")
        else:
            raise Exception("No CSV files found in the directory.")

    def closeEvent(self, event):
        self.main_window.show()
        event.accept()

    def set_image(self, image_path):
        self.chess_img_label.setProperty('image_path', image_path)
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(550, 600, Qt.KeepAspectRatio)
        self.chess_img_label.setPixmap(pixmap)
        image_name = os.path.basename(image_path)
        self.imge_label.setText(f"Image {image_name}")

    def set_chess_game(self, starting_fen):
        self.board = chess.Board(starting_fen)
        self.scene = Chessboard(self.board)
        self.chess_graphic_view.setScene(self.scene)
        self.scene.fenUpdated.connect(self.update_fen_label)
        self.scene.render()

    def update_fen_label(self, fen):
        fen_with_details = fen
        if self.extract_fen_details(fen) == "":
            fen_with_details = fen + " " + self.initial_fen_details
        self.new_fen = fen_with_details
        self.generated_fen_text_edit.setText(fen_with_details)

    def update_image_count_label(self):
        current_position = self.current_index + 1
        total_images = len(self.image_paths)
        self.count_images_label.setText(f"Image {current_position} out of {total_images}")

    def show_next_item(self):
        if self.current_index + 1 < len(self.image_paths):
            self.current_index += 1
            self.initial_fen_details = self.extract_fen_details(self.fen_strings[self.current_index])
            self.set_image(self.image_paths[self.current_index])
            self.set_chess_game(self.fen_strings[self.current_index])
            self.update_fen_label(self.fen_strings[self.current_index])
            self.update_image_count_label()
        else:
            QMessageBox.information(self, "Validation finished", "You have finished validating all the images")
            self.close()
            self.main_window.show()

    def create_folder_if_not_exists(self, folder_path):
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except OSError as error:
            print(f"Error creating directory: {error}")
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText("An error occurred while creating the directory to store the new csv file.")
            msg_box.setInformativeText(str(error))
            msg_box.exec_()
            raise

    def get_destination_csv_file_path(self, file_name):
        path = os.path.join(self.destination_folder_path, os.path.basename(self.folder_path))
        self.create_folder_if_not_exists(path)
        return os.path.join(path, file_name)

    def get_specific_row_with_headers_dict(self, csv_file_path, row_index):
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            headers = csv_reader.fieldnames
            for current_index, row in enumerate(csv_reader, start=0):
                if current_index == row_index:
                    return headers, row

    def copy_image(self, source_path, destination_folder):
        destination_path = os.path.join(destination_folder, os.path.basename(source_path))
        shutil.copy(source_path, destination_path)

    def store_updated_fen(self):
        headers, row_dict = self.get_specific_row_with_headers_dict(self.csv_file_path, self.current_index)
        row_dict['fen'] = self.new_fen
        row_dict['verified'] = 'Yes'
        destination_csv_file = self.get_destination_csv_file_path('labels.csv')
        file_exists = os.path.isfile(destination_csv_file)
        with open(destination_csv_file, mode='a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers + ['verified'])
                if not file_exists:
                    writer.writeheader()
                writer.writerow(row_dict)
        img_destination_path = os.path.join(self.destination_folder_path, os.path.basename(self.folder_path))
        self.copy_image(self.image_paths[self.current_index], img_destination_path )


    def extract_fen_details(self,fen):
        parts = fen.split(' ')
        if len(parts) > 1:
            details = ' '.join(parts[1:])
            return details
        else:
            return ""

    def show_image_dialog(self):
        image_path = self.chess_img_label.property('image_path')
        pixmap = QPixmap(image_path)
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(pixmap.scaled(980, 980, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label)
        dialog.setLayout(layout)
        if image_path and os.path.isfile(image_path):
            # Open the image with the system's default application
            if os.name == 'nt':  # If the system is Windows
                os.startfile(image_path)
            elif os.name == 'posix':
                if 'darwin' in os.sys.platform:  # macOS
                    subprocess.run(['open', image_path])
                else:  # Unix/Linux
                    subprocess.run(['xdg-open', image_path])
            else:
                print("OS not supported!")
        dialog.exec()


    def validate_and_show_next(self):
        self.store_updated_fen()
        self.show_next_item()



