#!/usr/bin/python3
"""function lists all states with a name startiing with N from
the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT id,name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    lines = cur.fetchall()
    for line in lines:
        if line[1][0] == 'N':
            print(line)
    cur.close()
    db.close()

