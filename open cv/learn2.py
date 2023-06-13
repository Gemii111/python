from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
window.setWindowTitle("Login Page")
username_label = QLabel("Username:")
username_input = QLineEdit()
password_label = QLabel("Password:")
password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.Password)
login_button = QPushButton("Login")
layout = QVBoxLayout()
layout.addWidget(username_label)
layout.addWidget(username_input)
layout.addWidget(password_label)
layout.addWidget(password_input)
layout.addWidget(login_button)
window.setLayout(layout)
def handle_login():
    username = username_input.text()
    password = password_input.text()
    if username == "admin" and password == "password":
        print("Login successful")
    else:
        print("Login failed")
login_button.clicked.connect(handle_login)
window.show()
app.exec_()
