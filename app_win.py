import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel


# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

# Create the application
app = QApplication(sys.argv)

# Try to open the connection and handle possible errors
if not con.open():
    QMessageBox.critical(None,
                         "App Name - Error!",
                         f"Database Error: {con.lastError().databaseText()}")
    sys.exit(1)

# Create the application's window
win = QLabel("Connection Successfully Opened!")
win.setWindowTitle("App Name")
win.resize(200, 100)
win.show()
sys.exit(app.exec_())
