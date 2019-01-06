from __future__ import unicode_literals

from django.conf import settings  # noqa

from appconf import AppConf

from .utils import load_path_attr


class ArabicBlogAppConf(AppConf):

    ALL_SECTION_NAME = "all"
    SECTIONS = []
    SLUG_UNIQUE = False
    PAGINATE_BY = 10


    class Meta:
        prefix = "arabicblog"



