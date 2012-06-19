# 2010 Ilshad Khabibullin <astoon@spacta.com>

from z3c.form.interfaces import IWidget
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser.widget import addFieldClass, HTMLTextAreaWidget
from zope.component import createObject, getMultiAdapter
from zope.interface import implementsOnly

class IMarkdownWidget(IWidget):
    """Markdown widget"""

class InputMarkdownWidget(HTMLTextAreaWidget, Widget):
    implementsOnly(IMarkdownWidget)

    klass = u'markdown-widget'
    value = u''

    def update(self):
        super(InputMarkdownWidget, self).update()
        addFieldClass(self)

def InputMarkdownFieldWidget(field, request):
    return FieldWidget(field, InputMarkdownWidget(request))
