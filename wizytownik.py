from faker import Faker
fake = Faker("pl_PL")




class BaseContact:
    def __init__(self, tel_priv, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.tel_priv = tel_priv

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.tel_priv}"

    def __repr__(self):
        return self.__str__()

    @property    
    def contact_phone(self):
        return self.tel_priv
    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")


    def contact(self):
        return f"Wybieram numer domowy: {self.contact_phone} i dzwonię do {self.first_name} {self.last_name}. "
    
   
print()

    
class BusinessContact(BaseContact):
    
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.occupation} {self.company} {self.tel_work}"

    @property    
    def contact_phone(self):
        return self.tel_work

    def contact(self):
        return f"{self.first_name} {self.last_name},wybieram numer firmowy: {self.tel_work} i dzwonię do {self.first_name} {self.last_name}."
    
    


osoba = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),company=fake.company(), occupation=fake.job(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
print(osoba.contact())
print(osoba.label_length)


print()


def create_contacts(contact_type="private", n=1):

    contacts = []

    for i in range(n):
        if contact_type == "private":
            card = BaseContact(
                first_name=fake.first_name(), 
                last_name=fake.last_name(),
                tel_priv=fake.phone_number(),
            )
        else:
            card = BusinessContact(
                first_name=fake.first_name(), 
                last_name=fake.last_name(),
                tel_priv=fake.phone_number(),
                tel_work=fake.phone_number(),
                company=fake.company(), 
                occupation=fake.job(), 
            )    
        contacts.append(card)
    return contacts


    

print(create_contacts())
print(create_contacts(contact_type="business"))