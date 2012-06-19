# 2010 Ilshad Khabibullin <astoon@spacta.com>

import string
from zope.interface import implements
from zope.container.btree import BTreeContainer
from zope.container.interfaces import INameChooser
from tacklets.project import interfaces
from tacklets.project.topic import Topic

class Project(BTreeContainer):
    implements(interfaces.IProject)

    topics = property(lambda self: self["topic"])
    milestones = property(lambda self: self["milestone"])
    issues = property(lambda self: self["issue"])
    notes = property(lambda self: self["note"])

class TopicFolder(BTreeContainer):
    implements(interfaces.ITopicFolder)

    def search(self, title):
        for k,v in self.items():
            if title == v.title:
                return v
        t = Topic(title)
        n = INameChooser(self).chooseName(u"", t)
        self[n] = t
        return t

class MilestoneFolder(BTreeContainer):
    implements(interfaces.IMilestoneFolder)

class IssueFolder(BTreeContainer):
    implements(interfaces.IIssueFolder)

class NoteFolder(BTreeContainer):
    implements(interfaces.INoteFolder)

def project_added(ob, event):
    ob["topic"] = TopicFolder()
    ob["milestone"] = MilestoneFolder()
    ob["issue"] = IssueFolder()
    ob["note"] = NoteFolder()
