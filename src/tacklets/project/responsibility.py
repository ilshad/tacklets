# 2010 Ilshad Khabibullin <astoon@spacta.com>

from persistent import Persistent
from zope.interface import implements
from zope.component import adapts
from zope.component import getUtility
from zope.annotation import factory
from zope.schema.fieldproperty import FieldProperty
from zope.authentication.interfaces import IAuthentication
from zope.authentication.interfaces import PrincipalLookupError
from interfaces import IResponsibility
from interfaces import IIssue

class Responsibility(Persistent):
    implements(IResponsibility)
    adapts(IIssue)

    responsible = FieldProperty(IResponsibility["responsible"])

    def get_principal(self):
        auth = getUtility(IAuthentication)
        if self.responsible is None:
            return None
        try:
            return auth.getPrincipal(self.responsible)
        except PrincipalLookupError:
            return None
    
annotation_factory = factory(Responsibility)
