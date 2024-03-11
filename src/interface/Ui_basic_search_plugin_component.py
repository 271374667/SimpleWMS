# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basic_search_plugin_component.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, ComboBox, DoubleSpinBox,
    LineEdit, PushButton, SpinBox, SwitchButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(596, 459)
        Form.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel_3 = BodyLabel(self.groupBox)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout_3.addWidget(self.BodyLabel_3)

        self.LineEdit_3 = LineEdit(self.groupBox)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.horizontalLayout_3.addWidget(self.LineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BodyLabel_7 = BodyLabel(self.groupBox)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.horizontalLayout_8.addWidget(self.BodyLabel_7)

        self.LineEdit_5 = LineEdit(self.groupBox)
        self.LineEdit_5.setObjectName(u"LineEdit_5")

        self.horizontalLayout_8.addWidget(self.LineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BodyLabel = BodyLabel(self.groupBox)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout_2.addWidget(self.BodyLabel)

        self.LineEdit = LineEdit(self.groupBox)
        self.LineEdit.setObjectName(u"LineEdit")

        self.horizontalLayout_2.addWidget(self.LineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel_5 = BodyLabel(self.groupBox)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout.addWidget(self.BodyLabel_5)

        self.ComboBox = ComboBox(self.groupBox)
        self.ComboBox.setObjectName(u"ComboBox")

        self.horizontalLayout.addWidget(self.ComboBox)

        self.DoubleSpinBox = DoubleSpinBox(self.groupBox)
        self.DoubleSpinBox.setObjectName(u"DoubleSpinBox")
        self.DoubleSpinBox.setMaximum(100000.000000000000000)

        self.horizontalLayout.addWidget(self.DoubleSpinBox)

        self.SwitchButton = SwitchButton(self.groupBox)
        self.SwitchButton.setObjectName(u"SwitchButton")

        self.horizontalLayout.addWidget(self.SwitchButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BodyLabel_2 = BodyLabel(self.groupBox)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.horizontalLayout_4.addWidget(self.BodyLabel_2)

        self.LineEdit_2 = LineEdit(self.groupBox)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.horizontalLayout_4.addWidget(self.LineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BodyLabel_4 = BodyLabel(self.groupBox)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.horizontalLayout_5.addWidget(self.BodyLabel_4)

        self.LineEdit_4 = LineEdit(self.groupBox)
        self.LineEdit_4.setObjectName(u"LineEdit_4")

        self.horizontalLayout_5.addWidget(self.LineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BodyLabel_6 = BodyLabel(self.groupBox)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.horizontalLayout_6.addWidget(self.BodyLabel_6)

        self.ComboBox_2 = ComboBox(self.groupBox)
        self.ComboBox_2.setObjectName(u"ComboBox_2")

        self.horizontalLayout_6.addWidget(self.ComboBox_2)

        self.SpinBox = SpinBox(self.groupBox)
        self.SpinBox.setObjectName(u"SpinBox")
        self.SpinBox.setMaximum(365)

        self.horizontalLayout_6.addWidget(self.SpinBox)

        self.SwitchButton_2 = SwitchButton(self.groupBox)
        self.SwitchButton_2.setObjectName(u"SwitchButton_2")

        self.horizontalLayout_6.addWidget(self.SwitchButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.PushButton = PushButton(self.groupBox)
        self.PushButton.setObjectName(u"PushButton")

        self.verticalLayout.addWidget(self.PushButton)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.CheckBox = CheckBox(self.groupBox_2)
        self.CheckBox.setObjectName(u"CheckBox")

        self.horizontalLayout_7.addWidget(self.CheckBox)

        self.CheckBox_2 = CheckBox(self.groupBox_2)
        self.CheckBox_2.setObjectName(u"CheckBox_2")

        self.horizontalLayout_7.addWidget(self.CheckBox_2)


        self.verticalLayout_2.addWidget(self.groupBox_2)

#if QT_CONFIG(shortcut)
        self.BodyLabel_3.setBuddy(self.LineEdit_3)
        self.BodyLabel_7.setBuddy(self.LineEdit_5)
        self.BodyLabel.setBuddy(self.LineEdit)
        self.BodyLabel_2.setBuddy(self.LineEdit_2)
        self.BodyLabel_4.setBuddy(self.LineEdit_4)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.LineEdit_3, self.LineEdit_5)
        QWidget.setTabOrder(self.LineEdit_5, self.LineEdit)
        QWidget.setTabOrder(self.LineEdit, self.ComboBox)
        QWidget.setTabOrder(self.ComboBox, self.DoubleSpinBox)
        QWidget.setTabOrder(self.DoubleSpinBox, self.LineEdit_2)
        QWidget.setTabOrder(self.LineEdit_2, self.LineEdit_4)
        QWidget.setTabOrder(self.LineEdit_4, self.ComboBox_2)
        QWidget.setTabOrder(self.ComboBox_2, self.SpinBox)
        QWidget.setTabOrder(self.SpinBox, self.PushButton)
        QWidget.setTabOrder(self.PushButton, self.CheckBox)
        QWidget.setTabOrder(self.CheckBox, self.CheckBox_2)

        self.retranslateUi(Form)
        self.PushButton.clicked.connect(self.LineEdit_4.clear)
        self.PushButton.clicked.connect(self.LineEdit_2.clear)
        self.PushButton.clicked.connect(self.LineEdit.clear)
        self.PushButton.clicked.connect(self.LineEdit_3.clear)
        self.PushButton.clicked.connect(self.LineEdit_5.clear)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u7b5b\u9009", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"\u6839\u636eEAN13\u67e5\u627e:", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_3.setToolTip(QCoreApplication.translate("Form", u"\u6bcf\u4e00\u4e2a\u5546\u54c1\u90fd\u6709\u81ea\u5df1\u7684\u4e00\u4e2aEAN13\u7801", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"13\u4f4d\u7684\u6570\u5b57\u7f16\u53f7", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u6839\u636e\u5546\u54c1\u540d\u79f0\u67e5\u627e:", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_5.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u6a21\u7cca\u641c\u7d22\u4e0d\u662f\u76f8\u4f3c\u63a8\u8350</p><p>\u641c\u7d22&quot;\u96f6\u98df&quot;\u53ea\u4f1a\u540c\u65f6\u641c\u7d22\u51fa&quot;\u597d\u96f6\u98df&quot;,&quot;\u96f6\u98df\u5999&quot;,\u800c\u65e0\u6cd5\u641c\u7d22\u51fa&quot;\u96f6\u5c0f\u98df&quot;\u6216\u8005&quot;\u85af\u7247&quot;</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u5546\u54c1\u7684\u540d\u79f0(\u9ed8\u8ba4\u6a21\u7cca\u641c\u7d22)", None))
        self.BodyLabel.setText(QCoreApplication.translate("Form", u"\u6839\u636e\u54c1\u724c\u67e5\u627e:", None))
#if QT_CONFIG(tooltip)
        self.LineEdit.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u6ce8\u610f\u54c1\u724c\u7684\u5927\u5c0f\u5199,\u76f8\u540c\u82f1\u6587\u4f46\u662f\u5927\u5c0f\u5199\u4e0d\u540c\u7684\u54c1\u724c\u4f1a\u88ab\u8ba4\u4e3a\u662f\u4e24\u4e2a\u54c1\u724c</p><p>\u6bd4\u5982Nike\u548cnike\u5c06\u4f1a\u88ab\u8ba4\u4e3a\u662f\u4e24\u4e2a\u724c\u5b50</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5546\u54c1\u7684\u54c1\u724c\u540d\u79f0(\u82f1\u6587\u533a\u5206\u5927\u5c0f\u5199)", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u6839\u636e\u4ef7\u683c\u67e5\u627e", None))
        self.ComboBox.setText(QCoreApplication.translate("Form", u"\u7b49\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.DoubleSpinBox.setToolTip(QCoreApplication.translate("Form", u"\u4ef7\u683c\u6700\u5927\u652f\u630110\u4e07\u5143", None))
#endif // QT_CONFIG(tooltip)
        self.DoubleSpinBox.setSuffix(QCoreApplication.translate("Form", u"\u5143", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u5f00\u542f\u8be5\u9009\u9879\u624d\u80fd\u8fdb\u884c\u4ef7\u683c\u67e5\u627e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.SwitchButton.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Form", u"\u6839\u636e\u6279\u6b21\u67e5\u627e", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>\u7f16\u53f7\u4e3a\u7eaf\u6570\u5b57,\u7f16\u53f7\u683c\u5f0f\u5982\u4e0b202401001</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u6279\u6b21\u7684\u7f16\u53f7", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"\u6839\u636e\u6ce2\u6b21\u67e5\u627e:", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_4.setToolTip(QCoreApplication.translate("Form", u"\u7f16\u53f7\u4e3a\u7eaf\u6570\u5b57,\u7f16\u53f7\u683c\u5f0f\u5982\u4e0b202401001", None))
#endif // QT_CONFIG(tooltip)
        self.LineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u6ce2\u6b21\u7684\u7f16\u53f7", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u6839\u636e\u5b58\u653e\u65f6\u95f4\u67e5\u627e:", None))
        self.ComboBox_2.setText(QCoreApplication.translate("Form", u"\u7b49\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.SpinBox.setToolTip(QCoreApplication.translate("Form", u"\u5929\u6570\u6700\u957f\u652f\u6301\u641c\u7d22365\u5929", None))
#endif // QT_CONFIG(tooltip)
        self.SpinBox.setSuffix(QCoreApplication.translate("Form", u"\u5929", None))
#if QT_CONFIG(tooltip)
        self.SwitchButton_2.setToolTip(QCoreApplication.translate("Form", u"\u5f00\u542f\u8be5\u9009\u9879\u624d\u80fd\u641c\u7d22\u5b58\u653e\u65f6\u95f4", None))
#endif // QT_CONFIG(tooltip)
        self.SwitchButton_2.setOnText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.SwitchButton_2.setOffText(QCoreApplication.translate("Form", u"\u7981\u7528", None))
#if QT_CONFIG(tooltip)
        self.PushButton.setToolTip(QCoreApplication.translate("Form", u"\u8be5\u6309\u94ae\u4f1a\u91cd\u7f6e\u6240\u6709\u7684\u641c\u7d22\u6761\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.PushButton.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e\u7b5b\u9009\u9879", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u66f4\u591a\u9009\u9879", None))
#if QT_CONFIG(tooltip)
        self.CheckBox.setToolTip(QCoreApplication.translate("Form", u"\u662f\u5426\u663e\u793a\u5df2\u7ecf\u5356\u51fa\u7684\u5546\u54c1", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u5df2\u5356\u51fa\u7684\u5546\u54c1", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.CheckBox_2.setText(QCoreApplication.translate("Form", u"\u9690\u85cf\u6709\u8fc7\u9000\u8d27\u7684\u5546\u54c1", None))
    # retranslateUi

