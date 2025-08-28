"""  
Gör ett program som frågar användaren efter namn och ålder.
Programmet ska sedan skriva ut enligt nedan.
Räkna med att man går i pension vid 67 års ålder.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej och välkommen till mitt program (Hampus). Du har (39) år kvar till pension.
"""


age = int(input("Enter your age unc"))
print(f"You have {67 - age} years left until retirement unc")
