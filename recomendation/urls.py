from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from recomendation.views.login import OAuthLoginNewView
from recomendation.views.suggestion import Suggetion


urlpatterns = patterns('recomendation.views',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^suggestion$', Suggetion.as_view(), name="suggestion"),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^team$', TemplateView.as_view(template_name='team.html'), name="team"),

    url(r'^login/new$', OAuthLoginNewView.as_view(), name='login_new'),
)
