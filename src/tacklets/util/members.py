# 2010 Ilshad Khabibullin <astoon@spacta.com>

""" Get principals who are members of group which
has given role on the context or its parents.

Role -> Group --> Principals

Cleanup local security map if principal or group removed.

We assume that security and authentication policy
is default of Tackle.
"""

from zope.component import getUtility
from zope.location import LocationIterator
from zope.authentication.interfaces import IAuthentication
from zope.authentication.interfaces import PrincipalLookupError
from zope.securitypolicy.interfaces import IPrincipalRoleMap
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.securitypolicy.interfaces import Allow

def get_members(context, role_id):
    members = []
    auth = getUtility(IAuthentication)
    for ob in LocationIterator(context):
        for x in IPrincipalRoleMap(ob).getPrincipalsForRole(role_id):
            if x[1] == Allow:
                try:
                    group = auth.getPrincipal(x[0])
                    for pid in group.getMembers():
                        if pid not in members:
                            try:
                                members.append(auth.getPrincipal(pid))
                            except PrincipalLookupError:
                                pass # TODO: remove member from group?
                except PrincipalLookupError:
                    IPrincipalRoleManager(ob).removeRoleFromPrincipal(x[0], role_id)
    return members
