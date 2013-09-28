from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('recomendation.views',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^login$', 'login', name="login"),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^team$', TemplateView.as_view(template_name='team.html'), name="team"),

)
