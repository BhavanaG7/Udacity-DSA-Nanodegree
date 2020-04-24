'''
--------------------------------------------------------------------------------------------------------------------------
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
----------------------------------------------------------------------------------------------------------------------------
'''
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    #to add group
    def set_group(self, group):
        self.groups.append(group)

    #to add users
    def set_user(self, user):
        self.users.append(user)

    #to fetch group
    def get_group(self):
        return self.groups

    #to fetch user
    def get_user(self):
        return self.users

    #to fetch name
    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    #if user is found return True
    if user in group.get_user(): 
        return True
    else:
        #Search otherwise
        if len(group.get_group()) == 0:
            return False
        else:
            for i in group.get_group():
                found = is_user_in_group(user, i)

                if found:
                    return True
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.set_user(sub_child_user)

child.set_group(sub_child)
parent.set_group(child)

print("user:parent_user, group:parent")
print(is_user_in_group('parent_user',parent))
print("----------------------------------------------------------")

print("user:child_user, group:parent")
print(is_user_in_group('child_user',parent))
print("----------------------------------------------------------")

print("user:sub_child_user, group=parent")
print(is_user_in_group('sub_child_user',parent))
print("----------------------------------------------------------")

print("user:sub_child_user, group=child")
print(is_user_in_group('sub_child_user',child))
print("----------------------------------------------------------")

# Edge Cases:

print("user:'',group:parent")
print(is_user_in_group('',parent))
print("----------------------------------------------------------")

print("user:'',group:child")
print(is_user_in_group('',child))
