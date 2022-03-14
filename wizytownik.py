import email
from tkinter import END
from faker import Faker
fake = Faker("pl_PL")






class BaseContact:
    def __init__(self, tel_priv, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.tel_priv = tel_priv

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.tel_priv}"


    def contact(self):
        return f"Wybieram numer domowy: {self.tel_priv} i dzwonię do {self.first_name} {self.last_name} "
    
    def create_contact(self):
        print("Dodaj pozycje do wizytownika.")
        self.first_name=input("Podaj imię: ")
        self.last_name=input("Podaj nazwisko: ")
        self.tel_priv=int(input("Podaj nr telefonu domowego: "))
        
    
        

  

@property
def contact(self):
    return self.tel_priv
    
class BusinessContact(BaseContact):
    
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.occupation} {self.company} {self.tel_work}"


    def work_contact(self):
        return f"Wybieram numer firmowy: {self.tel_work} i dzwonię do {self.first_name} {self.last_name} "
    

    def work_contact(self):
        return f"Telefon firmowy to: {self.tel_work} "  

    
    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")


osoba = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),company=fake.company(), occupation=fake.job(), tel_priv=fake.phone_number(), tel_work=fake.phone_number()) 


@property
def work_contact(self):
    return self.work_phone




print(osoba)
print(osoba.contact())
print(osoba.work_contact())
print(osoba.label_length)
print(osoba.create_contact())




