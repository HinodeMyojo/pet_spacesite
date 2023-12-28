from django.conf import settings

def post_access(request):
    return {
        'post_access_groups': settings.POST_ACCESS,
    }