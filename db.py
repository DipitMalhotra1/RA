#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="chom")        # name of the data base


def test(sql):

    cursor = db.cursor()
    # sql ="""INSERT INTO ref(Reference)
    #      VALUES ('Mac')"""
    try:

        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()
    db.close()

test("""INSERT INTO ref(Reference)
            VALUES ('Mac123')""")
