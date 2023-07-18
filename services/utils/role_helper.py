from bframe import g
from services.utils.static import role_admin, role_user, role_visitor


def check_role():
    if str(g.user.role) == str(role_visitor()):
        return role_visitor()
    if str(g.user.role) == str(role_admin()):
        return role_admin()
    if str(g.user.role) == str(role_user()):
        return role_user()
    raise Exception("No Set Current Role")
