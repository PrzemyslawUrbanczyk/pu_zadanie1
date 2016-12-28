# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                    home_number="", mobile_number="", work_number="", fax="", first_email="", second_email="",
                    third_email="", wwwpage="", birth_year="", anniversary_year="", second_address="",
                    second_private_number="", notes="", )] + [
    Contact(first_name=random_string("firstname", 10), middle_name=random_string("middlename", 10),
            last_name=random_string("lastname", 15), nickname=random_string("nickname", 10),
            title=random_string("title", 5),
            company=random_string("company", 10), address=random_string("address", 10),
            home_number=random_string("home", 9), mobile_number=random_string("mobile", 9),
            work_number=random_string("work", 9), fax=random_string("fax", 9),
            first_email=random_string("email", 10), second_email=random_string("email2", 10),
            third_email=random_string("email3", 10), wwwpage=random_string("homepage", 10),
            birth_year=random_string("byear", 4), anniversary_year=random_string("ayear", 4),
            second_address=random_string("address2", 10), second_private_number=random_string("phone2", 9),
            notes=random_string("notes", 20))
         for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


