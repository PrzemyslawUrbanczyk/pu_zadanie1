import re

from model.contact import Contact


def test_contact_details_with_database(app, db):

    name_from_home_page = list(map(lambda a: a.first_name, sorted(app.contact.get_contact_list(), key=Contact.id_or_max)))
    name_from_database = list(map(lambda b: b.first_name, sorted(db.get_contact_list(), key=Contact.id_or_max)))

    lastname_from_home_page = list(map(lambda c: c.last_name, sorted(app.contact.get_contact_list(), key=Contact.id_or_max)))
    lastname_from_database = list(map(lambda d: d.last_name, sorted(db.get_contact_list(), key=Contact.id_or_max)))

    contact_from_home_page = list(map(lambda f: f.all_phones_from_home_page, sorted(app.contact.get_contact_list(), key=Contact.id_or_max)))
    contact_from_database = list(map(lambda c: merge_phones_like_on_home_page(c), sorted(db.get_contact_list(), key=Contact.id_or_max)))

    email_from_home_page = list(map(lambda h: h.all_emails_from_home_page, sorted(app.contact.get_contact_list(), key=Contact.id_or_max)))
    email_from_database = list(map(lambda g: merge_emails_like_on_home_page(g), sorted(db.get_contact_list(), key=Contact.id_or_max)))

    address_from_home_page = list(map(lambda c: c.address, sorted(app.contact.get_contact_list(), key=Contact.id_or_max)))
    address_from_database = list(map(lambda c: c.address, sorted(db.get_contact_list(), key=Contact.id_or_max)))

    assert address_from_home_page == address_from_database
    assert email_from_home_page == email_from_database
    assert contact_from_home_page == contact_from_database
    assert name_from_home_page == name_from_database
    assert lastname_from_home_page == lastname_from_database


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_number, contact.mobile_number, contact.work_number,
                                        contact.second_private_number]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.first_email, contact.second_email, contact.third_email]))))
