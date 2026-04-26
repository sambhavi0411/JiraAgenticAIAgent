import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox

# connect backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.agent import run_agent


class JiraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jira Agent")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        # Label
        self.label = QLabel("Enter your request:")
        layout.addWidget(self.label)

        # 🔥 Input box (BIG + guaranteed visible)
        self.textbox = QTextEdit()
        layout.addWidget(self.textbox)

        # Button
        self.button = QPushButton("Create Ticket")
        self.button.clicked.connect(self.create_ticket)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def create_ticket(self):
        user_input = self.textbox.toPlainText()

        if not user_input.strip():
            QMessageBox.warning(self, "Warning", "Please enter a request")
            return

        issue_key = run_agent(user_input)

        if "Error" in issue_key:
            QMessageBox.critical(self, "Error", issue_key)
        else:
            QMessageBox.information(self, "Success", f"Ticket Created: {issue_key}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JiraApp()
    window.show()
    sys.exit(app.exec_())