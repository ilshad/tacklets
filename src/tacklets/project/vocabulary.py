# 2010 Ilshad Khabibullin <astoon@spacta.com>

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from tacklets.util.members import get_members
from tacklets.project.hooks import get_project

def project_members(context):
    members = get_members(get_project(), "tacklets.project.Member")
    return SimpleVocabulary([SimpleTerm(x.id, title=x.title) for x in members])
