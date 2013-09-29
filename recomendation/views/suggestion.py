# coding=utf-8
import json
from django.http import HttpResponse
from django.views.generic import View
import time


class Suggetion(View):

    def get(self, request):
        #git_username = request.user.username
        time.sleep(3)

        users = [{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            },{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            },{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            },{
                "avatar_url": 'https://2.gravatar.com/avatar/8f8d53501d40286f6a2f228326926909',
                "login": 'cesarFrias',
                "bio": 'minimin'
            }]

        return HttpResponse(json.dumps(users), mimetype='application/json')

