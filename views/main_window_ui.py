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
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
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
        self.title_frame = QFrame(self.content_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMinimumSize(QSize(0, 50))
        self.title_frame.setMaximumSize(QSize(16777215, 50))
        self.title_frame.setFont(font)
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.title_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: black;")
        self.title_label.setFrameShape(QFrame.NoFrame)
        self.title_label.setFrameShadow(QFrame.Plain)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label)


        self.verticalLayout_4.addWidget(self.title_frame)

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
        self.games_table = QTableWidget(self.table_frame)
        self.games_table.setObjectName(u"games_table")
        self.games_table.setMinimumSize(QSize(200, 200))
        self.games_table.setFont(font)
        self.games_table.setStyleSheet(u"")
        self.games_table.setFrameShape(QFrame.NoFrame)
        self.games_table.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.games_table)


        self.verticalLayout_4.addWidget(self.table_frame)

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
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        self.start_validation_btn.setFont(font2)
        self.start_validation_btn.setStyleSheet(u"QPushButton{\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon = QIcon()
        icon.addFile(u":/assets/icons/forward-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_validation_btn.setIcon(icon)
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
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Chess games with moves pending validation", None))
        self.start_validation_btn.setText(QCoreApplication.translate("MainWindow", u"Start Validation", None))
    # retranslateUi

