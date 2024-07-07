# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QGridLayout, QLineEdit, QPushButton, QSizePolicy, QWidget, 
QFrame, QLabel, QComboBox, QVBoxLayout)
import assets_rc
from decimal import Decimal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        icon = QIcon()
        icon.addFile(u":/assets/assets/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(13)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(330, 470)
        MainWindow.setMinimumSize(QSize(330, 470))
        MainWindow.setMaximumSize(QSize(330, 470))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 550 12pt \"Segoe UI\";\n"
"color: rgb(225,225,225);\n"
"background-color: rgb(55,55,55);\n"
"")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(75,75,75,64);\n"
"border-radius: 5px;\n"
"background-color: rgb(80,80,80);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 85, 85);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(90,90,90);\n"
"color: rgba(225,225,225,200);\n"
"border: 1px solid rgba(90,90,90,100);\n"
"}\n"
"QPushButton:disabled {\n"
"color: rgba(225,225,225,86);\n"
"background-color: rgba(100,100,100,180);\n"
"}\n"
"QLineEdit {\n"
"border: 2px solid rgb(75,75,75);\n"
"border-radius: 5px;\n"
"background-color: rgb(90,90,90);\n"
"font: 600 36pt \"Segoe UI\";\n"
"}\n"
"\n"
"")

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 170, 311, 291))

        self.layoutCanvasWidget = QWidget(self.centralwidget)
        self.layoutCanvasWidget.setObjectName(u"layoutCanvasWidget")
        self.layoutCanvasWidget.setGeometry(QRect(0, 0, 0, 0))

        self.layoutCanvas = QVBoxLayout(self.layoutCanvasWidget)
        self.layoutCanvas.setObjectName(u"layoutCanvas")
        self.layoutCanvas.setContentsMargins(0, 0, 0, 0)

        self.label_function = QLabel(self.centralwidget)
        self.label_function.setObjectName(u"label_function")
        self.label_function.setGeometry(QRect(15, 65, 24, 24))
        self.label_function.setPixmap(QPixmap(u":/assets/assets/function.svg"))

        self.label_mode = QLabel(self.centralwidget)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setGeometry(QRect(50, 10, 271, 31))
        self.label_mode.setStyleSheet(u"background-color: transparent")

        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 65, 311, 91))
        self.lineEdit.setMaximumSize(QSize(311, 91))
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setMaxLength(-1)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.pushButton_menu = QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setGeometry(QRect(10, 10, 31, 31))
        icon_menu = QIcon()
        icon_menu.addFile(u":/assets/assets/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon_menu_w = QIcon()
        icon_menu_w.addFile(u":/assets/assets/white/menu_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_menu.setIcon(icon_menu_w)
        self.pushButton_menu.setIconSize(QSize(28, 28))
        self.pushButton_menu.setAutoDefault(False)
        self.pushButton_menu.setFlat(True)

        self.icon_graph1 = QIcon()
        self.icon_graph1.addFile(u":/assets/assets/white/enter_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_graph2 = QIcon()
        self.icon_graph2.addFile(u":/assets/assets/white/close_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(126, 10, 30, 30))
        self.pushButton_close.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/white/close_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon4)
        self.pushButton_close.setIconSize(QSize(18, 18))
        self.pushButton_close.setAutoDefault(False)
        self.pushButton_close.setFlat(True)
        self.pushButton_close.hide()
        self.pushButton_close.setDisabled(True)

        self.pushButton_point = QPushButton(self.layoutWidget)
        self.pushButton_point.setObjectName(u"pushButton_point")
        self.pushButton_point.setSizePolicy(sizePolicy)

        self.pushButton_negate = QPushButton(self.layoutWidget)
        self.pushButton_negate.setObjectName(u"pushButton_negate")
        self.pushButton_negate.setSizePolicy(sizePolicy)

        self.pushButton_equal = QPushButton(self.layoutWidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        self.pushButton_equal.setSizePolicy(sizePolicy)

        self.pushButton_divide = QPushButton(self.layoutWidget)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setSizePolicy(sizePolicy)

        self.pushButton_three = QPushButton(self.layoutWidget)
        self.pushButton_three.setObjectName(u"pushButton_three")
        self.pushButton_three.setSizePolicy(sizePolicy)

        self.pushButton_multiply = QPushButton(self.layoutWidget)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setSizePolicy(sizePolicy)

        self.pushButton_six = QPushButton(self.layoutWidget)
        self.pushButton_six.setObjectName(u"pushButton_six")
        self.pushButton_six.setSizePolicy(sizePolicy)

        self.pushButton_plus = QPushButton(self.layoutWidget)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setSizePolicy(sizePolicy)

        self.pushButton_seven = QPushButton(self.layoutWidget)
        self.pushButton_seven.setObjectName(u"pushButton_seven")
        self.pushButton_seven.setSizePolicy(sizePolicy)

        self.pushButton_fraction = QPushButton(self.layoutWidget)
        self.pushButton_fraction.setObjectName(u"pushButton_fraction")
        self.pushButton_fraction.setSizePolicy(sizePolicy)

        self.pushButton_nine = QPushButton(self.layoutWidget)
        self.pushButton_nine.setObjectName(u"pushButton_nine")
        self.pushButton_nine.setSizePolicy(sizePolicy)

        self.pushButton_clear = QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setSizePolicy(sizePolicy)

        self.pushButton_squareRoot = QPushButton(self.layoutWidget)
        self.pushButton_squareRoot.setObjectName(u"pushButton_squareRoot")
        self.pushButton_squareRoot.setSizePolicy(sizePolicy)

        self.pushButton_four = QPushButton(self.layoutWidget)
        self.pushButton_four.setObjectName(u"pushButton_four")
        self.pushButton_four.setSizePolicy(sizePolicy)

        self.pushButton_zero = QPushButton(self.layoutWidget)
        self.pushButton_zero.setObjectName(u"pushButton_zero")
        self.pushButton_zero.setSizePolicy(sizePolicy)

        self.pushButton_one = QPushButton(self.layoutWidget)
        self.pushButton_one.setObjectName(u"pushButton_one")
        self.pushButton_one.setSizePolicy(sizePolicy)

        self.pushButton_delete = QPushButton(self.layoutWidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setSizePolicy(sizePolicy)
        icon13 = QIcon()
        icon13.addFile(u":/assets/assets/white/delete_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon13)
        self.pushButton_delete.setIconSize(QSize(24, 24))

        self.pushButton_eight = QPushButton(self.layoutWidget)
        self.pushButton_eight.setObjectName(u"pushButton_eight")
        self.pushButton_eight.setSizePolicy(sizePolicy)

        self.pushButton_five = QPushButton(self.layoutWidget)
        self.pushButton_five.setObjectName(u"pushButton_five")
        self.pushButton_five.setSizePolicy(sizePolicy)

        self.pushButton_percent = QPushButton(self.layoutWidget)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setSizePolicy(sizePolicy)

        self.pushButton_degree = QPushButton(self.layoutWidget)
        self.pushButton_degree.setObjectName(u"pushButton_degree")
        self.pushButton_degree.setSizePolicy(sizePolicy)

        self.pushButton_minus = QPushButton(self.layoutWidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setSizePolicy(sizePolicy)

        self.pushButton_two = QPushButton(self.layoutWidget)
        self.pushButton_two.setObjectName(u"pushButton_two")
        self.pushButton_two.setSizePolicy(sizePolicy)

        self.pushButton_cleanEntrance = QPushButton(self.layoutWidget)
        self.pushButton_cleanEntrance.setObjectName(u"pushButton_cleanEntrance")
        self.pushButton_cleanEntrance.setSizePolicy(sizePolicy)

        self.pushButton_pi = QPushButton(self.layoutWidget)
        self.pushButton_pi.setObjectName(u"pushButton_pi")
        self.pushButton_pi.setSizePolicy(sizePolicy)

        self.pushButton_e = QPushButton(self.layoutWidget)
        self.pushButton_e.setObjectName(u"pushButton_e")
        self.pushButton_e.setSizePolicy(sizePolicy)

        self.pushButton_square = QPushButton(self.layoutWidget)
        self.pushButton_square.setObjectName(u"pushButton_square")
        self.pushButton_square.setSizePolicy(sizePolicy)

        self.pushButton_abs = QPushButton(self.layoutWidget)
        self.pushButton_abs.setObjectName(u"pushButton_abs")
        self.pushButton_abs.setSizePolicy(sizePolicy)

        self.pushButton_div = QPushButton(self.layoutWidget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.pushButton_div.setSizePolicy(sizePolicy)

        self.pushButton_mod = QPushButton(self.layoutWidget)
        self.pushButton_mod.setObjectName(u"pushButton_mod")
        self.pushButton_mod.setSizePolicy(sizePolicy)

        self.pushButton_left_bracket = QPushButton(self.layoutWidget)
        self.pushButton_left_bracket.setObjectName(u"pushButton_left_bracket")
        self.pushButton_left_bracket.setSizePolicy(sizePolicy)

        self.pushButton_right_bracket = QPushButton(self.layoutWidget)
        self.pushButton_right_bracket.setObjectName(u"pushButton_right_bracket")
        self.pushButton_right_bracket.setSizePolicy(sizePolicy)

        self.pushButton_factorial = QPushButton(self.layoutWidget)
        self.pushButton_factorial.setObjectName(u"pushButton_factorial")
        self.pushButton_factorial.setSizePolicy(sizePolicy)

        self.pushButton_tendegree = QPushButton(self.layoutWidget)
        self.pushButton_tendegree.setObjectName(u"pushButton_tendegree")
        self.pushButton_tendegree.setSizePolicy(sizePolicy)

        self.pushButton_log = QPushButton(self.layoutWidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setSizePolicy(sizePolicy)

        self.pushButton_ln = QPushButton(self.layoutWidget)
        self.pushButton_ln.setObjectName(u"pushButton_ln")
        self.pushButton_ln.setSizePolicy(sizePolicy)

        self.pushButton_bit_shift_left = QPushButton(self.layoutWidget)
        self.pushButton_bit_shift_left.setObjectName(u"pushButton_bit_shift_left")
        self.pushButton_bit_shift_left.setSizePolicy(sizePolicy)

        self.pushButton_bit_shift_right = QPushButton(self.layoutWidget)
        self.pushButton_bit_shift_right.setObjectName(u"pushButton_bit_shift_right")
        self.pushButton_bit_shift_right.setSizePolicy(sizePolicy)

        self.pushButton_hex_ten = QPushButton(self.layoutWidget)
        self.pushButton_hex_ten.setObjectName(u"pushButton_hex_ten")
        self.pushButton_hex_ten.setSizePolicy(sizePolicy)

        self.pushButton_hex_eleven = QPushButton(self.layoutWidget)
        self.pushButton_hex_eleven.setObjectName(u"pushButton_hex_eleven")
        self.pushButton_hex_eleven.setSizePolicy(sizePolicy)

        self.pushButton_hex_twelve = QPushButton(self.layoutWidget)
        self.pushButton_hex_twelve.setObjectName(u"pushButton_hex_twelve")
        self.pushButton_hex_twelve.setSizePolicy(sizePolicy)

        self.pushButton_hex_thirteen = QPushButton(self.layoutWidget)
        self.pushButton_hex_thirteen.setObjectName(u"pushButton_hex_thirteen")
        self.pushButton_hex_thirteen.setSizePolicy(sizePolicy)

        self.pushButton_hex_fourteen = QPushButton(self.layoutWidget)
        self.pushButton_hex_fourteen.setObjectName(u"pushButton_hex_fourteen")
        self.pushButton_hex_fourteen.setSizePolicy(sizePolicy)

        self.pushButton_hex_fifteen = QPushButton(self.layoutWidget)
        self.pushButton_hex_fifteen.setObjectName(u"pushButton_hex_fifteen")
        self.pushButton_hex_fifteen.setSizePolicy(sizePolicy)

        self.pushButton_enter_function = QPushButton(self.layoutWidget)
        self.pushButton_enter_function.setObjectName(u"pushButton_enter_function")
        self.pushButton_enter_function.setSizePolicy(sizePolicy)
        icon_enter = QIcon()
        icon_enter.addFile(u":/assets/assets/white/enter_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_enter_function.setIcon(icon_enter)
        self.pushButton_enter_function.setIconSize(QSize(14, 14))

        self.pushButton_x = QPushButton(self.layoutWidget)
        self.pushButton_x.setObjectName(u"pushButton_x")
        self.pushButton_x.setSizePolicy(sizePolicy)

        #########################################
        ## CONVERTER
        #########################################

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 140, 311, 71))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2.hide()
        self.lineEdit_2.setReadOnly(True)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(115, 120, 206, 22))
        self.comboBox.setStyleSheet(u"font: 550 10pt \"Segoe UI\";")
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.hide()
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(115, 220, 206, 22))
        self.comboBox_2.setStyleSheet(u"font: 550 10pt \"Segoe UI\";")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.hide()

        #########################################
        ## CONVERTER
        #########################################


        #########################################
        ## SIDE MENU
        #########################################
    
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setGeometry(QRect(0, 0, 210, 470))
        self.frame_menu.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"\n"
"\n"
"\n"
"")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.frame_menu.raise_()
        self.label_calc_modes = QLabel(self.frame_menu)
        self.label_calc_modes.setObjectName(u"label_calc_modes")
        self.label_calc_modes.setGeometry(QRect(10, 40, 191, 31))
        self.label_calc_modes.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
"color: rgba(225, 225, 225, 200);")
        self.pushButton_normal_mode = QPushButton(self.frame_menu)
        self.pushButton_normal_mode.setObjectName(u"pushButton_normal_mode")
        self.pushButton_normal_mode.setGeometry(QRect(10, 70, 191, 31))
        self.pushButton_normal_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_normal_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/white/normal_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_normal_mode.setIcon(icon1)
        self.pushButton_normal_mode.setIconSize(QSize(19, 19))
        self.pushButton_normal_mode.setAutoDefault(False)
        self.pushButton_normal_mode.setFlat(True)
        self.pushButton_engineer_mode = QPushButton(self.frame_menu)
        self.pushButton_engineer_mode.setObjectName(u"pushButton_engineer_mode")
        self.pushButton_engineer_mode.setGeometry(QRect(10, 100, 191, 31))
        self.pushButton_engineer_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/white/engineer_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_engineer_mode.setIcon(icon2)
        self.pushButton_engineer_mode.setIconSize(QSize(19, 19))
        self.pushButton_engineer_mode.setAutoDefault(False)
        self.pushButton_engineer_mode.setFlat(True)
        self.pushButton_programmer_mode = QPushButton(self.frame_menu)
        self.pushButton_programmer_mode.setObjectName(u"pushButton_programmer_mode")
        self.pushButton_programmer_mode.setGeometry(QRect(10, 130, 191, 31))
        self.pushButton_programmer_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/assets/white/programmer_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_programmer_mode.setIcon(icon3)
        self.pushButton_programmer_mode.setIconSize(QSize(19, 19))
        self.pushButton_programmer_mode.setAutoDefault(False)
        self.pushButton_programmer_mode.setFlat(True)
        self.pushButton_volume_mode = QPushButton(self.frame_menu)
        self.pushButton_volume_mode.setObjectName(u"pushButton_volume_mode")
        self.pushButton_volume_mode.setGeometry(QRect(10, 220, 191, 31))
        self.pushButton_volume_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/white/volume_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_volume_mode.setIcon(icon4)
        self.pushButton_volume_mode.setIconSize(QSize(19, 19))
        self.pushButton_volume_mode.setAutoDefault(False)
        self.pushButton_volume_mode.setFlat(True)
        self.pushButton_graph_mode = QPushButton(self.frame_menu)
        self.pushButton_graph_mode.setObjectName(u"pushButton_graph_mode")
        self.pushButton_graph_mode.setGeometry(QRect(10, 160, 191, 30))
        self.pushButton_graph_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_graph_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/assets/assets/white/graph_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_graph_mode.setIcon(icon5)
        self.pushButton_graph_mode.setIconSize(QSize(19, 19))
        self.pushButton_graph_mode.setAutoDefault(False)
        self.pushButton_graph_mode.setFlat(True)
        self.pushButton_energy_mode = QPushButton(self.frame_menu)
        self.pushButton_energy_mode.setObjectName(u"pushButton_energy_mode")
        self.pushButton_energy_mode.setGeometry(QRect(10, 340, 191, 31))
        self.pushButton_energy_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/assets/assets/white/energy_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_energy_mode.setIcon(icon6)
        self.pushButton_energy_mode.setIconSize(QSize(19, 19))
        self.pushButton_energy_mode.setAutoDefault(False)
        self.pushButton_energy_mode.setFlat(True)
        self.pushButton_weight_mode = QPushButton(self.frame_menu)
        self.pushButton_weight_mode.setObjectName(u"pushButton_weight_mode")
        self.pushButton_weight_mode.setGeometry(QRect(10, 310, 191, 31))
        self.pushButton_weight_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/assets/assets/white/weight_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_weight_mode.setIcon(icon7)
        self.pushButton_weight_mode.setIconSize(QSize(19, 19))
        self.pushButton_weight_mode.setAutoDefault(False)
        self.pushButton_weight_mode.setFlat(True)
        self.pushButton_data_mode = QPushButton(self.frame_menu)
        self.pushButton_data_mode.setObjectName(u"pushButton_data_mode")
        self.pushButton_data_mode.setGeometry(QRect(10, 400, 191, 31))
        self.pushButton_data_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/assets/assets/white/data_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_data_mode.setIcon(icon8)
        self.pushButton_data_mode.setIconSize(QSize(19, 19))
        self.pushButton_data_mode.setAutoDefault(False)
        self.pushButton_data_mode.setFlat(True)
        self.pushButton_power_mode = QPushButton(self.frame_menu)
        self.pushButton_power_mode.setObjectName(u"pushButton_power_mode")
        self.pushButton_power_mode.setGeometry(QRect(10, 370, 191, 31))
        self.pushButton_power_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/assets/white/power_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_power_mode.setIcon(icon9)
        self.pushButton_power_mode.setIconSize(QSize(19, 19))
        self.pushButton_power_mode.setAutoDefault(False)
        self.pushButton_power_mode.setFlat(True)
        self.pushButton_square_mode = QPushButton(self.frame_menu)
        self.pushButton_square_mode.setObjectName(u"pushButton_square_mode")
        self.pushButton_square_mode.setGeometry(QRect(10, 250, 191, 31))
        self.pushButton_square_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_square_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/assets/assets/white/square_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_square_mode.setIcon(icon10)
        self.pushButton_square_mode.setIconSize(QSize(19, 19))
        self.pushButton_square_mode.setAutoDefault(False)
        self.pushButton_square_mode.setFlat(True)
        self.pushButton_pressure_mode = QPushButton(self.frame_menu)
        self.pushButton_pressure_mode.setObjectName(u"pushButton_pressure_mode")
        self.pushButton_pressure_mode.setGeometry(QRect(10, 430, 191, 31))
        self.pushButton_pressure_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/assets/assets/white/pressure_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pressure_mode.setIcon(icon11)
        self.pushButton_pressure_mode.setIconSize(QSize(19, 19))
        self.pushButton_pressure_mode.setAutoDefault(False)
        self.pushButton_pressure_mode.setFlat(True)
        self.label_converter_modes = QLabel(self.frame_menu)
        self.label_converter_modes.setObjectName(u"label_converter_modes")
        self.label_converter_modes.setGeometry(QRect(10, 190, 191, 31))
        self.label_converter_modes.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
"color: rgba(225, 225, 225, 200);")
        self.pushButton_length_mode = QPushButton(self.frame_menu)
        self.pushButton_length_mode.setObjectName(u"pushButton_length_mode")
        self.pushButton_length_mode.setGeometry(QRect(10, 280, 191, 31))
        self.pushButton_length_mode.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_length_mode.setStyleSheet(u"font: 550 10pt \"Segoe UI\";\n"
"text-align: left;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/assets/assets/white/length_mode_w.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_length_mode.setIcon(icon12)
        self.pushButton_length_mode.setIconSize(QSize(19, 19))
        self.pushButton_length_mode.setAutoDefault(False)
        self.pushButton_length_mode.setFlat(True)
        self.label_border = QLabel(self.frame_menu)
        self.label_border.setObjectName(u"label_border")
        self.label_border.setGeometry(QRect(208, 0, 2, 470))
        self.label_border.setStyleSheet(u"background-color: rgb(0, 0, 0)")

        ####################################
        ## SIDE MENU
        ####################################

        self.frame_toolbar = QFrame(self.centralwidget)
        self.frame_toolbar.setObjectName(u"frame_toolbar")
        self.frame_toolbar.setGeometry(QRect(10, 170, 311, 31))
        self.frame_toolbar.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(46, 139, 87);\n"
"}\n"
"text-align: center;")
        self.frame_toolbar.setFrameShape(QFrame.StyledPanel)
        self.frame_toolbar.setFrameShadow(QFrame.Raised)
        self.pushButton_toolbar_2 = QPushButton(self.frame_toolbar)
        self.pushButton_toolbar_2.setObjectName(u"pushButton_toolbar_2")
        self.pushButton_toolbar_2.setGeometry(QRect(63, 1, 62, 25))
        self.pushButton_toolbar_4 = QPushButton(self.frame_toolbar)
        self.pushButton_toolbar_4.setObjectName(u"pushButton_toolbar_4")
        self.pushButton_toolbar_4.setGeometry(QRect(187, 1, 62, 25))
        self.pushButton_toolbar_1 = QPushButton(self.frame_toolbar)
        self.pushButton_toolbar_1.setObjectName(u"pushButton_toolbar_1")
        self.pushButton_toolbar_1.setGeometry(QRect(1, 1, 62, 25))
        self.pushButton_toolbar_3 = QPushButton(self.frame_toolbar)
        self.pushButton_toolbar_3.setObjectName(u"pushButton_toolbar_3")
        self.pushButton_toolbar_3.setGeometry(QRect(125, 1, 62, 25))
        self.pushButton_toolbar_5 = QPushButton(self.frame_toolbar)
        self.pushButton_toolbar_5.setObjectName(u"pushButton_toolbar_5")
        self.pushButton_toolbar_5.setGeometry(QRect(249, 1, 62, 25))
        
        self.frame_menu.raise_()
        self.label_mode.raise_()
        self.pushButton_menu.raise_()
        self.pushButton_close.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.widget_lists = [
            self.normal_mode_widgets,
            self.engineer_mode_widgets,
            self.programmer_mode_widgets,
            self.graph_mode_widgets,
            self.converter_mode_widgets
        ]

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def normal_mode(self):
        self.hide_widgets(self.normal_mode_widgets)
        self.show_widgets(self.normal_mode_widgets)
        row = 0
        column = 0
        for widget in self.normal_mode_widgets():
            self.gridLayout.addWidget(widget, row, column, 1, 1)
            column += 1
            if column == 4:
                row += 1
                column = 0

    def engineer_mode(self):
        toolbar_text = {
            self.pushButton_div: 'div',
            self.pushButton_mod: 'mod',
            self.pushButton_toolbar_1: 'sin',
            self.pushButton_toolbar_2: 'cos',
            self.pushButton_toolbar_3: 'tan',
            self.pushButton_toolbar_4: 'ctg',
            self.pushButton_toolbar_5: 'sec',
        }
        for key, value in toolbar_text.items():
            key.setText(value)
        self.hide_widgets(self.engineer_mode_widgets)
        self.show_widgets(self.engineer_mode_widgets)
        self.frame_toolbar.show()
        row = 0
        column = 0
        for widget in self.engineer_mode_widgets():
            self.gridLayout.addWidget(widget, row, column, 1, 1)
            column += 1
            if column == 5:
                row += 1
                column = 0
        self.layoutWidget.setGeometry(QRect(10, 200, 312, 261))

    def programmer_mode(self):
        toolbar_text = {
            self.pushButton_div: '÷',
            self.pushButton_mod: '%',
            self.pushButton_toolbar_1: 'HEX',
            self.pushButton_toolbar_2: 'DEC',
            self.pushButton_toolbar_3: 'OCT',
            self.pushButton_toolbar_4: 'BIN',
            self.pushButton_toolbar_5: '...'
        }
        for key, value in toolbar_text.items():
            key.setText(value)
        self.pushButton_toolbar_5.setDisabled(True)
        self.hide_widgets(self.programmer_mode_widgets)
        self.show_widgets(self.programmer_mode_widgets)
        self.frame_toolbar.show()
        self.pushButton_point.setDisabled(True)
        row = 0
        column = 0
        for widget in self.programmer_mode_widgets():
            self.gridLayout.addWidget(widget, row, column, 1, 1)
            column += 1
            if column == 5:
                row += 1
                column = 0
        self.layoutWidget.setGeometry(QRect(10, 200, 312, 261))

    def graph_mode(self):
        self.hide_widgets(self.graph_mode_widgets)
        self.show_widgets(self.graph_mode_widgets)
        row = 0
        column = 0
        for widget in self.graph_mode_widgets():
            if widget in [self.label_function, self.pushButton_close]:
                continue
            self.gridLayout.addWidget(widget, row, column, 1, 1)
            column += 1
            if column == 5:
                row += 1
                column = 0

    def converter_mode(self, mode):
        self.hide_widgets(self.converter_mode_widgets)
        self.show_widgets(self.converter_mode_widgets)
        row = 0
        column = 1
        for widget in self.converter_mode_widgets():
            if widget in [self.lineEdit_2, self.comboBox, self.comboBox_2]:
                continue
            self.gridLayout.addWidget(widget, row, column, 1, 1)
            column += 1
            if column == 3:
                row += 1
                column = 0
        self.lineEdit.setGeometry(QRect(10, 50, 311, 61))
        self.lineEdit_2.setGeometry(QRect(10, 150, 311, 61))
        self.layoutWidget.setGeometry(QRect(10, 250, 311, 211))
        self.volume_items = {
            'миллилитров': 1000000, 
            'литров': 1000,
            'кубических сантиметров': 1000000, 
            'кубических дециметров': 1000, 
            'кубических метров': 1, # СИ
            'кубических дюймов': 61023.74, 
            'кубических футов': 35.31467, 
            'кубических ярдов': 1.307951,
        }
        self.square_items = {
            'квадратных миллиметров': 1000000,
            'квадратных сантиметров': 10000,
            'квадратных дециметров': 100,
            'квадратных метров': 1, # СИ
            'квадратных километров': 0.000001,
            'квадратных дюймов': 1550.003,
            'квадратных футов':  10.76391,
            'квадратных ярдов': 1.19599,
            'квадратных милей': 0.000000386102159
        }
        self.weight_items = {
            'миллиграммов': 1000000,
            'граммов': 1000,
            'килограммов': 1, # СИ
            'тонн': 0.001,
            'унций': 35.27,
            'фунтов': 2.204623,
            'стоунов': 0.157473
        }
        self.length_items = {
            'микрометров': 1000000,
            'миллиметров': 1000,
            'сантиметров': 100,
            'дециметров': 10,
            'метров': 1, # СИ
            'километров': 0.001,
            'дюймов': 39.37008,
            'футов': 3.28084,
            'ярдов': 1.093613,
            'милей': 1/Decimal('1609.344'),
            'морских милей': 0.00054
        }
        self.energy_items = {
            'джоулей': 1, # СИ
            'килоджоулей': 0.001,
            'мегаджоулей': 0.000001,
            'калорий': 0.239006,
            'килокалорий': 0.000239,
            'электрон-вольт': 6.241509e+18,
            'киловатт-час': 0.000000277777778,
        }
        self.power_items = {
            'ватт': 1, # СИ
            'киловатт': 0.001,
            'мегаватт': 0.000001,
            'лошадиных сил': 0.0014
        }
        self.data_items = {
            'битов': 2**23,
            'килобитов': 2**13,
            'мегабитов': 2**3,
            'гигабитов': 2**-7,
            'терабитов': 2**-17,
            'байтов': 2**20,
            'килобайтов': 2**10,
            'мегабайтов': 1, # СИ
            'гигабайтов': 2**-10,
            'терабайтов': 2**-20,
        }
        self.pressure_items = {
            'паскалей': 1, # СИ
            'килопаскалей': 0.001,
            'мегапаскалей': 0.000001,
            'атмосфер': 1/Decimal('101325'),
            'бар': 0.00001,
            'мм. рт. ст.': 0.007502
        }
        self.items = {
            'converter-volume': self.volume_items,
            'converter-square': self.square_items,
            'converter-weight': self.weight_items,
            'converter-length': self.length_items,
            'converter-energy': self.energy_items,
            'converter-power': self.power_items,
            'converter-data': self.data_items,
            'converter-pressure': self.pressure_items
        }
        self.lineEdit.setAlignment(Qt.AlignLeft|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setMaxLength(15)
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox.addItems(self.items[mode].keys())
        self.comboBox_2.addItems(self.items[mode].keys())
        self.lineEdit_2.setText('0')

    def normal_mode_widgets(self):
        widgets = [
            self.pushButton_percent,
            self.pushButton_cleanEntrance,
            self.pushButton_clear,
            self.pushButton_delete,
            self.pushButton_fraction,
            self.pushButton_degree,
            self.pushButton_squareRoot,
            self.pushButton_divide,
            self.pushButton_seven,
            self.pushButton_eight,
            self.pushButton_nine,
            self.pushButton_multiply,
            self.pushButton_four,
            self.pushButton_five,
            self.pushButton_six,
            self.pushButton_minus,
            self.pushButton_one,
            self.pushButton_two,
            self.pushButton_three,
            self.pushButton_plus,
            self.pushButton_negate,
            self.pushButton_zero,
            self.pushButton_point,
            self.pushButton_equal
        ]
        return widgets

    def engineer_mode_widgets(self):
        widgets = [
            self.pushButton_pi,
            self.pushButton_e,
            self.pushButton_cleanEntrance,
            self.pushButton_clear,
            self.pushButton_delete,
            self.pushButton_square,
            self.pushButton_fraction,
            self.pushButton_abs,
            self.pushButton_mod,
            self.pushButton_div,
            self.pushButton_squareRoot,
            self.pushButton_left_bracket,
            self.pushButton_right_bracket,
            self.pushButton_factorial,
            self.pushButton_divide,
            self.pushButton_degree,
            self.pushButton_seven,
            self.pushButton_eight,
            self.pushButton_nine,
            self.pushButton_multiply,
            self.pushButton_tendegree,
            self.pushButton_four,
            self.pushButton_five,
            self.pushButton_six,
            self.pushButton_minus,
            self.pushButton_log,
            self.pushButton_one,
            self.pushButton_two,
            self.pushButton_three,
            self.pushButton_plus,
            self.pushButton_ln,
            self.pushButton_negate,
            self.pushButton_zero,
            self.pushButton_point,
            self.pushButton_equal
        ]
        return widgets
    
    def programmer_mode_widgets(self):
        widgets = [
            self.pushButton_hex_ten,
            self.pushButton_bit_shift_left,
            self.pushButton_bit_shift_right,
            self.pushButton_clear,
            self.pushButton_delete,
            self.pushButton_hex_eleven,
            self.pushButton_left_bracket,
            self.pushButton_right_bracket,
            self.pushButton_mod,
            self.pushButton_div,
            self.pushButton_hex_twelve,
            self.pushButton_seven,
            self.pushButton_eight,
            self.pushButton_nine,
            self.pushButton_multiply,
            self.pushButton_hex_thirteen,
            self.pushButton_four,
            self.pushButton_five,
            self.pushButton_six,
            self.pushButton_minus,
            self.pushButton_hex_fourteen,
            self.pushButton_one,
            self.pushButton_two,
            self.pushButton_three,
            self.pushButton_plus,
            self.pushButton_hex_fifteen,
            self.pushButton_negate,
            self.pushButton_zero,
            self.pushButton_point,
            self.pushButton_equal
        ]
        return widgets
    
    def graph_mode_widgets(self):
        widgets = [
            self.label_function,
            self.pushButton_close
        ]
        for widget in self.engineer_mode_widgets():
            widgets.append(widget)
        to_replace = {
            15: self.pushButton_x,
            36: self.pushButton_enter_function
        }
        for key, value in to_replace.items():
            widgets[key] = value
        return widgets

    def converter_mode_widgets(self):
        widgets = [
            self.pushButton_cleanEntrance,
            self.pushButton_delete,
            self.pushButton_seven,
            self.pushButton_eight,
            self.pushButton_nine,
            self.pushButton_four,
            self.pushButton_five,
            self.pushButton_six,
            self.pushButton_one,
            self.pushButton_two,
            self.pushButton_three,
            self.pushButton_point,
            self.pushButton_zero,
            self.comboBox,
            self.comboBox_2,
            self.lineEdit_2
        ]
        return widgets

    def show_widgets(self, exact):
        for widget_list in self.widget_lists:
            if widget_list == exact:
                widgets = widget_list()
                for widget in widgets:
                    widget.show()

    def hide_widgets(self, exact):
        for widget_list in self.widget_lists:
            if widget_list != exact:
                widgets = widget_list()
                for widget in widgets:
                    widget.hide()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.pushButton_factorial.setText(QCoreApplication.translate("MainWindow", u"x!", None))
        self.pushButton_nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_negate.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.pushButton_degree.setText(QCoreApplication.translate("MainWindow", u"x\u207f", None))
        self.pushButton_four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_squareRoot.setText(QCoreApplication.translate("MainWindow", u"\u00b2\u221ax", None))
        self.pushButton_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.pushButton_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.pushButton_eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_left_bracket.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_right_bracket.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_tendegree.setText(QCoreApplication.translate("MainWindow", u"10\u207f", None))
        self.pushButton_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_minus.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        self.pushButton_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButton_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.pushButton_square.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.pushButton_fraction.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.pushButton_abs.setText(QCoreApplication.translate("MainWindow", u"| x |", None))
        self.pushButton_div.setText(QCoreApplication.translate("MainWindow", u"div", None))
        self.pushButton_mod.setText(QCoreApplication.translate("MainWindow", u"mod", None))
        self.pushButton_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_cleanEntrance.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_bit_shift_left.setText(QCoreApplication.translate("MainWindow", u"\u00ab", None))
        self.pushButton_bit_shift_right.setText(QCoreApplication.translate("MainWindow", u"\u00bb", None))
        self.pushButton_hex_ten.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.pushButton_hex_eleven.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushButton_hex_twelve.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_hex_thirteen.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_hex_fourteen.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_hex_fifteen.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.pushButton_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))

        self.pushButton_menu.setText("")
        self.label_calc_modes.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.pushButton_normal_mode.setText(QCoreApplication.translate("Form", u" \u041e\u0431\u044b\u0447\u043d\u044b\u0439", None))
        self.pushButton_engineer_mode.setText(QCoreApplication.translate("Form", u" \u0418\u043d\u0436\u0435\u043d\u0435\u0440\u043d\u044b\u0439", None))
        self.pushButton_programmer_mode.setText(QCoreApplication.translate("Form", u" \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442", None))
        self.pushButton_volume_mode.setText(QCoreApplication.translate("Form", u" \u041e\u0431\u044a\u0435\u043c", None))
        self.pushButton_graph_mode.setText(QCoreApplication.translate("Form", u" \u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.pushButton_energy_mode.setText(QCoreApplication.translate("Form", u" \u042d\u043d\u0435\u0440\u0433\u0438\u044f", None))
        self.pushButton_weight_mode.setText(QCoreApplication.translate("Form", u" \u041c\u0430\u0441\u0441\u0430", None))
        self.pushButton_length_mode.setText(QCoreApplication.translate("Form", u" \u0414\u043b\u0438\u043d\u0430", None))
        self.pushButton_data_mode.setText(QCoreApplication.translate("Form", u" \u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButton_power_mode.setText(QCoreApplication.translate("Form", u" \u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.pushButton_square_mode.setText(QCoreApplication.translate("Form", u" \u041f\u043b\u043e\u0449\u0430\u0434\u044c", None))
        self.pushButton_pressure_mode.setText(QCoreApplication.translate("Form", u" \u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_converter_modes.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_mode.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442", None))
    # retranslateUi

