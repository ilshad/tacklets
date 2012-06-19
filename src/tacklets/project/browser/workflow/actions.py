# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import getAdapter
from zope.component import getAdapters
from zope.component import getUtility
from zope.security import checkPermission
from hurry.workflow.interfaces import IWorkflow
from hurry.workflow.interfaces import IWorkflowInfo
from tacklets.project.interfaces import IAction
from tacklets.project.action import SimpleAction

class ActionsManager:

    def actions(self):
        info = getAdapter(self.context, IWorkflowInfo, "project.issue")
        workflow = getUtility(IWorkflow, name="project.issue")
        r = [IAction(workflow.getTransitionById(x))
             for x in info.getManualTransitionIds()]

        for name, action in getAdapters((self.context,), IAction):
            if checkPermission(action.permission, self.context):
                r.append(action)

        return r
