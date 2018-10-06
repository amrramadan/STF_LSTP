
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
from django.db import connection
cursor = connection.cursor()
cursor.execute("INSERT INTO Players (playerID, SID, firstName, lastName, email, phoneNumber, birthDate) VALUES (5, 5, 'karker', 'tuna', 'email', 123, '2018-11-07')")
connection.commit