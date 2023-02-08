from .models import User


def get_best_busters():
    best_busters = User.objects.filter(is_best=True).prefetch_related('mailbox').only(
        'avatar',
        'mailbox'
    )
    return best_busters
