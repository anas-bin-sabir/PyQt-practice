import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First app")
        self.setGeometry(0,0,700,300)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:blue;")
        label3.setStyleSheet("background-color:green;")
        label4.setStyleSheet("background-color:pink;")
        label5.setStyleSheet("background-color:brown;")
        
        vbox = QGridLayout()
        
        vbox.addWidget(label1,0,0)
        vbox.addWidget(label2,0,1)
        vbox.addWidget(label3,1,0)
        vbox.addWidget(label4,1,1)
        vbox.addWidget(label5,2,0)

        central_widget.setLayout(vbox)

        # label = QLabel(self)
        # label.setGeometry(0,0,250,250)
        
        # pixmap = QPixmap("image.png")     
        # label.setPixmap(pixmap)
        
        # label.setScaledContents(True)
        
        # label.setGeometry(
        #     (self.width() - label.width()) // 2, 
        #     (self.height() - label.height()) // 2, 
        #     label.width(), 
        #     label.height()
        # )
        
        # self.setWindowIcon(QIcon("image.png"))
        
        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 30))
        # label.setGeometry(0,0,500,100)
        # label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        
if __name__ == "__main__":
    main()