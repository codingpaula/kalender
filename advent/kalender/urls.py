from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="kalender/kalender_main.html"),
            name='kalender_main'),
    url(r'^(?P<tag_datum>[0-9]+)/tag/$',
            TemplateView.as_view(template_name="kalender/kalender_tag.html"),
            name='kalender_tag')
]
