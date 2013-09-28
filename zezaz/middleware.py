# coding=utf-8
from debug_toolbar.middleware import DebugToolbarMiddleware


class CustomDebugMiddleware(DebugToolbarMiddleware):
    def _show_toolbar(self, request):
        return super(CustomDebugMiddleware, self)._show_toolbar(request) \
            or request.user.is_superuser