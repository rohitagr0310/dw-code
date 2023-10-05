from PyQt5.QtWidgets import QPlainTextEdit, QFrame, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from .syntax_highlighter import SyntaxHighlighter
from .line_numbers import LineNumberArea
from PyQt5.QtGui import QPainter

class CodeEditor(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Create a layout for the code editor and line numbers
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create the code editor widget
        self.code_editor = QPlainTextEdit(self)
        self.code_editor.setLineWrapMode(QPlainTextEdit.NoWrap)

        # Create a syntax highlighter for the code editor
        self.highlighter = SyntaxHighlighter(self.code_editor.document())

        # Add code editor to the layout
        layout.addWidget(self.code_editor)

        # Create the line numbers widget
        self.line_numbers = LineNumberArea(self.code_editor)

        # Set the code editor's viewport margin to the width of the line numbers
        self.code_editor.setViewportMargins(self.line_numbers.width(), 0, 0, 0)

        # Connect the code editor's scrollbar to update the line numbers
        self.code_editor.verticalScrollBar().valueChanged.connect(self.update_line_numbers)

        # Initialize line numbers
        self.init_line_numbers()

        self.setLayout(layout)

    def init_line_numbers(self):
        self.code_editor.verticalScrollBar().valueChanged.connect(self.line_numbers.update)

    def line_number_width(self):
        digits = 1
        max_value = max(1, self.code_editor.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 3 + self.code_editor.fontMetrics().width('9') * digits
        return space

    def line_number_paint(self, event):
        painter = QPainter(self.line_numbers)
        painter.fillRect(event.rect(), Qt.lightGray)
        block = self.code_editor.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.code_editor.blockBoundingGeometry(block).translated(self.code_editor.contentOffset()).top()
        bottom = top + self.code_editor.blockBoundingRect(block).height()

        # Iterate over visible blocks and paint line numbers
        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.line_numbers.width(), self.code_editor.fontMetrics().height(), Qt.AlignRight, number)
            block = block.next()
            top = bottom
            bottom = top + self.code_editor.blockBoundingRect(block).height()
            block_number += 1
        painter.end()

    def update_line_numbers(self):
        self.line_numbers.update()
