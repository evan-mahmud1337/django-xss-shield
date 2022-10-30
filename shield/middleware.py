from django.http import HttpResponseBadRequest
from .the_shield import protect, bruter
from django.utils.deprecation import MiddlewareMixin

class XssShieldMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):

        datas = request.POST or request.GET
        for value in datas.values():
            if protect(value) is None or bruter(value) is None:
                return HttpResponseBadRequest('possible xss context found')
        return None