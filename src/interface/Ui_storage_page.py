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
        Form.resize(977, 738)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 959, 720))
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
        self.BodyLabel_6 = BodyLabel(self.CardWidget)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.gridLayout.addWidget(self.BodyLabel_6, 6, 0, 1, 1)

        self.BodyLabel_5 = BodyLabel(self.CardWidget)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.gridLayout.addWidget(self.BodyLabel_5, 4, 0, 1, 1)

        self.SpinBox = SpinBox(self.CardWidget)
        self.SpinBox.setObjectName(u"SpinBox")
        self.SpinBox.setMinimum(1)
        self.SpinBox.setMaximum(9999)

        self.gridLayout.addWidget(self.SpinBox, 5, 1, 1, 1)

        self.LineEdit = LineEdit(self.CardWidget)
        self.LineEdit.setObjectName(u"LineEdit")
        sizePolicy1.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)

        self.SpinBox_2 = SpinBox(self.CardWidget)
        self.SpinBox_2.setObjectName(u"SpinBox_2")
        self.SpinBox_2.setMinimum(1)
        self.SpinBox_2.setMaximum(999)

        self.gridLayout.addWidget(self.SpinBox_2, 4, 1, 1, 1)

        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.gridLayout.addWidget(self.PrimaryPushButton, 7, 0, 1, 2)

        self.BodyLabel_2 = BodyLabel(self.CardWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout.addWidget(self.BodyLabel_2, 1, 0, 1, 1)

        self.BodyLabel_3 = BodyLabel(self.CardWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout.addWidget(self.BodyLabel_3, 2, 0, 1, 1)

        self.SwitchButton = SwitchButton(self.CardWidget)
        self.SwitchButton.setObjectName(u"SwitchButton")
        self.SwitchButton.setChecked(False)

        self.gridLayout.addWidget(self.SwitchButton, 6, 1, 1, 1)

        self.BodyLabel_4 = BodyLabel(self.CardWidget)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.gridLayout.addWidget(self.BodyLabel_4, 5, 0, 1, 1)

        self.DoubleSpinBox = DoubleSpinBox(self.CardWidget)
        self.DoubleSpinBox.setObjectName(u"DoubleSpinBox")
        self.DoubleSpinBox.setMaximum(100000.000000000000000)

        self.gridLayout.addWidget(self.DoubleSpinBox, 2, 1, 1, 1)

        self.LineEdit_2 = LineEdit(self.CardWidget)
        self.LineEdit_2.setObjectName(u"LineEdit_2")
        sizePolicy1.setHeightForWidth(self.LineEdit_2.sizePolicy().hasHeightForWidth())
        self.LineEdit_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.LineEdit_2, 1, 1, 1, 1)

        self.BodyLabel = BodyLabel(self.CardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout.addWidget(self.BodyLabel, 0, 0, 1, 1)


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
        self.BodyLabel_5.setBuddy(self.SpinBox_2)
        self.BodyLabel_2.setBuddy(self.LineEdit_2)
        self.BodyLabel_3.setBuddy(self.DoubleSpinBox)
        self.BodyLabel_4.setBuddy(self.SpinBox)
        self.BodyLabel.setBuddy(self.LineEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.LineEdit, self.LineEdit_2)
        QWidget.setTabOrder(self.LineEdit_2, self.DoubleSpinBox)
        QWidget.setTabOrder(self.DoubleSpinBox, self.SpinBox_2)
        QWidget.setTabOrder(self.SpinBox_2, self.SpinBox)
        QWidget.setTabOrder(self.SpinBox, self.PrimaryPushButton)
        QWidget.setTabOrder(self.PrimaryPushButton, self.TransparentPushButton_4)
        QWidget.setTabOrder(self.TransparentPushButton_4, self.TransparentPushButton)
        QWidget.setTabOrder(self.TransparentPushButton, self.TransparentPushButton_3)
        QWidget.setTabOrder(self.TransparentPushButton_3, self.TableWidget_2)
        QWidget.setTabOrder(self.TableWidget_2, self.SmoothScrollArea)

        self.retranslateUi(Form)
        self.SwitchButton.checkedChanged.connect(self.BodyLabel_5.setHidden)
        self.SwitchButton.checkedChanged.connect(self.SpinBox_2.setHidden)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("Form", u"\u5165\u5e93", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u5c06\u5546\u54c1\u5f55\u5165\u7cfb\u7edf", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u6279\u6b21\uff1a", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"\u5165\u5e93\u4fe1\u606f", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6279\u6b21", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u6279\u6b21", None))
#if QT_CONFIG(tooltip)
        self.SpinBox.setToolTip(QCoreApplication.translate("Form", u"\u540c\u6837\u7684\u5546\u54c1\u7684\u6570\u91cf,\u6ce8\u610f\u8be5\u6570\u91cf\u4e0d\u8981\u8d85\u8fc7\u6253\u5370\u673a\u7684\u6253\u5370\u7eb8\u6570\u91cf", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.SpinBox_2.setToolTip(QCoreApplication.translate("Form", u"\u8fdb\u8d27\u6279\u6b21,\u53ef\u4ee5\u586b\u5199\u5f53\u6708\u7684\u8fc7\u5f80\u6279\u6b21,\u4f46\u662f\u4e0d\u5141\u8bb8\u6279\u6b21\u6570\u8d85\u8fc7\u6700\u65b0\u6279\u6b21\u6570+1", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.PrimaryPushButton.setToolTip(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u6570\u636e\u5230\u53f3\u4fa7\u8868\u683c\u5185", None))
#endif // QT_CONFIG(tooltip)
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u54c1\u724c", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f00\u542f\u540e\u4f1a\u4ece\u6570\u636e\u5e93\u4e2d\u5bfb\u627e\u76ee\u524d\u6700\u65b0\u7684\u6279\u6b21,\u5982\u679c\u6700\u65b0\u6279\u6b21\u662f\u4eca\u5929\u4ea7\u751f\u7684</p><p>\u5219\u4f1a\u6cbf\u7528\u8be5\u6279\u6b21,\u5426\u5219\u521b\u5efa\u65b0\u7684\u6279\u6b21</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u6570\u91cf", None))
#if QT_CONFIG(tooltip)
        self.DoubleSpinBox.setToolTip(QCoreApplication.translate("Form", u"\u652f\u6301\u5c0f\u6570\u70b9\u540e\u4e24\u4f4d,\u6700\u591a\u652f\u6301\u5355\u4ef7\u4e3a\u5341\u4e07", None))
#endif // QT_CONFIG(tooltip)
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u8863\u670d\u540d\u79f0", None))
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

