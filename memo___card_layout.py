''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

# віджети, які треба буде розмістити:
# віджети питання
b_menu = QPushButton('Меню')
b_rest = QPushButton('Відпочити')
b_answer = QPushButton('Відповісти')
b_timer = QSpinBox()
b_timer.setValue(30) 
question = QLabel('')
time = QLabel('хвилини')

Radiogroupbox = QGroupBox('Варіанти відповідей')
Radiogroup = QButtonGroup()

button1 = QRadioButton('')
button2 = QRadioButton('')
button3 = QRadioButton('')
button4 = QRadioButton('')

Radiogroup.addButton(button1)
Radiogroup.addButton(button2)
Radiogroup.addButton(button3)
Radiogroup.addButton(button4)

# Віджети результуючого вікна
AnswerRadiogroupbox = QGroupBox('Результат теста')
result = QLabel('')
correctansw = QLabel('')
V_lineresult1 = QVBoxLayout()
V_lineresult1.addWidget(result)
V_lineresult1.addWidget(correctansw)
AnswerRadiogroupbox.setLayout(V_lineresult1)
AnswerRadiogroupbox.hide()

# розміщення віджетів питання
# розміщення кнопочок питань
H_line1 = QHBoxLayout()
V_line1 = QVBoxLayout()
V_line2 = QVBoxLayout()
V_line1.addWidget(button1)
V_line1.addWidget(button3)
V_line2.addWidget(button2)
V_line2.addWidget(button4)
H_line1.addLayout(V_line1)
H_line1.addLayout(V_line2)
Radiogroupbox.setLayout(H_line1)


# 
V_linebutton1 = QVBoxLayout()
H_linebutton1 = QHBoxLayout()
H_linebutton2 = QHBoxLayout()
H_linebutton3 = QHBoxLayout()
H_linebutton4 = QHBoxLayout()

H_linebutton1.addWidget(b_menu)
H_linebutton1.addStretch(1)
H_linebutton1.addWidget(b_rest)
H_linebutton1.addWidget(b_timer)
H_linebutton1.addWidget(time)
H_linebutton2.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
H_linebutton3.addWidget(Radiogroupbox)
H_linebutton3.addWidget(AnswerRadiogroupbox)
H_linebutton4.addWidget(b_answer)

V_linebutton1.addLayout(H_linebutton1, stretch=1)
V_linebutton1.addLayout(H_linebutton2, stretch=2)
V_linebutton1.addLayout(H_linebutton3, stretch=8)
V_linebutton1.addStretch(1)
V_linebutton1.addLayout(H_linebutton4, stretch=1)
V_linebutton1.addStretch(1)
V_linebutton1.setSpacing(5)


# розміщення віджетів результатів

# розміщення кнопочок результатів

# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    Radiogroupbox.hide()
    AnswerRadiogroupbox.show()
    b_answer.setText('Наступне питання')

def show_question():
    Radiogroupbox.show()
    AnswerRadiogroupbox.hide()
    b_answer.setText('Відповісти')

    Radiogroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    Radiogroup.setExclusive(True)