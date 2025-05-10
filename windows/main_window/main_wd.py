import re

from PySide6.QtWidgets import QPushButton, QApplication


class Calculatrice:
    def __init__(self, ui):
        self.ui = ui
        self._operators = ["+", "-", "x", "÷", "."]

    def setupLogic(self) -> None:
        self.ui.btn_close.clicked.connect(QApplication.quit)
        self.ui.btn_love.clicked.connect(self.on_button_clear)
        self.ui.btn_del.clicked.connect(self.on_button_delete)
        self.ui.btn_equal.clicked.connect(self.calculate)

        for row in [self.ui.secondRow, self.ui.thirdRow, self.ui.fourthRow, self.ui.fifthRow]:
            for i in range(row.count()):
                widget = row.itemAt(i).widget()
                if isinstance(widget, QPushButton) and widget != self.ui.btn_equal:
                    val = widget.property("value")
                    widget.clicked.connect(lambda checked, v=val: self.on_buttons_clicked(v))  # type: ignore[attr-define]

    def on_button_clear(self):
        self.ui.display.line_edit.clear()

    def on_button_delete(self):
        text = self.ui.display.text()
        if text:
            self.ui.display.line_edit.setText(text[:-1])

    def on_buttons_clicked(self, value):
        current = self.ui.display.text()
        operators = self._operators[:-1]

        # don't allow an operator at the start and prevent multiple operators in a row
        if value in operators:
            if not current:
                return
            if current[-1] in operators:
                current = current[:-1]

        self.ui.display.setText(current + value)

    def calculate(self):
        """Calculate the result of the operation string left to right."""
        operation = self.ui.display.text()
        if not operation:
            return

        if operation[-1] in self._operators:
            return

        try:
            # Replace calculator symbols with Python operators
            operation = operation.replace("x", "*").replace("÷", "/")

            # Split into numbers and operators
            tokens = re.findall(r'[\d.]+|[+\-*/]', operation)
            if not tokens:
                raise ValueError("Invalid expression")

            # Initialize result with first number
            result = float(tokens[0])

            # Process left to right
            for i in range(1, len(tokens), 2):
                operator = tokens[i]
                next_num = float(tokens[i + 1])

                if operator == "+":
                    result += next_num
                elif operator == "-":
                    result -= next_num
                elif operator == "*":
                    result *= next_num
                elif operator == "/":
                    if next_num == 0:
                        raise ZeroDivisionError
                    result /= next_num

            if result.is_integer():
                result = int(result)
                self.ui.display.setText(str(result))
            else:
                formatted_result = f"{result:.6f}".rstrip("0").rstrip(".")
                self.ui.display.setText(formatted_result)

        except (ValueError, ZeroDivisionError, IndexError):
            self.ui.display.setText("Error")
