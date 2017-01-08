
import random
import string
import os.path
import jsonpickle
import getopt
import sys

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))