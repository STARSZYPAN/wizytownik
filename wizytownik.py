from faker import Faker

faker = Faker('pl_PL')

class Osoba:
   def __init__(name,job, mail):
       self.name = faker.name
       self.stanowisko =faker.job
       self.mail = mail





for _ in range(5): 
    print (f"imię i nazwisko:{faker.name()} Stanowisko:{faker.job()} Adress E-mail:")
    