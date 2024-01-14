
from django.conf import settings
from django.core.management import call_command

class CollectStaticMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not settings.DEBUG:
            call_command('collectstatic', interactive=False, clear=True)
        response = self.get_response(request)
        return response
