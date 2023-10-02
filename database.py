import sqlite3 as sql
import os

db = "training'sDictionary.db"
if os.path.exists(db) != True:
    f = open(db, "x")
    f.close()
    conn = sql.connect(db)
    #conn.execute("""CREATE TABLE `excercises` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT)""")
    conn.execute("""CREATE TABLE `proportions` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `date` DATE, `height` INT, `knee` INT, `elbow` INT, `crimson` INT, `shoulder` INT, `chest` INT, `arm` INT, `calf` INT, `thigh` INT, `forearm` INT, `neck` INT)""")
    conn.execute("""CREATE TABLE `propCol` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `name` TEXT)""")
    conn.execute("""Insert Into `propCol` (`name`) values ('date'), ('height'), ('knee'), ('elbow'), ('crimson'), ('shoulde'), ('ches'), ('ar'), ('cal'), ('thig'), ('forear'), ('nec')""")
    conn.commit()
else:
    conn = sql.connect(db)

conn.close()