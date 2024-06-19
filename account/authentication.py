from django.contrib.auth.models import User
from .models import Profile
class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            profile = Profile.objects.get(phone_number=username)
            if profile.user.check_password(password):
                return profile.user
            return None
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None