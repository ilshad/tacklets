# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import adapts
from zope.interface import implements
from hurry.workflow.workflow import Transition
from tacklets.project.interfaces import IAction

class TransitionAction(object):
    implements(IAction)
    adapts(Transition)

    permission = None

    def __init__(self, context):
        self.context = context

    @property
    def name(self):
        return self.context.transition_id

    @property
    def title(self):
        return self.context.title

class SimpleAction(object):
    implements(IAction)

    def __init__(self, name, title, permission):
        self.name = name
        self.title = title
        self.permission = permission

def edit_action(context):
    return SimpleAction("edit", "Edit", "tacklets.project.Action")

def topics_action(context):
    return SimpleAction("topics", "Topics", "tacklets.project.Action")
