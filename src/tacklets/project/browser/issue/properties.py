# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getAdapter
from zope.security import checkPermission
from zope.browserpage import ViewPageTemplateFile
from hurry.workflow.interfaces import IWorkflowState
from tacklets.project.interfaces import IResponsibility

class IssuePropertiesView:

    template = ViewPageTemplateFile("properties.pt")

    def __call__(self):
        if checkPermission("tacklets.project.Watch", self.context):
            return self.template()
        return u""

    def get_state(self):
        state = getAdapter(self.context, IWorkflowState, "project.issue")
        return state.getState()

    def get_responsible(self):
        p = IResponsibility(self.context).get_principal()
        return p and p.title or u""
