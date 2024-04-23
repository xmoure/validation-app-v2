# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class EditWindow(object):
    def setupUi(self, EditWindow):
        if not EditWindow.objectName():
            EditWindow.setObjectName(u"EditWindow")
        EditWindow.resize(500, 300)
        EditWindow.setMinimumSize(QSize(500, 300))
        EditWindow.setMaximumSize(QSize(500, 300))
        self.verticalLayout = QVBoxLayout(EditWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_widget_frame = QFrame(EditWindow)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.central_widget_frame.setFont(font)
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
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
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 20, 0, 20)
        self.fields_frame = QFrame(self.content_frame)
        self.fields_frame.setObjectName(u"fields_frame")
        self.fields_frame.setMinimumSize(QSize(0, 0))
        self.fields_frame.setMaximumSize(QSize(16777215, 50))
        self.fields_frame.setFont(font)
        self.fields_frame.setFrameShape(QFrame.NoFrame)
        self.fields_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fields_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 12, -1, -1)
        self.chess_material_label = QLabel(self.fields_frame)
        self.chess_material_label.setObjectName(u"chess_material_label")
        self.chess_material_label.setMaximumSize(QSize(150, 16777215))
        self.chess_material_label.setFont(font)

        self.horizontalLayout.addWidget(self.chess_material_label)

        self.material_combobox = QComboBox(self.fields_frame)
        self.material_combobox.setObjectName(u"material_combobox")
        self.material_combobox.setFont(font)
        self.material_combobox.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.material_combobox)


        self.verticalLayout_2.addWidget(self.fields_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_frame = QFrame(self.content_frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setFont(font)
        self.btn_frame.setFrameShape(QFrame.NoFrame)
        self.btn_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.btn_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancel_btn = QPushButton(self.btn_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 30))
        self.cancel_btn.setMaximumSize(QSize(16777215, 30))
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"	background-color : #343a40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #5a6268};")
        icon = QIcon()
        icon.addFile(u":/assets/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_btn.setIcon(icon)
        self.cancel_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(self.btn_frame)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 30))
        self.save_btn.setMaximumSize(QSize(16777215, 30))
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon1)
        self.save_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.save_btn)


        self.verticalLayout_2.addWidget(self.btn_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(EditWindow)

        QMetaObject.connectSlotsByName(EditWindow)
    # setupUi

    def retranslateUi(self, EditWindow):
        EditWindow.setWindowTitle(QCoreApplication.translate("EditWindow", u"Form", None))
        self.chess_material_label.setText(QCoreApplication.translate("EditWindow", u"Chess board material: ", None))
        self.cancel_btn.setText(QCoreApplication.translate("EditWindow", u"Cancel", None))
        self.save_btn.setText(QCoreApplication.translate("EditWindow", u"Save", None))
    # retranslateUi

