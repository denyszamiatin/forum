from django.conf.urls import url

from .views import (add, index, detail, edit, IndexView)

urlpatterns = [
    url(r"^index/$", index, name='index'),
    url(r"^add/$", add),
    url(r"^indextv/$",
        IndexView.as_view()),
    url(r"^edit/(?P<id>[0-9]+)/$", edit),
    url(r"^(?P<id>[0-9]+)/$", detail),
]