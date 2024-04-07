from familyDB import FamilyDB
from database import Database

db = Database("bolt://44.195.93.13:7687", "neo4j", "diagnoses-silks-characteristic")
family_db = FamilyDB(db)

opcao = int(input("""[1] - Quem são os pais de Lucas?
[2] - Quem é irmão da Luana?
[3] - Luana namora com quem desde quando?
OPCÃO: """))
if opcao == 1:
    print("Pais de Lucas")
    print(family_db.get_parents("Lucas"))
elif opcao == 2:
    print("Irmão da Luana:")
    print(family_db.get_siblings("Luana"))
elif opcao == 3:
    print("Namorado de Luana e data de início do relacionamento:")
    print(family_db.get_relationship("Luana"))

db.close()