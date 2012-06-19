# 2010 Ilshad Khabibullin <astoon@spacta.com>

from hurry.workflow.workflow import Transition
from hurry.workflow.workflow import Workflow
from hurry.workflow.workflow import WorkflowInfo
from hurry.workflow.workflow import WorkflowState
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.securitypolicy.interfaces import Allow
from tacklets.util.security import clean_roles
from tacklets.project.interfaces import IResponsibility

## main route

create_transition = Transition(
    transition_id="create",
    title="Create",
    source=None,
    destination="waiting",
    permission="tacklets.project.CreateIssue")

assign_transition = Transition(
    transition_id="assign",
    title="Assign",
    source="waiting",
    destination="assigned",
    permission="tacklets.project.Responsibility")

resolve_transition = Transition(
    transition_id="resolve",
    title="Resolve",
    source="assigned",
    destination="resolved",
    permission="tacklets.project.Action")

verify_transition = Transition(
    transition_id="verify",
    title="Verify",
    source="resolved",
    destination="verified",
    permission="tacklets.project.CloseIssue")

# reassign
reassign_from_resolved_transition = Transition(
    transition_id="reassign_from_resolved",
    title="Reassign",
    source="resolved",
    destination="assigned",
    permission="tacklets.project.Action")

# reject
reject_from_waiting_transition = Transition(
    transition_id="reject_from_waiting",
    title="Reject",
    source="waiting",
    destination="rejected",
    permission="tacklets.project.CloseIssue")

reject_from_assigned_transition = Transition(
    transition_id="reject_from_assigned",
    title="Reject",
    source="assigned",
    destination="rejected",
    permission="tacklets.project.CloseIssue")

reject_from_deferred_transition = Transition(
    transition_id="reject_from_deferred",
    title="Reject",
    source="deferred",
    destination="rejected",
    permission="tacklets.project.CloseIssue")

# split
split_from_waiting_transition = Transition(
    transition_id="split_from_waiting",
    title="Split",
    source="waiting",
    destination="split",
    permission="tacklets.project.Action")

split_from_assigned_transition = Transition(
    transition_id="split_from_assigned",
    title="Split",
    source="assigned",
    destination="split",
    permission="tacklets.project.Action")

split_from_resolved_transition = Transition(
    transition_id="split_from_resolved",
    title="Split",
    source="resolved",
    destination="split",
    permission="tacklets.project.Action")

# defer
defer_transition = Transition(
    transition_id="defer",
    title="Defer",
    source="assigned",
    destination="deferred",
    permission="tacklets.project.Action")

proceed_from_defer_transition = Transition(
    transition_id="proceed_from_defer",
    title="Proceed",
    source="deferred",
    destination="assigned",
    permission="tacklets.project.Action")

# feedback
request_transition = Transition(
    transition_id="request",
    title="Request",
    source="assigned",
    destination="feedback",
    permission="tacklets.project.Action")

proceed_from_feedback_transition = Transition(
    transition_id="proceed_from_feedback",
    title="Proceed",
    source="feedback",
    destination="assigned",
    permission="tacklets.project.Action")

abolish_transition = Transition(
    transition_id="abolish",
    title="Abolish",
    source="feedback",
    destination="abolished",
    permission="tacklets.project.CreateIssue")

# responsibility
responsibility_assigned_transition = Transition(
    transition_id="responsibility_assigned",
    title="Responsibility",
    source="assigned",
    destination="assigned",
    permission="tacklets.project.Responsibility")

# restore
restore_from_verified_transition = Transition(
    transition_id="restore_from_verified",
    title="Restore",
    source="verified",
    destination="waiting",
    permission="tacklets.project.Restore")

restore_from_rejected_transition = Transition(
    transition_id="restore_from_rejected",
    title="Restore",
    source="rejected",
    destination="waiting",
    permission="tacklets.project.Restore")

restore_from_abolished_transition = Transition(
    transition_id="restore_from_abolished",
    title="Restore",
    source="abolished",
    destination="waiting",
    permission="tacklets.project.Restore")

restore_from_split_transition = Transition(
    transition_id="restore_from_split",
    title="Restore",
    source="split",
    destination="waiting",
    permission="tacklets.project.Restore")

# utility
issue_workflow = Workflow(
    [create_transition,#
     assign_transition,#
     resolve_transition,#
     verify_transition,#
     reassign_from_resolved_transition,#
     reject_from_waiting_transition,#
     reject_from_assigned_transition,# 
     reject_from_deferred_transition,#
     split_from_waiting_transition,#
     split_from_assigned_transition,#
     split_from_resolved_transition,#
     defer_transition,#
     proceed_from_defer_transition,#
     request_transition,#
     proceed_from_feedback_transition,#
     abolish_transition,#
     responsibility_assigned_transition,#
     restore_from_verified_transition,#
     restore_from_rejected_transition,#
     restore_from_abolished_transition,#
     restore_from_split_transition#
     ])

# workflow info
class IssueWorkflowInfo(WorkflowInfo):

    name="project.issue"

# workflow state
class IssueWorkflowState(WorkflowState):

    state_key = "project.issue.state"
    id_key = "project.issue.id"

UPDATE_RESPONSIBILITY = ("assign", "responsibility_assigned")

def issue_transition_handler(ob, e):
    if e.transition.transition_id in UPDATE_RESPONSIBILITY:
        clean_roles(ob, "dynamic_tacklets.project.DocumentResponsible")

        prinrole = IPrincipalRoleManager(ob)
        principal_id = IResponsibility(ob).responsible
        prinrole.assignRoleToPrincipal("dynamic_tacklets.project.DocumentResponsible", principal_id)
