# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(532, 611)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Calculator)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Calculator)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_4 = QPushButton(self.frame)
        self.pb_4.setObjectName(u"pb_4")
        sizePolicy.setHeightForWidth(self.pb_4.sizePolicy().hasHeightForWidth())
        self.pb_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.pb_4.setFont(font)

        self.gridLayout_2.addWidget(self.pb_4, 3, 0, 1, 1)

        self.pb_clearCurrent = QPushButton(self.frame)
        self.pb_clearCurrent.setObjectName(u"pb_clearCurrent")
        sizePolicy.setHeightForWidth(self.pb_clearCurrent.sizePolicy().hasHeightForWidth())
        self.pb_clearCurrent.setSizePolicy(sizePolicy)
        self.pb_clearCurrent.setFont(font)

        self.gridLayout_2.addWidget(self.pb_clearCurrent, 6, 1, 1, 1)

        self.pb_3 = QPushButton(self.frame)
        self.pb_3.setObjectName(u"pb_3")
        sizePolicy.setHeightForWidth(self.pb_3.sizePolicy().hasHeightForWidth())
        self.pb_3.setSizePolicy(sizePolicy)
        self.pb_3.setFont(font)

        self.gridLayout_2.addWidget(self.pb_3, 4, 2, 1, 1)

        self.pb_clearAll = QPushButton(self.frame)
        self.pb_clearAll.setObjectName(u"pb_clearAll")
        sizePolicy.setHeightForWidth(self.pb_clearAll.sizePolicy().hasHeightForWidth())
        self.pb_clearAll.setSizePolicy(sizePolicy)
        self.pb_clearAll.setFont(font)

        self.gridLayout_2.addWidget(self.pb_clearAll, 6, 0, 1, 1)

        self.pb_1 = QPushButton(self.frame)
        self.pb_1.setObjectName(u"pb_1")
        sizePolicy.setHeightForWidth(self.pb_1.sizePolicy().hasHeightForWidth())
        self.pb_1.setSizePolicy(sizePolicy)
        self.pb_1.setFont(font)

        self.gridLayout_2.addWidget(self.pb_1, 4, 0, 1, 1)

        self.pb_subtract = QPushButton(self.frame)
        self.pb_subtract.setObjectName(u"pb_subtract")
        sizePolicy.setHeightForWidth(self.pb_subtract.sizePolicy().hasHeightForWidth())
        self.pb_subtract.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(18)
        self.pb_subtract.setFont(font1)

        self.gridLayout_2.addWidget(self.pb_subtract, 4, 3, 1, 1)

        self.pb_multiply = QPushButton(self.frame)
        self.pb_multiply.setObjectName(u"pb_multiply")
        sizePolicy.setHeightForWidth(self.pb_multiply.sizePolicy().hasHeightForWidth())
        self.pb_multiply.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(16)
        self.pb_multiply.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_multiply, 2, 3, 1, 1)

        self.calc_num = QLabel(self.frame)
        self.calc_num.setObjectName(u"calc_num")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calc_num.sizePolicy().hasHeightForWidth())
        self.calc_num.setSizePolicy(sizePolicy1)
        self.calc_num.setMinimumSize(QSize(0, 85))
        font3 = QFont()
        font3.setFamilies([u"Digital-7"])
        font3.setPointSize(66)
        font3.setBold(False)
        font3.setItalic(False)
        self.calc_num.setFont(font3)
        self.calc_num.setStyleSheet(u"QLabel {\n"
"	color: black;\n"
"}")
        self.calc_num.setFrameShape(QFrame.Box)
        self.calc_num.setFrameShadow(QFrame.Plain)
        self.calc_num.setLineWidth(1)
        self.calc_num.setTextFormat(Qt.PlainText)
        self.calc_num.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calc_num.setIndent(10)

        self.gridLayout_2.addWidget(self.calc_num, 0, 0, 1, 4)

        self.pb_divide = QPushButton(self.frame)
        self.pb_divide.setObjectName(u"pb_divide")
        sizePolicy.setHeightForWidth(self.pb_divide.sizePolicy().hasHeightForWidth())
        self.pb_divide.setSizePolicy(sizePolicy)
        self.pb_divide.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_divide, 3, 3, 1, 1)

        self.pb_8 = QPushButton(self.frame)
        self.pb_8.setObjectName(u"pb_8")
        sizePolicy.setHeightForWidth(self.pb_8.sizePolicy().hasHeightForWidth())
        self.pb_8.setSizePolicy(sizePolicy)
        self.pb_8.setFont(font)

        self.gridLayout_2.addWidget(self.pb_8, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(5, 8, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.pb_6 = QPushButton(self.frame)
        self.pb_6.setObjectName(u"pb_6")
        sizePolicy.setHeightForWidth(self.pb_6.sizePolicy().hasHeightForWidth())
        self.pb_6.setSizePolicy(sizePolicy)
        self.pb_6.setFont(font)

        self.gridLayout_2.addWidget(self.pb_6, 3, 2, 1, 1)

        self.pb_decimal = QPushButton(self.frame)
        self.pb_decimal.setObjectName(u"pb_decimal")
        sizePolicy.setHeightForWidth(self.pb_decimal.sizePolicy().hasHeightForWidth())
        self.pb_decimal.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(24)
        self.pb_decimal.setFont(font4)
        self.pb_decimal.setAutoDefault(False)
        self.pb_decimal.setFlat(False)

        self.gridLayout_2.addWidget(self.pb_decimal, 5, 2, 1, 1)

        self.pb_7 = QPushButton(self.frame)
        self.pb_7.setObjectName(u"pb_7")
        sizePolicy.setHeightForWidth(self.pb_7.sizePolicy().hasHeightForWidth())
        self.pb_7.setSizePolicy(sizePolicy)
        self.pb_7.setFont(font)
        self.pb_7.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pb_7, 2, 0, 1, 1)

        self.pb_9 = QPushButton(self.frame)
        self.pb_9.setObjectName(u"pb_9")
        sizePolicy.setHeightForWidth(self.pb_9.sizePolicy().hasHeightForWidth())
        self.pb_9.setSizePolicy(sizePolicy)
        self.pb_9.setFont(font)

        self.gridLayout_2.addWidget(self.pb_9, 2, 2, 1, 1)

        self.pb_2 = QPushButton(self.frame)
        self.pb_2.setObjectName(u"pb_2")
        sizePolicy.setHeightForWidth(self.pb_2.sizePolicy().hasHeightForWidth())
        self.pb_2.setSizePolicy(sizePolicy)
        self.pb_2.setFont(font)

        self.gridLayout_2.addWidget(self.pb_2, 4, 1, 1, 1)

        self.pb_5 = QPushButton(self.frame)
        self.pb_5.setObjectName(u"pb_5")
        sizePolicy.setHeightForWidth(self.pb_5.sizePolicy().hasHeightForWidth())
        self.pb_5.setSizePolicy(sizePolicy)
        self.pb_5.setFont(font)

        self.gridLayout_2.addWidget(self.pb_5, 3, 1, 1, 1)

        self.pb_0 = QPushButton(self.frame)
        self.pb_0.setObjectName(u"pb_0")
        sizePolicy.setHeightForWidth(self.pb_0.sizePolicy().hasHeightForWidth())
        self.pb_0.setSizePolicy(sizePolicy)
        self.pb_0.setFont(font)

        self.gridLayout_2.addWidget(self.pb_0, 5, 0, 1, 2)

        self.pb_add = QPushButton(self.frame)
        self.pb_add.setObjectName(u"pb_add")
        sizePolicy.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy)
        self.pb_add.setFont(font2)

        self.gridLayout_2.addWidget(self.pb_add, 5, 3, 1, 1)

        self.pb_equals = QPushButton(self.frame)
        self.pb_equals.setObjectName(u"pb_equals")
        sizePolicy.setHeightForWidth(self.pb_equals.sizePolicy().hasHeightForWidth())
        self.pb_equals.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(20)
        self.pb_equals.setFont(font5)

        self.gridLayout_2.addWidget(self.pb_equals, 6, 2, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pb_7, self.pb_8)
        QWidget.setTabOrder(self.pb_8, self.pb_9)
        QWidget.setTabOrder(self.pb_9, self.pb_multiply)
        QWidget.setTabOrder(self.pb_multiply, self.pb_4)
        QWidget.setTabOrder(self.pb_4, self.pb_5)
        QWidget.setTabOrder(self.pb_5, self.pb_6)
        QWidget.setTabOrder(self.pb_6, self.pb_divide)
        QWidget.setTabOrder(self.pb_divide, self.pb_1)
        QWidget.setTabOrder(self.pb_1, self.pb_2)
        QWidget.setTabOrder(self.pb_2, self.pb_3)
        QWidget.setTabOrder(self.pb_3, self.pb_subtract)
        QWidget.setTabOrder(self.pb_subtract, self.pb_0)
        QWidget.setTabOrder(self.pb_0, self.pb_decimal)
        QWidget.setTabOrder(self.pb_decimal, self.pb_add)
        QWidget.setTabOrder(self.pb_add, self.pb_clearAll)
        QWidget.setTabOrder(self.pb_clearAll, self.pb_clearCurrent)
        QWidget.setTabOrder(self.pb_clearCurrent, self.pb_equals)

        self.retranslateUi(Calculator)

        self.pb_decimal.setDefault(False)


        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.pb_4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.pb_clearCurrent.setText(QCoreApplication.translate("Calculator", u"C", None))
        self.pb_3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.pb_clearAll.setText(QCoreApplication.translate("Calculator", u"CE", None))
        self.pb_1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.pb_subtract.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.pb_multiply.setText(QCoreApplication.translate("Calculator", u"X", None))
        self.calc_num.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pb_divide.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.pb_8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.pb_6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.pb_decimal.setText(QCoreApplication.translate("Calculator", u".", None))
        self.pb_7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.pb_9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.pb_2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.pb_5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.pb_0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pb_add.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.pb_equals.setText(QCoreApplication.translate("Calculator", u"=", None))
    # retranslateUi

