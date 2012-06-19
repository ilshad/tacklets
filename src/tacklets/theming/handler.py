# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import directlyProvides
from interfaces import ITheming

def applyTheme(site, event):
    directlyProvides(event.request, ITheming(event.request).theme)
