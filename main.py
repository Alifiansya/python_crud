from tkinter import W
from login import login
from run import Database
if __name__ == "__main__":
    login()
    db = Database()
    print(db.show_all())
    print(db.delete_row('q'))
