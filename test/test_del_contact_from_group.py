from fixture.orm import ORMFixture
import random

from model.contact import Contact
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_random_contact(app):

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(Contact(first_name="tester", last_name="tester"), group)
    old_contacts = db.get_contacts_in_group(group)
    removed_contacts = db.get_contacts_not_in_group(group)
    if sorted(old_contacts, key=Group.id_or_max) == sorted(removed_contacts, key=Group.id_or_max) :
        old_contacts.remove(removed_contacts)
    return old_contacts
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = old_contacts.remove(contact)
    assert old_contacts == new_contacts