# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import implements
from zope.schema.interfaces import ISourceText
from zope.schema import SourceText

class IMarkdownSourceText(ISourceText):
    """Field with markdown"""

class MarkdownSourceText(SourceText):
    implements(IMarkdownSourceText)
