# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_manager_component.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ComboBox, LineEdit, PushButton, TableWidget,
    TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(617, 488)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        self.TitleLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.TitleLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.TitleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TableWidget = TableWidget(Form)
        if (self.TableWidget.columnCount() < 2):
            self.TableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.TableWidget.setShowGrid(False)
        self.TableWidget.setSortingEnabled(True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)
        self.TableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout.addWidget(self.TableWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LineEdit = LineEdit(Form)
        self.LineEdit.setObjectName(u"LineEdit")
        sizePolicy.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.LineEdit)

        self.LineEdit_2 = LineEdit(Form)
        self.LineEdit_2.setObjectName(u"LineEdit_2")
        sizePolicy.setHeightForWidth(self.LineEdit_2.sizePolicy().hasHeightForWidth())
        self.LineEdit_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.LineEdit_2)

        self.ComboBox = ComboBox(Form)
        self.ComboBox.setObjectName(u"ComboBox")

        self.verticalLayout.addWidget(self.ComboBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.PushButton = PushButton(Form)
        self.PushButton.setObjectName(u"PushButton")

        self.verticalLayout.addWidget(self.PushButton)

        self.PushButton_2 = PushButton(Form)
        self.PushButton_2.setObjectName(u"PushButton_2")

        self.verticalLayout.addWidget(self.PushButton_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u8d26\u53f7\u7ba1\u7406", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u6743\u9650", None));
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.LineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.ComboBox.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6743\u9650", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u8d26\u6237", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u8d26\u6237", None))
    # retranslateUi

