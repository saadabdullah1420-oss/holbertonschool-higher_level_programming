#!/usr/bin/python3
"""List states matching the supplied name in ascending ID order."""

import sys
import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
