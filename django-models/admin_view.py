# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

@login_required
@admin_required
def admin_view(request):
    # Your view logic here
    return render(request, 'relationship_app/admin_view.html')



# relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def libraries_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


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