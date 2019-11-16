from PyQt5 import QtWidgets
from ui.Sketch import MainWindow

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()   
    sys.exit(app.exec_())
    sys.excepthook = except_hook
