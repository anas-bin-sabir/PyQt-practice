import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me", self)
        self.label = QLabel("Hello", self)
        self.setGeometry(700,300,500,500)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 120)
        self.button.setStyleSheet("font-size:30px;")
        
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size:30px;")
        
        self.button.clicked.connect(self.on_click)
        
    def on_click(self):
        print("Button Clicked")
        self.label.setText("GoodBye")
        self.button.setText("Clicked")
        self.button.setDisabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())