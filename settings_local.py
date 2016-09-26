# coding=utf-8

from settings_base import *    # pylint: disable=W0614,W0401
from django.utils.translation import ugettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['example.com']

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(VAR_ROOT, 'dev.db'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fgs-2',
        'USER': 'fgs',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", "blog.BlogPost",
       "generic.ThreadedComment", (_("Media Library"), "media-library"),)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
)

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
