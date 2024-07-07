# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_menuPMSTNH.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(331, 471)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(5, 0, 30, 30))
        icon = QIcon()
        icon.addFile(u":/assets/assets/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(28, 28))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 231, 491))
        self.frame.setStyleSheet(u"background-color: #E7E7E7;\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 191, 31))
        self.label.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
"color: #666666;")
        self.pushButton_normal_mode = QPushButton(self.frame)
        self.pushButton_normal_mode.setObjectName(u"pushButton_normal_mode")
        self.pushButton_normal_mode.setGeometry(QRect(10, 50, 191, 31))
        self.pushButton_normal_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_normal_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/normal_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_normal_mode.setIcon(icon1)
        self.pushButton_normal_mode.setIconSize(QSize(19, 19))
        self.pushButton_normal_mode.setAutoDefault(False)
        self.pushButton_normal_mode.setFlat(True)
        self.pushButton_engineer_mode = QPushButton(self.frame)
        self.pushButton_engineer_mode.setObjectName(u"pushButton_engineer_mode")
        self.pushButton_engineer_mode.setGeometry(QRect(10, 80, 221, 31))
        self.pushButton_engineer_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/engineer_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_engineer_mode.setIcon(icon2)
        self.pushButton_engineer_mode.setIconSize(QSize(19, 19))
        self.pushButton_engineer_mode.setAutoDefault(False)
        self.pushButton_engineer_mode.setFlat(True)
        self.pushButton_programmer_mode = QPushButton(self.frame)
        self.pushButton_programmer_mode.setObjectName(u"pushButton_programmer_mode")
        self.pushButton_programmer_mode.setGeometry(QRect(10, 110, 221, 31))
        self.pushButton_programmer_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/assets/programmer_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_programmer_mode.setIcon(icon3)
        self.pushButton_programmer_mode.setIconSize(QSize(19, 19))
        self.pushButton_programmer_mode.setAutoDefault(False)
        self.pushButton_programmer_mode.setFlat(True)
        self.pushButton_volume_mode = QPushButton(self.frame)
        self.pushButton_volume_mode.setObjectName(u"pushButton_volume_mode")
        self.pushButton_volume_mode.setGeometry(QRect(10, 200, 191, 31))
        self.pushButton_volume_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/volume_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_volume_mode.setIcon(icon4)
        self.pushButton_volume_mode.setIconSize(QSize(19, 19))
        self.pushButton_volume_mode.setAutoDefault(False)
        self.pushButton_volume_mode.setFlat(True)
        self.pushButton_graph_mode = QPushButton(self.frame)
        self.pushButton_graph_mode.setObjectName(u"pushButton_graph_mode")
        self.pushButton_graph_mode.setGeometry(QRect(10, 140, 191, 31))
        self.pushButton_graph_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_graph_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/assets/assets/graph_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_graph_mode.setIcon(icon5)
        self.pushButton_graph_mode.setIconSize(QSize(19, 19))
        self.pushButton_graph_mode.setAutoDefault(False)
        self.pushButton_graph_mode.setFlat(True)
        self.pushButton_energy_mode = QPushButton(self.frame)
        self.pushButton_energy_mode.setObjectName(u"pushButton_energy_mode")
        self.pushButton_energy_mode.setGeometry(QRect(10, 320, 191, 31))
        self.pushButton_energy_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/assets/assets/energy_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_energy_mode.setIcon(icon6)
        self.pushButton_energy_mode.setIconSize(QSize(19, 19))
        self.pushButton_energy_mode.setAutoDefault(False)
        self.pushButton_energy_mode.setFlat(True)
        self.pushButton_weight_mode = QPushButton(self.frame)
        self.pushButton_weight_mode.setObjectName(u"pushButton_weight_mode")
        self.pushButton_weight_mode.setGeometry(QRect(10, 260, 191, 31))
        self.pushButton_weight_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/assets/assets/weight_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_weight_mode.setIcon(icon7)
        self.pushButton_weight_mode.setIconSize(QSize(19, 19))
        self.pushButton_weight_mode.setAutoDefault(False)
        self.pushButton_weight_mode.setFlat(True)
        self.pushButton_length_mode = QPushButton(self.frame)
        self.pushButton_length_mode.setObjectName(u"pushButton_length_mode")
        self.pushButton_length_mode.setGeometry(QRect(10, 290, 191, 31))
        self.pushButton_length_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_length_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/assets/assets/length_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_length_mode.setIcon(icon8)
        self.pushButton_length_mode.setIconSize(QSize(19, 19))
        self.pushButton_length_mode.setAutoDefault(False)
        self.pushButton_length_mode.setFlat(True)
        self.pushButton_data_mode = QPushButton(self.frame)
        self.pushButton_data_mode.setObjectName(u"pushButton_data_mode")
        self.pushButton_data_mode.setGeometry(QRect(10, 380, 191, 31))
        self.pushButton_data_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/assets/data_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_data_mode.setIcon(icon9)
        self.pushButton_data_mode.setIconSize(QSize(19, 19))
        self.pushButton_data_mode.setAutoDefault(False)
        self.pushButton_data_mode.setFlat(True)
        self.pushButton_power_mode = QPushButton(self.frame)
        self.pushButton_power_mode.setObjectName(u"pushButton_power_mode")
        self.pushButton_power_mode.setGeometry(QRect(10, 350, 191, 31))
        self.pushButton_power_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/assets/assets/power_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_power_mode.setIcon(icon10)
        self.pushButton_power_mode.setIconSize(QSize(19, 19))
        self.pushButton_power_mode.setAutoDefault(False)
        self.pushButton_power_mode.setFlat(True)
        self.pushButton_square_mode = QPushButton(self.frame)
        self.pushButton_square_mode.setObjectName(u"pushButton_square_mode")
        self.pushButton_square_mode.setGeometry(QRect(10, 230, 191, 31))
        self.pushButton_square_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_square_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/assets/assets/square_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_square_mode.setIcon(icon11)
        self.pushButton_square_mode.setIconSize(QSize(19, 19))
        self.pushButton_square_mode.setAutoDefault(False)
        self.pushButton_square_mode.setFlat(True)
        self.pushButton_pressure_mode = QPushButton(self.frame)
        self.pushButton_pressure_mode.setObjectName(u"pushButton_pressure_mode")
        self.pushButton_pressure_mode.setGeometry(QRect(10, 410, 191, 31))
        self.pushButton_pressure_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/assets/assets/pressure_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pressure_mode.setIcon(icon12)
        self.pushButton_pressure_mode.setIconSize(QSize(19, 19))
        self.pushButton_pressure_mode.setAutoDefault(False)
        self.pushButton_pressure_mode.setFlat(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 170, 191, 31))
        self.label_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
