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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, IconWidget,
    LargeTitleLabel, PrimaryPushButton, PushButton, SimpleCardWidget,
    SmoothScrollArea, StrongBodyLabel, VerticalSeparator)
from qframelesswindow.webengine import FramelessWebEngineView
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

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.BodyLabel_2 = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.BodyLabel_2)

        self.ComboBox = ComboBox(self.scrollAreaWidgetContents)
        self.ComboBox.setObjectName(u"ComboBox")

        self.horizontalLayout_2.addWidget(self.ComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.BodyLabel_3 = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy2.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.BodyLabel_3)

        self.ComboBox_2 = ComboBox(self.scrollAreaWidgetContents)
        self.ComboBox_2.setObjectName(u"ComboBox_2")
        self.ComboBox_2.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.ComboBox_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.StrongBodyLabel = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        sizePolicy1.setHeightForWidth(self.StrongBodyLabel.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.StrongBodyLabel)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_2.addWidget(self.widget)

        self.PrimaryPushButton = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.verticalLayout_2.addWidget(self.PrimaryPushButton)

        self.widget_2 = FramelessWebEngineView(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setMinimumSize(QSize(0, 400))
        self.widget_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_2.addWidget(self.widget_2)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u56fe\u8868", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u56fe\u8868\u76f4\u89c2\u7684\u89c2\u5bdf\u6570\u636e\u5e93", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7edf\u8ba1\u6a21\u5f0f:", None))
#if QT_CONFIG(tooltip)
        self.ComboBox.setToolTip(QCoreApplication.translate("Form", u"\u53ef\u4ee5\u9009\u62e9\u4e0d\u540c\u7684\u89d2\u5ea6\u6765\u89c2\u5bdf\u6570\u636e,\u6bd4\u5982\u67e5\u770b\u9000\u8d27\u7387,\u552e\u51fa\u7387\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.ComboBox.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u60a8\u9700\u8981\u53ef\u89c6\u5316\u7684\u5185\u5bb9", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u56fe\u8868\u6837\u5f0f:", None))
#if QT_CONFIG(tooltip)
        self.ComboBox_2.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9\u7ed8\u5236\u4e0d\u540c\u7c7b\u578b\u7684\u56fe\u6807,\u6bd4\u5982\u6298\u7ebf\u56fe,\u76f4\u65b9\u56fe\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.ComboBox_2.setText(QCoreApplication.translate("Form", u"\u5728\u6b64\u5904\u9009\u62e9\u60a8\u5177\u4f53\u9700\u8981\u7ed8\u5236\u7684\u6837\u5f0f", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u914d\u7f6e:\u5f53\u524d\u6ca1\u6709\u9009\u62e9\u4efb\u4f55\u6a21\u5f0f", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u7ed8\u5236\u56fe\u8868", None))
    # retranslateUi

