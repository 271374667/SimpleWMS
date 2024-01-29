# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QSizePolicy, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, IconWidget, LargeTitleLabel,
    LineEdit, SearchLineEdit, SimpleCardWidget, SmoothScrollArea,
    TableWidget, VerticalSeparator)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(978, 738)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 948, 708))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SimpleCardWidget = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget.setObjectName(u"SimpleCardWidget")
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
        icon.addFile(u":/icons/images/icons/database_administrator.svg", QSize(), QIcon.Normal, QIcon.Off)
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.SearchLineEdit = SearchLineEdit(self.scrollAreaWidgetContents)
        self.SearchLineEdit.setObjectName(u"SearchLineEdit")

        self.horizontalLayout.addWidget(self.SearchLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.TableWidget = TableWidget(self.scrollAreaWidgetContents)
        if (self.TableWidget.columnCount() < 5):
            self.TableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.TableWidget.rowCount() < 100):
            self.TableWidget.setRowCount(100)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setRowCount(100)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.TableWidget)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u64cd\u4f5c(\u7b49\u5f85\u65bd\u5de5)", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u76f4\u63a5\u64cd\u4f5c\u6570\u636e\u5e93\u4fee\u6539\u5f02\u5e38\u6570\u636e(\u6ce8\u610f\uff0c\u6b64\u64cd\u4f5c\u6709\u4e00\u5b9a\u98ce\u9669)", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u4ece\u6570\u636e\u5e93\u4e2d\u641c\u7d22:", None))
        self.SearchLineEdit.setInputMask(QCoreApplication.translate("Form", u"9999999999999", None))
        self.SearchLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165EAN13\u7801", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u54c1\u724c", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u6279\u6b21", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"EAN13\u7801", None));
        ___qtablewidgetitem5 = self.TableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem6 = self.TableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem7 = self.TableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"3", None));
    # retranslateUi

