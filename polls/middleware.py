from django.http import Http404

from .models import Logs


class LogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        meth = request.method
        path = request.path

        if ('admin' or 'favicon') not in path:
            Logs.objects.create(path=path, method=meth)

        response = self.get_response(request)
        return response
