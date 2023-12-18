#!/usr/bin/python3
"""function takes in the name of a state as an arg and shows
all cities of that state, using the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities as c \
    JOIN states as s ON c.state_id = s.id WHERE s.name LIKE %s \
    ORDER BY c.id", (argv[4],))
    rows = cur.fetchall()
    print(", ".join(c[0] for c in rows))
    cur.close()
    db.close()

