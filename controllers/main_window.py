from PySide6.QtCore import Qt, QSize,QCoreApplication
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QSizePolicy, QLabel, QPushButton
from PySide6.QtGui import QIcon
from styles.styles import styles_table_files, styles_btn_disabled, styles_btn_enabled, styles_table_frame
from views.main_window_ui import MainWindow
from controllers.validation_window import ValidationWindowForm
from database.mongo_db import mongo_db_instance
from datetime import datetime
from controllers.edit_window import EditDialog
from functools import partial

BUTTON_DISABLED_TEXT = "Button disabled. You need to select a chess game."

class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.set_no_matches_label()
        self.local_ui_setup()

    def local_ui_setup(self):
        self.setWindowTitle('FEN Validation')
        self.selected_match_id = ''
        self.start_validation_btn.setEnabled(False)
        self.update_button_style()
        self.config_table()
        self.load_matches()
        self.start_validation_btn.setToolTip(BUTTON_DISABLED_TEXT)
        self.games_table.itemSelectionChanged.connect(self.row_selected)
        self.start_validation_btn.clicked.connect(self.open_validation_window)


    def set_no_matches_label(self):
        self.title_frame.hide()
        self.no_matches_label = QLabel(self.content_frame)
        self.no_matches_label.setObjectName(u"no_matches_label")
        self.no_matches_label.setStyleSheet(u"color: #d1221f; font-size: 22px")
        self.no_matches_label.setAlignment(Qt.AlignCenter)
        self.no_matches_label.setText(QCoreApplication.translate("MainWindow", u"There are no chess games with unverified moves", None))
        self.no_matches_label.hide()
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.no_matches_label.setSizePolicy(sizePolicy)

    def open_validation_window(self):
        if self.selected_match_id:
            window =  ValidationWindowForm(self, self.selected_match_id)
            window.show()


    def config_table(self):
        self.table_frame.setStyleSheet(styles_table_frame)
        self.games_table.setStyleSheet(styles_table_files)
        self.games_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.games_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.games_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.games_table.verticalHeader().setVisible(False)

        column_labels = ("MATCH ID", "SOURCE", "TOTAL MOVES", "VERIFIED", "EDIT")
        self.games_table.setColumnCount(len(column_labels))
        self.games_table.setHorizontalHeaderLabels(column_labels)
        self.games_table.verticalHeader().setDefaultSectionSize(150)


    def update_tooltip(self):
        if not self.start_validation_btn.isEnabled():
            self.start_validation_btn.setToolTip(BUTTON_DISABLED_TEXT)
            self.start_validation_btn.setToolTipDuration(3000)
        else:
            self.start_validation_btn.setToolTip("")

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

    def load_matches(self):
        if not mongo_db_instance.is_connected():
            mongo_db_instance.connect()
        unverified_matches_cursor = mongo_db_instance.find_matches_with_not_validated_moves()
        unverified_matches = list(unverified_matches_cursor)
        total_unverified = len(unverified_matches)

        if total_unverified == 0:
            self.show_no_matches_label()
        else:
            self.title_frame.show()
            self.set_table_data(unverified_matches)


    def set_table_data(self, unverified_matches):
        self.hide_no_matches_label()
        self.games_table.setRowCount(0)
        self.games_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header = self.games_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        for match in unverified_matches:


            row_position = self.games_table.rowCount()
            self.games_table.insertRow(row_position)

            match_id_item = QTableWidgetItem(match['match_id'])
            match_id_item.setTextAlignment(Qt.AlignCenter)
            match_id_item.setData(Qt.UserRole, str(match['_id']))
            """ date =  self.extract_and_format_datetime(match['match_id'])
            date_item = QTableWidgetItem(date)
            date_item.setTextAlignment(Qt.AlignCenter) """
            source_item = QTableWidgetItem(match['source'])
            source_item.setTextAlignment(Qt.AlignCenter)
            total_moves_item = QTableWidgetItem(str(match['total_moves']))
            total_moves_item.setTextAlignment(Qt.AlignCenter)
            verified_item = QLabel()
            verified_item.setAlignment(Qt.AlignCenter)
            verified_item.setPixmap(QIcon(u":/assets/icons/x.svg").pixmap(22, 22))
            verified_item.setStyleSheet("background-color: transparent;")

            btn_edit = QPushButton()
            btn_edit.setIcon(QIcon(u":/assets/icons/edit.svg"))
            btn_edit.setStyleSheet("background-color: transparent;")
            match_id = match['_id']
            material = match.get('material', '')
            btn_edit.clicked.connect(partial(self.create_edit_dialog, match_id, material))


            self.games_table.setItem(row_position, 0, match_id_item)
            #self.games_table.setItem(row_position,1, date_item)
            self.games_table.setItem(row_position, 1, source_item)
            self.games_table.setItem(row_position, 2, total_moves_item)
            self.games_table.setCellWidget(row_position, 3, verified_item)
            self.games_table.setCellWidget(row_position, 4, btn_edit)

    def create_edit_dialog(self, match_id, material):
        edit_dialog = EditDialog(self)
        edit_dialog.set_data({'_id': match_id, 'material': material})
        edit_dialog.dialog_saved.connect(self.on_edit_dialog_saved)
        edit_dialog.showDialog()

    def on_edit_dialog_saved(self):
        self.load_matches()


    def show_no_matches_label(self):
        self.table_frame.hide()
        self.validation_btn_frame.hide()
        self.no_matches_label.show()
        self.verticalLayout_4.addWidget(self.no_matches_label)

    def hide_no_matches_label(self):
        self.no_matches_label.hide()
        self.title_frame.show()
        self.table_frame.show()
        self.games_table.show()
        self.validation_btn_frame.show()

    def row_selected(self):
        selected_indexes = self.games_table.selectedIndexes()
        if selected_indexes:
            self.start_validation_btn.setEnabled(True)
            selected_row_index = selected_indexes[0].row()
            match_id_item = self.games_table.item(selected_row_index, 0)
            if match_id_item:
                 match_mongo_id = match_id_item.data(Qt.UserRole)
                 self.selected_match_id = match_mongo_id
        else:
            self.start_validation_btn.setEnabled(False)
        self.update_button_style()
        self.update_tooltip()

    def extract_and_format_datetime(self,match_id):
        """
        Extracts a datetime string from a given input string in the format
        'match-YYYYMMDDTHHMMSS' and converts it to 'Month DD, YYYY, HH:MM:SS' format.
        """
        try:
            date_str = match_id.split('match-')[-1]
            dt = datetime.strptime(date_str, "%Y%m%dT%H%M%S")
            formatted_date = dt.strftime("%B %d, %Y, %H:%M:%S")
            return formatted_date
        except ValueError as e:
            return f"Error parsing date: {str(e)}"






