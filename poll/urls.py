
from django.conf.urls import url
from django.views.generic import TemplateView

from poll.views import VoteView


urlpatterns = [

    url(r'^latest/$', TemplateView.as_view(
        template_name='poll/latest.html'), name='latest'),

    url(r'^vote/$', VoteView.as_view(), name='vote')

]