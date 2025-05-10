from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QVBoxLayout, QMainWindow, QHBoxLayout

from widgets.button import ImageButton
from widgets.display import ImageWidget
from widgets.label import Label

from assets import icons  # noqa


class CalculatriceUI:
    def __init__(self, main_window: QMainWindow):
        self.main_window = main_window

        self.window_icon_path = ":/assets/app_icon.ico"
        self.window_bg_path = ":/assets/svg/bg.svg"
        self.scale_size = QSize(280, 370)
        self.renderer = None
        self.drag_pos = None

        self.btn_close = None
        self.display = None
        self.firstRow = None
        self.secondRow = None
        self.thirdRow = None
        self.fourthRow = None
        self.fifthRow = None

        self.btn_love = None
        self.btn_clear = None
        self.btn_del = None
        self.btn_equal = None

    def setupUi(self):
        self.main_window.setWindowTitle("La Calculatrice")
        self.main_window.setWindowIcon(QIcon(self.window_icon_path))
        self.main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.main_window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.renderer = QSvgRenderer(self.window_bg_path)
        self.main_window.setFixedSize(self.scale_size)

        # MAIN LAYOUT
        central_widget = QWidget(self.main_window)
        self.main_window.setCentralWidget(central_widget)
        mainLayout = QVBoxLayout(central_widget)
        mainLayout.setSpacing(10)
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # ////////////////////////////////////////////////////////////////////////////////////////////////////

        # HINT LAYOUT
        hintLayout = QVBoxLayout()
        hintLayout.setSpacing(0)
        labelLayout = QHBoxLayout()
        app_label = Label(" La Calculatrice")
        self.btn_close = ImageButton(":/assets/svg/btn_close.svg", size=(35, 35))
        self.btn_close.setCursor(Qt.CursorShape.PointingHandCursor)
        labelLayout.addWidget(app_label)
        labelLayout.addStretch()
        labelLayout.addWidget(self.btn_close)
        self.display = ImageWidget(":/assets/svg/display_bar.svg", (250, 50))
        hintLayout.addLayout(labelLayout)
        hintLayout.addWidget(self.display)

        # BUTTON CONTAINER
        btnContainer = QWidget()
        btnLayout = QVBoxLayout(btnContainer)
        btnLayout.setContentsMargins(0, 0, 0, 0)
        btnLayout.setSpacing(0)

        self.firstRow = QHBoxLayout()
        self.firstRow.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.firstRow.setContentsMargins(5, 0, 0, 0)
        self.btn_love = ImageButton(":/assets/svg/btn_love.svg")
        self.btn_del = ImageButton(":/assets/svg/btn_del.svg")
        self.firstRow.addWidget(self.btn_love)
        self.firstRow.addSpacing(120)
        self.firstRow.addWidget(self.btn_del)

        self.secondRow = QHBoxLayout()
        btn_seven = ImageButton(":/assets/svg/btn_7.svg", "7")
        btn_eight = ImageButton(":/assets/svg/btn_8.svg", "8")
        btn_nine = ImageButton(":/assets/svg/btn_9.svg", "9")
        btn_divide = ImageButton(":/assets/svg/btn_div.svg", "÷")
        self.secondRow.addWidget(btn_seven)
        self.secondRow.addWidget(btn_eight)
        self.secondRow.addWidget(btn_nine)
        self.secondRow.addWidget(btn_divide)

        self.thirdRow = QHBoxLayout()
        btn_four = ImageButton(":/assets/svg/btn_4.svg", "4")
        btn_five = ImageButton(":/assets/svg/btn_5.svg", "5")
        btn_six = ImageButton(":/assets/svg/btn_6.svg", "6")
        btn_times = ImageButton(":/assets/svg/btn_multi.svg", "x")
        self.thirdRow.addWidget(btn_four)
        self.thirdRow.addWidget(btn_five)
        self.thirdRow.addWidget(btn_six)
        self.thirdRow.addWidget(btn_times)

        self.fourthRow = QHBoxLayout()
        btn_one = ImageButton(":/assets/svg/btn_1.svg", "1")
        btn_two = ImageButton(":/assets/svg/btn_2.svg", "2")
        btn_three = ImageButton(":/assets/svg/btn_3.svg", "3")
        btn_sub = ImageButton(":/assets/svg/btn_sub.svg", "-")
        self.fourthRow.addWidget(btn_one)
        self.fourthRow.addWidget(btn_two)
        self.fourthRow.addWidget(btn_three)
        self.fourthRow.addWidget(btn_sub)

        self.fifthRow = QHBoxLayout()
        btn_zero = ImageButton(":/assets/svg/btn_0.svg", "0")
        btn_point = ImageButton(":/assets/svg/btn_float.svg", ".")
        btn_add = ImageButton(":/assets/svg/btn_add.svg", "+")
        self.btn_equal = ImageButton(":/assets/svg/btn_equal.svg")
        self.fifthRow.addWidget(btn_zero)
        self.fifthRow.addWidget(btn_point)
        self.fifthRow.addWidget(btn_add)
        self.fifthRow.addWidget(self.btn_equal)

        btnLayout.addLayout(self.firstRow)
        btnLayout.addLayout(self.secondRow)
        btnLayout.addLayout(self.thirdRow)
        btnLayout.addLayout(self.fourthRow)
        btnLayout.addLayout(self.fifthRow)

        # ---------------------------------------

        mainLayout.addLayout(hintLayout)
        mainLayout.addWidget(btnContainer)
