# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validation_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

from views.components import ClickableLabel
import resource_rc

class ValidationWindow(object):
    def setupUi(self, ValidationWindow):
        if not ValidationWindow.objectName():
            ValidationWindow.setObjectName(u"ValidationWindow")
        ValidationWindow.resize(1450, 870)
        font = QFont()
        font.setFamilies([u"Arial"])
        ValidationWindow.setFont(font)
        self.verticalLayout = QVBoxLayout(ValidationWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(ValidationWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFont(font)
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(2, 2, 2, 2)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setFont(font)
        self.background_frame.setStyleSheet(u"background-color: #f0f0f0;")
        self.background_frame.setFrameShape(QFrame.NoFrame)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFont(font)
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.img_count_frame = QFrame(self.content_frame)
        self.img_count_frame.setObjectName(u"img_count_frame")
        self.img_count_frame.setMinimumSize(QSize(0, 0))
        self.img_count_frame.setFont(font)
        self.img_count_frame.setFrameShape(QFrame.NoFrame)
        self.img_count_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.img_count_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 8, 0, 8)
        self.count_images_label = QLabel(self.img_count_frame)
        self.count_images_label.setObjectName(u"count_images_label")
        self.count_images_label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.count_images_label.setFont(font1)
        self.count_images_label.setStyleSheet(u"color: black;\n"
"")
        self.count_images_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.count_images_label)


        self.verticalLayout_5.addWidget(self.img_count_frame)

        self.image_board_frame = QFrame(self.content_frame)
        self.image_board_frame.setObjectName(u"image_board_frame")
        self.image_board_frame.setMinimumSize(QSize(940, 370))
        self.image_board_frame.setMaximumSize(QSize(16777215, 16777215))
        self.image_board_frame.setFont(font)
        self.image_board_frame.setFrameShape(QFrame.NoFrame)
        self.image_board_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.image_board_frame)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.image_frame = QFrame(self.image_board_frame)
        self.image_frame.setObjectName(u"image_frame")
        self.image_frame.setMinimumSize(QSize(0, 350))
        self.image_frame.setFont(font)
        self.image_frame.setFrameShape(QFrame.Panel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.image_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.image_text_label = QLabel(self.image_frame)
        self.image_text_label.setObjectName(u"image_text_label")
        self.image_text_label.setMinimumSize(QSize(0, 0))
        self.image_text_label.setMaximumSize(QSize(16777215, 20))
        self.image_text_label.setFont(font)
        self.image_text_label.setStyleSheet(u"color: black;")
        self.image_text_label.setLineWidth(1)
        self.image_text_label.setMargin(0)

        self.verticalLayout_2.addWidget(self.image_text_label)

        self.chess_img_label = ClickableLabel(self.image_frame)
        self.chess_img_label.setObjectName(u"chess_img_label")
        self.chess_img_label.setMinimumSize(QSize(300, 300))
        self.chess_img_label.setFont(font)
        self.chess_img_label.setStyleSheet(u"margin-top: 20px;")

        self.verticalLayout_2.addWidget(self.chess_img_label)


        self.horizontalLayout.addWidget(self.image_frame)

        self.board_frame = QFrame(self.image_board_frame)
        self.board_frame.setObjectName(u"board_frame")
        self.board_frame.setMinimumSize(QSize(0, 350))
        self.board_frame.setMaximumSize(QSize(16777215, 16777215))
        self.board_frame.setFont(font)
        self.board_frame.setFrameShape(QFrame.Panel)
        self.board_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.board_frame)
#ifndef Q_OS_MAC
        self.verticalLayout_4.setSpacing(-1)
