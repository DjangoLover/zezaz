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



