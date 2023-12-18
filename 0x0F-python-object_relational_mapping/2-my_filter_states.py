#!/usr/bin/python3
"""function that takes in an arg and shows all val in the states
table of hbtn_0e_0_usa where name matches the arg"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT id,name FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    lines = cur.fetchall()
    for line in lines:
        if line[1] == argv[4]:
            print(line)
    cur.close()
    db.close()

