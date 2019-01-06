from django.conf.urls import url

from .conf import settings
from .views import (
    BlogIndexView,
    DateBasedPostDetailView,
    SecretKeyPostDetailView,
    SectionIndexView,
    StaffPostDetailView,
)

app_name = "arabicblog"

urlpatterns = [
    url(r"^$", BlogIndexView.as_view(), name="blog"),
    url(r"^section/(?P<section>[-\w]+)/$", SectionIndexView.as_view(), name="blog_section"),
    url(r"^post/(?P<post_pk>\d+)/$", StaffPostDetailView.as_view(), name="blog_post_pk"),
    url(r"^post/(?P<post_secret_key>\w+)/$", SecretKeyPostDetailView.as_view(), name="blog_post_secret"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$", DateBasedPostDetailView.as_view(), name="blog_post"),
]
