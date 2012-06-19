# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.interface import classProvides
from zope.componentvocabulary.vocabulary import UtilityVocabulary
from zope.schema.interfaces import IVocabularyFactory
from interfaces import ITheme

class ThemingVocabulary(UtilityVocabulary):

    classProvides(IVocabularyFactory)
    interface = ITheme
