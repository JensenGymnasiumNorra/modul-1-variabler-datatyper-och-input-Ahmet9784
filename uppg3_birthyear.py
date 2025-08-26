"""  
Skapa en variabel för ditt födelseår
Programmet ska sedan skriva ut din ålder

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Du är (16) år gammal.

"""
import datetime

birth_year = 2008
birth_month = 2
birth_day = 21

today = datetime.date(2025, 8, 26)

birth_date= datetime.date(birth_year, birth_month, birth_day)

age = today.year - birth_date.year

print(f"You are {age} years old.")
