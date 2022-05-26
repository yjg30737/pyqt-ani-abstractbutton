from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation
from PyQt5.QtWidgets import QAbstractButton


class AniAbstractButton(QAbstractButton):
    def __init__(self, size: int = 20):
        super().__init__()
        self.__initVal(size)
        self.__initUi()

    def __initVal(self, size):
        self.__size = size

    def __initUi(self):
        self.setFixedSize(self.__size, self.__size)
        self.__animation = QPropertyAnimation(self, b"border")
        self.__animation.valueChanged.connect(self.__initStyle)
        self.__animation.setStartValue(0)
        max_border_width = self.__size//6
        self.__animation.setEndValue(max_border_width)
        self.__animation.setDuration(50)
        self.__initStyle(self.__animation.startValue())

    def __initStyle(self, border_width):
        padding = abs(border_width-self.__animation.endValue())
        self.setStyleSheet(f'''
                            QAbstractButton 
                            {{
                            border: {border_width}px solid #AAAAAA;
                            background-color: #CCCCCC;
                            background-clip: content;
                            padding: {padding};
                            }}
                            '''
                            )

    def enterEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Forward)
        self.__animation.start()
        return super().enterEvent(e)

    def leaveEvent(self, e):
        self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()
        return super().leaveEvent(e)