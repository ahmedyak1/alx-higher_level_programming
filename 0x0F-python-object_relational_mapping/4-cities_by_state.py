#!/usr/bin/python3
"""functionn that shows all cities from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, states.name FROM cities as c\
    JOIN states as s ON c.state_id = s.id ORDER BY c.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

