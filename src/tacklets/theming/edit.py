# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.form import field
from z3c.formui import form
from interfaces import ITheming

class ThemingForm(form.EditForm):

    fields = field.Fields(ITheming)

    def getContent(self):
        return self.request

    def update(self):
        super(ThemingForm, self).update()
        if self.status == self.successMessage:
            self.request.response.redirect(self.request.URL)
