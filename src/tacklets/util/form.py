# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import button
from zc.resourcelibrary import need

class EditForm(form.EditForm):
    """Quite convenient customization of standard edit form.

    1) Change behavior for "apply" action: if updated succesfully,
    then redirect to nextURL().
    2) Added "Cancel" action.
    3) If there are resource libraries, load them.
    """

    resourcelibraries = ()

    @button.buttonAndHandler(u"Apply", name="apply")
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        changes = self.applyChanges(data)
        if changes:
            self.request.response.redirect(self.nextURL())
        else:
            self.status = self.noChangesMessage

    @button.buttonAndHandler(u"Cancel", name="cancel")
    def handleCancel(self, action):
        self.request.response.redirect(self.nextURL())

    def nextURL(self):
        return u"."

    def update(self):
        for x in self.resourcelibraries:
            need(x)
        super(EditForm, self).update()
