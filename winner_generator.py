from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
def show_winner():
    if question.text() == '?':
        random_number = randint(1, 20)
        question.setText(str(random_number))
        text.setText('Победитель')


app = QApplication([])
window = QWidget()
window.resize(600, 400)
window.setWindowTitle('Определитель победителя')
window.move(50, 200)



text = QLabel('Нажми чтобы узнать победителя')
question = QLabel('?')

btn = QPushButton('Сгенирировать')
btn.clicked.connect(show_winner)

v_line = QVBoxLayout()
v_line.addWidget(text, alignment=Qt.AlignCenter)
v_line.addWidget(question, alignment=Qt.AlignCenter)
v_line.addWidget(btn, alignment=Qt.AlignCenter)

window.setLayout(v_line)


window.show()
app.exec()