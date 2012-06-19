# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.securitypolicy.interfaces import IPrincipalPermissionManager
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.securitypolicy.interfaces import Allow

def clean_permissions(context, permission_id, setting=Allow):
    """Remove given permission for all principals"""
    prinper = IPrincipalPermissionManager(context)
    old = prinper.getPrincipalsForPermission(permission_id)
    for x in old:
        if x[1] == setting:
            prinper.unsetPermissionForPrincipal(permission_id, x[0])

def clean_roles(context, role_id, setting=Allow):
    """Remove given role for all principals"""
    prinrole = IPrincipalRoleManager(context)
    old = prinrole.getPrincipalsForRole(role_id)
    for x in old:
        if x[1] == setting:
            prinrole.unsetRoleForPrincipal(role_id, x[0])
