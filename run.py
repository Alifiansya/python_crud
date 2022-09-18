import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("user_data.db")
        self.cur = self.con.cursor() 
    def show_all(self):
        return self.cur.execute("SELECT * FROM mahasiswa").fetchall()
    def delete_row(self, pr_key):
        if(self.cur.execute("SELECT * FROM mahasiswa WHERE nim = ?", pr_key) == None):
            return "Data tidak ditemukan!"
        self.cur.execute("DELETE FROM mahasiswa WHERE nim = ?", pr_key)
        return f"Data {pr_key} telah dihapus!"
    def add_row(self, data_row : list):
        try:
            self.con.execute("INSERT INTO mahasiswa VALUES(?, ?, ?, ?)", data_row)
            return "Data berhasil dimasukan."
        except:
            return "Data yang dimasukan tidak benar."
        
    