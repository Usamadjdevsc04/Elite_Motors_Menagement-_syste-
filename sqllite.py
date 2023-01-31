# import sqlite3
#
# conn = sqlite3.connect("sqlite3.db")
# ins = '''insert into student(st_name,st_class,st_email) VALUES ('RAvi','10th',"ravi@gmail.com")
#
#  '''
# # conn.execute('''
# #        create table student(
# #                 st_id int AUTO_INCREMENT PRIMARY KEY,
# #                 st_name VARCHAR(50),
# #                 st_class VARCHAR(10),
# #                 st_email VARCHAR(30)
# #
# #
# #
# #
# #        )
# # ''')
# conn.execute(ins)
# conn.commit()
# conn.close()
import sqlite3

#
# conn = sqlite3.connect("sqlite3.db")
# data = conn.execute("SELECT * FROM student limit 2,2")
# print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
# for n in data:
#     print(n[0], n[1], n[2], n[3])
# import sqlite3
#
# conn = sqlite3.connect("inventory.db")
# cur = conn.cursor()
# sql = '''
# Create table inventory(
#            primary key(NAME)
#            MAKE TEXT,
#            MODEL INTEGER,
#            VARIANT TEXT,
#            MILEAGE INTEGER,
#            COLOUR TEXT,
#            ENGINE TYPE TEXT,
#            CC INTEGER,
#            RATING INTEGER,
#            REGISTRATION TEXT,
#            REGISTRATION_CITY TEXT,
#            CHASSIS_NO TEXT,
#            PRICE INTEGER,
#            PURCHASING DATE TEXT,
#            SELLING DATE TEXT,
#            PURCHASING PRICE INTEGER,
#            SELLING PRICE INTEGER,
#            PROFIT_LOSS INTEGER)
# '''
# cur.execute(sql)
# print("Database has been created")
#
# conn.commit()
# conn.close()

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
with open("inventory.csv", 'r') as file:
    records = 0
    for row in file:
        cursor.execute("INSERT INTO inventory(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        records += 1
    connection.close()
    print('\n{} Records Transfer Completed'.format(records))
