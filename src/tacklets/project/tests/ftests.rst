=======================
Tackle functional tests
=======================

:doctest:
:functional-zcml-layer: ftesting.zcml

Prepare tests::

  >>> from zope.testbrowser.testing import Browser
  >>> from zope.interface.verify import verifyObject
  >>> root = getRootFolder()
  >>> root_url = 'http://localhost'
  >>> browser = Browser()

Open site's root::

  >>> browser.open(root_url)
  >>> browser.headers['status']
  '200 Ok'

Sign in::

  >>> browser.getControl(name='login').value='manager'
  >>> browser.getControl(name='password').value='password'
  >>> browser.getControl(name='SUBMIT').click()

Go to system settings::

  >>> browser.getLink(text=u'System').click()
  >>> browser.url
  'http://localhost/++etc++site'

Add project:

  >>> browser.getLink(text=u'Content').click()
  >>> browser.getControl(label=u'Content type').value
  ['tacklets.project']

  >>> browser.getControl(name=u'form.widgets.contents.from').options
  []

  >>> browser.getControl(name=u'form.widgets.contents.to').options
  []

  >>> browser.getControl(label=u'Identifier').value=u'pr01'
  >>> browser.getControl(label=u'Dublin Core Title').value=u'Project 01'
  >>> browser.getControl(label=u'Add').click()

  >>> browser.getLink(text=u'Project 01').attrs
  {'href': 'http://localhost/pr01', 'class': ''}
