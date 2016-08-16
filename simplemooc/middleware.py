import random
from django.http import HttpResponse


def log_middleware(get_response):
    def middleware(request):
        # antes de qualquer view
        response = get_response(request)
        # depois de qualquer view
        return response
    return middleware