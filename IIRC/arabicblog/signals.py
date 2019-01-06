import django.dispatch

post_viewed = django.dispatch.Signal(providing_args=["post", "request"])
post_created = django.dispatch.Signal(providing_args=["post"])
post_redirected = django.dispatch.Signal(providing_args=["post", "request"])
