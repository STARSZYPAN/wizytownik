#import email
#from tkinter import END
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
        return f"Wybieram numer domowy: {self.tel_priv} i dzwonię do {self.first_name} {self.last_name}. "
    
    def show_contact(self):
        wybór_operacji=int(input("Jaki typ kontaktu chcesz wywołać? 1-prywatny,2-firmowy :  "))
        if wybór_operacji==1:  
            print(osoba.contact())
        if wybór_operacji==2:
            print(osoba)
            print(osoba.work_contact())

    @property
    def label_length(self):
            return len(f"{self.first_name} {self.last_name}")

    def add_contact(self):
        dodaj_kontakt=int(input("Czy czcesz dodać nowy kontakt do listy? TAK-1/NIE-2:  "))  
        if dodaj_kontakt==1:
            print(osoba_2)
            print()
            print("Dodano osobę do listy kontaktów!")
            
        if dodaj_kontakt==2:
            print("Dziękuję,kończę program!")


   

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
        return f"{self.first_name} {self.last_name},wybieram numer firmowy: {self.tel_work} i dzwonię do {self.first_name} {self.last_name}."
    
@property
def work_contact(self):
    return self.tel_work
    
    
  


osoba = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),company=fake.company(), occupation=fake.job(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
osoba_2=BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),company=fake.company(), occupation=fake.job(), tel_priv=fake.phone_number(), tel_work=fake.phone_number()) 
print(osoba.show_contact())
print()
print(osoba.label_length)
print(osoba.add_contact())







