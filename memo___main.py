from memo___card_layout import (app, button1, button2, button3, button4,
    question, result, correctansw, show_result, b_answer, show_question, b_timer, b_rest)
from PyQt5.QtWidgets import QWidget
from random import shuffle, randint # будем перемешивать ответы в карточке вопроса
from memo___card_layout import (V_linebutton1)
from data import questions
from time import sleep

card_width, card_height = 600, 500 # начальные размеры окна "карточка"
text_wrong = 'Неправильно'
text_correct = 'Правильно'

frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'


radio_list = [button1, button2, button3, button4]
shuffle(radio_list)
answer = radio_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]



def show_data():
    global radio_list,answer, wrong_answer1, wrong_answer2, wrong_answer3
    shuffle(radio_list)
    answer = radio_list[0]
    wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]
    question.setText(frm_question)
    answer.setText(frm_right)
    result.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)


def check_result():
    correct = answer.isChecked()
    if correct:
        result.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            result.setText(text_wrong)
            show_result()

def click_ok():
    if b_answer.text() != 'Наступне питання':
        check_result()
    else:
        next_question()

def next_question():
    global frm_question, frm_right, frm_wrong1, frm_wrong2,frm_wrong3
    random_number = randint(1, len(questions))
    frm_question = questions[random_number]["question"]
    frm_right = questions[random_number]["correct_ans"]
    frm_wrong1 = questions[random_number]["wrong_ans_1"]
    frm_wrong2 = questions[random_number]["wrong_ans_2"]
    frm_wrong3 = questions[random_number]["wrong_ans_3"]
    show_data()
    show_question()
    b_answer.setText('Ок')

def rest():
    win_card.hide()
    n = b_timer.value()
    sleep(n)
    win_card.show()





win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.setWindowTitle('Memory Card')
win_card.setLayout(V_linebutton1)
show_data()
show_question()
b_answer.clicked.connect(click_ok)
b_rest.clicked.connect(rest)


#здесь должны быть параметры окна

win_card.show()
app.exec_()