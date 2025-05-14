# api/throttles.py

from rest_framework.throttling import SimpleRateThrottle

class CustomViewThrottle(SimpleRateThrottle):
    scope = 'custom'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return f'user-{request.user.id}'
        return self.get_ident(request)  # fallback to IP
