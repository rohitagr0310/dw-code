from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QAction

def create_menu_bar(root):
    menubar = root.menuBar()

    # Create a "File" menu
    file_menu = menubar.addMenu("File")

    # Add menu items to the "File" menu
    new_action = QAction("New", root)
    open_action = QAction("Open", root)
    save_action = QAction("Save", root)
    save_as_action = QAction("Save As", root)
    exit_action = QAction("Exit", root)

    file_menu.addAction(new_action)
    file_menu.addAction(open_action)
    file_menu.addAction(save_action)
    file_menu.addAction(save_as_action)
    file_menu.addSeparator()  # Add a separator line
    file_menu.addAction(exit_action)

    # Connect menu items to functions or actions as needed
    # For example, exit_action.triggered.connect(on_exit)
