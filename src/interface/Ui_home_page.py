# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ElevatedCardWidget, HorizontalSeparator,
    IconWidget, LargeTitleLabel, SimpleCardWidget, SmoothScrollArea,
    SubtitleLabel, TitleLabel, ToolButton, VerticalSeparator)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(969, 739)
        self.verticalLayout_21 = QVBoxLayout(Form)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setLineWidth(1)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 951, 721))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.SimpleCardWidget = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.SimpleCardWidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.SimpleCardWidget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.IconWidget = IconWidget(self.SimpleCardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(36, 36))
        self.IconWidget.setMaximumSize(QSize(84, 84))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/billboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.IconWidget)

        self.VerticalSeparator = VerticalSeparator(self.SimpleCardWidget)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout_3.addWidget(self.VerticalSeparator)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LargeTitleLabel.sizePolicy().hasHeightForWidth())
        self.LargeTitleLabel.setSizePolicy(sizePolicy1)
        self.LargeTitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.LargeTitleLabel)

        self.BodyLabel_7 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        sizePolicy1.setHeightForWidth(self.BodyLabel_7.sizePolicy().hasHeightForWidth())
        self.BodyLabel_7.setSizePolicy(sizePolicy1)
        self.BodyLabel_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BodyLabel_7.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_14.addWidget(self.BodyLabel_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.ToolButton = ToolButton(self.SimpleCardWidget)
        self.ToolButton.setObjectName(u"ToolButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/available_updates.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolButton.setIcon(icon1)

        self.verticalLayout_16.addWidget(self.ToolButton)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_16.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_16)


        self.verticalLayout_48.addWidget(self.SimpleCardWidget)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_48.addItem(self.verticalSpacer_3)

        self.SubtitleLabel_2 = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        self.SubtitleLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.SubtitleLabel_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ElevatedCardWidget_5 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_5.setObjectName(u"ElevatedCardWidget_5")
        self.ElevatedCardWidget_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_5.setLineWidth(1)
        self.ElevatedCardWidget_5.setBorderRadius(10)
        self.verticalLayout_9 = QVBoxLayout(self.ElevatedCardWidget_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.TitleLabel_5 = TitleLabel(self.ElevatedCardWidget_5)
        self.TitleLabel_5.setObjectName(u"TitleLabel_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TitleLabel_5.sizePolicy().hasHeightForWidth())
        self.TitleLabel_5.setSizePolicy(sizePolicy2)
        self.TitleLabel_5.setMinimumSize(QSize(0, 0))
        self.TitleLabel_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.TitleLabel_5)

        self.BodyLabel_5 = BodyLabel(self.ElevatedCardWidget_5)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")
        sizePolicy1.setHeightForWidth(self.BodyLabel_5.sizePolicy().hasHeightForWidth())
        self.BodyLabel_5.setSizePolicy(sizePolicy1)
        self.BodyLabel_5.setAlignment(Qt.AlignCenter)
        self.BodyLabel_5.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_10.addWidget(self.BodyLabel_5)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.horizontalLayout_2.addWidget(self.ElevatedCardWidget_5)

        self.ElevatedCardWidget_6 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_6.setObjectName(u"ElevatedCardWidget_6")
        self.ElevatedCardWidget_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_6.setLineWidth(1)
        self.ElevatedCardWidget_6.setBorderRadius(10)
        self.verticalLayout_11 = QVBoxLayout(self.ElevatedCardWidget_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.TitleLabel_6 = TitleLabel(self.ElevatedCardWidget_6)
        self.TitleLabel_6.setObjectName(u"TitleLabel_6")
        sizePolicy2.setHeightForWidth(self.TitleLabel_6.sizePolicy().hasHeightForWidth())
        self.TitleLabel_6.setSizePolicy(sizePolicy2)
        self.TitleLabel_6.setMinimumSize(QSize(0, 0))
        self.TitleLabel_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.TitleLabel_6)

        self.BodyLabel_6 = BodyLabel(self.ElevatedCardWidget_6)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")
        sizePolicy1.setHeightForWidth(self.BodyLabel_6.sizePolicy().hasHeightForWidth())
        self.BodyLabel_6.setSizePolicy(sizePolicy1)
        self.BodyLabel_6.setAlignment(Qt.AlignCenter)
        self.BodyLabel_6.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_12.addWidget(self.BodyLabel_6)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.horizontalLayout_2.addWidget(self.ElevatedCardWidget_6)


        self.verticalLayout_48.addLayout(self.horizontalLayout_2)

        self.HorizontalSeparator = HorizontalSeparator(self.scrollAreaWidgetContents)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")

        self.verticalLayout_48.addWidget(self.HorizontalSeparator)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ElevatedCardWidget = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.ElevatedCardWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget.setLineWidth(1)
        self.ElevatedCardWidget.setBorderRadius(10)
        self.verticalLayout_2 = QVBoxLayout(self.ElevatedCardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = TitleLabel(self.ElevatedCardWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy2.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy2)
        self.TitleLabel.setMinimumSize(QSize(0, 0))
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.TitleLabel)

        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy1.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy1)
        self.BodyLabel.setAlignment(Qt.AlignCenter)
        self.BodyLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout.addWidget(self.BodyLabel)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget)

        self.ElevatedCardWidget_4 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_4.setObjectName(u"ElevatedCardWidget_4")
        self.ElevatedCardWidget_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_4.setLineWidth(1)
        self.ElevatedCardWidget_4.setBorderRadius(10)
        self.verticalLayout_7 = QVBoxLayout(self.ElevatedCardWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.TitleLabel_4 = TitleLabel(self.ElevatedCardWidget_4)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")
        sizePolicy2.setHeightForWidth(self.TitleLabel_4.sizePolicy().hasHeightForWidth())
        self.TitleLabel_4.setSizePolicy(sizePolicy2)
        self.TitleLabel_4.setMinimumSize(QSize(0, 0))
        self.TitleLabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.TitleLabel_4)

        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget_4)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        sizePolicy1.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy1)
        self.BodyLabel_4.setAlignment(Qt.AlignCenter)
        self.BodyLabel_4.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_8.addWidget(self.BodyLabel_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_4)

        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        self.ElevatedCardWidget_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_2.setLineWidth(1)
        self.ElevatedCardWidget_2.setBorderRadius(10)
        self.verticalLayout_3 = QVBoxLayout(self.ElevatedCardWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TitleLabel_2 = TitleLabel(self.ElevatedCardWidget_2)
        self.TitleLabel_2.setObjectName(u"TitleLabel_2")
        sizePolicy2.setHeightForWidth(self.TitleLabel_2.sizePolicy().hasHeightForWidth())
        self.TitleLabel_2.setSizePolicy(sizePolicy2)
        self.TitleLabel_2.setMinimumSize(QSize(0, 0))
        self.TitleLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.TitleLabel_2)

        self.BodyLabel_2 = BodyLabel(self.ElevatedCardWidget_2)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy1.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy1)
        self.BodyLabel_2.setAlignment(Qt.AlignCenter)
        self.BodyLabel_2.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_4.addWidget(self.BodyLabel_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_2)

        self.ElevatedCardWidget_3 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_3.setObjectName(u"ElevatedCardWidget_3")
        self.ElevatedCardWidget_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_3.setLineWidth(1)
        self.ElevatedCardWidget_3.setBorderRadius(10)
        self.verticalLayout_5 = QVBoxLayout(self.ElevatedCardWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.TitleLabel_3 = TitleLabel(self.ElevatedCardWidget_3)
        self.TitleLabel_3.setObjectName(u"TitleLabel_3")
        sizePolicy2.setHeightForWidth(self.TitleLabel_3.sizePolicy().hasHeightForWidth())
        self.TitleLabel_3.setSizePolicy(sizePolicy2)
        self.TitleLabel_3.setMinimumSize(QSize(0, 0))
        self.TitleLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.TitleLabel_3)

        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget_3)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy1.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy1)
        self.BodyLabel_3.setAlignment(Qt.AlignCenter)
        self.BodyLabel_3.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_6.addWidget(self.BodyLabel_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_3)


        self.verticalLayout_48.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(22, 119, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_2)

        self.SubtitleLabel = SubtitleLabel(self.scrollAreaWidgetContents)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_48.addWidget(self.SubtitleLabel)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ElevatedCardWidget_20 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_20.setObjectName(u"ElevatedCardWidget_20")
        self.ElevatedCardWidget_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_20.setLineWidth(1)
        self.ElevatedCardWidget_20.setBorderRadius(10)
        self.verticalLayout_44 = QVBoxLayout(self.ElevatedCardWidget_20)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.TitleLabel_20 = TitleLabel(self.ElevatedCardWidget_20)
        self.TitleLabel_20.setObjectName(u"TitleLabel_20")
        sizePolicy2.setHeightForWidth(self.TitleLabel_20.sizePolicy().hasHeightForWidth())
        self.TitleLabel_20.setSizePolicy(sizePolicy2)
        self.TitleLabel_20.setMinimumSize(QSize(0, 0))
        self.TitleLabel_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.TitleLabel_20)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.BodyLabel_22 = BodyLabel(self.ElevatedCardWidget_20)
        self.BodyLabel_22.setObjectName(u"BodyLabel_22")
        sizePolicy1.setHeightForWidth(self.BodyLabel_22.sizePolicy().hasHeightForWidth())
        self.BodyLabel_22.setSizePolicy(sizePolicy1)
        self.BodyLabel_22.setAlignment(Qt.AlignCenter)
        self.BodyLabel_22.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_45.addWidget(self.BodyLabel_22)


        self.verticalLayout_44.addLayout(self.verticalLayout_45)


        self.horizontalLayout_8.addWidget(self.ElevatedCardWidget_20)

        self.ElevatedCardWidget_21 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_21.setObjectName(u"ElevatedCardWidget_21")
        self.ElevatedCardWidget_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_21.setLineWidth(1)
        self.ElevatedCardWidget_21.setBorderRadius(10)
        self.verticalLayout_46 = QVBoxLayout(self.ElevatedCardWidget_21)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.TitleLabel_21 = TitleLabel(self.ElevatedCardWidget_21)
        self.TitleLabel_21.setObjectName(u"TitleLabel_21")
        sizePolicy2.setHeightForWidth(self.TitleLabel_21.sizePolicy().hasHeightForWidth())
        self.TitleLabel_21.setSizePolicy(sizePolicy2)
        self.TitleLabel_21.setMinimumSize(QSize(0, 0))
        self.TitleLabel_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.TitleLabel_21)

        self.BodyLabel_23 = BodyLabel(self.ElevatedCardWidget_21)
        self.BodyLabel_23.setObjectName(u"BodyLabel_23")
        sizePolicy1.setHeightForWidth(self.BodyLabel_23.sizePolicy().hasHeightForWidth())
        self.BodyLabel_23.setSizePolicy(sizePolicy1)
        self.BodyLabel_23.setAlignment(Qt.AlignCenter)
        self.BodyLabel_23.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_47.addWidget(self.BodyLabel_23)


        self.verticalLayout_46.addLayout(self.verticalLayout_47)


        self.horizontalLayout_8.addWidget(self.ElevatedCardWidget_21)


        self.verticalLayout_48.addLayout(self.horizontalLayout_8)

        self.HorizontalSeparator_3 = HorizontalSeparator(self.scrollAreaWidgetContents)
        self.HorizontalSeparator_3.setObjectName(u"HorizontalSeparator_3")

        self.verticalLayout_48.addWidget(self.HorizontalSeparator_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ElevatedCardWidget_7 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_7.setObjectName(u"ElevatedCardWidget_7")
        self.ElevatedCardWidget_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_7.setLineWidth(1)
        self.ElevatedCardWidget_7.setBorderRadius(10)
        self.verticalLayout_13 = QVBoxLayout(self.ElevatedCardWidget_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.TitleLabel_7 = TitleLabel(self.ElevatedCardWidget_7)
        self.TitleLabel_7.setObjectName(u"TitleLabel_7")
        sizePolicy2.setHeightForWidth(self.TitleLabel_7.sizePolicy().hasHeightForWidth())
        self.TitleLabel_7.setSizePolicy(sizePolicy2)
        self.TitleLabel_7.setMinimumSize(QSize(0, 0))
        self.TitleLabel_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.TitleLabel_7)

        self.BodyLabel_8 = BodyLabel(self.ElevatedCardWidget_7)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")
        sizePolicy1.setHeightForWidth(self.BodyLabel_8.sizePolicy().hasHeightForWidth())
        self.BodyLabel_8.setSizePolicy(sizePolicy1)
        self.BodyLabel_8.setAlignment(Qt.AlignCenter)
        self.BodyLabel_8.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_15.addWidget(self.BodyLabel_8)


        self.verticalLayout_13.addLayout(self.verticalLayout_15)


        self.horizontalLayout_7.addWidget(self.ElevatedCardWidget_7)

        self.ElevatedCardWidget_8 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_8.setObjectName(u"ElevatedCardWidget_8")
        self.ElevatedCardWidget_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_8.setLineWidth(1)
        self.ElevatedCardWidget_8.setBorderRadius(10)
        self.verticalLayout_17 = QVBoxLayout(self.ElevatedCardWidget_8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.TitleLabel_8 = TitleLabel(self.ElevatedCardWidget_8)
        self.TitleLabel_8.setObjectName(u"TitleLabel_8")
        sizePolicy2.setHeightForWidth(self.TitleLabel_8.sizePolicy().hasHeightForWidth())
        self.TitleLabel_8.setSizePolicy(sizePolicy2)
        self.TitleLabel_8.setMinimumSize(QSize(0, 0))
        self.TitleLabel_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.TitleLabel_8)

        self.BodyLabel_9 = BodyLabel(self.ElevatedCardWidget_8)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")
        sizePolicy1.setHeightForWidth(self.BodyLabel_9.sizePolicy().hasHeightForWidth())
        self.BodyLabel_9.setSizePolicy(sizePolicy1)
        self.BodyLabel_9.setAlignment(Qt.AlignCenter)
        self.BodyLabel_9.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_18.addWidget(self.BodyLabel_9)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.horizontalLayout_7.addWidget(self.ElevatedCardWidget_8)

        self.ElevatedCardWidget_9 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_9.setObjectName(u"ElevatedCardWidget_9")
        self.ElevatedCardWidget_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_9.setLineWidth(1)
        self.ElevatedCardWidget_9.setBorderRadius(10)
        self.verticalLayout_19 = QVBoxLayout(self.ElevatedCardWidget_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.TitleLabel_9 = TitleLabel(self.ElevatedCardWidget_9)
        self.TitleLabel_9.setObjectName(u"TitleLabel_9")
        sizePolicy2.setHeightForWidth(self.TitleLabel_9.sizePolicy().hasHeightForWidth())
        self.TitleLabel_9.setSizePolicy(sizePolicy2)
        self.TitleLabel_9.setMinimumSize(QSize(0, 0))
        self.TitleLabel_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.TitleLabel_9)

        self.BodyLabel_10 = BodyLabel(self.ElevatedCardWidget_9)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")
        sizePolicy1.setHeightForWidth(self.BodyLabel_10.sizePolicy().hasHeightForWidth())
        self.BodyLabel_10.setSizePolicy(sizePolicy1)
        self.BodyLabel_10.setAlignment(Qt.AlignCenter)
        self.BodyLabel_10.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_20.addWidget(self.BodyLabel_10)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)


        self.horizontalLayout_7.addWidget(self.ElevatedCardWidget_9)

        self.ElevatedCardWidget_19 = ElevatedCardWidget(self.scrollAreaWidgetContents)
        self.ElevatedCardWidget_19.setObjectName(u"ElevatedCardWidget_19")
        self.ElevatedCardWidget_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.ElevatedCardWidget_19.setLineWidth(1)
        self.ElevatedCardWidget_19.setBorderRadius(10)
        self.verticalLayout_42 = QVBoxLayout(self.ElevatedCardWidget_19)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.TitleLabel_19 = TitleLabel(self.ElevatedCardWidget_19)
        self.TitleLabel_19.setObjectName(u"TitleLabel_19")
        sizePolicy2.setHeightForWidth(self.TitleLabel_19.sizePolicy().hasHeightForWidth())
        self.TitleLabel_19.setSizePolicy(sizePolicy2)
        self.TitleLabel_19.setMinimumSize(QSize(0, 0))
        self.TitleLabel_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.TitleLabel_19)

        self.BodyLabel_21 = BodyLabel(self.ElevatedCardWidget_19)
        self.BodyLabel_21.setObjectName(u"BodyLabel_21")
        sizePolicy1.setHeightForWidth(self.BodyLabel_21.sizePolicy().hasHeightForWidth())
        self.BodyLabel_21.setSizePolicy(sizePolicy1)
        self.BodyLabel_21.setAlignment(Qt.AlignCenter)
        self.BodyLabel_21.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_43.addWidget(self.BodyLabel_21)


        self.verticalLayout_42.addLayout(self.verticalLayout_43)


        self.horizontalLayout_7.addWidget(self.ElevatedCardWidget_19)


        self.verticalLayout_48.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_48.addItem(self.verticalSpacer_7)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_21.addWidget(self.SmoothScrollArea)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u9762\u677f", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u6570\u636e\u9762\u677f\u4ee5\u4fbf\u76f4\u89c2\u7684\u89c2\u5bdf\u5f53\u524d\u4ed3\u5e93\u7684\u60c5\u51b5,\u70b9\u51fb\u4e0b\u65b9\u65b9\u683c\u67e5\u770b\u8be6\u7ec6\u4fe1\u606f", None))
        self.ToolButton.setText("")
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u672c\u6708\u73b0\u72b6", None))
        self.TitleLabel_5.setText(QCoreApplication.translate("Form", u"2024\u5e741\u6708\u7b2c1\u6279", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u6279\u6b21", None))
        self.TitleLabel_6.setText(QCoreApplication.translate("Form", u"2024\u5e741\u6708\u7b2c1\u6ce2", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u6ce2\u6b21", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"100", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u603b\u91cf", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("Form", u"51344677", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u91d1\u989d", None))
        self.TitleLabel_2.setText(QCoreApplication.translate("Form", u"513", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u672c\u6708\u8fdb\u8d27", None))
        self.TitleLabel_3.setText(QCoreApplication.translate("Form", u"471", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u672c\u6708\u552e\u51fa", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u521b\u4e1a\u56de\u987e", None))
        self.TitleLabel_20.setText(QCoreApplication.translate("Form", u"31", None))
        self.BodyLabel_22.setText(QCoreApplication.translate("Form", u"\u603b\u6279\u6b21\u6570", None))
        self.TitleLabel_21.setText(QCoreApplication.translate("Form", u"52", None))
        self.BodyLabel_23.setText(QCoreApplication.translate("Form", u"\u603b\u6ce2\u6b21\u6570", None))
        self.TitleLabel_7.setText(QCoreApplication.translate("Form", u"56541", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Form", u"\u4ed3\u5e93\u8fc7\u5f80\u5b58\u50a8\u603b\u6570", None))
        self.TitleLabel_8.setText(QCoreApplication.translate("Form", u"100000000", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Form", u"\u603b\u6295\u5165", None))
        self.TitleLabel_9.setText(QCoreApplication.translate("Form", u"75213", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Form", u"\u8fc7\u5f80\u6240\u6709\u8fdb\u8d27\u6570\u91cf", None))
        self.TitleLabel_19.setText(QCoreApplication.translate("Form", u"75213", None))
        self.BodyLabel_21.setText(QCoreApplication.translate("Form", u"\u8fc7\u5f80\u6240\u6709\u552e\u51fa\u6570\u91cf", None))
    # retranslateUi

