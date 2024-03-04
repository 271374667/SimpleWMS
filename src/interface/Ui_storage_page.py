# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storage_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLCDNumber, QSizePolicy,
    QSpacerItem, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, DoubleSpinBox, HorizontalSeparator,
    IconWidget, LargeTitleLabel, LineEdit, PrimaryPushButton,
    PushButton, SimpleCardWidget, SmoothScrollArea, SpinBox,
    SubtitleLabel, SwitchButton, TableWidget, TransparentPushButton,
    VerticalSeparator)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(923, 738)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 905, 720))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        icon.addFile(u":/icons/images/icons/database_export.svg", QSize(), QIcon.Normal, QIcon.Off)
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

        self.SubtitleLabel_2 = SubtitleLabel(self.SimpleCardWidget)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SubtitleLabel_2.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel_2.setSizePolicy(sizePolicy2)
        self.SubtitleLabel_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.SubtitleLabel_2)

        self.lcdNumber = QLCDNumber(self.SimpleCardWidget)
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

        self.horizontalLayout_3.addWidget(self.lcdNumber)


        self.verticalLayout_5.addWidget(self.SimpleCardWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.verticalLayout = QVBoxLayout(self.CardWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.SubtitleLabel = SubtitleLabel(self.CardWidget)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        sizePolicy1.setHeightForWidth(self.SubtitleLabel.sizePolicy().hasHeightForWidth())
        self.SubtitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.HorizontalSeparator = HorizontalSeparator(self.CardWidget)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")
        sizePolicy1.setHeightForWidth(self.HorizontalSeparator.sizePolicy().hasHeightForWidth())
        self.HorizontalSeparator.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.HorizontalSeparator)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.BodyLabel_3 = BodyLabel(self.CardWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout.addWidget(self.BodyLabel_3, 2, 0, 1, 1)

        self.LineEdit_3 = LineEdit(self.CardWidget)
        self.LineEdit_3.setObjectName(u"LineEdit_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LineEdit_3.sizePolicy().hasHeightForWidth())
        self.LineEdit_3.setSizePolicy(sizePolicy4)
        self.LineEdit_3.setMaxLength(13)
        self.LineEdit_3.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.LineEdit_3.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.LineEdit_3, 8, 0, 1, 2)

        self.LineEdit = LineEdit(self.CardWidget)
        self.LineEdit.setObjectName(u"LineEdit")
        sizePolicy1.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.CardWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout.addWidget(self.BodyLabel_2, 1, 0, 1, 1)

        self.BodyLabel_8 = BodyLabel(self.CardWidget)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.gridLayout.addWidget(self.BodyLabel_8, 6, 0, 1, 1)

        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.gridLayout.addWidget(self.PrimaryPushButton, 10, 0, 1, 2)

        self.LineEdit_2 = LineEdit(self.CardWidget)
        self.LineEdit_2.setObjectName(u"LineEdit_2")
        sizePolicy1.setHeightForWidth(self.LineEdit_2.sizePolicy().hasHeightForWidth())
        self.LineEdit_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.LineEdit_2, 1, 1, 1, 1)

        self.BodyLabel = BodyLabel(self.CardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1)

        self.BodyLabel_6 = BodyLabel(self.CardWidget)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.gridLayout.addWidget(self.BodyLabel_6, 5, 0, 1, 1)

        self.SwitchButton_2 = SwitchButton(self.CardWidget)
        self.SwitchButton_2.setObjectName(u"SwitchButton_2")

        self.gridLayout.addWidget(self.SwitchButton_2, 6, 1, 1, 1)

        self.PushButton = PushButton(self.CardWidget)
        self.PushButton.setObjectName(u"PushButton")

        self.gridLayout.addWidget(self.PushButton, 9, 0, 1, 2)

        self.BodyLabel_4 = BodyLabel(self.CardWidget)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.gridLayout.addWidget(self.BodyLabel_4, 4, 0, 1, 1)

        self.SwitchButton = SwitchButton(self.CardWidget)
        self.SwitchButton.setObjectName(u"SwitchButton")
        self.SwitchButton.setChecked(False)

        self.gridLayout.addWidget(self.SwitchButton, 5, 1, 1, 1)

        self.BodyLabel_5 = BodyLabel(self.CardWidget)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.gridLayout.addWidget(self.BodyLabel_5, 3, 0, 1, 1)

        self.CompactDoubleSpinBox = DoubleSpinBox(self.CardWidget)
        self.CompactDoubleSpinBox.setObjectName(u"CompactDoubleSpinBox")
        self.CompactDoubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout.addWidget(self.CompactDoubleSpinBox, 2, 1, 1, 1)

        self.CompactSpinBox = SpinBox(self.CardWidget)
        self.CompactSpinBox.setObjectName(u"CompactSpinBox")
        self.CompactSpinBox.setMinimum(1)
        self.CompactSpinBox.setMaximum(999)

        self.gridLayout.addWidget(self.CompactSpinBox, 3, 1, 1, 1)

        self.CompactSpinBox_2 = SpinBox(self.CardWidget)
        self.CompactSpinBox_2.setObjectName(u"CompactSpinBox_2")
        self.CompactSpinBox_2.setMinimum(1)
        self.CompactSpinBox_2.setMaximum(9999)

        self.gridLayout.addWidget(self.CompactSpinBox_2, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.CardWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TransparentPushButton_4 = TransparentPushButton(self.scrollAreaWidgetContents)
        self.TransparentPushButton_4.setObjectName(u"TransparentPushButton_4")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TransparentPushButton_4.setIcon(icon1)
        self.TransparentPushButton_4.setProperty("hasIcon", True)

        self.horizontalLayout.addWidget(self.TransparentPushButton_4)

        self.TransparentPushButton = TransparentPushButton(self.scrollAreaWidgetContents)
        self.TransparentPushButton.setObjectName(u"TransparentPushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/erase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TransparentPushButton.setIcon(icon2)
        self.TransparentPushButton.setProperty("hasIcon", True)

        self.horizontalLayout.addWidget(self.TransparentPushButton)

        self.TransparentPushButton_3 = TransparentPushButton(self.scrollAreaWidgetContents)
        self.TransparentPushButton_3.setObjectName(u"TransparentPushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/sign_out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TransparentPushButton_3.setIcon(icon3)
        self.TransparentPushButton_3.setProperty("hasIcon", True)

        self.horizontalLayout.addWidget(self.TransparentPushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.TableWidget_2 = TableWidget(self.scrollAreaWidgetContents)
        if (self.TableWidget_2.columnCount() < 4):
            self.TableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.TableWidget_2.rowCount() < 20):
            self.TableWidget_2.setRowCount(20)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget_2.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget_2.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TableWidget_2.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TableWidget_2.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TableWidget_2.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TableWidget_2.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TableWidget_2.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.TableWidget_2.setItem(1, 3, __qtablewidgetitem13)
        self.TableWidget_2.setObjectName(u"TableWidget_2")
        self.TableWidget_2.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.TableWidget_2.setShowGrid(False)
        self.TableWidget_2.setSortingEnabled(True)
        self.TableWidget_2.setRowCount(20)
        self.TableWidget_2.setSelectRightClickedRow(False)
        self.TableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.TableWidget_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.TableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.TableWidget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.SmoothScrollArea)

#if QT_CONFIG(shortcut)
        self.BodyLabel_2.setBuddy(self.LineEdit_2)
        self.BodyLabel.setBuddy(self.LineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.LineEdit, self.LineEdit_2)
        QWidget.setTabOrder(self.LineEdit_2, self.CompactDoubleSpinBox)
        QWidget.setTabOrder(self.CompactDoubleSpinBox, self.CompactSpinBox)
        QWidget.setTabOrder(self.CompactSpinBox, self.CompactSpinBox_2)
        QWidget.setTabOrder(self.CompactSpinBox_2, self.LineEdit_3)
        QWidget.setTabOrder(self.LineEdit_3, self.PushButton)
        QWidget.setTabOrder(self.PushButton, self.PrimaryPushButton)
        QWidget.setTabOrder(self.PrimaryPushButton, self.TransparentPushButton_4)
        QWidget.setTabOrder(self.TransparentPushButton_4, self.TransparentPushButton)
        QWidget.setTabOrder(self.TransparentPushButton, self.TransparentPushButton_3)
        QWidget.setTabOrder(self.TransparentPushButton_3, self.TableWidget_2)
        QWidget.setTabOrder(self.TableWidget_2, self.SmoothScrollArea)

        self.retranslateUi(Form)
        self.SwitchButton.checkedChanged.connect(self.BodyLabel_5.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.LineEdit_3.setVisible)
        self.SwitchButton_2.checkedChanged.connect(self.PushButton.setVisible)
        self.SwitchButton_2.checkedChanged.connect(self.PrimaryPushButton.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.BodyLabel_4.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.BodyLabel_3.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.BodyLabel_2.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.LineEdit_2.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.LineEdit.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.BodyLabel.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.BodyLabel_6.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.SwitchButton.setHidden)
        self.SwitchButton_2.checkedChanged.connect(self.BodyLabel_5.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u5165\u5e93", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u5c06\u5546\u54c1\u5199\u5165\u6570\u636e\u5e93,\u751f\u6210excel\u540e\u4f7f\u7528\u6253\u5370\u673a\u6253\u5370", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u6279\u6b21\uff1a", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u5165\u5e93\u4fe1\u606f", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_3.setToolTip(QCoreApplication.translate("Form", u"\u60a8\u53ef\u4ee5\u76f4\u63a5\u5728\u6b64\u5904\u4f7f\u7528\u626b\u7801\u67aa\u6216\u8005\u4f7f\u7528\u56de\u8f66\u8fdb\u884c\u5feb\u6377\u8f93\u5165", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit_3.setInputMask("")
        self.LineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u5728\u6b64\u5904\u8f93\u5165\u9000\u8d27\u7684EAN13\u7801", None))
#if QT_CONFIG(tooltip)
        self.LineEdit.setToolTip(QCoreApplication.translate("Form", u"\u5546\u54c1\u7684\u540d\u79f0\u53ef\u4ee5\u91cd\u590d", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5546\u54c1\u7684\u540d\u79f0", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u54c1\u724c", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Form", u"\u9000\u8d27\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.PrimaryPushButton.setToolTip(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u6570\u636e\u5230\u53f3\u4fa7\u8868\u683c\u5185", None))
#endif // QT_CONFIG(tooltip)
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_2.setToolTip(QCoreApplication.translate("Form", u"\u8be5\u9009\u9879\u533a\u5206\u5927\u5c0f\u5199,Nike\u548cNIKE\u4f1a\u88ab\u89c6\u4e3a\u4e24\u4e2a\u724c\u5b50", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8f93\u5165\u54c1\u724c\u540d\u79f0", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u540d\u79f0", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6279\u6b21", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton_2.setToolTip(QCoreApplication.translate("Form", u"\u4f7f\u7528\u8be5\u9009\u9879\u4f1a\u8fdb\u5165\u7279\u6b8a\u7684\u9000\u8d27\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton_2.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton_2.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.PushButton.setToolTip(QCoreApplication.translate("Form", u"\u70b9\u51fb\u6b64\u5904\u8fdb\u884c\u9000\u8d27,\u60a8\u4e5f\u53ef\u4ee5\u5728\u4e0a\u65b9\u56de\u8f66\u6216\u8005\u4f7f\u7528\u626b\u7801\u67aa", None))
#endif // QT_CONFIG(tooltip)
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u9000\u8d27", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u6570\u91cf", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f00\u542f\u540e\u4f1a\u4ece\u6570\u636e\u5e93\u4e2d\u5bfb\u627e\u76ee\u524d\u6700\u65b0\u7684\u6279\u6b21,\u5982\u679c\u6700\u65b0\u6279\u6b21\u662f\u4eca\u5929\u4ea7\u751f\u7684</p><p>\u5219\u4f1a\u6cbf\u7528\u8be5\u6279\u6b21,\u5426\u5219\u521b\u5efa\u65b0\u7684\u6279\u6b21</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u6279\u6b21", None))
#if QT_CONFIG(tooltip)
        self.CompactDoubleSpinBox.setToolTip(QCoreApplication.translate("Form", u"\u652f\u6301\u5c0f\u6570\u70b9\u540e\u4e24\u4f4d,\u6700\u591a\u652f\u6301\u5355\u4ef7\u4e3a\u5341\u4e07", None))
#endif // QT_CONFIG(tooltip)
        self.CompactDoubleSpinBox.setSuffix(QCoreApplication.translate("Form", u"\u5143", None))
#if QT_CONFIG(tooltip)
        self.CompactSpinBox.setToolTip(QCoreApplication.translate("Form", u"\u8fdb\u8d27\u6279\u6b21,\u53ef\u4ee5\u586b\u5199\u5f53\u6708\u7684\u8fc7\u5f80\u6279\u6b21,\u4f46\u662f\u4e0d\u5141\u8bb8\u6279\u6b21\u6570\u8d85\u8fc7\u6700\u65b0\u6279\u6b21\u6570+1", None))
#endif // QT_CONFIG(tooltip)
        self.CompactSpinBox.setSuffix(QCoreApplication.translate("Form", u"\u6279", None))
        self.CompactSpinBox.setPrefix(QCoreApplication.translate("Form", u"\u7b2c", None))
#if QT_CONFIG(tooltip)
        self.CompactSpinBox_2.setToolTip(QCoreApplication.translate("Form", u"\u540c\u6837\u7684\u5546\u54c1\u7684\u6570\u91cf,\u6ce8\u610f\u8be5\u6570\u91cf\u4e0d\u8981\u8d85\u8fc7\u6253\u5370\u673a\u7684\u6253\u5370\u7eb8\u6570\u91cf", None))
#endif // QT_CONFIG(tooltip)
        self.CompactSpinBox_2.setSuffix(QCoreApplication.translate("Form", u"\u4ef6", None))
        self.TransparentPushButton_4.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5f53\u524d\u884c", None))
        self.TransparentPushButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u5168\u90e8", None))
#if QT_CONFIG(tooltip)
        self.TransparentPushButton_3.setToolTip(QCoreApplication.translate("Form", u"\u6570\u636e\u4f1a\u5148\u6253\u5370\u518d\u5165\u5e93,\u786e\u4fdd\u6253\u5370\u673a\u5185\u6709\u5145\u8db3\u6253\u5370\u7eb8", None))
#endif // QT_CONFIG(tooltip)
        self.TransparentPushButton_3.setText(QCoreApplication.translate("Form", u"\u5165\u5e93", None))
        ___qtablewidgetitem = self.TableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.TableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u54c1\u724c", None));
        ___qtablewidgetitem2 = self.TableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None));
        ___qtablewidgetitem3 = self.TableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u6279\u6b21", None));
        ___qtablewidgetitem4 = self.TableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem5 = self.TableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"2", None));

        __sortingEnabled = self.TableWidget_2.isSortingEnabled()
        self.TableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.TableWidget_2.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Nike\u8fd0\u52a8\u978b", None));
        ___qtablewidgetitem7 = self.TableWidget_2.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"NIKE", None));
        ___qtablewidgetitem8 = self.TableWidget_2.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"367", None));
        ___qtablewidgetitem9 = self.TableWidget_2.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"202401001", None));
        ___qtablewidgetitem10 = self.TableWidget_2.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Nike\u8fd0\u52a8\u978b\u4e0a\u8863", None));
        ___qtablewidgetitem11 = self.TableWidget_2.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"NIKE", None));
        ___qtablewidgetitem12 = self.TableWidget_2.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"246", None));
        ___qtablewidgetitem13 = self.TableWidget_2.item(1, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"202401002", None));
        self.TableWidget_2.setSortingEnabled(__sortingEnabled)

    # retranslateUi

