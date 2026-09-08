from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication
from frontend.ventanas import VentanaLogin


if __name__ == "__main__":
    app = QApplication([])
    login = VentanaLogin()

    login.show()
    app.exec()
    