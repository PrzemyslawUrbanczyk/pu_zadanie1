
import random

from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact_list = db.get_contact_list()
    contact = random.choice(contact_list)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    contacts_in_groups = db.get_contacts_in_group(group)
    if contact in contacts_in_groups:
        contact = random.choice(contact_list)
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        return contact, group
    old_contacts = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group_by_id(contact.id, group)
    new_contacts = db.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)