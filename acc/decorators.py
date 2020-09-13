from django.http import HttpResponseRedirect
from django.shortcuts import reverse


def non_authenticated(func):
    def wrap(request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("acc_profile"))
        return func(request,*args,**kwargs)
    return wrap