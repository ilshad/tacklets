# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.component import createObject
from zope.component import getMultiAdapter
from zc.resourcelibrary import need

class Pagelet:

    def update(self):
        source = createObject("tackle.markdown", self.context.description)
        renderer = getMultiAdapter((source, self.request))
        self.description = renderer.render()

        need("tacklets.project")
        need("tacklets.todo")
