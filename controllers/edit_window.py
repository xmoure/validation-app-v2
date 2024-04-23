from PySide6.QtWidgets import  QDialog, QVBoxLayout, QComboBox, QPushButton, QMessageBox
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtUiTools import QUiLoader
from constants import CHESS_MATERIALS
from styles.styles import styles_combobox, styles_btn_disabled, styles_btn_enabled
from database.mongo_db import mongo_db_instance

class EditDialog(QDialog):

    dialog_saved = Signal()

    def __init__(self, parent=None):
        super(EditDialog, self).__init__(parent)
        self.main_window = parent
        self.setWindowTitle("Edit Chess Material")
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        file = QFile("./ui_files/edit_window.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.cancel_btn = self.ui.findChild(QPushButton, 'cancel_btn')
        self.save_btn = self.ui.findChild(QPushButton, 'save_btn')
        self.save_btn.setStyleSheet(styles_btn_disabled)
        self.material_combobox = self.ui.findChild(QComboBox, 'material_combobox')
        self.material_combobox.setStyleSheet(styles_combobox)
        self.material_combobox.currentIndexChanged.connect(self.on_combobox_changed)
        self.save_btn.clicked.connect(self.on_save_clicked)

        self.cancel_btn.clicked.connect(self.on_cancel_clicked)
        self.on_combobox_changed()
        self.update_button_style()

    def on_combobox_changed(self):
        has_selection = self.material_combobox.currentIndex() != -1
        self.save_btn.setEnabled(has_selection)
        self.update_button_style()

    def set_data(self, data):
        self.match_id = data['_id']
        self.material = data['material']
        self.populate_combobox()

    def capitalize_first_letter(self, text):
        return text.capitalize()

    def showDialog(self):
        self.setModal(True)
        self.exec_()

    def on_cancel_clicked(self):
        self.reject()

    def update_button_style(self):
        if self.save_btn.isEnabled():
            self.save_btn.setStyleSheet(styles_btn_enabled)
        else:
            self.save_btn.setStyleSheet(styles_btn_disabled)

    def populate_combobox(self):
        self.material_combobox.clear()
        self.material_combobox.addItems(CHESS_MATERIALS)
        if self.material:
            formatted_material = self.capitalize_first_letter(self.material)
            index = self.material_combobox.findText(formatted_material, Qt.MatchFixedString)
            if index >= 0:
                self.material_combobox.setCurrentIndex(index)
        else:
            # If self.material is an empty string, set the combobox to have no current index
            self.material_combobox.setCurrentIndex(-1)

    def closeEvent(self, event):
        event.accept()

    def on_save_clicked(self):
        try:
            if not mongo_db_instance.is_connected():
                mongo_db_instance.connect()

            selected_material = self.material_combobox.currentText()

            matched_count, modified_count = mongo_db_instance.update_board_material_by_match_id(
                self.match_id,
                selected_material
            )
            if matched_count == 0:
                raise ValueError("No matching document found with the provided match_id.")
            QMessageBox.information(self, "Update Successful", "The material has been updated successfully .")
            self.dialog_saved.emit()  # Emit the signal
            self.accept()
            return True

        except Exception as e:
            QMessageBox.critical(self, "Update Failed", f"An error occurred while updating the material for the match: {e}")
            return False




