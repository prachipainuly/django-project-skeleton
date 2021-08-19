from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views.create_view_sample import CreateView
from .views.details_view_sample import DetailsView

urlpatterns = {
    url(r'^create_sample/$', CreateView.as_view(), name="create"),
    url(r'^update_sample/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)

