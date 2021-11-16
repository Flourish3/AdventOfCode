import sqlite3
import re

try:
    db = sqlite3.connect('/home/johan/.config/google-chrome/Default/Cookies')

    cursor = db.cursor()

    cursor.execute('''SELECT encrypted_value FROM cookies WHERE host_key=".adventofcode.com"''')

    for row in cursor:
        print(row)

except Exception as e:
    db.rollback()

finally:
    db.close()