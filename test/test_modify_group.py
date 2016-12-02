from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group((Group(name="modified123", header="modified123", footer="modified123")))
    app.session.logout()