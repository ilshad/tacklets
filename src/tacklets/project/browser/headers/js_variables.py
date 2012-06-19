# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.traversing.browser.absoluteurl import absoluteURL
from tacklets.project.hooks import get_project

class View:

    def __call__(self):
        self.request.response.setHeader('Content-Type','application/x-javascript')
        self.request.response.setHeader('Cache-Control','public,max-age=86400')

        response_text = ""
        response_text += "var PROJECT_URL = \"%s\";\n" % absoluteURL(get_project(), self.request)

        return response_text.encode('utf-8')
