# myapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from cdy.models import User
class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current path requested by the user
        path = request.path_info

        # Paths that require authentication to access
        protected_paths = ['/home', '/rake', '/settings/']  # Add your protected paths here
        k=User.objects.get(val=1)
        # Check if the requested path requires authentication
        if k:
          while len(protected_paths) > 0:
                 protected_paths.pop()
              
        else:    
            return redirect('%s?next=%s' % (reverse('login'), path))

        response = self.get_response(request)
        return response
