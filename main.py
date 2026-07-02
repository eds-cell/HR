import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from database import create_database
from ui.main_window import MainWindow

app = QApplication(sys.argv)

style_file = Path("styles/style.qss")

if style_file.exists():
    with open(style_file, "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

create_database( )

window = MainWindow()
window.show()

sys.exit(app.exec())