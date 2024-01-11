import sys
from PyQt5.uic import loadUi
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QTableWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class CoffeeInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi('main.ui', self)

        self.comboBox.currentIndexChanged.connect(self.had)

        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        cursor.execute('SELECT Name FROM coffee')
        data = cursor.fetchall()
        for value in data:
            self.comboBox.addItem(str(value[0]))

        model = QStandardItemModel(len(data), 7)
        model.setHorizontalHeaderLabels(["ID", "Name", "Roasting", "View", "Description", "Price", "Volume"])
        selected_item = self.comboBox.currentText()
        v = cursor.execute("SELECT * FROM coffee WHERE Name = ?", (selected_item,)).fetchall()
        for row in range(len(v)):
            for column in range(7):
                item = QStandardItem(f"{v[row][column]}")
                model.setItem(row, column, item)
        self.tableView.setModel(model)
        connection.close()

    def had(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        cursor.execute('SELECT Name FROM coffee')
        data = cursor.fetchall()

        model = QStandardItemModel(len(data), 7)
        model.setHorizontalHeaderLabels(["ID", "Name", "Roasting", "View", "Description", "Price", "Volume"])
        selected_item = self.comboBox.currentText()
        v = cursor.execute("SELECT * FROM coffee WHERE Name = ?", (selected_item,)).fetchall()
        for row in range(len(v)):
            for column in range(7):
                item = QStandardItem(f"{v[row][column]}")
                model.setItem(row, column, item)
        self.tableView.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_app = CoffeeInfoApp()
    coffee_app.show()
    sys.exit(app.exec_())
