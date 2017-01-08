# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_some_contact(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", last_name="test2"))
    old_contacts = app.contact.get_contact_list()
    contact = json_contacts
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







