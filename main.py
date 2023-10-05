import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from components.code_editor.code_editor import CodeEditor
from components.menu_bar.menu_bar import create_menu_bar

def create_base_window():
    app = QApplication(sys.argv)
    root = QMainWindow()
    root.setWindowTitle("My Python IDE")
    root.setGeometry(100, 100, 800, 600)  # Set the window size

    # Create the custom code editor component
    code_editor = CodeEditor(root)
    root.setCentralWidget(code_editor)

    # Create the menu bar
    create_menu_bar(root)

    return app, root

if __name__ == "__main__":
    app, main_window = create_base_window()
    main_window.show()
    sys.exit(app.exec_())
