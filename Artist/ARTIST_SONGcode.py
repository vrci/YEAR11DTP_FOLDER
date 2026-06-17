import os
import sqlite3  #imports sqlite into the vs code


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "ARTIST_SONG.db")


def print_all_artists():  #defines the print all artist functions
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()  #connects it from the database
    sql = "SELECT First_Name, Last_name FROM ARTISTS;"  #gets the right things
    cursor.execute(sql)
    results = cursor.fetchall()
    print('First_Name    Last_name')
    for name in results:
        print(f"{name[0]:<11}{name[1]}")  #gap so it looks aesthetically pleasing


def print_all_bands():  #same command but defines the bands
    print("All bands: ")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "SELECT First_Name, Last_name FROM ARTISTS WHERE Type = 'Band';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('First_Name    Last_name')
    for name in results:
        print(f"{name[0]:<11} {name[1]}")


def print_all_songs():  #defines all songs and prints the song name and plays descending
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "SELECT Song_Name, Song_plays FROM Song ORDER BY Song_plays DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Song_name    Song_plays')
    print(results)
    for name in results:
        print(f"{name[0]:<31} {name[1]}")


def print_all_singers():  #defines all the singers not inc bands
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "SELECT First_Name, Last_name FROM ARTISTS WHERE Type == 'Singer';"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Song_name    Song_plays')
    for name in results:
        print(f"{name[0]:<11} {name[1]}")


def print_all_albums():  #defines all album dates and album names
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "SELECT Album_Name, Release_Date FROM ALBUMS;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print('Album_Name    Release_Date')
    for name in results:
       print(f"{name[0]:<31}{name[1]}")


print_all_artists()
while True:  #loop so it can break later on
    print('Options: Songs, Individuals, Bands, Albums')  #options
    question1 = input('What else would you like to know? (Enter "Cancel" to exit) ').title() #takes any for of answer
    try:
        if question1 == "Songs":
            print_all_songs()
        elif question1 == "Individuals":
            print_all_singers()
        elif question1 == "Bands":
            print_all_bands()
        elif question1 == "Albums":
            print_all_albums()
        elif question1 == "Cancel":
            break
    except ValueError:  #if valuerror, it reasks

        print('Unkown input, please try again.')

print("Now you know about Singers, songs and albums. Thanks for using this code.")
