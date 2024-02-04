

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import secrets 

class PassGenerator(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.puck.clicked.connect(self.generator_password)


    def generator_password(self):
        password = secrets.token_hex(8)
        self.ui.Pasrot.setText(password)
        with open("Me pass.txt", "a") as file:
            file.write('\n'+password)

app = QApplication([])
ex = PassGenerator()
ex.show()
app.exec_()
