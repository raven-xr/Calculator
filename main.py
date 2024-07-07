from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import (QRect, Qt)
from ui_main import Ui_MainWindow

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
NavigationToolbar.toolitems = (
    ('Home', None, 'home', 'home'),
    ('Back', None, 'back', 'back'),
    ('Forward', None, 'forward', 'forward'),
    ('Zoom', None, 'zoom_to_rect', 'zoom'),
    ('Pan', None, 'move', 'pan'),
)

from decimal import Decimal
import numpy as np
import math
import sys
import re

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=80):
        fig = Figure(dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        # Конструктор
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'е', '(', ')', 'A', 'B', 'C', 'D', 'E', 'F', 'x']
        self.operators = ['÷', '×', '^', '-', '+', ' div ', ' mod ', '«', '»']
        self.specials = ['1/', '√', '10^', 'negate', 'abs', 'ln', 'log', 'fact', 'sin', 'cos', 'tan', 'ctg', 'sec']
        self.dependents = ['%']
        self.others = ['.']

        self.result_status = False
        self.is_menu_opened = False
        self.current_mode = 'normal'
        self.current_numsys = 10
        self.change_mode('normal')
        self.change_numsys(1)
        
        connect_buttons = {
            self.ui.pushButton_zero: lambda: self.input('0'),
            self.ui.pushButton_one: lambda: self.input('1'),
            self.ui.pushButton_two: lambda: self.input('2'),
            self.ui.pushButton_three: lambda: self.input('3'),
            self.ui.pushButton_four: lambda: self.input('4'),
            self.ui.pushButton_five: lambda: self.input('5'),
            self.ui.pushButton_six: lambda: self.input('6'),
            self.ui.pushButton_seven: lambda: self.input('7'),
            self.ui.pushButton_eight: lambda: self.input('8'),
            self.ui.pushButton_nine: lambda: self.input('9'),

            self.ui.pushButton_divide: lambda: self.input('÷'),
            self.ui.pushButton_multiply: lambda: self.input('×'),
            self.ui.pushButton_minus: lambda: self.input('-'),
            self.ui.pushButton_plus: lambda: self.input('+'),
            self.ui.pushButton_delete: self.delete,
            self.ui.pushButton_degree: lambda: self.input('^'),
            self.ui.pushButton_square: lambda: [self.ui.pushButton_degree.click(), self.ui.pushButton_two.click()],

            self.ui.pushButton_hex_ten: lambda: self.input('A'),
            self.ui.pushButton_hex_eleven: lambda: self.input('B'),
            self.ui.pushButton_hex_twelve: lambda: self.input('C'),
            self.ui.pushButton_hex_thirteen: lambda: self.input('D'),
            self.ui.pushButton_hex_fourteen: lambda: self.input('E'),
            self.ui.pushButton_hex_fifteen: lambda: self.input('F'),

            self.ui.pushButton_clear: self.clear,
            self.ui.pushButton_cleanEntrance: self.cleanEntrance,
            self.ui.pushButton_equal: self.equal,
            self.ui.pushButton_menu: self.menu,

            self.ui.pushButton_enter_function: lambda: self.show_graph(2),
            self.ui.pushButton_close: lambda: self.show_graph(0),

            self.ui.pushButton_normal_mode: lambda: self.change_mode('normal'),
            self.ui.pushButton_engineer_mode: lambda: self.change_mode('engineer'),
            self.ui.pushButton_programmer_mode: lambda: self.change_mode('programmer'),
            self.ui.pushButton_graph_mode: lambda: self.change_mode('graph'),

            self.ui.pushButton_volume_mode: lambda: self.change_mode('converter-volume'),
            self.ui.pushButton_square_mode: lambda: self.change_mode('converter-square'),
            self.ui.pushButton_weight_mode: lambda: self.change_mode('converter-weight'),
            self.ui.pushButton_length_mode: lambda: self.change_mode('converter-length'),
            self.ui.pushButton_energy_mode: lambda: self.change_mode('converter-energy'),
            self.ui.pushButton_power_mode: lambda: self.change_mode('converter-power'),
            self.ui.pushButton_data_mode: lambda: self.change_mode('converter-data'),
            self.ui.pushButton_pressure_mode: lambda: self.change_mode('converter-pressure'),

            self.ui.pushButton_fraction: lambda: self.input('1/'),
            self.ui.pushButton_squareRoot: lambda: self.input('√'),
            self.ui.pushButton_negate: lambda: self.input('negate'),
            self.ui.pushButton_abs: lambda: self.input('abs'),
            self.ui.pushButton_percent: lambda: self.input('%'),
            self.ui.pushButton_factorial: lambda: self.input('fact'),
            self.ui.pushButton_log: lambda: self.input('log'),
            self.ui.pushButton_ln: lambda: self.input('ln'),
            self.ui.pushButton_tendegree: lambda: self.input('10^'),

            self.ui.pushButton_mod: lambda: self.input(' mod '),
            self.ui.pushButton_div: lambda: self.input(' div '),

            self.ui.pushButton_e: lambda: self.input('е'),
            self.ui.pushButton_pi: lambda: self.input('π'),

            self.ui.pushButton_point: lambda: self.input('.'),
            self.ui.pushButton_left_bracket: lambda: self.input('('),
            self.ui.pushButton_right_bracket: lambda: self.input(')'),
            self.ui.pushButton_bit_shift_left: lambda: self.input('«'),
            self.ui.pushButton_bit_shift_right: lambda: self.input('»'),

            self.ui.pushButton_x: lambda: self.input('x'),
            self.ui.pushButton_enter_function: self.enter_function
        }
        
        for key, value in connect_buttons.items():
            key.clicked.connect(value)

    def menu(self) -> None:
        # Меню
        if self.is_menu_opened:
            self.ui.frame_menu.hide()
            self.is_menu_opened = False
        else:
            self.ui.frame_menu.show()
            self.is_menu_opened = True

    def change_mode(self, mode: str) -> None:
        # Изменение режима калькулятора
        def engineer_mode():
            self.ui.engineer_mode()
            connect_toolbar = {
                self.ui.pushButton_toolbar_1: lambda: self.input('sin'),
                self.ui.pushButton_toolbar_2: lambda: self.input('cos'),
                self.ui.pushButton_toolbar_3: lambda: self.input('tan'),
                self.ui.pushButton_toolbar_4: lambda: self.input('ctg'),
                self.ui.pushButton_toolbar_5: lambda: self.input('sec')
            }
            for key, value in connect_toolbar.items():
                try: key.clicked.disconnect()
                except: pass
                key.clicked.connect(value)
                key.setEnabled(True)

        def programmer_mode():
            self.ui.programmer_mode()
            connect_toolbar = {
                self.ui.pushButton_toolbar_1: lambda: self.change_numsys(0),
                self.ui.pushButton_toolbar_2: lambda: self.change_numsys(1),
                self.ui.pushButton_toolbar_3: lambda: self.change_numsys(2),
                self.ui.pushButton_toolbar_4: lambda: self.change_numsys(3)
            }
            for key, value in connect_toolbar.items():
                try: key.clicked.disconnect()
                except: pass
                key.clicked.connect(value)

        self.clear()
        self.ui.frame_menu.hide()
        self.is_menu_opened = False
        modes_localization = {
            'normal': 'Обычный',
            'engineer': 'Инженерный',
            'programmer': 'Программист',
            'graph': 'Графики',
            'converter-volume': 'Объем',
            'converter-square': 'Площадь',
            'converter-length': 'Длина',
            'converter-weight': 'Масса',
            'converter-energy': 'Энергия',
            'converter-power': 'Мощность',
            'converter-data': 'Данные',
            'converter-pressure': 'Давление',
        }
        self.ui.label_mode.setText(modes_localization[mode])
        if self.current_mode == 'programmer' or 'engineer':
            self.ui.frame_toolbar.hide()
            self.ui.layoutWidget.setGeometry(QRect(10, 170, 311, 291))
        if self.current_mode == 'programmer':
            self.ui.pushButton_toolbar_5.setEnabled(True)
            for widget in self.ui.normal_mode_widgets():
                widget.setEnabled(True)
            self.ui.pushButton_point.setEnabled(True)
            self.current_numsys = 10
            self.ui.pushButton_div.setText('div')
            self.ui.pushButton_mod.setText('mod')
        elif self.current_mode == 'graph':
            self.show_graph(0)
        elif self.current_mode == 'engineer':
            self.ui.pushButton_toolbar_2.setDisabled(True)
        elif 'converter' in self.current_mode:
            self.ui.lineEdit.setGeometry(QRect(10, 65, 311, 91))
            self.ui.layoutWidget.setGeometry(QRect(10, 170, 311, 291))
            self.ui.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
            self.ui.lineEdit.setMaxLength(-1)
            self.ui.comboBox.currentIndexChanged.disconnect()
            self.ui.comboBox_2.currentIndexChanged.disconnect()
        modes = {
            'normal': self.ui.normal_mode,
            'engineer': engineer_mode,
            'programmer': programmer_mode,
            'graph': self.ui.graph_mode
        }
        self.current_mode = mode
        if mode in modes.keys():
            modes[mode]()
        else:
            self.ui.converter_mode(mode)
            self.ui.comboBox.currentIndexChanged.connect(self.convert)
            self.ui.comboBox_2.currentIndexChanged.connect(self.convert)

    def input(self, symbol: str) -> None:
        if (self.result_status) and ((symbol in self.numbers) or (self.ui.lineEdit.text() == 'Ошибка')):
            self.clear()
        self.result_status = False
        text = self.ui.lineEdit.text()
        last_element = re.split(r'[+^-÷×()«»]| div | mod ', text)[-1]
        if (last_element == '0') and (symbol in self.numbers):
            text = text[:-1]

        def input_number(text: str, symbol: str) -> str:
            textends_withop, operator = self.get_textends_withop(text)
            if (text.endswith('0')) and (symbol == '0'):
                last_element = re.split(r'[+^-÷×()«»]| div | mod ', text)[-1]
                if (last_element == '0') and not ('.' in last_element):
                    text = text[:-1]

            if not (textends_withop) and (len(text) > 0):
                if (symbol in ['π', 'е', 'x', 'y'] and not (text.endswith('('))) or ((text[-1] in ['π', 'е', ')', 'x', 'y']) and (symbol != ')')):
                    symbol = '×' + symbol
                elif (symbol in ['(', ')']):
                    if (text[-1] != '(') and (symbol == '('):
                        symbol = '×' + symbol
                    elif (symbol == ')') and (text.count('(') == text.count(')')):
                        symbol = ''
                    elif (text[-1] == '(') and (symbol == ')'):
                        symbol = '0' + symbol
            elif (symbol == ')') and (len(text) == 0):
                text = '0'
                symbol = ''
            elif (textends_withop) and (symbol == ')'):
                text = text[:len(text)-len(operator)]
            return text, symbol
        
        def input_operator(text: str, symbol: str) -> str:
            while re.search(r'(\.(\d*0+)?)$', text): 
                text = text[:-1]
            textends_withop, operator = self.get_textends_withop(text)
            if textends_withop:
                text = text[:len(text)-len(operator)]
            if text.endswith('('):
                symbol = '0' + symbol
            return text, symbol

        def input_special(text: str, symbol: str) -> str:
            while re.search(r'(\.(\d*0+)?)$', text): text = text[:-1]
            textends_withop, operator = self.get_textends_withop(text)
            element = self.get_element(text, textends_withop, operator)
            if not textends_withop:
                text = text[:len(text)-len(element)]
            if element == 'Ошибка':
                return 'Ошибка', ''
            if (element.startswith('(')) and (element.endswith(')')):
                symbol = symbol + element
            else:
                symbol = symbol + '(' + element + ')'
            return text, symbol
        
        def input_dependent(text: str, symbol: str) -> str:
            textends_withop, operator = self.get_textends_withop(text)
            percent = self.get_element(text, textends_withop, operator)
            if not textends_withop:
                text = text[:len(text)-len(percent)]
                textends_withop, operator = self.get_textends_withop(text)
                element = self.get_element(text, textends_withop, operator)
            else:
                element = percent
            if len(element) != len(text):
                try:
                    symbol = str((Decimal(element)/100*Decimal(percent)).normalize())
                except:
                    text, symbol = 'Ошибка', ''
                    self.result_status = True
            else:
                text, symbol = '0', ''
            return text, symbol

        def input_other(text: str, symbol: str) -> str:
            textends_withop, operator = self.get_textends_withop(text)
            if text.endswith('.'):
                symbol = ''
            elif textends_withop:
                symbol = '0.'
            elif text.endswith(')'):
                symbol = '+0.'
            last_element = re.split(r'[+^-÷×()«»]| div | mod ', text)[-1]
            if '.' in last_element:
                symbol = ''
            return text, symbol

        if symbol in self.numbers: func = input_number
        elif symbol in self.operators: func = input_operator
        elif symbol in self.specials: func = input_special
        elif symbol in self.dependents: func = input_dependent
        else: func = input_other
        text, add = func(text, symbol)
        text = text + add
        self.ui.lineEdit.setText(text)
        if 'converter' in self.current_mode:
            self.convert()
        self.format_style()

    def calculate(self, text: str) -> str:
        # Вычисление
        text = self.convert_numsys_2dec(text)
        text = self.prep(text)
        text = self.replace(text)
        try:
            if self.current_mode != 'programmer':
                text = re.sub(r'(\d+(\.\d+)?)', r'Decimal("\1")', text)
            text = eval(text)
        except Exception as error:
            print(f'class MainWindow.calculate >> {error}')
            text = 'Ошибка'
        else:
            if 'E' in str(text):
                text = text.normalize()
            text = str(text)
            while ('.' in text) and (text.endswith('.') or text.endswith('0')):
                text = text[:-1]
            if self.current_numsys != 10:
                text = self.convert_numsys(text, self.current_numsys)
            if text.startswith('-'):
                text = '(' + text + ')'
        return text

    def replace(self, text: str) -> str:
        to_replace = {
            'E': '*10^',
            'е': '2.7182818284',
            'π': '3.1415926535',
            '»': '>>',
            '«': '<<',
            '^': '**',
            ' mod ': '%',
            ' div ': '//',
            '×': '*',
            '÷': '/',
            '√': 'self.sqrt',
            'fact': 'self.fact',
            'sin': 'self.sin',
            'cos': 'self.cos',
            'tan': 'self.tan',
            'ctg': 'self.ctg',
            'sec': 'self.sec',
            'log': 'self.log',
            'ln': 'self.ln',
            'negate': 'self.negate'
        }
        for key, value in to_replace.items():
            text = text.replace(key, value)
        return text

    def prep(self, text: str) -> str:
        # Подготовка
        if text.endswith('('):
            text = text + '0)'
        textends_withop, operator = self.get_textends_withop(text)
        if textends_withop:
            element = self.get_element(text, textends_withop, operator)
            text = text + element
        if text.endswith('.'):
            text = text[:len(text)-len('.')]
        if text.count('(') > text.count(')'):
            text = text + ')'*(text.count('(')-text.count(')'))
        return text

    def clear(self) -> None:
        # Очистка
        self.ui.lineEdit.setText('0')
        self.format_style()

    def cleanEntrance(self) -> None:
        # Чистый вход
        text = self.ui.lineEdit.text()
        textends_withop, operator = self.get_textends_withop(text)
        if not (textends_withop):
            element = self.get_element(text, textends_withop, operator)
            text = text[:len(text)-len(element)]
            if text == '':
                text = '0'
            self.ui.lineEdit.setText(text)
        if 'converter' in self.current_mode:
            self.convert()

    def delete(self) -> None:
        # Удаление
        if not self.result_status:
            text = self.ui.lineEdit.text()
            for operator in self.operators:
                if text.endswith(operator):
                    text = text[:len(text)-len(operator)]
                    break
            else:
                text = text[:len(text)-1]
            if len(text) == 0:
                text = '0'
            self.ui.lineEdit.setText(text)
        else:
            self.clear()
        if 'converter' in self.current_mode:
            self.convert()
        self.format_style()
        
    def format_style(self) -> None:
        # Форматирование
        text = self.ui.lineEdit.text()
        text_2 = self.ui.lineEdit_2.text()

        styleSheets = {
            0: u"font: 600 36pt \"Segoe UI\";\n""border: 2px solid rgb(75,75,75);\n""border-radius: 5px;\n""background-color: rgb(90,90,90);",
            11: u"font: 600 28pt \"Segoe UI\";\n""border: 2px solid rgb(75,75,75);\n""border-radius: 5px;\n""background-color: rgb(90,90,90);",
            14: u"font: 600 24pt \"Segoe UI\";\n""border: 2px solid rgb(75,75,75);\n""border-radius: 5px;\n""background-color: rgb(90,90,90);",
            17: u"font: 600 19pt \"Segoe UI\";\n""border: 2px solid rgb(75,75,75);\n""border-radius: 5px;\n""background-color: rgb(90,90,90);",
            20: u"font: 600 17pt \"Segoe UI\";\n""border: 2px solid rgb(75,75,75);\n""border-radius: 5px;\n""background-color: rgb(90,90,90);",
        }
        for key, value in styleSheets.items():
            if len(text) > key:
                styleSheet = value
            if len(text_2) > key:
                styleSheet_2 = value

        self.ui.lineEdit.setStyleSheet(styleSheet)
        self.ui.lineEdit_2.setStyleSheet(styleSheet_2.replace('600', '550'))

    # Перевод систем счисления

    def format_numsys(self, text: str) -> str:
        convert = {
            16: hex,
            8: oct,
            2: bin
        }
        func = convert[self.current_numsys]
        text = str(func(int(text)))[2:]
        if func == hex:
            text = text.upper()
        return text
    
    def change_numsys(self, index: int) -> None:
        # Изменения системы счисления
        text = self.ui.lineEdit.text()
        text = self.convert_numsys_2dec(text)

        def disable_button(index: int):
            disable_button = {
                0: self.ui.pushButton_toolbar_1,
                1: self.ui.pushButton_toolbar_2,
                2: self.ui.pushButton_toolbar_3,
                3: self.ui.pushButton_toolbar_4
            }
            disable_button[index].setDisabled(True)
            for key, value in disable_button.items():
                if key == index: continue
                value.setEnabled(True)
    
        for widget in self.ui.programmer_mode_widgets():
            if widget != self.ui.pushButton_point:
                widget.setEnabled(True)

        if index == 0:
            self.current_numsys = 16
            self.ui.lineEdit.setText(self.convert_numsys(text, 16))
            self.format_style()
            return disable_button(index)
        else:
            self.ui.pushButton_hex_ten.setDisabled(True)
            self.ui.pushButton_hex_eleven.setDisabled(True)
            self.ui.pushButton_hex_twelve.setDisabled(True)
            self.ui.pushButton_hex_thirteen.setDisabled(True)
            self.ui.pushButton_hex_fourteen.setDisabled(True)
            self.ui.pushButton_hex_fifteen.setDisabled(True)

        if index == 1:
            self.current_numsys = 10
            self.ui.lineEdit.setText(text)
            self.format_style()
            return disable_button(index)
        else:
            self.ui.pushButton_eight.setDisabled(True)
            self.ui.pushButton_nine.setDisabled(True)

        if index == 2:
            self.current_numsys = 8
            self.ui.lineEdit.setText(self.convert_numsys(text, 8))
            self.format_style()
            return disable_button(index)
        else:
            self.ui.pushButton_seven.setDisabled(True)
            self.ui.pushButton_four.setDisabled(True)
            self.ui.pushButton_five.setDisabled(True)
            self.ui.pushButton_six.setDisabled(True)
            self.ui.pushButton_two.setDisabled(True)
            self.ui.pushButton_three.setDisabled(True)

        if index == 3:
            self.current_numsys = 2
            self.ui.lineEdit.setText(self.convert_numsys(text, 2))
            self.format_style()
            return disable_button(index)

    def convert_numsys(self, text: str, sys: int) -> str:
        numsys = {
            16: hex,
            8: oct,
            2: bin
        }
        textends_withop, operator = self.get_textends_withop(text)
        text = text[:len(text)-len(operator)]
        elements = set(re.split(r'[-÷^×+«»()]| mod | div ', text))
        if '' in elements:
            elements.remove('')
        for element in elements:
            text = text.replace(element, numsys[sys](int(element))[2:])
        text = text.upper()
        text.replace('DIV', 'div')
        text.replace('MOD', 'mod')
        return text

    def convert_numsys_2dec(self, text: str) -> str:
        if self.current_numsys != 10:
            elements = set(re.split(r'[-÷^×+«»()]| mod | div ', text))
            for element in elements:
                if element == '': continue
                text = text.replace(element, str(int(element, self.current_numsys)))
        return text

    # Графики

    def enter_function(self) -> None:
        self.show_graph(2)

    def show_graph(self, state: int) -> None:
        def replace(text: str) -> str:
            to_replace = {
                'E': '*10^',
                'е': '2.7182818284',
                'π': '3.1415926535',
                '»': '>>',
                '«': '<<',
                '^': '**',
                ' mod ': '%',
                ' div ': '//',
                '×': '*',
                '÷': '/',
                '√': 'np.sqrt',
                'log': 'np.log10',
                'ln': 'np.log',
                'negate': 'self.negate'
            }
            for key, value in to_replace.items():
                text = text.replace(key, value)
            return text
        
        if state == 2:
            text = self.ui.lineEdit.text()
            text = self.prep(text)
            text = replace(text)
            canvas = MplCanvas(self)
            toolbar = NavigationToolbar(canvas)
            x = np.around(np.arange(-100, 100, 0.01), decimals=4)
            try:
                y = eval(text)
            except Exception as error:
                self.ui.lineEdit.setText('Ошибка')
                print(f'class MainWindow.show_graph >> eval() >> {error}')
                self.result_status = True
                return
            try:
                if 'x' in text:
                    canvas.axes.plot(x, y, color = '#AAAAAA')
                else:
                    canvas.axes.plot([min(x), max(x)], [y, y], color = '#AAAAAA')
                    canvas.axes.set_xlim(-10, 10)
                    canvas.axes.set_ylim(y-10, y+10)
            except Exception as error:
                self.ui.lineEdit.setText('Ошибка')
                print(f'class MainWindow.show_graph >> canvas.axes.plot() >> {error}')
                self.result_status = True
                return
            else:
                canvas.axes.tick_params(axis='x', colors='#CCCCCC')
                canvas.axes.tick_params(axis='y', colors='#CCCCCC')
                canvas.axes.grid(True, color = '#000000')
                canvas.axes.set_facecolor('#505050')
                canvas.figure.set_facecolor('#373737')
                self.ui.layoutCanvas.addWidget(canvas)
                self.ui.layoutCanvas.addWidget(toolbar)
                self.ui.layoutCanvasWidget.setGeometry(QRect(0, 150, 331, 321))
                self.ui.pushButton_close.setEnabled(True)
            self.result_status = True
        else:
            for i in reversed(range(self.ui.layoutCanvas.count())): 
                self.ui.layoutCanvas.itemAt(i).widget().setParent(None)
            self.ui.layoutCanvasWidget.setGeometry(QRect(0, 0, 0, 0))
            self.ui.pushButton_close.setDisabled(True)

    # Преобразователь

    def convert(self) -> None:
        text = self.ui.lineEdit.text()
        ratio = Decimal(str(self.ui.items[self.current_mode][self.ui.comboBox.currentText()])) / Decimal(str(self.ui.items[self.current_mode][self.ui.comboBox_2.currentText()]))
        text = Decimal(text) / ratio
        if 'E' in str(text):
            text = text.normalize()
        text = str(text)
        while ('.' in text) and (text.endswith('.') or text.endswith('0')):
            text = text[:-1]
        self.ui.lineEdit_2.setText(text)
        self.format_style()
        self.ui.lineEdit.setCursorPosition(0)
        self.ui.lineEdit_2.setCursorPosition(0)

    # Инструменты

    def get_textends_withop(self, text: str) -> (bool | str):
        for operator in self.operators:
            if text.endswith(operator):
                textends_withop = True
                break
            else:
                textends_withop, operator = False, ''
        return textends_withop, operator

    def get_element(self, text: str, textends_withop: bool, operator: str) -> str:
        right_pos = len(text) - len(operator)
        right_bracket_count = 0
        left_pos = 0
        left_bracket_count = 0
        if text.endswith(')'):
            for i in range(-1, -len(text)-1, -1):
                if text[i] == ')':
                    right_bracket_count += 1
                elif text[i] == '(':
                    left_bracket_count += 1
                if ((left_bracket_count == right_bracket_count) and (text[i] in ['÷', '×', '^', '-', '+', ' ', '«', '»'])) or (left_bracket_count > right_bracket_count):
                    left_pos = i+1
                    break
            element = text[left_pos: right_pos]
        elif textends_withop:
            for i in range(-1, -len(text)-1, -1):
                if text[i] == ')':
                    right_bracket_count += 1
                elif text[i] == '(':
                    left_bracket_count += 1
                if left_bracket_count > right_bracket_count:
                    left_pos = i+1
                    break
            element = self.calculate(text[left_pos: right_pos])
        else:
            for i in range(-1, -len(text)-1, -1):
                if (text[i] in ['÷', '×', '^', '-', ' ', '+', '«', '»']):
                    left_pos = i+1
                    break
            element = text[left_pos: right_pos]
        if element == '':
            element = '0'
        return element

    # Математические функции

    def sin(self, number: Decimal) -> Decimal:
        result = Decimal(str(math.sin(number*Decimal(str(math.pi))/180)))
        result = round(result, 6)
        return result
    
    def cos(self, number: Decimal) -> Decimal:
        result = Decimal(str(math.cos(number*Decimal(str(math.pi))/180)))
        result = round(result, 6)
        return result
    
    def tan(self, number: Decimal) -> Decimal:
        result = Decimal(str(math.tan(number*Decimal(str(math.pi))/180)))
        result = round(result, 6)
        return result
    
    def ctg(self, number: Decimal) -> Decimal:
        result = 1/Decimal(str(math.tan(number*Decimal(str(math.pi))/180)))
        result = round(result, 6)
        return result
    
    def sec(self, number: Decimal) -> Decimal:
        result = 1/Decimal(math.cos(number*Decimal(str(math.pi))/180))
        result = round(result, 6)
        return result
    
    def log(self, number: Decimal) -> Decimal:
        result = Decimal(str(math.log10(number)))
        return result

    def ln(self, number: Decimal) -> Decimal:
        result = Decimal(str(math.log(number)))
        return result
    
    def fact(self, number: Decimal) -> Decimal:
        result = Decimal(str(math.gamma(number+1)))
        return result
    
    def sqrt(self, number: Decimal) -> Decimal:
        result = Decimal.sqrt(number)
        return result
    
    def negate(self, number: Decimal) -> Decimal:
        result = -number
        return result

    def equal(self) -> None:
        self.ui.lineEdit.setText(self.calculate(self.ui.lineEdit.text()))
        self.format_style()
        self.ui.lineEdit.setCursorPosition(0)
        self.result_status = True

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()