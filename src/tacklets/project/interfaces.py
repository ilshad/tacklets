# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import Interface, Attribute
from zope.schema import TextLine, Choice
from zope.annotation.interfaces import IAttributeAnnotatable
from tacklets.markdown import MarkdownSourceText

class IProject(Interface):
    """Project content type"""

    topics = Attribute("Topic folder")
    milestones = Attribute("Milestones folder")
    issues = Attribute("Issues folder")
    notes = Attribute("Notes folder")

## Document term. We describe basic functionality here.
class IDocument(Interface, IAttributeAnnotatable):
    """Document"""

    title = TextLine(
        title=u"Title")

    description = MarkdownSourceText(
        title=u"Description",
        required=False)

    milestone = Attribute("Get milestones")

    def update_topics(titles):
        """Update topics list"""

    def get_topics():
        """Get topics"""

class IIssue(IDocument):
    """Issue"""

class INote(IDocument):
    """Note"""

## Annotations. We describe additional properties which arise
## when the workflow transitions occur.
class IResponsibility(Interface):

    responsible = Choice(
        title=u"Responsible person",
        vocabulary="Project Members",
        required=False,
        default=None)

    def get_principal():
        """Get IPrincipal object"""

## Rubrication. Business logic of structured documents.
class ITopic(Interface):
    """Topic container type"""

    title = TextLine(
        title=u"Title")

    def add_doc(doc):
        """Add IDocument object"""

    def del_doc(doc):
        """Remove IDocument object"""

    def issues():
        """Iter IIssue objects"""

    def is_empty():
        """Return True if has not issues or False"""
        
class IMilestone(Interface):
    """Milestone container type"""

    title = TextLine(
        title=u"Title")

## System folders. Need for organize documens and rubrics
## in object database.
class ITopicFolder(Interface):
    """Folder for topics"""

    def search(title):
        """Return topic by title or create new one"""

class IMilestoneFolder(Interface):
    """Folder for milestones"""

class IIssueFolder(Interface):
    """Folder for issues"""

class INoteFolder(Interface):
    """Folder for notes"""

# misc interfaces
class IAction(Interface):
    """Arbitrary user's action"""

    name = Attribute("Name")

    title = Attribute("Title")

    permission = Attribute("Security permission")
