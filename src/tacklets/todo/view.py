# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.browserpage import ViewPageTemplateFile
from zope.container.interfaces import INameChooser
from zope.traversing.browser.absoluteurl import absoluteURL
from zope.lifecycleevent import ObjectModifiedEvent
from zope.event import notify
from interfaces import ITODO, IItem
from todo import Item

class View(object):

    __call__ = ViewPageTemplateFile('view.pt')
    change_template = ViewPageTemplateFile('change.pt')

    @property
    def todo(self):
        return ITODO(self.context)

    def add(self):
        subject = self.request.get('subject')
        ob = Item()
        ob.subject = subject
        name = INameChooser(self.todo).chooseName(u"", ob)
        self.todo[name] = ob
        notify(ObjectModifiedEvent(self.todo))

    def listing(self):
        absolute_url = u"'" + absoluteURL(self.context, self.request) + u"'"
        result = [u'<ol class="todo_list">']
        for key in self.todo:
            key_str = u"'" + key + u"'"
            item = self.todo[key]
            if item.closed:
                subject = u'<del>' + item.subject + u'</del>'
            else:
                subject = item.subject
            result.append(
                u'<li><span onclick="todo.change(this, %s, %s)" class="todo_item">%s&nbsp;</span></li>' % (
                    absolute_url, key_str, subject or u'...'))
        result.append(u'</ol>')
        return u''.join(result)

    def change(self):
        key = self.request.get('item_key')
        self.item = self.todo.get(key)
        subject = self.request.get('subject')
        if key and self.item and subject:
            self.item.subject = subject
            raw_closed = self.request.get('closed')
            if raw_closed == 'true':
                self.item.closed = True
            elif raw_closed == 'false':
                self.item.closed = False
        notify(ObjectModifiedEvent(self.todo))
        return self.change_template()

    def remove(self):
        key = self.request.get('item_key')
        if self.todo.get(key):
            del self.todo[key]
            notify(ObjectModifiedEvent(self.todo))
