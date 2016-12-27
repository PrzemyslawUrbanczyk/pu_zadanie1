import re

from model.contact import Contact


def test_contact_details_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", last_name="test2"))

    name_from_home_page = app.contact.get_contact_list()[0]
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    lastname_from_home_page = app.contact.get_contact_list()[0]
    lastname_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    address_from_home_page = app.contact.get_contact_list()[0]
    address_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)


    assert name_from_home_page.address == name_from_edit_page.address
    assert lastname_from_home_page.last_name == lastname_from_edit_page.last_name
    assert address_from_home_page.address == address_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert email_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(email_from_edit_page)




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