from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPainter

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.code_editor = editor

    def sizeHint(self):
        return QSize(self.line_number_width(), 0)

    def line_number_width(self):
        digits = len(str(self.code_editor.blockCount()))
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(event.rect(), Qt.lightGray)
        block = self.code_editor.firstVisibleBlock()
        block_number = block.blockNumber() + 1
        top = self.code_editor.blockBoundingGeometry(block).translated(self.code_editor.contentOffset()).top()
        bottom = top + self.code_editor.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                text = str(block_number)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.width(), self.fontMetrics().height(), Qt.AlignRight | Qt.AlignVCenter, text)
            block = block.next()
            top = bottom
            bottom = top + self.code_editor.blockBoundingRect(block).height()
            block_number += 1
