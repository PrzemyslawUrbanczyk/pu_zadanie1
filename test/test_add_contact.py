# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="sdfdsfdsf", middle_name="sdfsdfsdf", last_name="sdfsdfsdfds",
                              nickname="sdfsdfsdfsf", title="sfsdfsdfsfd", company="dsfsdfsfdsdfs",
                              address="gsdgdgsdsdgdg", home_number="23423424234", mobile_number="234234324",
                              work_number="23423423423", fax="23423423424", first_email="efssdfdfdsfds@qwe.com",
                              second_email="sdedfefe@qwe.com", third_email="ddfgsdsffsd@qwe.com", wwwpage="www.yuwqyqwyuqwuywq.com",
                              birth_year="1988", anniversary_year="2015", second_address="dsfdsfsdfsdfsdfsdfd",
                              second_private_number="fdsdfsdfsdfsd", notes="fdsdfssdfdssfdsf"))
    app.session.logout()




