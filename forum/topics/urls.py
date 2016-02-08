from django.conf.urls import url
from .views import (add, index, detail)

urlpatterns = [
    url(r"^index/$", index, name='index'),
    url(r"^add/$", add),
    url(r"^(?P<id>[0-9]+)/$", detail),
]