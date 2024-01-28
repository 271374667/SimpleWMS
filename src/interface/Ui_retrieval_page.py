# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retrieval_page.ui'
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
    QHeaderView, QSizePolicy, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, CardWidget, HorizontalSeparator,
    IconWidget, LargeTitleLabel, LineEdit, PlainTextEdit,
    PushButton, SimpleCardWidget, SmoothScrollArea, SubtitleLabel,
    TableWidget, VerticalSeparator)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(975, 738)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 957, 720))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SimpleCardWidget_2 = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget_2.setObjectName(u"SimpleCardWidget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.SimpleCardWidget_2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.IconWidget = IconWidget(self.SimpleCardWidget_2)
        self.IconWidget.setObjectName(u"IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(36, 36))
        self.IconWidget.setMaximumSize(QSize(84, 84))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/sign_out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.IconWidget.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.IconWidget)

        self.VerticalSeparator = VerticalSeparator(self.SimpleCardWidget_2)
        self.VerticalSeparator.setObjectName(u"VerticalSeparator")

        self.horizontalLayout_2.addWidget(self.VerticalSeparator)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget_2)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LargeTitleLabel.sizePolicy().hasHeightForWidth())
        self.LargeTitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.LargeTitleLabel)

        self.BodyLabel_7 = BodyLabel(self.SimpleCardWidget_2)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        sizePolicy1.setHeightForWidth(self.BodyLabel_7.sizePolicy().hasHeightForWidth())
        self.BodyLabel_7.setSizePolicy(sizePolicy1)
        self.BodyLabel_7.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_14.addWidget(self.BodyLabel_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_14)

        self.VerticalSeparator_2 = VerticalSeparator(self.SimpleCardWidget_2)
        self.VerticalSeparator_2.setObjectName(u"VerticalSeparator_2")

        self.horizontalLayout_2.addWidget(self.VerticalSeparator_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.LineEdit = LineEdit(self.SimpleCardWidget_2)
        self.LineEdit.setObjectName(u"LineEdit")
        sizePolicy1.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy1)
        self.LineEdit.setMinimumSize(QSize(15, 33))

        self.gridLayout_2.addWidget(self.LineEdit, 1, 0, 1, 1)

        self.PushButton_2 = PushButton(self.SimpleCardWidget_2)
        self.PushButton_2.setObjectName(u"PushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PushButton_2.sizePolicy().hasHeightForWidth())
        self.PushButton_2.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.PushButton_2, 1, 1, 1, 1)

        self.SubtitleLabel_2 = SubtitleLabel(self.SimpleCardWidget_2)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SubtitleLabel_2.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_2.setSizePolicy(sizePolicy3)
        self.SubtitleLabel_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.SubtitleLabel_2, 0, 0, 1, 2)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.SimpleCardWidget_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.SimpleCardWidget_3 = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.verticalLayout_18 = QVBoxLayout(self.SimpleCardWidget_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.SubtitleLabel = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        sizePolicy1.setHeightForWidth(self.SubtitleLabel.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_17.addWidget(self.SubtitleLabel)

        self.CaptionLabel = CaptionLabel(self.SimpleCardWidget_3)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        sizePolicy1.setHeightForWidth(self.CaptionLabel.sizePolicy().hasHeightForWidth())
        self.CaptionLabel.setSizePolicy(sizePolicy1)
        self.CaptionLabel.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_17.addWidget(self.CaptionLabel)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)

        self.PushButton = PushButton(self.SimpleCardWidget_3)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout_5.addWidget(self.PushButton)


        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.HorizontalSeparator = HorizontalSeparator(self.SimpleCardWidget_3)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")

        self.verticalLayout_18.addWidget(self.HorizontalSeparator)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.PushButton_5 = PushButton(self.SimpleCardWidget_3)
        self.PushButton_5.setObjectName(u"PushButton_5")
        self.PushButton_5.setEnabled(True)

        self.gridLayout.addWidget(self.PushButton_5, 0, 1, 1, 1)

        self.PushButton_4 = PushButton(self.SimpleCardWidget_3)
        self.PushButton_4.setObjectName(u"PushButton_4")

        self.gridLayout.addWidget(self.PushButton_4, 0, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout)

        self.PlainTextEdit = PlainTextEdit(self.SimpleCardWidget_3)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.PlainTextEdit.setSizePolicy(sizePolicy4)
        self.PlainTextEdit.setReadOnly(True)
        self.PlainTextEdit.setCenterOnScroll(False)

        self.verticalLayout_18.addWidget(self.PlainTextEdit)


        self.horizontalLayout_4.addWidget(self.SimpleCardWidget_3)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.TableWidget = TableWidget(self.scrollAreaWidgetContents)
        if (self.TableWidget.columnCount() < 6):
            self.TableWidget.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.TableWidget.rowCount() < 2):
            self.TableWidget.setRowCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TableWidget.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TableWidget.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.TableWidget.setItem(0, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.TableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.TableWidget.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.TableWidget.setItem(1, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.TableWidget.setItem(1, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.TableWidget.setItem(1, 4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.TableWidget.setItem(1, 5, __qtablewidgetitem19)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setShowGrid(False)
        self.TableWidget.setSortingEnabled(True)
        self.TableWidget.setSelectRightClickedRow(False)
        self.TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.TableWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SmoothScrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u51fa\u5e93", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u5c06\u8d27\u7269\u79fb\u51fa\u4ed3\u5e93", None))
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u8fd9\u91cc\u8f93\u5165EAN13\u7801", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u624b\u52a8\u51fa\u5e93", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u624b\u52a8\u51fa\u5e93", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u626b\u7801\u67aa", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u672a\u8fde\u63a5", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u626b\u7801\u67aa", None))
#if QT_CONFIG(tooltip)
        self.PushButton_5.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5728\u8be5\u6a21\u5f0f\u4e0b\u6570\u636e\u4e0d\u4f1a\u5165\u5e93\uff0c\u53ea\u4f1a\u663e\u793a\u6240\u6709\u7684\u4fe1\u606f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.PushButton_5.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2\u6a21\u5f0f", None))
        self.PushButton_4.setText(QCoreApplication.translate("Form", u"\u51fa\u5e93\u6a21\u5f0f", None))
        self.PlainTextEdit.setPlainText("")
        self.PlainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u60a8\u7684\u626b\u7801\u7ed3\u679c\u663e\u793a\u5728\u8fd9\u91cc", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u54c1\u724c", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u552e\u51fa", None));
        ___qtablewidgetitem5 = self.TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"EAN13\u7801", None));
        ___qtablewidgetitem6 = self.TableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem7 = self.TableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"2", None));

        __sortingEnabled = self.TableWidget.isSortingEnabled()
        self.TableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.TableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem9 = self.TableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem10 = self.TableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem11 = self.TableWidget.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem12 = self.TableWidget.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem13 = self.TableWidget.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"a", None));
        ___qtablewidgetitem14 = self.TableWidget.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem15 = self.TableWidget.item(1, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem16 = self.TableWidget.item(1, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem17 = self.TableWidget.item(1, 3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem18 = self.TableWidget.item(1, 4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem19 = self.TableWidget.item(1, 5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"2", None));
        self.TableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

