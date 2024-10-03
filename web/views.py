from django.shortcuts import render
from django.http import HttpResponseRedirect


def HomePage(request):
    return render(request, "index.html")


def ChangeLanguage(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
