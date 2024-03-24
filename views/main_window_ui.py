# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import resource_rc

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 670)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(MainWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.background_frame.setFont(font)
        self.background_frame.setStyleSheet(u"background-color: #f0f0f0;")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 25))
        self.content_frame.setFont(font)
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.selection_frame = QFrame(self.content_frame)
        self.selection_frame.setObjectName(u"selection_frame")
        self.selection_frame.setMinimumSize(QSize(0, 120))
        self.selection_frame.setMaximumSize(QSize(16777215, 130))
        self.selection_frame.setFont(font)
        self.selection_frame.setFrameShape(QFrame.NoFrame)
        self.selection_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.selection_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.path_selection_frame = QFrame(self.selection_frame)
        self.path_selection_frame.setObjectName(u"path_selection_frame")
        self.path_selection_frame.setMinimumSize(QSize(0, 25))
        self.path_selection_frame.setMaximumSize(QSize(16777215, 50))
        self.path_selection_frame.setFrameShape(QFrame.NoFrame)
        self.path_selection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.path_selection_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.select_folder_label = QLabel(self.path_selection_frame)
        self.select_folder_label.setObjectName(u"select_folder_label")
        self.select_folder_label.setMinimumSize(QSize(320, 0))
        self.select_folder_label.setMaximumSize(QSize(320, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.select_folder_label.setFont(font1)
        self.select_folder_label.setStyleSheet(u"color: black;\n"
"")

        self.horizontalLayout.addWidget(self.select_folder_label)

        self.folder_path_line_edit = QLineEdit(self.path_selection_frame)
        self.folder_path_line_edit.setObjectName(u"folder_path_line_edit")
        self.folder_path_line_edit.setEnabled(False)
        self.folder_path_line_edit.setMinimumSize(QSize(180, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.folder_path_line_edit.setFont(font2)
        self.folder_path_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;")
        self.folder_path_line_edit.setFrame(True)

        self.horizontalLayout.addWidget(self.folder_path_line_edit)

        self.select_folder_btn = QToolButton(self.path_selection_frame)
        self.select_folder_btn.setObjectName(u"select_folder_btn")
        self.select_folder_btn.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/assets/icons/folder-yellow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.select_folder_btn.setIcon(icon)
        self.select_folder_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.select_folder_btn)


        self.verticalLayout_5.addWidget(self.path_selection_frame)

        self.path_selection_frame_2 = QFrame(self.selection_frame)
        self.path_selection_frame_2.setObjectName(u"path_selection_frame_2")
        self.path_selection_frame_2.setMinimumSize(QSize(0, 0))
        self.path_selection_frame_2.setMaximumSize(QSize(16777215, 50))
        self.path_selection_frame_2.setFrameShape(QFrame.NoFrame)
        self.path_selection_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.path_selection_frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.select_destination_folder_label = QLabel(self.path_selection_frame_2)
        self.select_destination_folder_label.setObjectName(u"select_destination_folder_label")
        self.select_destination_folder_label.setMinimumSize(QSize(320, 0))
        self.select_destination_folder_label.setMaximumSize(QSize(320, 16777215))
        self.select_destination_folder_label.setFont(font1)
        self.select_destination_folder_label.setStyleSheet(u"color: black;\n"
"")

        self.horizontalLayout_2.addWidget(self.select_destination_folder_label)

        self.destination_folder_path_line_edit = QLineEdit(self.path_selection_frame_2)
        self.destination_folder_path_line_edit.setObjectName(u"destination_folder_path_line_edit")
        self.destination_folder_path_line_edit.setEnabled(False)
        self.destination_folder_path_line_edit.setMinimumSize(QSize(180, 30))
        self.destination_folder_path_line_edit.setFont(font2)
        self.destination_folder_path_line_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;")
        self.destination_folder_path_line_edit.setFrame(True)

        self.horizontalLayout_2.addWidget(self.destination_folder_path_line_edit)

        self.select_destination_folder_btn = QToolButton(self.path_selection_frame_2)
        self.select_destination_folder_btn.setObjectName(u"select_destination_folder_btn")
        self.select_destination_folder_btn.setMinimumSize(QSize(0, 30))
        self.select_destination_folder_btn.setIcon(icon)
        self.select_destination_folder_btn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.select_destination_folder_btn)


        self.verticalLayout_5.addWidget(self.path_selection_frame_2)


        self.verticalLayout_4.addWidget(self.selection_frame)

        self.table_frame = QFrame(self.content_frame)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setEnabled(True)
        self.table_frame.setMinimumSize(QSize(850, 300))
        self.table_frame.setFont(font)
        self.table_frame.setStyleSheet(u"background-color: #FFFFFF;")
        self.table_frame.setFrameShape(QFrame.Panel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.table_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.files_table = QTableWidget(self.table_frame)
        self.files_table.setObjectName(u"files_table")
        self.files_table.setMinimumSize(QSize(200, 200))
        self.files_table.setFont(font)
        self.files_table.setStyleSheet(u"")
        self.files_table.setFrameShape(QFrame.NoFrame)
        self.files_table.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.files_table)


        self.verticalLayout_4.addWidget(self.table_frame)

        self.number_files_label = QLabel(self.content_frame)
        self.number_files_label.setObjectName(u"number_files_label")
        self.number_files_label.setFont(font1)
        self.number_files_label.setStyleSheet(u"color: black;\n"
"")

        self.verticalLayout_4.addWidget(self.number_files_label)

        self.validation_btn_frame = QFrame(self.content_frame)
        self.validation_btn_frame.setObjectName(u"validation_btn_frame")
        self.validation_btn_frame.setMinimumSize(QSize(0, 0))
        self.validation_btn_frame.setFont(font)
        self.validation_btn_frame.setFrameShape(QFrame.NoFrame)
        self.validation_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.validation_btn_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.start_validation_btn = QPushButton(self.validation_btn_frame)
        self.start_validation_btn.setObjectName(u"start_validation_btn")
        self.start_validation_btn.setMinimumSize(QSize(230, 35))
        self.start_validation_btn.setMaximumSize(QSize(230, 35))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setBold(True)
        self.start_validation_btn.setFont(font3)
        self.start_validation_btn.setStyleSheet(u"QPushButton{\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/forward-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_validation_btn.setIcon(icon1)
        self.start_validation_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.start_validation_btn)


        self.verticalLayout_4.addWidget(self.validation_btn_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.select_folder_label.setText(QCoreApplication.translate("MainWindow", u"Select the folder that contains the images:", None))
        self.select_folder_btn.setText("")
        self.select_destination_folder_label.setText(QCoreApplication.translate("MainWindow", u"Select the folder to store the validated images: ", None))
        self.select_destination_folder_btn.setText("")
        self.number_files_label.setText(QCoreApplication.translate("MainWindow", u"Number of files: ", None))
        self.start_validation_btn.setText(QCoreApplication.translate("MainWindow", u"Start Validation", None))
    # retranslateUi

