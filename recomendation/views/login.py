# -*- coding: utf-8
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