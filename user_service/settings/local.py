from .base import *

# region GENERAL ---------------------------------------------------------------

DEBUG = True

# endregion --------------------------------------------------------------------

# region DJANGO-DEBUG-TOOLBAR ----------------------------------------------------------------

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# endregion --------------------------------------------------------------------
