from django.http import Http404

from .models import Logs


class LogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        meth = request.method
        path = request.path

        if ('admin' or 'favicon' or '__debug__') not in path:
            Logs.objects.create(path=path, method=meth)

        if 'silk' in path and not request.user.is_superuser:
            raise Http404("You not a superuser")

        response = self.get_response(request)
        return response
