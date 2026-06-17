import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "ARTIST_SONG.db")


def print_all_artists():
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        sql = "SELECT First_Name, Last_name FROM ARTIST;"
        cursor.excecute(sql)
        results = cursor.fetchall()
        print('Name: {First_Name}, {Last_name}')
        for name in results:
            print(f"{name[1]}{name[2]}")


print("Hello")     