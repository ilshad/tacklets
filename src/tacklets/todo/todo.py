# 2010 Ilshad Khabibullin <astoon@spacta.com>

from persistent import Persistent
from zope.component import adapts
from zope.interface import implements
from zope.container import btree
from zope.annotation import factory
from zope.schema.fieldproperty import FieldProperty
from interfaces import ITODOAnnotatable, ITODO, IItem

class TODO(btree.BTreeContainer):
    implements(ITODO)
    adapts(ITODOAnnotatable)

    @property
    def progress(self):
        try:
            return len(
                [x for x in self.values() if x.closed]) / len(
                self) * 100
        except ZeroDivisionError:
            return 0

class Item(Persistent):
    implements(IItem)

    subject = FieldProperty(IItem['subject'])
    closed = FieldProperty(IItem['closed'])

annotation_factory = factory(TODO)
