# 2010 Ilshad Khabibullin <astoon@spacta.com>

import base64, urllib, tackle
from zope.interface import implements
from zope.component import adapts, getUtility
from zope.publisher.interfaces import browser
from zope.schema.interfaces import IVocabularyFactory
from rwproperty import getproperty, setproperty
from interfaces import ITheming

class Theming(object):
    implements(ITheming)
    adapts(browser.IBrowserRequest)

    cookie_name = 'tackle.skin'
    expires = 'Tue, 19 Jan 2038 00:00:00 GMT'

    def __init__(self, request):
        self.request = request

    @getproperty
    def theme(self):
        factory = getUtility(IVocabularyFactory, name="Themes")
        cookie = self.request.get(self.cookie_name)
        if cookie:
            token = base64.decodestring(urllib.unquote(cookie))
            try:
                return factory(None).getTermByToken(token).value
            except LookupError:
                pass
        return tackle.persistent_config("Default Theme").theme

    @setproperty
    def theme(self, value):
        factory = getUtility(IVocabularyFactory, name="Themes")
        token = factory(None).getTerm(value).token
        self.request.response.setCookie(
                self.cookie_name,
                urllib.quote(base64.encodestring(token)),
                expires=self.expires,
                path="/")
