import CatDog
from temp import predict
import sys
from keras.models import load_model
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window = CatDog.Ui_MainWindow()
        self.main_window.setupUi(self)

        self.image = self.main_window.Image
        self.button = self.main_window.predict
        self.getImage = self.main_window.getImage
        self.Class = self.main_window.Class

        self.button.clicked.connect(self.Predict)

    def Predict(self):
        try:
            img = self.getImage.toPlainText()
            prediction = str(predict(img)[0])
            print(type(prediction))
            print(prediction)
            if int(prediction) == 1:
                self.Class.setText("Dog")
            elif int(prediction) == 0:
                self.Class.setText("Cat")
            pixmap = QPixmap(img)
            self.image.setPixmap(pixmap)

        except Exception as err:
            print(str(err))
            QMessageBox.about(self, "Invalid Image", "Enter valid image path")
        


if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    ex = Main()
    ex.show()
    sys.exit(app.exec_())
