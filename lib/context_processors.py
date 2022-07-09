from django.conf import settings


def context_settings(request):
    data = {}
    print(settings.STATIC_URL)
    data['settings'] = settings
    return data