# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.schema import Choice
from zope.interface import Interface
from zope.component.interface import provideInterface
from zope.publisher.interfaces.browser import IBrowserSkinType
from tackle.skin.interfaces import ISkin

class ITheming(Interface):
    """Theming schema"""

    theme = Choice(
        title=u"Style theme",
        default=ISkin,
        vocabulary="Themes")

class ITheme(IBrowserSkinType):
    """If an layer skin provides this interface type
    then that skin are considered style"""

provideInterface('Tackle', ISkin, ITheme)

class IDefaultThemePersistentConfig(Interface):
    """Persistent config defines default theme"""

    theme = Choice(
        title=u"Style theme",
        default=ISkin,
        vocabulary="Themes")
