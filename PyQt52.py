from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys #Programı çalıştırma esnasında parametre göndermek için'''
def window():
    app = QApplication(sys.argv)
    
    win = QMainWindow()
    win.setWindowTitle("Hello PyQt") #Pencereye başlık ekledik.
    win.setGeometry(100,100,600,400) #Pencere kordinatları yani uzunluk ve genişlik elirtmek için
    
    labelHello = QLabel(win)
    labelHello.setGeometry(50,50,200,200) #Labelin konumu ayarlandı
    labelHello.setText("Hello, this is first label")
    
    buttonTry = QPushButton("Click Here", win)
    buttonTry.setGeometry(10,30,200,100)

    win.show()
    sys.exit(app.exec())
window()


