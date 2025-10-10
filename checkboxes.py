import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hehe")
        self.setGeometry(700,300,500,500)
        self.checkBox = QCheckBox("Do you like food?", self)
        self.initUI()
        
    def initUI(self):
        self.checkBox.setGeometry(10, 0, 500, 100)
        self.checkBox.setStyleSheet("font-size:30px;")
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checkBox_changed)
        
    def checkBox_changed(self, state):
        print("You like food") if state == Qt.Checked else print("You don't like food")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    