# 2010 Ilshad Khabibullin <astoon@spacta.com>

import zope.container.contained

class IntegerNameChooser(zope.container.contained.NameChooser):
    """Choose names like `1`, `2`, etc."""

    def chooseName(self, *args):
        container = self.context
        i = 1
        while unicode(i) in container:
            i += 1
        return unicode(i)

class DigitNameChooser(zope.container.contained.NameChooser):
    """Choose names like `000001`,  '000002`, etc."""

    ndigits = 6

    def chooseName(self, name, ob):
        if len(self.context):
            num = unicode(max((int(x) for x in self.context.keys())) + 1)
            zero = u''.join(u'0' for x in range(self.ndigits - len(num)))
            return zero + num
        return u''.join(u'0' for x in range(self.ndigits - 1)) + u'1'
