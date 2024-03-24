import os
import resource_rc
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QLabel, QAbstractItemView, QDialog, QVBoxLayout, QHeaderView, QSizePolicy, QMessageBox
from PySide6.QtGui import QPixmap, QIcon, QColor
from styles.styles import styles_table_files, styles_btn_disabled, styles_btn_enabled
from natsort import natsorted
from views.main_window_ui import MainWindow
from controllers.validation_window import ValidationWindowForm

BUTTON_DISABLED_TEXT = "Button disabled. You need to select the image and destination folders."

class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.local_ui_setup()

    def local_ui_setup(self):
        self.setWindowTitle('FEN Validation')
        self.destination_folder_path = ''
        self.folder_path = ''
        self.table_frame.setVisible(False)
        self.number_files_label.setVisible(False)
        self.start_validation_btn.setVisible(False)
        self.start_validation_btn.setEnabled(False)
        self.image_paths = {}
        self.config_table()
        self.files_table.cellClicked.connect(self.cell_clicked)
        self.start_validation_btn.setToolTip(BUTTON_DISABLED_TEXT)
        self.select_folder_btn.clicked.connect(self.select_images_folder)
        self.select_destination_folder_btn.clicked.connect(self.select_destination_folder)
        self.start_validation_btn.clicked.connect(self.open_validation_window)

    def open_validation_window(self):
        window =  ValidationWindowForm(self, self.folder_path, self.destination_folder_path)
        window.show()

    def get_folder_contents(self):
        try:
            contents = os.listdir(self.folder_path)
            return contents
        except FileNotFoundError:
            print(f"The directory {self.folder_path} does not exist")
            QMessageBox.critical(self, "Error", f"The directory {self.folder_path} does not exist")
            return []
        except PermissionError:
            print("You do not have permissions to access the directory")
            QMessageBox.critical(self, "Error", "You do not have permissions to access the directory")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            return []

    def select_images_folder(self):
        self.folder_path= QFileDialog.getExistingDirectory(self, "Select folder")
        if self.folder_path:
            self.folder_content = self.get_folder_contents()
            self.folder_path_line_edit.setText(self.folder_path)
            self.populate_table_with_folder_contents(self.folder_path)
            self.table_frame.setVisible(True)
            self.start_validation_btn.setVisible(True)
            self.number_files_label.setVisible(True)
            self.toggle_button_state()

    def select_destination_folder(self):
        self.destination_folder_path= QFileDialog.getExistingDirectory(self, "Select destination folder")
        if self.destination_folder_path:
            print("Selected destination folder", self.destination_folder_path)
            self.destination_folder_path_line_edit.setText(self.destination_folder_path)
            self.toggle_button_state()

    def config_table(self):
        self.files_table.setStyleSheet(styles_table_files)
        #self.files_table.horizontalHeader().setStyleSheet(styles_table_files)
        #self.files_table.verticalHeader().setStyleSheet(styles_table_files)
        self.files_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.files_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.files_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.files_table.verticalHeader().setVisible(False)
        self.files_table.setAlternatingRowColors(True)

        column_labels = ("FILE NAME", "IMAGE")
        self.files_table.setColumnCount(len(column_labels))
        self.files_table.setRowCount(len(self.folder_path))
        self.files_table.setHorizontalHeaderLabels(column_labels)
        self.files_table.setColumnWidth(1, 400)
        self.files_table.setColumnWidth(0,150)
        self.files_table.verticalHeader().setDefaultSectionSize(150)
        self.files_table.setSelectionBehavior(QAbstractItemView.SelectRows)


    def populate_table_with_folder_contents(self, folder_path):
        files = os.listdir(folder_path)
        sorted_files = natsorted(files)
        self.files_table.setRowCount(len(sorted_files))
        self.files_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header = self.files_table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.number_files_label.setText(f"Number of files: {len(files)}")

        even_color = QColor('#FFFFFF')
        odd_color = QColor('#FFFFFF')

        for row, file in enumerate(sorted_files):
            file_path = os.path.join(folder_path, file)
            item = QTableWidgetItem(file)
            # Make the item non-editable
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignCenter)
            background_color = even_color if row % 2 == 0 else odd_color
            item.setBackground(background_color)
            self.files_table.setItem(row, 0, item)
            self.files_table.setRowHeight(row, 350)

            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                self.image_paths[(row, 1)] = file_path
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)
                pixmap = QPixmap(file_path)
                pixmap = pixmap.scaled(500, 500, Qt.KeepAspectRatio)
                label.setPixmap(pixmap)
                label.setStyleSheet("margin-left: 10px")
                label.setStyleSheet("background-color: {}".format(background_color.name()))
                self.files_table.setCellWidget(row, 1, label)

            else:
                self.files_table.setRowHeight(row, 130)
                icon = QIcon()
                icon.addFile(u":/assets/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
                label = QLabel()
                label.setAlignment(Qt.AlignCenter)
                label.setPixmap(icon.pixmap(100, 100))
                label.setStyleSheet("background-color: {}".format(background_color.name()))
                self.files_table.setCellWidget(row, 1, label)


    def cell_clicked(self, row, column):
        if (row, column) in self.image_paths:
            image_path = self.image_paths[(row, column)]
            pixmap = QPixmap(image_path)
            self.show_image_dialog(pixmap)

    def show_image_dialog(self, pixmap):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(pixmap.scaled(980, 980, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(label)
        dialog.setLayout(layout)
        dialog.exec()

    def update_tooltip(self):
        if not self.start_validation_btn.isEnabled():
            self.start_validation_btn.setToolTip(BUTTON_DISABLED_TEXT)
            self.start_validation_btn.setToolTipDuration(3000)
        else:
            self.start_validation_btn.setToolTip("")

    def toggle_button_state(self):
        if self.folder_path and self.destination_folder_path:
            self.start_validation_btn.setEnabled(True)
            self.update_tooltip()
        else:
            self.start_validation_btn.setEnabled(False)
        self.update_button_style()

    def update_button_style(self):
        if self.start_validation_btn.isEnabled():
            self.start_validation_btn.setStyleSheet(styles_btn_enabled)
            self.set_validation_btn_icon()
        else:
            self.start_validation_btn.setStyleSheet(styles_btn_disabled)
            self.set_validation_btn_icon()

    def set_validation_btn_icon(self):
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/play-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_validation_btn.setIcon(icon1)
        self.start_validation_btn.setIconSize(QSize(22, 22))




