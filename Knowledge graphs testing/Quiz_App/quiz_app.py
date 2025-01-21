import json
import sys
import os
import random
from PyQt6.QtGui import QFontDatabase, QFont, QPixmap, QIcon
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineWidgets import QWebEngineView
from quiz_manager import QuizManager

class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("INFO216 Quiz")
        self.setGeometry(100, 100, 800, 600)

        # Load custom font
        font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'ProductSans-Black.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f"Successfully loaded font: {font_family}")
            app_font = QFont(font_family)
            QApplication.setFont(app_font)
        else:
            print("Error loading custom font")

        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1F2334;
                color: white;
            }

            QLabel {
                color: #ffffff;
                font-size: 14px;
                padding: 10px;
            }
            QLabel#questionText {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                padding: 15px;
            }
            QRadioButton {
                color: #ffffff;
                font-size: 13px;
                padding: 8px;
                spacing: 8px;
            }
            QRadioButton::indicator {
                width: 15px;
                height: 15px;
            }
            QRadioButton::indicator:unchecked {
                background-color: #2b304a;
                border: 2px solid #3b4167;
                border-radius: 7px;
            }
            QRadioButton::indicator:checked {
                background-color: #4CAF50;
                border: 2px solid #4CAF50;
                border-radius: 7px;
            }
            QRadioButton:hover {
                background-color: #2b304a;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QProgressBar {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                text-align: center;
                color: white;
                background-color: #2b304a;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
            }
            QMessageBox {
                background-color: #1F2334;
                color: white;
            }
            QMessageBox QLabel {
                color: white;
            }
            QMessageBox QPushButton {
                min-width: 80px;
                min-height: 25px;
            }
        """)

        # Set custom dock icon for macOS and window icon for Windows
        icon_path = os.path.join(os.path.dirname(__file__), 'quiz.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            QApplication.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Icon file not found: {icon_path}")

        # Initialize quiz state
        self.quiz_manager = QuizManager()
        self.current_question = 0
        self.score = 0
        self.randomized = False

        self.setup_ui()
        self.load_questions('info216_2023exam_questions.json')

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        # Top layout for logo
        top_layout = QHBoxLayout()
        top_layout.addStretch()  # Pushes the logo to the right

        # Logo in the upper right corner
        logo_button = QPushButton()
        logo_button.setStyleSheet("border: none; background: none;")
        logo_pixmap = QPixmap(os.path.join(os.path.dirname(__file__), 'henvagdevborder.jpg'))
        scaled_pixmap = logo_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_icon = QIcon(scaled_pixmap)
        logo_button.setIcon(logo_icon)
        logo_button.setIconSize(scaled_pixmap.size())
        logo_button.clicked.connect(self.open_henvag_link)
        top_layout.addWidget(logo_button, alignment=Qt.AlignmentFlag.AlignRight)

        main_layout.addLayout(top_layout)

        # Title for the toggle
        toggle_title = QLabel("INFO216 Exam Year Switch")
        toggle_title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 5px; text-decoration: underline;")
        main_layout.addWidget(toggle_title)

        # File selection dropdown
        self.file_selector = QComboBox()
        self.file_selector.addItems(['2023', '2022'])
        self.file_selector.setFixedWidth(100)
        self.file_selector.setStyleSheet("font-size: 14px; padding: 5px;")
        self.file_selector.currentIndexChanged.connect(self.on_file_change)
        main_layout.addWidget(self.file_selector, alignment=Qt.AlignmentFlag.AlignLeft)

        # Toggle button for randomized question order
        randomize_layout = QHBoxLayout()
        self.randomize_button = QPushButton("Randomize Options")
        self.randomize_button.setCheckable(True)
        self.randomize_button.setFixedWidth(150)
        self.randomize_button.setStyleSheet("background-color: #2b304a; color: white; border: 1px solid #3b4167; padding: 5px;")
        self.randomize_button.toggled.connect(self.toggle_randomized_order)
        randomize_layout.addWidget(self.randomize_button)

        # Description label for the toggle button
        randomize_description = QLabel("(Randomizes the order of options)")
        randomize_description.setStyleSheet("color: white; padding: 5px;")
        randomize_layout.addWidget(randomize_description)

        main_layout.addLayout(randomize_layout)

        # Progress and score frame
        progress_frame = QFrame()
        progress_layout = QHBoxLayout()
        self.progress_label = QLabel()
        self.score_label = QLabel()
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.score_label)
        progress_frame.setLayout(progress_layout)
        main_layout.addWidget(progress_frame)

        # Progress bar
        self.progress_bar = QProgressBar()
        main_layout.addWidget(self.progress_bar)

        # Question
        self.question_label = QLabel()
        self.question_label.setObjectName("questionText")
        self.question_label.setWordWrap(True)
        main_layout.addWidget(self.question_label)

        # Options frame - now dynamic
        self.options_frame = QFrame()
        self.options_layout = QVBoxLayout()
        self.button_group = QButtonGroup()
        self.option_buttons = []
        self.options_frame.setLayout(self.options_layout)
        main_layout.addWidget(self.options_frame)

        # Submit button
        self.submit_button = QPushButton("Submit Answer")
        self.submit_button.clicked.connect(self.check_answer)
        main_layout.addWidget(self.submit_button)

        central_widget.setLayout(main_layout)

    def open_henvag_link(self):
        QDesktopServices.openUrl(QUrl("https://henvag.github.io"))

    def load_questions(self, filename):
        self.quiz_manager.load_questions(filename)
        self.questions = self.quiz_manager.questions

        if not self.questions:
            QMessageBox.critical(self, "Error", f"No questions found in {filename}")
            sys.exit(1)

        self.current_question = 0
        self.score = 0
        if self.randomized:
            for question in self.questions:
                question.shuffle_options()
        self.show_question()

    def on_file_change(self):
        file_map = {
            '2023': 'info216_2023exam_questions.json',
            '2022': 'info216_2024exam_questions.json'
        }
        selected_file = self.file_selector.currentText()
        self.load_questions(file_map[selected_file])

    def toggle_randomized_order(self, checked):
        self.randomized = checked
        if self.randomized:
            self.questions[self.current_question].shuffle_options()
        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.progress_label.setText(f"Question {self.current_question + 1}/{len(self.questions)}")
        self.score_label.setText(f"Score: {self.score}")
        self.progress_bar.setValue(int((self.current_question / len(self.questions)) * 100))

        self.question_label.setText(question.question)

        # Clear existing options
        for button in self.option_buttons:
            self.options_layout.removeWidget(button)
            button.deleteLater()
        self.option_buttons.clear()

        # Create new options
        for i, option in enumerate(question.options):
            radio = QRadioButton(option)
            radio.setStyleSheet("""
                QRadioButton::indicator { width: 15px; height: 15px; }
                QRadioButton { padding: 5px; color: white; }
            """)
            self.option_buttons.append(radio)
            self.button_group.addButton(radio, i)
            self.options_layout.addWidget(radio)

    class CustomMessageBox(QMessageBox):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Correct! ✓")
            self.setText("That's the right answer!")

            # List of Lottie animation URLs
            lottie_urls = [
                "https://cdn.lottielab.com/l/5Bpozs48ozT8HY.html",
                "https://cdn.lottielab.com/l/BNhnMu53BdL9dv.html",
                "https://cdn.lottielab.com/l/4sZkhwrR2h7VJZ.html"
            ]

            # Randomly select a Lottie animation URL
            selected_url = random.choice(lottie_urls)

            # Add QWebEngineView to display LottieLab animation
            web_view = QWebEngineView()
            web_view.setUrl(QUrl(selected_url))
            web_view.setFixedSize(200, 150)  # Set a smaller size for the web view
            self.layout().addWidget(web_view, self.layout().rowCount(), 0, 1, self.layout().columnCount())

            # Center the "Ok" button and make it smaller
            button_layout = QHBoxLayout()
            button_layout.addStretch()
            ok_button = self.addButton(QMessageBox.StandardButton.Ok)
            ok_button.setFixedSize(60, 30)  # Set a smaller size for the button
            button_layout.addWidget(ok_button)
            button_layout.addStretch()
            self.layout().addLayout(button_layout, self.layout().rowCount(), 0, 1, self.layout().columnCount())

    class CustomWrongMessageBox(QMessageBox):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Wrong ✗")
            self.setText("That's the wrong answer!")

            # List of Lottie animation URLs for wrong answers
            lottie_urls = [
                "https://cdn.lottielab.com/l/82XAVyJm6pzKzm.html",
                "https://cdn.lottielab.com/l/7Ehs8q7naRKWKt.html",
                "https://cdn.lottielab.com/l/9N8mcdFKp7FU3C.html"
            ]

            # Randomly select a Lottie animation URL
            selected_url = random.choice(lottie_urls)

            # Add QWebEngineView to display LottieLab animation
            web_view = QWebEngineView()
            web_view.setUrl(QUrl(selected_url))
            web_view.setFixedSize(200, 150)  # Set a smaller size for the web view
            self.layout().addWidget(web_view, self.layout().rowCount(), 0, 1, self.layout().columnCount())

            # Center the "Ok" button, make it smaller, and red
            button_layout = QHBoxLayout()
            button_layout.addStretch()
            ok_button = self.addButton(QMessageBox.StandardButton.Ok)
            ok_button.setFixedSize(60, 30)  # Set a smaller size for the button
            ok_button.setStyleSheet("background-color: red; color: white;")
            button_layout.addWidget(ok_button)
            button_layout.addStretch()
            self.layout().addLayout(button_layout, self.layout().rowCount(), 0, 1, self.layout().columnCount())

    def check_answer(self):
        selected = self.button_group.checkedId()
        if selected == -1:
            QMessageBox.warning(self, "Warning", "Please select an answer")
            return

        question = self.questions[self.current_question]
        if selected == question.correct:
            self.score += 0.5
            self.option_buttons[selected].setStyleSheet("QRadioButton { color: #90EE90; font-weight: bold; }")

            # Use the custom message box with LottieLab animation for correct answers
            msg_box = self.CustomMessageBox(self)
            msg_box.exec()
        else:
            self.option_buttons[selected].setStyleSheet("QRadioButton { color: #FF6B6B; }")
            self.option_buttons[question.correct].setStyleSheet("QRadioButton { color: #90EE90; font-weight: bold; }")

            # Use the custom message box with LottieLab animation for wrong answers
            msg_box = self.CustomWrongMessageBox(self)
            msg_box.exec()

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        percentage = (self.score / len(self.questions)) * 100
        QMessageBox.information(self, "Quiz Complete",
                              f"Final Score: {self.score}/{len(self.questions)} ({percentage:.1f}%)")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    icon_path = os.path.join(os.path.dirname(__file__), 'quiz.png')
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    quiz = QuizApp()
    quiz.show()
    sys.exit(app.exec())