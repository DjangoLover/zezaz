# coding=utf-8
from social.backends.github import GithubOAuth2


class ZezazGithubOAuth2(GithubOAuth2):
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires'),
        ('avatar_url', 'avatar_url')
    ]