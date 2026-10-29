import sys
from PyQt5 import QtWidgets


class RobloxLauncherWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roblox Linux Compatibility Launcher")
        self.resize(640, 400)

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)

        layout = QtWidgets.QVBoxLayout(central)

        self.title = QtWidgets.QLabel("Roblox on Raspberry Pi 5")
        self.title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(self.title)

        self.status = QtWidgets.QLabel("Ready")
        layout.addWidget(self.status)

        self.launch_button = QtWidgets.QPushButton("Launch Roblox")
        layout.addWidget(self.launch_button)

        self.settings_button = QtWidgets.QPushButton("Open Settings")
        layout.addWidget(self.settings_button)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RobloxLauncherWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
