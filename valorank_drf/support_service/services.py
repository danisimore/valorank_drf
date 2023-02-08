from .models import Request


def get_requests():
    requests = Request.objects.all()
    return requests
