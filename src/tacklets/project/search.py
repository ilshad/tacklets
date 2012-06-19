# 2010 Ilshad Khabibullin <astoon@spacta.com>

import tackle
from zope.component import adapts
from zope.interface import implements
from zope.index.text.interfaces import ISearchableText
from tacklets.project.interfaces import IDocument

class DocumentSearchResultItem(object):
    implements(tackle.ISearchResultItem)
    adapts(IDocument)

    def __init__(self, doc):
        self.doc = doc

    @property
    def title(self):
        return self.doc.title

    @property
    def description(self):
        return self.doc.description[:300] + u" ..."

class DocumentSearchableText(object):
    implements(ISearchableText)
    adapts(IDocument)

    def __init__(self, doc):
        self.doc = doc

    def getSearchableText(self):
        return self.doc.title, self.doc.description