"color: #666666;")
        self.pushButton_time_mode = QPushButton(self.frame)
        self.pushButton_time_mode.setObjectName(u"pushButton_time_mode")
        self.pushButton_time_mode.setGeometry(QRect(10, 440, 191, 31))
        self.pushButton_time_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/assets/assets/time_mode.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_time_mode.setIcon(icon13)
        self.pushButton_time_mode.setIconSize(QSize(19, 19))
        self.pushButton_time_mode.setAutoDefault(False)
        self.pushButton_time_mode.setFlat(True)
        self.frame.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)

        self.pushButton.setDefault(False)
        self.pushButton_normal_mode.setDefault(False)
        self.pushButton_engineer_mode.setDefault(False)
        self.pushButton_programmer_mode.setDefault(False)
        self.pushButton_volume_mode.setDefault(False)
        self.pushButton_graph_mode.setDefault(False)
        self.pushButton_energy_mode.setDefault(False)
        self.pushButton_weight_mode.setDefault(False)
        self.pushButton_length_mode.setDefault(False)
        self.pushButton_data_mode.setDefault(False)
        self.pushButton_power_mode.setDefault(False)
        self.pushButton_square_mode.setDefault(False)
        self.pushButton_pressure_mode.setDefault(False)
        self.pushButton_time_mode.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.pushButton_normal_mode.setText(QCoreApplication.translate("Form", u" \u041e\u0431\u044b\u0447\u043d\u044b\u0439", None))
        self.pushButton_engineer_mode.setText(QCoreApplication.translate("Form", u" \u0418\u043d\u0436\u0435\u043d\u0435\u0440\u043d\u044b\u0439", None))
        self.pushButton_programmer_mode.setText(QCoreApplication.translate("Form", u" \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442", None))
        self.pushButton_volume_mode.setText(QCoreApplication.translate("Form", u" \u041e\u0431\u044a\u0435\u043c", None))
        self.pushButton_graph_mode.setText(QCoreApplication.translate("Form", u" \u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.pushButton_energy_mode.setText(QCoreApplication.translate("Form", u" \u042d\u043d\u0435\u0440\u0433\u0438\u044f", None))
        self.pushButton_weight_mode.setText(QCoreApplication.translate("Form", u" \u0412\u0435\u0441 \u0438 \u043c\u0430\u0441\u0441\u0430", None))
        self.pushButton_length_mode.setText(QCoreApplication.translate("Form", u" \u0414\u043b\u0438\u043d\u0430", None))
        self.pushButton_data_mode.setText(QCoreApplication.translate("Form", u" \u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_power_mode.setText(QCoreApplication.translate("Form", u" \u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.pushButton_square_mode.setText(QCoreApplication.translate("Form", u" \u041f\u043b\u043e\u0449\u0430\u0434\u044c", None))
        self.pushButton_pressure_mode.setText(QCoreApplication.translate("Form", u" \u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.pushButton_time_mode.setText(QCoreApplication.translate("Form", u" \u0412\u0440\u0435\u043c\u044f", None))
    # retranslateUi

