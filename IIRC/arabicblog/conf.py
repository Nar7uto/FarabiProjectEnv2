from __future__ import unicode_literals

from django.conf import settings  # noqa

from appconf import AppConf

from .utils import load_path_attr


def is_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False

class ArabicBlogAppConf(AppConf):

    ALL_SECTION_NAME = "all"
    SECTIONS = []
    UNPUBLISHED_STATES = [
        "Draft"
    ]
    FEED_TITLE = "Blog"
    SECTION_FEED_TITLE = "Blog (%s)"
    SCOPING_MODEL = None
    SCOPING_URL_VAR = None
    SLUG_UNIQUE = False
    PAGINATE_BY = 10
    ADMIN_JS = ("js/admin_post_form.js",)

    class Meta:
        prefix = "arabicblog"
