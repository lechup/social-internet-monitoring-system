# -*- coding: utf-8 -*-

########
# This file shouldn't be under any version control!
########
# It is local version of settings.py for
# particular developer, stage or production environment
# here You cant overwrite or update settings/default.py's

DEBUG = True
TEMPLATE_DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': projectpath('dev.db'),
        }
    }

# APPS SETTINGS #########################################
# staticserve
MIDDLEWARE_CLASSES += (
    'staticserve.middleware.StaticServe',
    'staticserve.middleware.MediaServe'
)

# debug_toolbar
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    )
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False
}
# APPS SETTINGS #########################################
