from PyQt5.QtWidgets import QMessageBox


class MessageInformation(QMessageBox):
    def __init__(self, text):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setText(text)
        self.setWindowTitle("Information")
        self.exec_()
