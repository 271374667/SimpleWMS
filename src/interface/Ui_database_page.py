# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QColor,
    QIcon,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from qfluentwidgets import (
    BodyLabel,
    ComboBox,
    IconWidget,
    LargeTitleLabel,
    PrimaryPushButton,
    SimpleCardWidget,
    SmoothScrollArea,
    StrongBodyLabel,
    TableWidget,
    VerticalSeparator,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(978, 738)
        Form.setStyleSheet("")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.SmoothScrollArea = SmoothScrollArea(Form)
        self.SmoothScrollArea.setObjectName("SmoothScrollArea")
        self.SmoothScrollArea.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.SmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 948, 710))
        self.scrollAreaWidgetContents.setStyleSheet(
            "background-color: rgba(0, 0, 0, 0);"
        )
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, -1, 15)
        self.SimpleCardWidget = SimpleCardWidget(self.scrollAreaWidgetContents)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.SimpleCardWidget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.IconWidget = IconWidget(self.SimpleCardWidget)
        self.IconWidget.setObjectName("IconWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setMinimumSize(QSize(36, 36))
        self.IconWidget.setMaximumSize(QSize(84, 84))
        icon = QIcon()
        icon.addFile(
            ":/icons/images/icons/database_administrator.svg",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.IconWidget.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.IconWidget)

        self.VerticalSeparator = VerticalSeparator(self.SimpleCardWidget)
        self.VerticalSeparator.setObjectName("VerticalSeparator")

        self.horizontalLayout_3.addWidget(self.VerticalSeparator)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.LargeTitleLabel = LargeTitleLabel(self.SimpleCardWidget)
        self.LargeTitleLabel.setObjectName("LargeTitleLabel")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.LargeTitleLabel.sizePolicy().hasHeightForWidth()
        )
        self.LargeTitleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_14.addWidget(self.LargeTitleLabel)

        self.BodyLabel_7 = BodyLabel(self.SimpleCardWidget)
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        sizePolicy1.setHeightForWidth(self.BodyLabel_7.sizePolicy().hasHeightForWidth())
        self.BodyLabel_7.setSizePolicy(sizePolicy1)
        self.BodyLabel_7.setProperty("lightColor", QColor(96, 96, 96))

        self.verticalLayout_14.addWidget(self.BodyLabel_7)

        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.verticalLayout_2.addWidget(self.SimpleCardWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BodyLabel_2 = BodyLabel(self.scrollAreaWidgetContents)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.BodyLabel_2)

        self.ComboBox = ComboBox(self.scrollAreaWidgetContents)
        self.ComboBox.setObjectName("ComboBox")

        self.horizontalLayout_2.addWidget(self.ComboBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.StrongBodyLabel = StrongBodyLabel(self.scrollAreaWidgetContents)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")

        self.verticalLayout_2.addWidget(self.StrongBodyLabel)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")

        self.verticalLayout_2.addWidget(self.widget)

        self.PrimaryPushButton = PrimaryPushButton(self.scrollAreaWidgetContents)
        self.PrimaryPushButton.setObjectName("PrimaryPushButton")

        self.verticalLayout_2.addWidget(self.PrimaryPushButton)

        self.TableWidget = TableWidget(self.scrollAreaWidgetContents)
        if self.TableWidget.columnCount() < 5:
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
        if self.TableWidget.rowCount() < 20:
            self.TableWidget.setRowCount(20)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        self.TableWidget.setObjectName("TableWidget")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TableWidget.sizePolicy().hasHeightForWidth())
        self.TableWidget.setSizePolicy(sizePolicy3)
        self.TableWidget.setMinimumSize(QSize(0, 400))
        self.TableWidget.setMaximumSize(QSize(16777215, 16777209))
        self.TableWidget.setTabletTracking(False)
        self.TableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.TableWidget.setEditTriggers(
            QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked
        )
        self.TableWidget.setShowGrid(False)
        self.TableWidget.setSortingEnabled(True)
        self.TableWidget.setRowCount(20)
        self.TableWidget.setSelectRightClickedRow(False)
        self.TableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.TableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.TableWidget)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SmoothScrollArea)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.LargeTitleLabel.setText(
            QCoreApplication.translate("Form", "\u6570\u636e\u5e93\u5206\u6790", None)
        )
        self.BodyLabel_7.setText(
            QCoreApplication.translate(
                "Form",
                "\u591a\u65b9\u4f4d\u66f4\u52a0\u5168\u9762\u7684\u7406\u89e3\u4f60\u7684\u6570\u636e",
                None,
            )
        )
        self.BodyLabel_2.setText(
            QCoreApplication.translate(
                "Form", "\u9009\u62e9\u5c55\u793a\u6a21\u5f0f:", None
            )
        )
        self.ComboBox.setText(
            QCoreApplication.translate(
                "Form",
                "\u8bf7\u9009\u62e9\u4e00\u4e2a\u6a21\u5f0f\u6765\u83b7\u53d6\u6570\u636e",
                None,
            )
        )
        self.StrongBodyLabel.setText(
            QCoreApplication.translate(
                "Form",
                "\u5f53\u524d\u914d\u7f6e:\u5f53\u524d\u6ca1\u6709\u9009\u62e9\u4efb\u4f55\u6a21\u5f0f",
                None,
            )
        )
        self.PrimaryPushButton.setText(
            QCoreApplication.translate("Form", "\u5f00\u59cb\u67e5\u627e", None)
        )
        ___qtablewidgetitem = self.TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("Form", "\u540d\u79f0", None)
        )
        ___qtablewidgetitem1 = self.TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("Form", "\u54c1\u724c", None)
        )
        ___qtablewidgetitem2 = self.TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("Form", "\u4ef7\u683c", None)
        )
        ___qtablewidgetitem3 = self.TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("Form", "\u6279\u6b21", None)
        )
        ___qtablewidgetitem4 = self.TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("Form", "EAN13\u7801", None)
        )
        ___qtablewidgetitem5 = self.TableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", "1", None))
        ___qtablewidgetitem6 = self.TableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", "2", None))
        ___qtablewidgetitem7 = self.TableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", "3", None))


# retranslateUi
