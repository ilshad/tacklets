# 2010 Ilshad Khabibullin <astoon@spacta.com>

from markdown import Markdown
from zope.component import adapts
from zope.interface import implements
from zope.publisher.browser import BrowserView
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.renderer.interfaces import ISource, IHTMLRenderer
from zope.app.renderer import SourceFactory

class IMarkdownSource(ISource):
    """Marker interface for a markdown text source"""

MarkdownSourceFactory = SourceFactory(
    IMarkdownSource, "Markdown", "Markdown Text Source")

class MarkdownHTMLRenderer(BrowserView):
    implements(IHTMLRenderer)
    adapts(IMarkdownSource, IBrowserRequest)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def render(self, *args):
        md = Markdown()
        return md.convert(self.context)
