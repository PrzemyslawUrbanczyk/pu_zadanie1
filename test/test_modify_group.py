from model.group import Group

import random


def test_modify_group_name(app, db, json_groups):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = json_groups
    old_group = random.choice(old_groups)
    group.id = old_group.id
    app.group.modify_group_by_id(old_group.id, group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    app.group.modify_first_group((Group(header="New header")))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

#def test_modify_group_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    app.group.modify_first_group((Group(footer="New footer")))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
