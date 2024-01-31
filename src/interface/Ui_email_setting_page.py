# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_setting_page.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, LineEdit, PasswordLineEdit, PrimaryPushButton,
    PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(267, 190)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BodyLabel_2 = BodyLabel(Form)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout.addWidget(self.BodyLabel_2, 1, 0, 1, 1)

        self.BodyLabel = BodyLabel(Form)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1)

        self.PasswordLineEdit = PasswordLineEdit(Form)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")

        self.gridLayout.addWidget(self.PasswordLineEdit, 1, 1, 1, 1)

        self.LineEdit = LineEdit(Form)
        self.LineEdit.setObjectName(u"LineEdit")

        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)

        self.PrimaryPushButton = PrimaryPushButton(Form)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.gridLayout.addWidget(self.PrimaryPushButton, 2, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u79d8\u94a5:", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7:", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u8bbe\u7f6e", None))
    # retranslateUi

