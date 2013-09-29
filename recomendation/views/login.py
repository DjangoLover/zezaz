# -*- coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from recomendation.forms import LogInForm


def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = LogInForm(request)
        context['form'] = form
        if not form.is_valid():
            return render_to_response('login.html', context)

        # return HttpResponseRedirect()

    else:
        context['form'] = LogInForm()
        return render_to_response('login.html', context)

from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
from django.contrib import messages


class OAuthLoginNewView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        if self.request.user.is_authenticated():
            messages.add_message(
                self.request,
                messages.SUCCESS,
                "You account was created!"
            )
        else:
            messages.add_message(
                self.request,
                messages.ERROR,
                "Error on creating account"
            )
        return reverse('recomendation:home')