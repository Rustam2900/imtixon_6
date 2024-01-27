from .models import Result
from  django.contrib.auth import get_user_model

User = get_user_model()


class Base:
    def result(self):
        return Result.objects.all()

    def user(self):
        return User.objects.all()