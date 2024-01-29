# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chart_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, IconWidget, LargeTitleLabel,
    SimpleCardWidget, SmoothScrollArea, VerticalSeparator)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(977, 739)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 959, 721))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
        self.SimpleCardWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.horizontalLayout_3 = QHBoxLayout(self.SimpleCardWidget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.IconWidget = IconWidget(self.SimpleCardWidget)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(36, 36))
        self.IconWidget.setMaximumSize(QSize(84, 84))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/chart_bar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.IconWidget)

        self.VerticalSeparator = VerticalSeparator(self.SimpleCardWidget)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout_3.addWidget(self.VerticalSeparator)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LargeTitleLabel.sizePolicy().hasHeightForWidth())
        self.LargeTitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.LargeTitleLabel)

        self.BodyLabel_7 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        sizePolicy1.setHeightForWidth(self.BodyLabel_7.sizePolicy().hasHeightForWidth())
        self.BodyLabel_7.setSizePolicy(sizePolicy1)
        self.BodyLabel_7.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_14.addWidget(self.BodyLabel_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_2.addWidget(self.SimpleCardWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u56fe\u8868(\u7b49\u5f85\u65bd\u5de5)", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u56fe\u8868\u76f4\u89c2\u7684\u89c2\u5bdf\u6570\u636e\u5e93", None))
    # retranslateUi

