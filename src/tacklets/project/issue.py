# 2010 Ilshad Khabibullin <astoon@spacta.com>

from persistent.list import PersistentList
from zope.interface import implements
from zope.component import getAdapter
from zope.container.btree import BTreeContainer
from zope.schema.fieldproperty import FieldProperty
from zope.security.proxy import getObject
from hurry.workflow.interfaces import IWorkflowInfo
from tacklets.project.interfaces import IIssue
from tacklets.project.hooks import get_project
from tacklets.project.topic import valid_title_p

class Issue(BTreeContainer):
    implements(IIssue)

    title = FieldProperty(IIssue["title"])
    description = FieldProperty(IIssue["description"])

    milestone = None

    def __init__(self):
        super(Issue, self).__init__()
        self._topics = PersistentList()

    def update_topics(self, titles):
        dels = []
        for ob in self._topics:
            if ob.title not in titles:
                dels.append(ob)
        for ob in dels:
            self._topics.remove(ob)
            ob.del_doc(self)
            if ob.is_empty():
                topic_key = ob.__name__
                project = get_project()
                try:
                    del project.topics[topic_key]
                except KeyError:
                    pass
        topic_folder = get_project().topics
        topics_keys = [x.__name__ for x in self._topics]
        for title in titles:
            if valid_title_p(title):
                ob = getObject(topic_folder.search(title))
                if ob.__name__ not in topics_keys:
                    self._topics.append(ob)
                    ob.add_doc(self)

    def get_topics(self):
        return self._topics

def issue_added(ob, event):
    info = getAdapter(ob, IWorkflowInfo, name="project.issue")
    info.fireTransition("create")
