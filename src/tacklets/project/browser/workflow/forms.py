# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.form import form, field, button
from hurry.workflow.interfaces import IWorkflowInfo
from zope.component import getAdapter
from tacklets.project.interfaces import IResponsibility
from tacklets.project.interfaces import IDocument

class Assign(form.EditForm):

    fields = field.Fields(IResponsibility)

    @button.buttonAndHandler(u"Assign", name="assign")
    def handle_assign(self, action):
        data, errors = self.extractData()
        if not errors:
            issue = self.getContent()
            info = getAdapter(issue, IWorkflowInfo, name="project.issue")
            form.applyChanges(self, issue, data)
            info.fireTransition("assign")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class Resolve(form.EditForm):

    @button.buttonAndHandler(u"Resolve", name="resolve")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("resolve")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class Verify(form.EditForm):

    @button.buttonAndHandler(u"Verify", name="resolve")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("verify")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class ReassignFromResolved(form.EditForm):

    @button.buttonAndHandler(u"Reassign", name="reassign")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("reassign_from_resolved")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RejectFromWaiting(form.EditForm):

    @button.buttonAndHandler(u"Reject", name="resolve")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("reject_from_waiting")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RejectFromAssigned(form.EditForm):

    @button.buttonAndHandler(u"Reject", name="resolve")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("reject_from_assigned")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RejectFromDeferred(form.EditForm):

    @button.buttonAndHandler(u"Reject", name="resolve")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("reject_from_deferred")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class SplitFromWaiting(form.EditForm):

    @button.buttonAndHandler(u"Split", name="split")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("split_from_waiting")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class SplitFromAssigned(form.EditForm):

    @button.buttonAndHandler(u"Split", name="split")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("split_from_assigned")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class SplitFromResolved(form.EditForm):

    @button.buttonAndHandler(u"Split", name="split")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("split_from_resolved")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class Defer(form.EditForm):

    @button.buttonAndHandler(u"Defer", name="defer")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("defer")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class ProceedFromDefer(form.EditForm):

    @button.buttonAndHandler(u"Proceed", name="proceed")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("proceed_from_defer")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class Request(form.EditForm):

    @button.buttonAndHandler(u"Request", name="request")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("request")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class ProceedFromFeedback(form.EditForm):

    @button.buttonAndHandler(u"Proceed", name="proceed")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("proceed_from_feedback")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class Abolish(form.EditForm):

    @button.buttonAndHandler(u"Abolish", name="abolish")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("abolish")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class ResponsibilityAssigned(form.EditForm):

    fields = field.Fields(IResponsibility)

    @button.buttonAndHandler(u"Change responsibility", name="assign")
    def handle_assign(self, action):
        data, errors = self.extractData()
        if not errors:
            issue = self.getContent()
            info = getAdapter(issue, IWorkflowInfo, name="project.issue")
            form.applyChanges(self, issue, data)
            info.fireTransition("responsibility_assigned")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RestoreFromVerified(form.EditForm):

    @button.buttonAndHandler(u"Restore", name="restore")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("restore_from_verified")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RestoreFromRejected(form.EditForm):

    @button.buttonAndHandler(u"Restore", name="restore")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("restore_from_rejected")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RestoreFromAbolished(form.EditForm):

    @button.buttonAndHandler(u"Restore", name="restore")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("restore_from_abolished")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

class RestoreFromSplit(form.EditForm):

    @button.buttonAndHandler(u"Restore", name="restore")
    def handle_assign(self, action):
        info = getAdapter(self.context, IWorkflowInfo, name="project.issue")
        info.fireTransition("restore_from_split")
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

### simple actions

class Edit(form.EditForm):

    fields = field.Fields(IDocument)

    @button.buttonAndHandler(u"Save", name="save")
    def handle_save(self, action):
        data, errors = self.extractData()
        if not errors:
            issue = self.getContent()
            form.applyChanges(self, issue, data)
        self.request.response.redirect(".")

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handle_cancel(self, action):
        self.request.response.redirect(".")

    