#endif
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.move_pieces_label = QLabel(self.board_frame)
        self.move_pieces_label.setObjectName(u"move_pieces_label")
        self.move_pieces_label.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(13)
        self.move_pieces_label.setFont(font2)
        self.move_pieces_label.setStyleSheet(u"color: black;\n"
"margin-bottom: 5px;\n"
"padding-top: 5px;")

        self.verticalLayout_4.addWidget(self.move_pieces_label)

        self.chess_graphic_view = QGraphicsView(self.board_frame)
        self.chess_graphic_view.setObjectName(u"chess_graphic_view")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chess_graphic_view.sizePolicy().hasHeightForWidth())
        self.chess_graphic_view.setSizePolicy(sizePolicy)
        self.chess_graphic_view.setMinimumSize(QSize(300, 300))
        self.chess_graphic_view.setMaximumSize(QSize(1200, 16777215))
        self.chess_graphic_view.setFont(font)
        self.chess_graphic_view.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.chess_graphic_view)


        self.horizontalLayout.addWidget(self.board_frame)


        self.verticalLayout_5.addWidget(self.image_board_frame)

        self.generated_fen_frame = QFrame(self.content_frame)
        self.generated_fen_frame.setObjectName(u"generated_fen_frame")
        self.generated_fen_frame.setMaximumSize(QSize(16777215, 70))
        self.generated_fen_frame.setFont(font)
        self.generated_fen_frame.setFrameShape(QFrame.NoFrame)
        self.generated_fen_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.generated_fen_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.generated_fen_label = QLabel(self.generated_fen_frame)
        self.generated_fen_label.setObjectName(u"generated_fen_label")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.generated_fen_label.setFont(font3)
        self.generated_fen_label.setStyleSheet(u"color: black;")

        self.horizontalLayout_2.addWidget(self.generated_fen_label)

        self.generated_fen_text_edit = QTextEdit(self.generated_fen_frame)
        self.generated_fen_text_edit.setObjectName(u"generated_fen_text_edit")
        self.generated_fen_text_edit.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        self.generated_fen_text_edit.setFont(font4)
        self.generated_fen_text_edit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid #ff6e40;\n"
"color: black;\n"
"text-align: center;")

        self.horizontalLayout_2.addWidget(self.generated_fen_text_edit)


        self.verticalLayout_5.addWidget(self.generated_fen_frame)

        self.btns_frame = QFrame(self.content_frame)
        self.btns_frame.setObjectName(u"btns_frame")
        self.btns_frame.setMaximumSize(QSize(16777215, 70))
        self.btns_frame.setFont(font)
        self.btns_frame.setFrameShape(QFrame.NoFrame)
        self.btns_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.btns_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cancel_validation_btn = QPushButton(self.btns_frame)
        self.cancel_validation_btn.setObjectName(u"cancel_validation_btn")
        self.cancel_validation_btn.setMinimumSize(QSize(180, 35))
        self.cancel_validation_btn.setMaximumSize(QSize(160, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setBold(True)
        self.cancel_validation_btn.setFont(font5)
        self.cancel_validation_btn.setStyleSheet(u"QPushButton{\n"
"	background-color : #343a40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #5a6268};")
        icon = QIcon()
        icon.addFile(u":/assets/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_validation_btn.setIcon(icon)
        self.cancel_validation_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.cancel_validation_btn)

        self.save_validation_btn = QPushButton(self.btns_frame)
        self.save_validation_btn.setObjectName(u"save_validation_btn")
        self.save_validation_btn.setMinimumSize(QSize(180, 35))
        self.save_validation_btn.setMaximumSize(QSize(160, 16777215))
        self.save_validation_btn.setFont(font5)
        self.save_validation_btn.setStyleSheet(u"QPushButton{\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_validation_btn.setIcon(icon1)
        self.save_validation_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.save_validation_btn)


        self.verticalLayout_5.addWidget(self.btns_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(ValidationWindow)

        QMetaObject.connectSlotsByName(ValidationWindow)
    # setupUi

    def retranslateUi(self, ValidationWindow):
        ValidationWindow.setWindowTitle(QCoreApplication.translate("ValidationWindow", u"Form", None))
        self.count_images_label.setText(QCoreApplication.translate("ValidationWindow", u"One image out of 100", None))
        self.image_text_label.setText(QCoreApplication.translate("ValidationWindow", u"Image", None))
        self.chess_img_label.setText("")
        self.move_pieces_label.setText(QCoreApplication.translate("ValidationWindow", u"Move the pieces to generate new fen", None))
        self.generated_fen_label.setText(QCoreApplication.translate("ValidationWindow", u"Generated FEN: ", None))
        self.cancel_validation_btn.setText(QCoreApplication.translate("ValidationWindow", u"Cancel", None))
        self.save_validation_btn.setText(QCoreApplication.translate("ValidationWindow", u"Validate and Save", None))
    # retranslateUi

