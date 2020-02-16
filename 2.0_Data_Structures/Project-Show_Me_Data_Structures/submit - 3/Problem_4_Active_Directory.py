class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    result = False

    if user in group.get_users():
        return True
    # for u_User in group.get_users():
    #     if u_User == user:
    #         return True
    for g_Group in group.get_groups():
        result |= is_user_in_group(user, g_Group)
    return result

#Groups
parent = Group("parent")

child1 = Group("child1")
child2 = Group("child2")

sub_child11 = Group("subchild11")
sub_child12 = Group("subchild12")


#Users
parent_user_1 = "parent_user_1"
child1_user_1 = "child1_user_1"
child2_user_1 = "child2_user_1"
sub_child11_user_1 = "sub_child11_user_1"
sub_child12_user_1 = "sub_child12_user_1"


parent_user_2 = "parent_user_2"
child1_user_2 = "child1_user_2"
child2_user_2 = "child2_user_2"
sub_child11_user_2 = "sub_child11_user_2"
sub_child12_user_2 = "sub_child12_user_2"


parent.add_user(parent_user_1)
parent.add_user(parent_user_2)

parent.add_group(child1)
child1.add_user(child1_user_1)
child1.add_user(child1_user_2)

parent.add_group(child2)
child2.add_user(child2_user_1)
child2.add_user(child2_user_2)

child1.add_group(sub_child11)
child1.add_group(sub_child12)

sub_child11.add_user(sub_child11_user_2)



# TEST CASES
print('TEST CASES')
print(is_user_in_group(parent_user_1, child1))
# Prints False

print(is_user_in_group(parent_user_2, parent))
# Prints True

print(is_user_in_group(child2_user_2, parent))
# Prints True

print(is_user_in_group(sub_child11_user_2, group=sub_child11))
# Prints true

# EDGE CASE
print('EDGDE CASES')
print (is_user_in_group(child2_user_2, parent))
# Prints True

print(is_user_in_group(user='', group=parent))
# Prints False

print(is_user_in_group(child1_user_1, group=child1))
# Prints True

print(is_user_in_group('', group=sub_child11))
# Prints False




