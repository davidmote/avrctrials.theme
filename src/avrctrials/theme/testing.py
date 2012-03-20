from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class AvrctrialsTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import avrctrials.theme
        xmlconfig.file('configure.zcml',
                       avrctrials.theme,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'avrctrials.theme:default')

AVRCTRIALS_THEME_FIXTURE = AvrctrialsTheme()
AVRCTRIALS_THEME_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(AVRCTRIALS_THEME_FIXTURE, ),
                       name="AvrctrialsTheme:Integration")