import os
import sqlite3

def show_players(cursor):
    cursor.execute("select player_name from player")
    return cursor.fetchall()

def main():
    base_dir=os.path.dirname(os.path.abspath(__file__))
    db_path=os.path.join(base_dir,"sports.db")
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()

    players=show_players(cursor)
    print("All players")
    for player in players:
        print(f"{player[0]}")
    
    conn.close()

if(__name__=="__main__"):
    main()

