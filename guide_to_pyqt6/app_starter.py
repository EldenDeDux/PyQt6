"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic Calculator App")


        # TODO: add a text input for user's name
        self.number_1 = QLineEdit(placeholderText = "0")
        self.number_2 = QLineEdit(placeholderText = "0")

        # TODO: add a push button to greet user
        addition_button = QPushButton("+")
        addition_button.clicked.connect(self.get_input_addition)
        subtraction_button = QPushButton("-")
        subtraction_button.clicked.connect(self.get_input_subtraction)

        # TODO: add a label to greet user
        self.instructions = "Enter two numbers, then click one of the buttons."
        self.output_label = QLabel(self.instructions)
        self.output_label.setWordWrap(True)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.number_1)
        layout.addWidget(self.number_2)
        layout.addWidget(addition_button)
        layout.addWidget(subtraction_button)
        layout.addWidget(self.output_label)
        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)



    def get_input_addition(self):
        output = ""
        try:
            number_1 = float(self.number_1.text())
            number_2 = float(self.number_2.text())
            answer = number_1 + number_2
            output = f"Your answer is {answer}."
            self.output_label.setText(output)
        except ValueError:
            output = "Warning: Please enter valid numbers in both slots."
            self.output_label.setText(output)

    def get_input_subtraction(self):
        output = ""
        try:
            number_1 = float(self.number_1.text())
            number_2 = float(self.number_2.text())
            answer = number_1 - number_2
            output = f"Your answer is {answer}."
            self.output_label.setText(output)
        except ValueError:
            output = "Warning: Please enter valid numbers in both slots."
            self.output_label.setText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
