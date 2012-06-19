# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import Interface
from zope.schema import Text, Bool, Int

class ITODOAnnotatable(Interface):
    """If an object provides this interface then it is
    able to annotate by TODO listing.
    """

class ITODO(Interface):
    """TODO LIST"""

    progress = Int(
        title=u"Progress, %",
        readonly=True)

class IItem(Interface):
    """TODO item"""

    subject = Text(
        required=False)

    closed = Bool(
        default=False,
        required=False)
