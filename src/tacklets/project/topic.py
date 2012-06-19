# 2010 Ilshad Khabibullin <astoon@spacta.com>

import string
from BTrees import IFBTree
from persistent import Persistent
from zope.interface import implements
from zope.container.contained import Contained
from zope.schema.fieldproperty import FieldProperty
from tacklets.project.interfaces import ITopic
from tacklets.project.hooks import get_project

class Topic(Persistent, Contained):
    implements(ITopic)

    title = FieldProperty(ITopic["title"])

    def __init__(self, title):
        self._ids = IFBTree.IFTreeSet()
        self.title = title

    def add_doc(self, doc):
        self._ids.insert(int(doc.__name__))

    def del_doc(self, doc):
        try:
            self._ids.remove(int(doc.__name__))
        except KeyError:
            pass

    def issues(self):
        project = get_project()
        for id in self._ids:
            try:
                yield project.issues[str(id)]
            except KeyError:
                pass

    def is_empty(self):
        return len(self._ids) == 0

def valid_title_p(title):
    for character in title:
        if character in string.punctuation:
            return False
    if title == "":
        return False
    return True
