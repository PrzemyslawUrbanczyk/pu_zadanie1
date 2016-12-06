# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(first_name="modified", middle_name="modified", last_name="modified",
                               nickname="modified", company="modified", title="modified",
                               address="modified", home_number="modified", mobile_number="modified",
                               work_number="modified", fax="modified", first_email="modified",
                               second_email="modified", third_email="modified", wwwpage="modified",
                               birth_year="3000", anniversary_year="3000", second_address="modified",
                               second_private_number="modified", notes="modified"))




