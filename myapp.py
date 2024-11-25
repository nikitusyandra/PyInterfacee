from PyQt5.QtWidgets import (
    QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt, QTimer  



class FactoryGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.coins = 0  
        self.worker_count = 0 
        self.worker_cost = 50  
        self.coins_per_worker = 1 

        self.setWindowTitle("Фабрика монет")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.coins_label = QLabel(f"Монеты: {self.coins}", self)
        self.coins_label.setAlignment(Qt.AlignCenter)
        self.coins_label.setStyleSheet("font-size: 20px;")
        self.layout.addWidget(self.coins_label)

        self.click_button = QPushButton("Произвести монеты", self)
        self.click_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.click_button.clicked.connect(self.produce_coin)
        self.layout.addWidget(self.click_button)

        self.worker_label = QLabel(f"Рабочие: {self.worker_count} (производят {self.worker_count * self.coins_per_worker} монет/сек)", self)
        self.worker_label.setAlignment(Qt.AlignCenter)
        self.worker_label.setStyleSheet("font-size: 16px;")
        self.layout.addWidget(self.worker_label)

        self.hire_button = QPushButton(f"Нанять рабочего - {self.worker_cost} монет", self)
        self.hire_button.setStyleSheet("font-size: 16px; padding: 8px;")
        self.hire_button.clicked.connect(self.hire_worker)
        self.layout.addWidget(self.hire_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_produce)
        self.timer.start(1000)  

    def produce_coin(self):
        """Производство монет при нажатии кнопки."""
        self.coins += 1
        self.update_ui()

    def hire_worker(self):
        """Найм рабочего."""
        if self.coins >= self.worker_cost:
            self.coins -= self.worker_cost
            self.worker_count += 1
            self.worker_cost = int(self.worker_cost * 1.5)  
            self.update_ui()

    def auto_produce(self):
        """Автоматическое производство монет рабочими."""
        self.coins += self.worker_count * self.coins_per_worker
        self.update_ui()

    def update_ui(self):
        """Обновление интерфейса."""
        self.coins_label.setText(f"Монеты: {self.coins}")
        self.worker_label.setText(f"Рабочие: {self.worker_count} (производят {self.worker_count * self.coins_per_worker} монет/сек)")
        self.hire_button.setText(f"Нанять рабочего - {self.worker_cost} монет")


if __name__ == "__main__":
    app = QApplication([])

    window = FactoryGame()
    window.show()

    app.exec()

