# coding=utf-8

from debug_toolbar.panels import DebugPanel
from django.conf import settings
import git


class GitDebugPanel(DebugPanel):
    name = 'Git'

    def nav_title(self):
        return 'Git'

    def nav_subtitle(self):
        repo = git.Repo(settings.PROJECT_DIR)
        return '%s [%s]' % (repo.active_branch, str(repo.head.commit)[:8])

    def url(self):
        return ''

    def title(self):
        return 'Git'