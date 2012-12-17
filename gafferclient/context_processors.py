from django.conf import settings


def gaffer_server(request):
    return {"gaffer_server": settings.GAFFER_SERVER, }
