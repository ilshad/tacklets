# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.formui import form
from z3c.form import field
from zc.resourcelibrary import need
from zope.container.interfaces import INameChooser
from zope.traversing.browser.absoluteurl import absoluteURL
from tacklets.project.interfaces import IIssue
from tacklets.project.issue import Issue

class Pagelet(form.AddForm):

    label = u"New issue"
    fields = field.Fields(IIssue)

    i_name = None

    def create(self, data):
        ob = Issue()
        form.applyChanges(self, ob, data)
        return ob

    def add(self, ob):
        self.i_name = INameChooser(self.context).chooseName(u"", ob)
        self.context[self.i_name] = ob

    def nextURL(self):
        return absoluteURL(self.context, self.request) + \
            "/" + self.i_name

    def update(self):
        need("tacklets.project")
        super(Pagelet, self).update()
