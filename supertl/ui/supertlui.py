# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supertl.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_supertl_ui(object):
    def setupUi(self, supertl_ui):
        if not supertl_ui.objectName():
            supertl_ui.setObjectName(u"supertl_ui")
        supertl_ui.resize(800, 600)
        supertl_ui.setMinimumSize(QSize(800, 600))
        self.verticalLayout = QVBoxLayout(supertl_ui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(supertl_ui)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.main_app_frame = QFrame(supertl_ui)
        self.main_app_frame.setObjectName(u"main_app_frame")
        self.main_app_frame.setStyleSheet(u"background-color: #aaaa00;")
        self.main_app_frame.setFrameShape(QFrame.StyledPanel)
        self.main_app_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_app_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar_frame = QFrame(self.main_app_frame)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_frame.setStyleSheet(u"background-color: #550055;")
        self.sidebar_frame.setFrameShape(QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.calendar_widget = QWidget(self.sidebar_frame)
        self.calendar_widget.setObjectName(u"calendar_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendar_widget.sizePolicy().hasHeightForWidth())
        self.calendar_widget.setSizePolicy(sizePolicy1)
        self.calendar_widget.setMinimumSize(QSize(400, 600))
        self.calendar_widget.setMaximumSize(QSize(400, 600))
        self.calendar_widget.setStyleSheet(u"background-color: #5555aa;")

        self.verticalLayout_2.addWidget(self.calendar_widget)

        self.activity_buttons_frame = QFrame(self.sidebar_frame)
        self.activity_buttons_frame.setObjectName(u"activity_buttons_frame")
        self.activity_buttons_frame.setStyleSheet(u"background-color: #004444;")
        self.activity_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.activity_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.activity_buttons_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.activity_buttons_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.activity_buttons_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.activity_buttons_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.activity_buttons_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.activity_buttons_frame)

        self.log_buttons_frame = QFrame(self.sidebar_frame)
        self.log_buttons_frame.setObjectName(u"log_buttons_frame")
        self.log_buttons_frame.setStyleSheet(u"background-color: #aa0000;")
        self.log_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.log_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.log_buttons_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_6 = QPushButton(self.log_buttons_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.log_buttons_frame)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_4.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.log_buttons_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_4.addWidget(self.pushButton_9)


        self.verticalLayout_2.addWidget(self.log_buttons_frame)

        self.filler_frame = QFrame(self.sidebar_frame)
        self.filler_frame.setObjectName(u"filler_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.filler_frame.sizePolicy().hasHeightForWidth())
        self.filler_frame.setSizePolicy(sizePolicy2)
        self.filler_frame.setStyleSheet(u"background-color: #00AA00;")
        self.filler_frame.setFrameShape(QFrame.StyledPanel)
        self.filler_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.filler_frame)


        self.horizontalLayout.addWidget(self.sidebar_frame)

        self.primary_frame = QFrame(self.main_app_frame)
        self.primary_frame.setObjectName(u"primary_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.primary_frame.sizePolicy().hasHeightForWidth())
        self.primary_frame.setSizePolicy(sizePolicy3)
        self.primary_frame.setStyleSheet(u"background-color: #00aa55;")
        self.primary_frame.setFrameShape(QFrame.StyledPanel)
        self.primary_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.primary_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.primary_frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.weekly_summary_widget = QWidget(self.splitter)
        self.weekly_summary_widget.setObjectName(u"weekly_summary_widget")
        self.weekly_summary_widget.setStyleSheet(u"background-color: #0000FF;")
        self.pushButton_7 = QPushButton(self.weekly_summary_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(540, 270, 85, 28))
        self.splitter.addWidget(self.weekly_summary_widget)
        self.activity_detail_frame = QFrame(self.splitter)
        self.activity_detail_frame.setObjectName(u"activity_detail_frame")
        self.activity_detail_frame.setStyleSheet(u"background-color: #FF00FF;")
        self.activity_detail_frame.setFrameShape(QFrame.StyledPanel)
        self.activity_detail_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.activity_detail_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_2 = QSplitter(self.activity_detail_frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.activity_summary_widget = QWidget(self.splitter_2)
        self.activity_summary_widget.setObjectName(u"activity_summary_widget")
        self.activity_summary_widget.setStyleSheet(u"background-color: #FFFF00;")
        self.pushButton_10 = QPushButton(self.activity_summary_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(250, 200, 85, 28))
        self.splitter_2.addWidget(self.activity_summary_widget)
        self.activity_map_widget = QWidget(self.splitter_2)
        self.activity_map_widget.setObjectName(u"activity_map_widget")
        self.activity_map_widget.setStyleSheet(u"background-color: #00FFFF;")
        self.pushButton_11 = QPushButton(self.activity_map_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(210, 200, 85, 28))
        self.splitter_2.addWidget(self.activity_map_widget)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.activity_detail_frame)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.primary_frame)


        self.verticalLayout.addWidget(self.main_app_frame)


        self.retranslateUi(supertl_ui)

        QMetaObject.connectSlotsByName(supertl_ui)
    # setupUi

    def retranslateUi(self, supertl_ui):
        supertl_ui.setWindowTitle(QCoreApplication.translate("supertl_ui", u"QT Design Super TL Layout", None))
        self.pushButton.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("supertl_ui", u"PushButton", None))
    # retranslateUi

