# relationship_app/decorators.py

from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import UserProfile

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        if user_profile.role == 'Admin':
            return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _wrapped_view