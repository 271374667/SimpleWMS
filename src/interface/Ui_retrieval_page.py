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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLCDNumber, QSizePolicy, QTableWidgetItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, CompactSpinBox, HorizontalSeparator,
    IconWidget, LargeTitleLabel, LineEdit, PlainTextEdit,
    PushButton, SimpleCardWidget, SmoothScrollArea, SubtitleLabel,
    SwitchButton, TableWidget, TransparentPushButton, VerticalSeparator)
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
        self.SmoothScrollArea.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 957, 720))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SimpleCardWidget_2 = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget_2.setObjectName(u"SimpleCardWidget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.SimpleCardWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.SubtitleLabel_3 = SubtitleLabel(self.SimpleCardWidget_2)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SubtitleLabel_3.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_3.setSizePolicy(sizePolicy2)
        self.SubtitleLabel_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.SubtitleLabel_3)

        self.lcdNumber = QLCDNumber(self.SimpleCardWidget_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(51)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy3)
        self.lcdNumber.setMaximumSize(QSize(130, 16777215))
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 0)

        self.horizontalLayout_2.addWidget(self.lcdNumber)


        self.verticalLayout_4.addWidget(self.SimpleCardWidget_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SimpleCardWidget_3 = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget_3.setObjectName(u"SimpleCardWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.SimpleCardWidget_3)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.SubtitleLabel_2 = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        sizePolicy2.setHeightForWidth(self.SubtitleLabel_2.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_2.setSizePolicy(sizePolicy2)
        self.SubtitleLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.SubtitleLabel_2)

        self.HorizontalSeparator_2 = HorizontalSeparator(self.SimpleCardWidget_3)
        self.HorizontalSeparator_2.setObjectName(u"HorizontalSeparator_2")

        self.verticalLayout_3.addWidget(self.HorizontalSeparator_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BodyLabel = BodyLabel(self.SimpleCardWidget_3)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout_7.addWidget(self.BodyLabel)

        self.SwitchButton = SwitchButton(self.SimpleCardWidget_3)
        self.SwitchButton.setObjectName(u"SwitchButton")

        self.horizontalLayout_7.addWidget(self.SwitchButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BodyLabel_3 = BodyLabel(self.SimpleCardWidget_3)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout_8.addWidget(self.BodyLabel_3)

        self.SwitchButton_3 = SwitchButton(self.SimpleCardWidget_3)
        self.SwitchButton_3.setObjectName(u"SwitchButton_3")
        self.SwitchButton_3.setChecked(False)

        self.horizontalLayout_8.addWidget(self.SwitchButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_5 = BodyLabel(self.SimpleCardWidget_3)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout_4.addWidget(self.BodyLabel_5)

        self.SpinBox_2 = CompactSpinBox(self.SimpleCardWidget_3)
        self.SpinBox_2.setObjectName(u"SpinBox_2")
        self.SpinBox_2.setMinimum(1)
        self.SpinBox_2.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.SpinBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LineEdit = LineEdit(self.SimpleCardWidget_3)
        self.LineEdit.setObjectName(u"LineEdit")
        sizePolicy1.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy1)
        self.LineEdit.setMinimumSize(QSize(15, 33))

        self.horizontalLayout_3.addWidget(self.LineEdit)

        self.PushButton_2 = PushButton(self.SimpleCardWidget_3)
        self.PushButton_2.setObjectName(u"PushButton_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PushButton_2.sizePolicy().hasHeightForWidth())
        self.PushButton_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.PushButton_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.PlainTextEdit = PlainTextEdit(self.SimpleCardWidget_3)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.PlainTextEdit.sizePolicy().hasHeightForWidth())
        self.PlainTextEdit.setSizePolicy(sizePolicy5)
        self.PlainTextEdit.setReadOnly(True)
        self.PlainTextEdit.setCenterOnScroll(False)

        self.verticalLayout_3.addWidget(self.PlainTextEdit)


        self.horizontalLayout_6.addWidget(self.SimpleCardWidget_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TransparentPushButton_4 = TransparentPushButton(self.scrollAreaWidgetContents)
        self.TransparentPushButton_4.setObjectName(u"TransparentPushButton_4")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TransparentPushButton_4.setIcon(icon1)
        self.TransparentPushButton_4.setProperty("hasIcon", True)

        self.horizontalLayout.addWidget(self.TransparentPushButton_4)

        self.TransparentPushButton_5 = TransparentPushButton(self.scrollAreaWidgetContents)
        self.TransparentPushButton_5.setObjectName(u"TransparentPushButton_5")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/erase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TransparentPushButton_5.setIcon(icon2)
        self.TransparentPushButton_5.setProperty("hasIcon", True)

        self.horizontalLayout.addWidget(self.TransparentPushButton_5)

        self.TransparentPushButton_6 = TransparentPushButton(self.scrollAreaWidgetContents)
        self.TransparentPushButton_6.setObjectName(u"TransparentPushButton_6")
        self.TransparentPushButton_6.setIcon(icon)
        self.TransparentPushButton_6.setProperty("hasIcon", True)

        self.horizontalLayout.addWidget(self.TransparentPushButton_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

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
        if (self.TableWidget.rowCount() < 18):
            self.TableWidget.setRowCount(18)
        self.TableWidget.setObjectName(u"TableWidget")
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TableWidget.setDragEnabled(False)
        self.TableWidget.setTextElideMode(Qt.ElideRight)
        self.TableWidget.setShowGrid(False)
        self.TableWidget.setSortingEnabled(True)
        self.TableWidget.setRowCount(18)
        self.TableWidget.setColumnCount(6)
        self.TableWidget.setSelectRightClickedRow(False)
        self.TableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.TableWidget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SmoothScrollArea)

        QWidget.setTabOrder(self.LineEdit, self.PushButton_2)
        QWidget.setTabOrder(self.PushButton_2, self.TransparentPushButton_4)
        QWidget.setTabOrder(self.TransparentPushButton_4, self.TransparentPushButton_5)
        QWidget.setTabOrder(self.TransparentPushButton_5, self.TransparentPushButton_6)
        QWidget.setTabOrder(self.TransparentPushButton_6, self.TableWidget)
        QWidget.setTabOrder(self.TableWidget, self.SpinBox_2)
        QWidget.setTabOrder(self.SpinBox_2, self.PlainTextEdit)
        QWidget.setTabOrder(self.PlainTextEdit, self.SmoothScrollArea)

        self.retranslateUi(Form)
        self.SwitchButton_3.checkedChanged.connect(self.BodyLabel_5.setHidden)
        self.SwitchButton_3.checkedChanged.connect(self.SpinBox_2.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u51fa\u5e93", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u626b\u7801\u67aa\u626b\u7801\u5c06\u8d27\u7269\u6807\u8bb0\u4e3a\u51fa\u5e93", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u6ce2\u6b21\uff1a", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u51fa\u5e93", None))
#if QT_CONFIG(tooltip)
        self.BodyLabel.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f53\u6709\u91cd\u590d\u7684\u5546\u54c1\u88ab\u51fa\u5e93\u4f1a\u8986\u76d6\u4e0a\u4e00\u6b21\u7684\u51fa\u5e93\u65f6\u95f4\u548c\u6ce2\u6b21</p><p>\u5982\u679c\u60a8\u5173\u95ed\u8be5\u9009\u9879\u90a3\u4e48\u4f1a\u9ed8\u8ba4\u8df3\u8fc7\u91cd\u590d\u7684\u5546\u54c1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u8986\u76d6\u91cd\u590d\u51fa\u5e93\u7684\u5546\u54c1", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f53\u6709\u91cd\u590d\u7684\u5546\u54c1\u88ab\u51fa\u5e93\u4f1a\u8986\u76d6\u4e0a\u4e00\u6b21\u7684\u51fa\u5e93\u65f6\u95f4\u548c\u6ce2\u6b21</p><p>\u5982\u679c\u60a8\u5173\u95ed\u8be5\u9009\u9879\u90a3\u4e48\u4f1a\u9ed8\u8ba4\u8df3\u8fc7\u91cd\u590d\u7684\u5546\u54c1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.BodyLabel_3.setToolTip(QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u7ed3\u679c\u4f1a\u6309\u6b21\u5bfc\u51fa\u5230\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6ce2\u6b21", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f00\u542f\u540e\u4f1a\u4ece\u6570\u636e\u5e93\u4e2d\u5bfb\u627e\u76ee\u524d\u6700\u65b0\u7684\u6ce2\u6b21,\u5982\u679c\u6700\u65b0\u6ce2\u6b21\u662f\u4eca\u5929\u4ea7\u751f\u7684</p><p>\u5219\u4f1a\u6cbf\u7528\u8be5\u6ce2\u6b21,\u5426\u5219\u521b\u5efa\u65b0\u7684\u6ce2\u6b21</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton_3.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton_3.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u6ce2\u6b21", None))
#if QT_CONFIG(tooltip)
        self.SpinBox_2.setToolTip(QCoreApplication.translate("Form", u"\u51fa\u8d27\u6ce2\u6b21,\u53ef\u4ee5\u586b\u5199\u5f53\u6708\u7684\u8fc7\u5f80\u6ce2\u6b21,\u4f46\u662f\u4e0d\u5141\u8bb8\u6ce2\u6b21\u6570\u8d85\u8fc7\u6700\u65b0\u6ce2\u6b21\u6570+1", None))
#endif // QT_CONFIG(tooltip)
        self.SpinBox_2.setSuffix(QCoreApplication.translate("Form", u"\u6ce2", None))
        self.SpinBox_2.setPrefix(QCoreApplication.translate("Form", u"\u7b2c", None))
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u8fd9\u91cc\u8f93\u5165EAN13\u7801", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.PlainTextEdit.setPlainText("")
        self.PlainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u60a8\u7684\u626b\u7801\u7ed3\u679c\u663e\u793a\u5728\u8fd9\u91cc(\u65e0\u8bba\u662f\u5426\u6210\u529f\u6dfb\u52a0\u90fd\u4f1a\u5728\u8fd9\u91cc\u663e\u793a\u503c)", None))
        self.TransparentPushButton_4.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5f53\u524d\u884c", None))
        self.TransparentPushButton_5.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u5168\u90e8", None))
#if QT_CONFIG(tooltip)
        self.TransparentPushButton_6.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5c06\u6570\u636e\u5728\u6570\u636e\u5e93\u4e2d\u6807\u8bb0\u4e3a\u51fa\u5e93\u5e76\u8f93\u51faexcel</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.TransparentPushButton_6.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u51fa\u5e93", None))
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u54c1\u724c", None));
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None));
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u6ce2\u6b21\u7f16\u53f7", None));
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u5165\u5e93\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"EAN13\u7801", None));
    # retranslateUi

